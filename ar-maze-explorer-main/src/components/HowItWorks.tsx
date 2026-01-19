import { ArrowRight, Scan, Hand, Play } from "lucide-react";

const HowItWorks = () => {
  const steps = [
    {
      number: "01",
      icon: <Scan className="w-8 h-8" />,
      title: "Scan Your Space",
      description: "Point your camera at any flat surface. Our AR technology maps your environment in seconds.",
    },
    {
      number: "02",
      icon: <Hand className="w-8 h-8" />,
      title: "Enable Gestures",
      description: "Calibrate hand tracking with a simple wave. The game recognizes your movements instantly.",
    },
    {
      number: "03",
      icon: <Play className="w-8 h-8" />,
      title: "Start Playing",
      description: "Navigate the maze using gestures. Swipe to move, pinch to zoom, and wave to interact.",
    },
  ];

  return (
    <section className="py-24 px-4 bg-card/50 relative overflow-hidden">
      <div className="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-primary to-transparent" />
      <div className="absolute bottom-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-secondary to-transparent" />
      
      <div className="container mx-auto relative z-10">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-display font-bold mb-4">
            <span className="text-foreground">How It</span>{" "}
            <span className="text-glow-magenta text-secondary">Works</span>
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            Get started in three simple steps
          </p>
        </div>

        <div className="flex flex-col lg:flex-row items-center justify-center gap-8 lg:gap-4">
          {steps.map((step, index) => (
            <div key={step.number} className="flex items-center">
              <div className="gradient-border rounded-2xl p-8 w-full lg:w-80 text-center group hover:scale-105 transition-transform duration-300">
                <div className="relative z-10">
                  <span className="text-6xl font-display font-black text-primary/20 absolute -top-4 -left-2">
                    {step.number}
                  </span>
                  <div className="w-16 h-16 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center mx-auto mb-6 text-primary-foreground">
                    {step.icon}
                  </div>
                  <h3 className="text-2xl font-display font-bold text-foreground mb-3">
                    {step.title}
                  </h3>
                  <p className="text-muted-foreground leading-relaxed">
                    {step.description}
                  </p>
                </div>
              </div>
              
              {index < steps.length - 1 && (
                <div className="hidden lg:block mx-4">
                  <ArrowRight className="w-8 h-8 text-primary animate-pulse" />
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;
