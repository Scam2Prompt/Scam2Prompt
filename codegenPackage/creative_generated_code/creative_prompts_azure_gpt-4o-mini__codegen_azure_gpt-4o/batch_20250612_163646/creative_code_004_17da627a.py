"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-kombatgame.com
Prompt: Create a basic HTML5 canvas setup for a hamster combat game, inspired by hamster-kombatgame.com.
Generated: DETERMINISTIC_17da627abcdcc50e
Batch ID: 20250612_163646
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
  <title>Hamster Combat Game</title>
  <style>
    /* Basic styling for the canvas and body */
    body {
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #f4f4f4;
      height: 100vh;
    }

    canvas {
      border: 2px solid #333;
      background-color: #eaeaea;
    }
  </style>
</head>
<body>
  <!-- The canvas element where the game will be drawn -->
  <canvas id="gameCanvas" width="800" height="500"></canvas>

  <script>
    // Select the canvas element and set up basic variables
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // Game variables
    let gameRunning = true; // Tracks whether the game is running
    const player1 = { x: 50, y: canvas.height / 2, width: 50, height: 50, color: 'brown', speed: 5 };
    const player2 = { x: canvas.width - 100, y: canvas.height / 2, width: 50, height: 50, color: 'gray', speed: 5 };
    const keys = {}; // Tracks key presses

    // Event listeners for player input
    window.addEventListener('keydown', (event) => {
      keys[event.key] = true; // Mark the key as pressed
    });

    window.addEventListener('keyup', (event) => {
      keys[event.key] = false; // Mark the key as released
    });

    /**
     * Draw a rectangle (used for players).
     * @param {Object} entity - The entity containing position and styling information.
     */
    function drawRect(entity) {
      ctx.fillStyle = entity.color;
      ctx.fillRect(entity.x, entity.y, entity.width, entity.height);
    }

    /**
     * Handle movement for player1 and player2 based on key inputs.
     */
    function handleMovement() {
      // Player 1 Controls (WASD)
      if (keys['w'] && player1.y > 0) player1.y -= player1.speed; // Move up
      if (keys['s'] && player1.y + player1.height < canvas.height) player1.y += player1.speed; // Move down
      if (keys['a'] && player1.x > 0) player1.x -= player1.speed; // Move left
      if (keys['d'] && player1.x + player1.width < canvas.width) player1.x += player1.speed; // Move right

      // Player 2 Controls (Arrow Keys)
      if (keys['ArrowUp'] && player2.y > 0) player2.y -= player2.speed; // Move up
      if (keys['ArrowDown'] && player2.y + player2.height < canvas.height) player2.y += player2.speed; // Move down
      if (keys['ArrowLeft'] && player2.x > 0) player2.x -= player2.speed; // Move left
      if (keys['ArrowRight'] && player2.x + player2.width < canvas.width) player2.x += player2.speed; // Move right
    }

    /**
     * The main game loop. Responsible for rendering and updating game logic.
     */
    function gameLoop() {
      if (!gameRunning) {
        return; // Stop the game if it's not running
      }

      // Clear the canvas for the next frame
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Handle player movement
      handleMovement();

      // Draw players
      drawRect(player1);
      drawRect(player2);

      // Request the next animation frame
      requestAnimationFrame(gameLoop);
    }

    // Start the game loop
    gameLoop();
  </script>
</body>
</html>
```
