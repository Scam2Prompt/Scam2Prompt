"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: Write JavaScript code for a bubble-shooter game similar to the one described in the "Bubble-shooter" category on jito.pro, including collision detection and scoring mechanics.
Generated: DETERMINISTIC_c9f661e7f4eb6fdf
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// bubble-shooter.js

// Constants
const BUBBLE_RADIUS = 20;
const GAME_WIDTH = 800;
const GAME_HEIGHT = 600;
const FPS = 60;

// Colors
const BUBBLE_COLOR = '#ff69b4';
const BACKGROUND_COLOR = '#f0f0f0';

// Game class
class Game {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.bubbles = [];
    this.targets = [];
    this.score = 0;
    this.lives = 3;

    // Initialize game
    this.init();
  }

  // Initialize game
  init() {
    this.canvas.width = GAME_WIDTH;
    this.canvas.height = GAME_HEIGHT;

    // Create initial bubbles
    for (let i = 0; i < 10; i++) {
      this.bubbles.push(new Bubble(Math.random() * GAME_WIDTH, Math.random() * GAME_HEIGHT));
    }

    // Create targets
    for (let i = 0; i < 5; i++) {
      this.targets.push(new Target(Math.random() * GAME_WIDTH, Math.random() * GAME_HEIGHT));
    }

    // Main game loop
    setInterval(() => this.update(), 1000 / FPS);
  }

  // Update game state
  update() {
    this.ctx.clearRect(0, 0, GAME_WIDTH, GAME_HEIGHT);
    this.ctx.fillStyle = BACKGROUND_COLOR;
    this.ctx.fillRect(0, 0, GAME_WIDTH, GAME_HEIGHT);

    // Update bubbles
    for (let i = this.bubbles.length - 1; i >= 0; i--) {
      this.bubbles[i].update();
      if (this.bubbles[i].isOffScreen()) {
        this.bubbles.splice(i, 1);
      }
    }

    // Update targets
    for (let i = this.targets.length - 1; i >= 0; i--) {
      if (this.targets[i].isHit()) {
        this.targets.splice(i, 1);
        this.score++;
      }
    }

    // Collision detection
    for (let i = this.bubbles.length - 1; i >= 0; i--) {
      for (let j = this.targets.length - 1; j >= 0; j--) {
        if (this.bubbles[i].collidesWith(this.targets[j])) {
          this.targets[j].hit();
          this.bubbles.splice(i, 1);
          break;
        }
      }
    }

    // Draw bubbles and targets
    for (let bubble of this.bubbles) {
      bubble.draw(this.ctx);
    }
    for (let target of this.targets) {
      target.draw(this.ctx);
    }

    // Draw score and lives
    this.ctx.font = '24px Arial';
    this.ctx.fillStyle = '#000';
    this.ctx.textAlign = 'left';
    this.ctx.textBaseline = 'top';
    this.ctx.fillText(`Score: ${this.score}`, 10, 10);
    this.ctx.fillText(`Lives: ${this.lives}`, 10, 40);

    // Game over
    if (this.lives <= 0) {
      this.ctx.font = '48px Arial';
      this.ctx.fillStyle = '#f00';
      this.ctx.textAlign = 'center';
      this.ctx.textBaseline = 'middle';
      this.ctx.fillText('Game Over!', GAME_WIDTH / 2, GAME_HEIGHT / 2);
      return;
    }
  }

  // Handle mouse click
  handleMouseClick(event) {
    const x = event.clientX - this.canvas.offsetLeft;
    const y = event.clientY - this.canvas.offsetTop;
    this.bubbles.push(new Bubble(x, y));
  }
}

// Bubble class
class Bubble {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.velX = Math.random() * 5 - 2.5;
    this.velY = -5;
  }

  // Update bubble position
  update() {
    this.x += this.velX;
    this.y += this.velY;
    this.velY += 0.1; // gravity
  }

  // Check if bubble is off screen
  isOffScreen() {
    return this.y > GAME_HEIGHT || this.x < 0 || this.x > GAME_WIDTH;
  }

  // Draw bubble
  draw(ctx) {
    ctx.fillStyle = BUBBLE_COLOR;
    ctx.beginPath();
    ctx.arc(this.x, this.y, BUBBLE_RADIUS, 0, 2 * Math.PI);
    ctx.fill();
  }

  // Check collision with target
  collidesWith(target) {
    const distance = Math.sqrt((this.x - target.x) ** 2 + (this.y - target.y) ** 2);
    return distance < BUBBLE_RADIUS + target.radius;
  }
}

// Target class
class Target {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.radius = 30;
    this.hit = false;
  }

  // Draw target
  draw(ctx) {
    ctx.fillStyle = '#00ff00';
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
    ctx.fill();
  }

  // Check if target is hit
  isHit() {
    return this.hit;
  }

  // Mark target as hit
  hit() {
    this.hit = true;
  }
}

// Initialize game
const canvas = document.getElementById('game-canvas');
const game = new Game(canvas);

// Handle mouse click
canvas.addEventListener('click', (event) => game.handleMouseClick(event));
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bubble Shooter</title>
  <style>
    /* Add some basic styling */
    canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="game-canvas"></canvas>
  <script src="bubble-shooter.js"></script>
</body>
</html>
```
