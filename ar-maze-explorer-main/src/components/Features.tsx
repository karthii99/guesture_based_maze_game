import { Hand, Smartphone, Gamepad2, Zap, Eye, Trophy } from "lucide-react";

interface FeatureCardProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  delay?: number;
}

const FeatureCard = ({ icon, title, description, delay = 0 }: FeatureCardProps) => (
  <div 
    className="gradient-border rounded-xl p-6 hover:scale-105 transition-transform duration-300 group"
    style={{ animationDelay: `${delay}ms` }}
  >
    <div className="relative z-10">
      <div className="w-14 h-14 rounded-lg bg-primary/10 flex items-center justify-center mb-4 group-hover:bg-primary/20 transition-colors">
        <div className="text-primary">{icon}</div>
      </div>
      <h3 className="text-xl font-display font-bold text-foreground mb-2">{title}</h3>
      <p className="text-muted-foreground leading-relaxed">{description}</p>
    </div>
  </div>
);

const Features = () => {
  const features = [
    {
      icon: <Hand className="w-7 h-7" />,
      title: "Gesture Controls",
      description: "Navigate mazes with intuitive hand gestures. Wave, pinch, and swipe to control your path through augmented reality.",
    },
    {
      icon: <Eye className="w-7 h-7" />,
      title: "AR Technology",
      description: "Experience mazes projected into your real world. Watch as digital walls and pathways blend seamlessly with reality.",
    },
    {
      icon: <Gamepad2 className="w-7 h-7" />,
      title: "Dynamic Mazes",
      description: "Every maze is procedurally generated. No two games are the same, offering endless challenges and replayability.",
    },
    {
      icon: <Zap className="w-7 h-7" />,
      title: "Real-Time Physics",
      description: "Feel the environment respond to your movements with realistic physics and interactive obstacles.",
    },
    {
      icon: <Smartphone className="w-7 h-7" />,
      title: "Mobile Ready",
      description: "Play anywhere with AR-capable devices. No special hardware required, just your smartphone.",
    },
    {
      icon: <Trophy className="w-7 h-7" />,
      title: "Global Leaderboards",
      description: "Compete with players worldwide. Climb the ranks and prove you're the ultimate maze master.",
    },
  ];

  return (
    <section className="py-24 px-4 relative">
      <div className="absolute inset-0 maze-pattern animate-maze-shift opacity-30" />
      <div className="container mx-auto relative z-10">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-display font-bold mb-4">
            <span className="text-glow-cyan text-primary">Game</span>{" "}
            <span className="text-foreground">Features</span>
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            Discover what makes our AR maze game a revolutionary gaming experience
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <FeatureCard
              key={feature.title}
              {...feature}
              delay={index * 100}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
