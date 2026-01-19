import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
import time
import random

# =============== FULL SCREEN SETUP ==================
root = tk.Tk()
SCREEN_W = root.winfo_screenwidth()
SCREEN_H = root.winfo_screenheight()
root.destroy()

WINDOW_NAME = "Gesture Neon Maze – Simple & Fast"
cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# =============== MEDIAPIPE HANDS ====================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# =============== GAME CONSTANTS =====================
GESTURE_THRESHOLD = 25      # smaller => easier left/right/up/down
OPEN_HAND_MIN_FINGERS = 3   # >= 3 fingers extended => "open"
MOVE_COOLDOWN = 0.18        # seconds between ball moves (smaller = faster)

# =============== HAND HELPERS =======================
def is_open_hand(hand_landmarks):
    """
    Returns True if hand is open (3 or more fingers extended).
    Uses fingertip vs PIP joint Y values.
    """
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    open_count = 0
    for tip_i, pip_i in zip(tips, pips):
        tip_y = hand_landmarks.landmark[tip_i].y
        pip_y = hand_landmarks.landmark[pip_i].y
        if tip_y < pip_y:
            open_count += 1
    return open_count >= OPEN_HAND_MIN_FINGERS

# =============== MAZE GENERATION ====================
def generate_maze(cell_rows, cell_cols):
    """
    Simple DFS backtracker maze.
    Logical grid cell_rows x cell_cols -> real maze (2*rows+1) x (2*cols+1)
    Always has path from start to goal.
    """
    rows = cell_rows * 2 + 1
    cols = cell_cols * 2 + 1
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    visited = [[False for _ in range(cell_cols)] for _ in range(cell_rows)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def carve(r, c):
        visited[r][c] = True
        maze[r * 2 + 1][c * 2 + 1] = 0
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < cell_rows and 0 <= nc < cell_cols and not visited[nr][nc]:
                maze[r * 2 + 1 + dr][c * 2 + 1 + dc] = 0
                carve(nr, nc)

    carve(0, 0)
    start = (1, 1)
    goal = (rows - 2, cols - 2)
    maze[start[0]][start[1]] = 0
    maze[goal[0]][goal[1]] = 0
    return maze, start, goal

# =============== DRAW HELPERS =======================
def draw_background(frame):
    h, w, _ = frame.shape
    for y in range(h):
        t = y / h
        b = int(40 + 30 * t)
        g = int(30 + 10 * t)
        r = 20
        frame[y, :] = (b, g, r)

def draw_walls(frame, maze, color, cw, ch):
    rows = len(maze)
    cols = len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                x1 = c * cw
                y1 = r * ch
                x2 = x1 + cw
                y2 = y1 + ch
                cv2.rectangle(frame, (x1 + 6, y1 + 6),
                              (x2 - 6, y2 - 6), color, -1, cv2.LINE_AA)
                cv2.rectangle(frame, (x1 + 6, y2 - 4),
                              (x2 - 2, y2 + 1), (15, 15, 40), -1, cv2.LINE_AA)

def draw_trail(frame, points):
    if len(points) < 2:
        return
    overlay = frame.copy()
    n = len(points)
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        t = i / (n - 1)
        g = int(255 * (1 - t))
        b = 255
        col = (b, g, 0)
        th = int(18 - 14 * t)
        cv2.line(overlay, (x1, y1), (x2, y2), col, th, cv2.LINE_AA)
    frame[:] = cv2.addWeighted(overlay, 0.8, frame, 0.2, 0)

def draw_ball(frame, x, y):
    overlay = frame.copy()
    for r in range(16, 38, 5):
        alpha = (38 - r) / 22.0
        col = (0, int(255 * alpha), 255)
        cv2.circle(overlay, (x, y), r, col, 3, cv2.LINE_AA)
    frame[:] = cv2.addWeighted(overlay, 0.8, frame, 0.2, 0)
    cv2.circle(frame, (x, y), 13, (0, 255, 0), -1, cv2.LINE_AA)

def draw_cursor(frame, x, y):
    cv2.circle(frame, (x, y), 18, (255, 0, 255), 2, cv2.LINE_AA)
    cv2.circle(frame, (x, y), 6, (255, 0, 255), -1, cv2.LINE_AA)

# =============== SIMPLE LEVEL LOGIC =================
def maze_size_for_level(level):
    # very easy first levels, get bigger slowly
    if level <= 3:
        return 4, 6       # small
    elif level <= 6:
        return 6, 10
    else:
        return 8, 14      # large

def load_level(level):
    global maze, ball_r, ball_c, goal_r, goal_c
    global ROWS, COLS, CW, CH, level_start_time, trail_points
    cells_r, cells_c = maze_size_for_level(level)
    maze, start, goal = generate_maze(cells_r, cells_c)
    ball_r, ball_c = start
    goal_r, goal_c = goal
    ROWS = len(maze)
    COLS = len(maze[0])
    CW = SCREEN_W // COLS
    CH = SCREEN_H // ROWS
    sx = ball_c * CW + CW // 2
    sy = ball_r * CH + CH // 2
    trail_points = [(sx, sy)]
    level_start_time = time.time()
    return trail_points

# =============== GLOBAL STATE =======================
maze = None
ball_r = ball_c = 0
goal_r = goal_c = 0
ROWS = COLS = 0
CW = CH = 0
current_level = 1
trail_points = []
level_start_time = time.time()
last_move_time = time.time()

# hand tracking (smoothed)
hand_x = hand_y = None
prev_hand_x = None
prev_hand_y = None
cursor_x = SCREEN_W // 2
cursor_y = SCREEN_H // 2
gesture = "NONE"
open_hand_state = False

# init level 1
trail_points = load_level(current_level)

# =============== MAIN LOOP ==========================
cap = cv2.VideoCapture(0)

while True:
    ok, cam = cap.read()
    if not ok:
        break

    cam = cv2.flip(cam, 1)
    cam = cv2.resize(cam, (SCREEN_W, SCREEN_H))

    frame = np.zeros_like(cam)
    draw_background(frame)
    cam_dark = cv2.addWeighted(cam, 0.25, np.zeros_like(cam), 0.75, 0)
    frame = cv2.addWeighted(frame, 0.9, cam_dark, 0.1, 0)

    now = time.time()

    # ---------- Hand detection ----------
    rgb = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture = "NONE"
    open_hand_state = False
    hand_present = False

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        hand_present = True

        # open or closed
        if is_open_hand(hand):
            open_hand_state = True

        # index fingertip position (raw)
        tip = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        x = int(tip.x * SCREEN_W)
        y = int(tip.y * SCREEN_H)

        # smooth hand position for stable gestures & cursor
        if hand_x is None:
            hand_x, hand_y = x, y
            prev_hand_x, prev_hand_y = x, y
        else:
            prev_hand_x, prev_hand_y = hand_x, hand_y
            hand_x = int(hand_x * 0.7 + x * 0.3)
            hand_y = int(hand_y * 0.7 + y * 0.3)

        cursor_x, cursor_y = hand_x, hand_y

        # movement delta based on smoothed position
        dx = hand_x - prev_hand_x
        dy = hand_y - prev_hand_y

        # only detect gesture if hand is open
        if open_hand_state:
            if abs(dx) > abs(dy):
                if dx > GESTURE_THRESHOLD:
                    gesture = "RIGHT"
                elif dx < -GESTURE_THRESHOLD:
                    gesture = "LEFT"
            else:
                if dy > GESTURE_THRESHOLD:
                    gesture = "DOWN"
                elif dy < -GESTURE_THRESHOLD:
                    gesture = "UP"

    else:
        hand_x = hand_y = None
        prev_hand_x = prev_hand_y = None

    # if fist closed or no hand => ignore gesture
    if not open_hand_state:
        gesture = "NONE"

    # ---------- Draw maze ----------
    wall_color = (185, 185, 225)
    draw_walls(frame, maze, wall_color, CW, CH)

    # ---------- Move ball ----------
    if gesture != "NONE" and (now - last_move_time) > MOVE_COOLDOWN:
        old_r, old_c = ball_r, ball_c
        nr, nc = old_r, old_c

        if gesture == "UP" and maze[old_r - 1][old_c] == 0:
            nr -= 1
        elif gesture == "DOWN" and maze[old_r + 1][old_c] == 0:
            nr += 1
        elif gesture == "LEFT" and maze[old_r][old_c - 1] == 0:
            nc -= 1
        elif gesture == "RIGHT" and maze[old_r][old_c + 1] == 0:
            nc += 1

        if (nr, nc) != (old_r, old_c):
            ball_r, ball_c = nr, nc
            last_move_time = now
            cx = ball_c * CW + CW // 2
            cy = ball_r * CH + CH // 2
            trail_points.append((cx, cy))
            if len(trail_points) > 120:
                trail_points.pop(0)

    # ---------- Draw trail, ball, goal ----------
    bx = ball_c * CW + CW // 2
    by = ball_r * CH + CH // 2
    gx = goal_c * CW + CW // 2
    gy = goal_r * CH + CH // 2

    draw_trail(frame, trail_points)
    draw_ball(frame, bx, by)
    cv2.circle(frame, (gx, gy), 18, (0, 255, 0), 3, cv2.LINE_AA)

    # ---------- Draw cursor ----------
    if hand_present and hand_x is not None:
        draw_cursor(frame, cursor_x, cursor_y)

    # ---------- Level complete (simple) ----------
    if (ball_r, ball_c) == (goal_r, goal_c):
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (SCREEN_W, SCREEN_H),
                      (0, 0, 0), -1)
        frame[:] = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)
        cv2.putText(frame, f"LEVEL {current_level} CLEARED!",
                    (SCREEN_W // 6, SCREEN_H // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.7,
                    (0, 255, 255), 4, cv2.LINE_AA)
        cv2.imshow(WINDOW_NAME, frame)
        cv2.waitKey(800)  # short pause

        current_level += 1
        trail_points = load_level(current_level)
        continue

    # ---------- HUD ----------
    elapsed = now - level_start_time
    cv2.putText(frame,
                f"Level: {current_level}",
                (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 255, 255), 3, cv2.LINE_AA)
    cv2.putText(frame,
                f"Time: {elapsed:4.1f}s",
                (30, 95), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame,
                f"Gesture: {gesture}",
                (30, 140), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (200, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame,
                f"Hand: {'OPEN' if open_hand_state else 'CLOSED/NO'}",
                (30, 185), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (0, 255, 0) if open_hand_state else (0, 0, 255),
                2, cv2.LINE_AA)
    cv2.putText(frame,
                "Press Q to quit",
                (30, SCREEN_H - 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow(WINDOW_NAME, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
