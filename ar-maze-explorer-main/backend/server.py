from flask import Flask
import subprocess
import sys
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/play", methods=["GET"])
def play():
    print("🔥 /play endpoint triggered")

    game_path = os.path.abspath(os.path.join(os.getcwd(), "..", "src", "ar_maze_phase1.py"))

    print("Launching game file:", game_path)

    subprocess.Popen([sys.executable, game_path])

    return {"status": "Game started"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
