"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Create a script to display dynamic seasonal patterns (spring, summer, autumn, winter) inspired by the Hikeshi NFT project's theme, using HTML5 Canvas or CSS animations.
Generated: DETERMINISTIC_7db36c183b325122
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Seasonal Patterns</title>
  <style>
    /* Basic styles for canvas and body */
    body {
      margin: 0;
      overflow: hidden; /* Ensure no scrollbars */
      background-color: #000; /* Background for contrast */
    }
    canvas {
      display: block;
    }
  </style>
</head>
<body>
  <!-- HTML5 Canvas -->
  <canvas id="seasonalCanvas"></canvas>

  <script>
    // Select the canvas element and set its size dynamically
    const canvas = document.getElementById('seasonalCanvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Utility function for random numbers
    function randomBetween(min, max) {
      return Math.random() * (max - min) + min;
    }

    // Seasonal patterns data
    const seasons = {
      spring: { color: 'rgba(144,238,144,0.8)', shape: 'circle', count: 200 },
      summer: { color: 'rgba(255,223,0,0.8)', shape: 'circle', count: 150 },
      autumn: { color: 'rgba(255,140,0,0.8)', shape: 'triangle', count: 100 },
      winter: { color: 'rgba(135,206,235,0.8)', shape: 'flake', count: 250 },
    };

    let currentSeason = 'spring'; // Default season

    // Function to draw shapes for each season
    function drawSeasonalPattern(seasonData) {
      ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas

      for (let i = 0; i < seasonData.count; i++) {
        const x = randomBetween(0, canvas.width);
        const y = randomBetween(0, canvas.height);
        const size = randomBetween(10, 20);

        ctx.fillStyle = seasonData.color;

        if (seasonData.shape === 'circle') {
          ctx.beginPath();
          ctx.arc(x, y, size / 2, 0, Math.PI * 2);
          ctx.fill();
        } else if (seasonData.shape === 'triangle') {
          ctx.beginPath();
          ctx.moveTo(x, y);
          ctx.lineTo(x - size / 2, y + size);
          ctx.lineTo(x + size / 2, y + size);
          ctx.closePath();
          ctx.fill();
        } else if (seasonData.shape === 'flake') {
          ctx.beginPath();
          for (let j = 0; j < 6; j++) { // Draw snowflake-like pattern
            const angle = (Math.PI / 3) * j;
            ctx.lineTo(x + size * Math.cos(angle), y + size * Math.sin(angle));
          }
          ctx.closePath();
          ctx.fill();
        }
      }
    }

    // Function to cycle through seasons
    function cycleSeasons() {
      const seasonKeys = Object.keys(seasons);
      const currentIndex = seasonKeys.indexOf(currentSeason);
      const nextIndex = (currentIndex + 1) % seasonKeys.length;
      currentSeason = seasonKeys[nextIndex];

      drawSeasonalPattern(seasons[currentSeason]);
    }

    // Set interval to cycle through seasons dynamically
    setInterval(cycleSeasons, 5000); // Change season every 5 seconds

    // Draw initial season
    drawSeasonalPattern(seasons[currentSeason]);

    // Handle window resizing
    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      drawSeasonalPattern(seasons[currentSeason]); // Redraw patterns
    });
  </script>
</body>
</html>
```
