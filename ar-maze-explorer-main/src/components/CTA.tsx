import { Button } from "@/components/ui/button";
import { Download, ArrowRight, Play } from "lucide-react";

const CTA = () => {
  const handlePlay = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/play");
      const data = await response.json();
      console.log(data);
      alert("Launching the AR Maze Game...");
    } catch (err) {
      console.error(err);
      alert("Backend not running! Start server.py first.");
    }
  };

  return (
    <section className="py-24 px-4 relative overflow-hidden">
      {/* Background Effects */}
      <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-transparent to-secondary/10" />
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-primary/10 rounded-full blur-[150px]" />

      <div className="container mx-auto relative z-10">
        <div className="gradient-border rounded-3xl p-12 md:p-16 text-center max-w-4xl mx-auto">
          <div className="relative z-10">
            <h2 className="text-4xl md:text-6xl font-display font-bold mb-6">
              <span className="text-foreground">Ready to</span>{" "}
              <span className="text-glow-cyan text-primary">Enter</span>{" "}
              <span className="text-foreground">the</span>{" "}
              <span className="text-glow-magenta text-secondary">Maze?</span>
            </h2>

            <p className="text-muted-foreground text-lg md:text-xl max-w-2xl mx-auto mb-10">
              Step into the most immersive AR maze adventure ever built.
              Click below to launch the game instantly on your system!
            </p>

            {/* PLAY NOW BUTTON */}
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-6">
              <Button
                variant="hero"
                size="xl"
                className="group bg-primary text-primary-foreground hover:bg-primary/80 transition-transform"
                onClick={handlePlay}
              >
                <Play className="w-6 h-6 mr-2" />
                Play Now
              </Button>

              <Button variant="hero-outline" size="xl">
                <Download className="w-5 h-5 mr-2" />
                Download Free
                <ArrowRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
              </Button>

              <Button variant="hero-outline" size="xl">
                View on App Store
              </Button>
            </div>

            <p className="text-muted-foreground text-sm mt-4">
              Desktop version • Python game launcher • AR-enabled gameplay
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CTA;
