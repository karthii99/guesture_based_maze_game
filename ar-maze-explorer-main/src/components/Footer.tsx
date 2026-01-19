import { Github, Twitter, Instagram, Youtube } from "lucide-react";

const Footer = () => {
  const socialLinks = [
    { icon: <Twitter className="w-5 h-5" />, href: "#", label: "Twitter" },
    { icon: <Instagram className="w-5 h-5" />, href: "#", label: "Instagram" },
    { icon: <Youtube className="w-5 h-5" />, href: "#", label: "YouTube" },
    { icon: <Github className="w-5 h-5" />, href: "#", label: "GitHub" },
  ];

  const footerLinks = [
    { label: "Privacy Policy", href: "#" },
    { label: "Terms of Service", href: "#" },
    { label: "Support", href: "#" },
    { label: "Contact", href: "#" },
  ];

  return (
    <footer className="py-12 px-4 border-t border-border/30 bg-card/30">
      <div className="container mx-auto">
        <div className="flex flex-col md:flex-row items-center justify-between gap-8">
          {/* Logo */}
          <div className="text-center md:text-left">
            <h3 className="font-display font-bold text-2xl">
              <span className="text-primary">AR</span>
              <span className="text-foreground">Maze</span>
            </h3>
            <p className="text-muted-foreground text-sm mt-1">
              The future of gaming
            </p>
          </div>
          
          {/* Links */}
          <nav className="flex flex-wrap items-center justify-center gap-6">
            {footerLinks.map((link) => (
              <a
                key={link.label}
                href={link.href}
                className="text-muted-foreground hover:text-primary transition-colors text-sm"
              >
                {link.label}
              </a>
            ))}
          </nav>
          
          {/* Social Links */}
          <div className="flex items-center gap-4">
            {socialLinks.map((social) => (
              <a
                key={social.label}
                href={social.href}
                aria-label={social.label}
                className="w-10 h-10 rounded-lg border border-border/50 bg-card/50 flex items-center justify-center text-muted-foreground hover:text-primary hover:border-primary transition-colors"
              >
                {social.icon}
              </a>
            ))}
          </div>
        </div>
        
        {/* Copyright */}
        <div className="text-center mt-8 pt-8 border-t border-border/20">
          <p className="text-muted-foreground text-sm">
            © {new Date().getFullYear()} Gesture AR Maze. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
