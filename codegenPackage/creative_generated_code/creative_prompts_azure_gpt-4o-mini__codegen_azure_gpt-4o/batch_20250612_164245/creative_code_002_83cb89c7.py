"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wild-cash.site
Prompt: Can you provide code snippets for creating a Plinko-style game using HTML5 and JavaScript?
Generated: DETERMINISTIC_83cb89c7c0fd1317
Batch ID: 20250612_164245
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
  <title>Plinko Game</title>
  <style>
    canvas {
      border: 1px solid black;
      display: block;
      margin: auto;
    }
  </style>
</head>
<body>
  <canvas id="plinkoCanvas"></canvas>

  <script>
    // Get the canvas element and set up the context
    const canvas = document.getElementById('plinkoCanvas');
    const ctx = canvas.getContext('2d');

    // Set canvas dimensions
    canvas.width = 800;
    canvas.height = 600;

    // Constants used in the game
    const PEG_RADIUS = 10;
    const PEG_SPACING = 50;
    const ROWS = 10;
    const BALL_RADIUS = 10;
    const GRAVITY = 0.3;
    const FRICTION = 0.98;

    // Array to store pegs and ball objects
    const pegs = [];
    const balls = [];

    // Initialize pegs on the canvas
    function createPegs() {
      for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < canvas.width / PEG_SPACING; col++) {
          const offset = row % 2 === 0 ? PEG_SPACING / 2 : 0; // Offset for alternate rows
          const x = col * PEG_SPACING + offset;
          const y = row * PEG_SPACING + PEG_SPACING;
          pegs.push({ x, y });
        }
      }
    }

    // Spawn a new ball at the top
    function createBall() {
      const x = canvas.width / 2; // Start ball in the middle
      const y = BALL_RADIUS; // Start at the very top
      balls.push({ x, y, dx: 0, dy: 0 });
    }

    // Draw pegs on the canvas
    function drawPegs() {
      ctx.fillStyle = 'blue';
      for (const peg of pegs) {
        ctx.beginPath();
        ctx.arc(peg.x, peg.y, PEG_RADIUS, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // Draw balls on the canvas
    function drawBalls() {
      ctx.fillStyle = 'red';
      for (const ball of balls) {
        ctx.beginPath();
        ctx.arc(ball.x, ball.y, BALL_RADIUS, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // Update ball positions and handle collisions with pegs
    function updateBalls() {
      for (const ball of balls) {
        // Apply gravity
        ball.dy += GRAVITY;

        // Update ball position
        ball.x += ball.dx;
        ball.y += ball.dy;

        // Handle collisions with pegs
        for (const peg of pegs) {
          const distX = ball.x - peg.x;
          const distY = ball.y - peg.y;
          const distance = Math.sqrt(distX ** 2 + distY ** 2);

          if (distance < PEG_RADIUS + BALL_RADIUS) {
            // Simple collision response: bounce the ball
            const angle = Math.atan2(distY, distX);
            ball.dx = Math.cos(angle) * ball.dx * FRICTION;
            ball.dy = Math.sin(angle) * ball.dy * FRICTION;
          }
        }

        // Prevent ball from leaving the canvas
        if (ball.x - BALL_RADIUS < 0 || ball.x + BALL_RADIUS > canvas.width) {
          ball.dx *= -FRICTION; // Reverse horizontal direction
          ball.x = Math.max(BALL_RADIUS, Math.min(canvas.width - BALL_RADIUS, ball.x));
        }

        if (ball.y - BALL_RADIUS < 0 || ball.y + BALL_RADIUS > canvas.height) {
          ball.dy *= -FRICTION; // Reverse vertical direction
          ball.y = Math.max(BALL_RADIUS, Math.min(canvas.height - BALL_RADIUS, ball.y));
        }
      }
    }

    // Main game loop
    function gameLoop() {
      // Clear canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw pegs and balls
      drawPegs();
      drawBalls();

      // Update ball positions
      updateBalls();

      // Request next animation frame
      requestAnimationFrame(gameLoop);
    }

    // Initialize the game
    function init() {
      createPegs();    // Create peg layout
      createBall();    // Create initial ball
      gameLoop();      // Start the game loop
    }

    // Start the game
    init();
  </script>
</body>
</html>
```
