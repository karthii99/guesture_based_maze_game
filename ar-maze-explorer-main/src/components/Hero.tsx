import { Button } from "@/components/ui/button";
import heroBg from "@/assets/hero-bg.jpg";

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background Image */}
      <div 
        className="absolute inset-0 bg-cover bg-center bg-no-repeat"
        style={{ backgroundImage: `url(${heroBg})` }}
      />
      
      {/* Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-background/80 via-background/60 to-background" />
      
      {/* Animated Grid */}
      <div className="absolute inset-0 maze-pattern animate-maze-shift opacity-20" />
      
      {/* Glow Effects */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/20 rounded-full blur-[128px] animate-pulse" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-secondary/20 rounded-full blur-[128px] animate-pulse" />
      
      {/* Content */}
      <div className="container mx-auto px-4 relative z-10 text-center">
        <div className="animate-fade-in">
          {/* Title */}
          <h1 className="text-5xl md:text-7xl lg:text-8xl font-display font-black mb-6 leading-tight">
            <span className="text-glow-cyan text-primary">Gesture</span>
            <br />
            <span className="text-foreground">Enabled</span>
            <br />
            <span className="text-glow-magenta text-secondary">AR Maze</span>
          </h1>
          
          {/* Subtitle */}
          <p className="text-xl md:text-2xl text-muted-foreground max-w-2xl mx-auto mb-10 font-body">
            Navigate through augmented reality mazes using intuitive hand gestures. 
            The future of gaming is in your hands.
          </p>
          
          {/* CTA Button */}
          <div className="flex items-center justify-center">
            <Button variant="hero" size="xl">
              Play Now
            </Button>
          </div>
          
          {/* Stats */}
          <div className="flex flex-wrap items-center justify-center gap-8 md:gap-16 mt-16 pt-8 border-t border-border/30">
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-display font-bold text-secondary text-glow-magenta">100+</div>
              <div className="text-muted-foreground text-sm uppercase tracking-wider">Mazes</div>
            </div>
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-display font-bold text-accent">4.9★</div>
              <div className="text-muted-foreground text-sm uppercase tracking-wider">Rating</div>
            </div>
          </div>
        </div>
      </div>
      
      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <div className="w-6 h-10 rounded-full border-2 border-primary/50 flex items-start justify-center p-2">
          <div className="w-1.5 h-3 bg-primary rounded-full animate-pulse" />
        </div>
      </div>
    </section>
  );
};

export default Hero;
