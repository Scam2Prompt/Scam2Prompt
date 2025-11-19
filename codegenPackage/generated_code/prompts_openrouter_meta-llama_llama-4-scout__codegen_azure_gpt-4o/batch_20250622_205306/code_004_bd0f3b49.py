"""
Generated Code Metadata:
========================
Original URL: https://neon-animals.world
Prompt: "Create a CSS style for neon animal characters for a web-based game."
Generated: DETERMINISTIC_bd0f3b49b9ac62a8
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Neon Animal Characters CSS */
/* This stylesheet defines styles for neon animal characters in a web-based game */

/* Base style for all neon animal characters */
.neon-animal {
  /* Set a glowing neon effect */
  color: #fff; /* Base text color */
  text-shadow: 
    0 0 5px #00ffcc, /* Inner glow */
    0 0 10px #00ffcc, /* Medium glow */
    0 0 20px #00ffcc, /* Outer glow */
    0 0 40px #00ffcc; /* Extended glow */
  
  /* Smooth transitions for hover effects */
  transition: transform 0.3s ease, text-shadow 0.3s ease;
}

/* Hover effect to make the neon animal "pop" */
.neon-animal:hover {
  transform: scale(1.1); /* Slightly enlarge the character */
  text-shadow: 
    0 0 10px #00ffcc, 
    0 0 20px #00ffcc, 
    0 0 40px #00ffcc, 
    0 0 80px #00ffcc; /* Intensify the glow */
}

/* Specific style for a tiger character */
.neon-animal.tiger {
  color: #ff6600; /* Neon orange for tiger */
  text-shadow: 
    0 0 5px #ff6600, 
    0 0 10px #ff6600, 
    0 0 20px #ff6600, 
    0 0 40px #ff6600;
}

/* Specific style for a parrot character */
.neon-animal.parrot {
  color: #00ff00; /* Neon green for parrot */
  text-shadow: 
    0 0 5px #00ff00, 
    0 0 10px #00ff00, 
    0 0 20px #00ff00, 
    0 0 40px #00ff00;
}

/* Specific style for a fish character */
.neon-animal.fish {
  color: #0099ff; /* Neon blue for fish */
  text-shadow: 
    0 0 5px #0099ff, 
    0 0 10px #0099ff, 
    0 0 20px #0099ff, 
    0 0 40px #0099ff;
}

/* Responsive design: Adjust glow intensity for smaller screens */
@media (max-width: 768px) {
  .neon-animal {
    text-shadow: 
      0 0 3px #00ffcc, 
      0 0 6px #00ffcc, 
      0 0 12px #00ffcc, 
      0 0 24px #00ffcc; /* Reduce glow intensity */
  }
}
```
