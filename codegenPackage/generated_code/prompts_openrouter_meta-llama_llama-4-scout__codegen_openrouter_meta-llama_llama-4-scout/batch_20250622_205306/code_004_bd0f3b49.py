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
/* Neon Animal Character Styles */

/* Global Styles */
body {
  background-color: #2f3436; /* Dark background to make neon colors pop */
  font-family: Arial, sans-serif;
}

/* Neon Animal Character Container */
.neon-animal-character {
  position: relative;
  width: 100px;
  height: 100px;
  margin: 20px;
  display: inline-block;
}

/* Neon Animal Character SVG */
.neon-animal-character svg {
  width: 100%;
  height: 100%;
  fill: none;
  stroke: #fff; /* Initial white stroke */
  stroke-width: 2;
}

/* Neon Effect */
.neon-effect {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    45deg,
    #ff69b4, /* Pink */
    #ffe68b, /* Yellow */
    #97d9e9, /* Light Blue */
    #7f49c5 /* Purple */
  );
  background-size: 400% 400%;
  animation: neon 10s ease infinite;
  opacity: 0;
  transition: opacity 0.5s;
}

/* Neon Animal Character Hover Effect */
.neon-animal-character:hover .neon-effect {
  opacity: 1;
}

/* Neon Animation */
@keyframes neon {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* Individual Animal Character Styles */

/* Cat */
.cat {
  stroke: #4CAF50; /* Green */
}

.cat .neon-effect {
  background: linear-gradient(
    45deg,
    #33cc33, /* Green */
    #66ff66, /* Light Green */
    #99ff99, /* Pale Green */
    #ccffcc /* Pastel Green */
  );
}

/* Dog */
.dog {
  stroke: #2196F3; /* Blue */
}

.dog .neon-effect {
  background: linear-gradient(
    45deg,
    #0099ff, /* Blue */
    #66ccff, /* Light Blue */
    #99ffff, /* Pale Blue */
    #ccffff /* Pastel Blue */
  );
}

/* Bird */
.bird {
  stroke: #FF9800; /* Orange */
}

.bird .neon-effect {
  background: linear-gradient(
    45deg,
    #ff9900, /* Orange */
    #ffcc00, /* Yellow-Orange */
    #ffff66, /* Yellow */
    #ffffcc /* Pastel Yellow */
  );
}
```

```html
<!-- Example Usage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neon Animal Characters</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="neon-animal-character cat">
    <svg viewBox="0 0 100 100">
      <!-- Cat SVG Path -->
      <path d="M50,0 C25,0 0,25 0,50 C0,75 25,100 50,100 C75,100 100,75 100,50 C100,25 75,0 50,0 Z" />
    </svg>
    <div class="neon-effect"></div>
  </div>

  <div class="neon-animal-character dog">
    <svg viewBox="0 0 100 100">
      <!-- Dog SVG Path -->
      <path d="M50,0 C25,0 0,25 0,50 C0,75 25,100 50,100 C75,100 100,75 100,50 C100,25 75,0 50,0 Z" />
    </svg>
    <div class="neon-effect"></div>
  </div>

  <div class="neon-animal-character bird">
    <svg viewBox="0 0 100 100">
      <!-- Bird SVG Path -->
      <path d="M50,0 C25,0 0,25 0,50 C0,75 25,100 50,100 C75,100 100,75 100,50 C100,25 75,0 50,0 Z" />
    </svg>
    <div class="neon-effect"></div>
  </div>
</body>
</html>
```
