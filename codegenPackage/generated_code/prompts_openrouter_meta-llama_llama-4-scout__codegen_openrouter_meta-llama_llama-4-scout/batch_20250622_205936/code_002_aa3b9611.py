"""
Generated Code Metadata:
========================
Original URL: https://apesboard.in.net
Prompt: Generate a JavaScript code snippet that uses the HTML5 canvas element to create a simple game of Bắn Cá, similar to the one offered on Win55, including basic game mechanics and collision detection.
Generated: DETERMINISTIC_aa3b961128417e0a
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Get the canvas element
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Set canvas dimensions
canvas.width = 800;
canvas.height = 600;

// Define game variables
let player = {
  x: canvas.width / 2,
  y: canvas.height - 50,
  width: 50,
  height: 50,
  speed: 5,
  bullet: []
};

let fish = [];
let score = 0;

// Initialize game
function init() {
  // Create initial fish
  for (let i = 0; i < 10; i++) {
    fish.push({
      x: Math.random() * (canvas.width - 50),
      y: Math.random() * (canvas.height / 2),
      width: 30,
      height: 30,
      speed: Math.random() * 2 + 1
    });
  }
}

// Draw player
function drawPlayer() {
  ctx.fillStyle = 'blue';
  ctx.fillRect(player.x, player.y, player.width, player.height);
}

// Draw fish
function drawFish() {
  fish.forEach((f) => {
    ctx.fillStyle = 'green';
    ctx.fillRect(f.x, f.y, f.width, f.height);
  });
}

// Draw bullets
function drawBullets() {
  player.bullet.forEach((b) => {
    ctx.fillStyle = 'red';
    ctx.fillRect(b.x, b.y, 5, 10);
  });
}

// Update game state
function update() {
  // Move player bullets
  player.bullet.forEach((b, index) => {
    b.y -= 5;
    if (b.y < 0) {
      player.bullet.splice(index, 1);
    }
  });

  // Move fish
  fish.forEach((f) => {
    f.x += f.speed;
    if (f.x > canvas.width - f.width || f.x < 0) {
      f.speed *= -1;
    }
  });

  // Collision detection
  player.bullet.forEach((b) => {
    fish.forEach((f, index) => {
      if (b.x > f.x && b.x < f.x + f.width && b.y > f.y && b.y < f.y + f.height) {
        // Remove bullet and fish
        player.bullet.splice(player.bullet.indexOf(b), 1);
        fish.splice(index, 1);
        score++;
      }
    });
  });
}

// Draw everything
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawPlayer();
  drawFish();
  drawBullets();
  ctx.font = '24px Arial';
  ctx.fillStyle = 'black';
  ctx.textAlign = 'left';
  ctx.textBaseline = 'top';
  ctx.fillText(`Score: ${score}`, 10, 10);
}

// Handle keyboard input
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') {
    player.x -= player.speed;
  } else if (e.key === 'ArrowRight') {
    player.x += player.speed;
  } else if (e.key === ' ') {
    player.bullet.push({ x: player.x + player.width / 2, y: player.y });
  }
});

// Main game loop
init();
setInterval(() => {
  update();
  draw();
}, 16);

// Error handling
try {
  // No errors expected
} catch (error) {
  console.error('Game error:', error);
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bắn Cá Game</title>
  <style>
    /* Add some basic styling */
    canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <script src="script.js"></script>
</body>
</html>
```
