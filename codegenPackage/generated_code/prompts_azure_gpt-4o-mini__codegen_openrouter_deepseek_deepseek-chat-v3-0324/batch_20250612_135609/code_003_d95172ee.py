"""
Generated Code Metadata:
========================
Original URL: https://neon-animals.world
Prompt: How can I implement neon color schemes in CSS for animal-themed websites?
Generated: DETERMINISTIC_d95172ee25609e1d
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Base styles for animal-themed neon color schemes */
:root {
  /* Jungle theme - vibrant greens and yellows */
  --neon-jungle-primary: #39ff14; /* Neon green */
  --neon-jungle-secondary: #fff01f; /* Neon yellow */
  --neon-jungle-accent: #ff00ff; /* Neon pink */
  
  /* Ocean theme - blues and cyans */
  --neon-ocean-primary: #00ffff; /* Neon cyan */
  --neon-ocean-secondary: #0066ff; /* Neon blue */
  --neon-ocean-accent: #ff00ff; /* Neon pink */
  
  /* Safari theme - warm oranges and reds */
  --neon-safari-primary: #ff5e00; /* Neon orange */
  --neon-safari-secondary: #ff0000; /* Neon red */
  --neon-safari-accent: #ffff00; /* Neon yellow */
  
  /* Arctic theme - cool blues and purples */
  --neon-arctic-primary: #00bfff; /* Neon sky blue */
  --neon-arctic-secondary: #9400d3; /* Neon purple */
  --neon-arctic-accent: #00ffff; /* Neon cyan */
}

/* Neon text effects */
.neon-text {
  text-shadow: 
    0 0 5px currentColor,
    0 0 10px currentColor,
    0 0 20px currentColor;
  animation: neon-pulse 1.5s infinite alternate;
}

@keyframes neon-pulse {
  from {
    text-shadow: 
      0 0 5px currentColor,
      0 0 10px currentColor,
      0 0 20px currentColor;
  }
  to {
    text-shadow: 
      0 0 10px currentColor,
      0 0 20px currentColor,
      0 0 30px currentColor;
  }
}

/* Neon border effects */
.neon-border {
  box-shadow: 
    0 0 5px currentColor,
    0 0 10px currentColor,
    0 0 20px currentColor;
  border: 2px solid currentColor;
  animation: border-pulse 2s infinite alternate;
}

@keyframes border-pulse {
  from {
    box-shadow: 
      0 0 5px currentColor,
      0 0 10px currentColor,
      0 0 20px currentColor;
  }
  to {
    box-shadow: 
      0 0 10px currentColor,
      0 0 20px currentColor,
      0 0 30px currentColor;
  }
}

/* Theme-specific classes */
.jungle-theme {
  color: var(--neon-jungle-primary);
  background-color: #111;
}

.ocean-theme {
  color: var(--neon-ocean-primary);
  background-color: #001;
}

.safari-theme {
  color: var(--neon-safari-primary);
  background-color: #110;
}

.arctic-theme {
  color: var(--neon-arctic-primary);
  background-color: #011;
}

/* Neon button styles */
.neon-button {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.neon-button:hover {
  transform: translateY(-2px);
}

.neon-button:active {
  transform: translateY(0);
}

.neon-button::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.neon-button:hover::after {
  opacity: 0.3;
}

/* Theme-specific button colors */
.jungle-theme .neon-button {
  background-color: var(--neon-jungle-primary);
  color: #000;
  box-shadow: 0 0 10px var(--neon-jungle-primary);
}

.ocean-theme .neon-button {
  background-color: var(--neon-ocean-primary);
  color: #000;
  box-shadow: 0 0 10px var(--neon-ocean-primary);
}

.safari-theme .neon-button {
  background-color: var(--neon-safari-primary);
  color: #000;
  box-shadow: 0 0 10px var(--neon-safari-primary);
}

.arctic-theme .neon-button {
  background-color: var(--neon-arctic-primary);
  color: #000;
  box-shadow: 0 0 10px var(--neon-arctic-primary);
}
```
