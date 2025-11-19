"""
Generated Code Metadata:
========================
Original URL: https://nftbuy.site
Prompt: Generate a code snippet that creates a simple HTML5 game similar to the "Zombie Mission 13" featured on NFTBuy, focusing on player controls and enemy interactions.
Generated: DETERMINISTIC_37d9ca547585c003
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Zombie Mission Game</title>
  <style>
    /* Basic styling for the game canvas */
    body {
      margin: 0;
      overflow: hidden;
    }
    canvas {
      display: block;
      background: #333;
    }
  </style>
</head>
<body>
  <canvas id="gameCanvas"></canvas>
  <script>
    // Get the canvas and set up the context
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // Set canvas dimensions to fill the window
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Game variables
    const player = {
      x: canvas.width / 2,
      y: canvas.height - 50,
      width: 40,
      height: 40,
      color: 'blue',
      speed: 5,
      dx: 0,
      dy: 0
    };

    const enemies = [];
    const enemySpawnInterval = 2000; // Spawn an enemy every 2 seconds
    const enemySpeed = 2;

    let lastEnemySpawnTime = 0;

    // Key press event listeners for player movement
    document.addEventListener('keydown', (e) => {
      switch (e.key) {
        case 'ArrowLeft':
          player.dx = -player.speed;
          break;
        case 'ArrowRight':
          player.dx = player.speed;
          break;
        case 'ArrowUp':
          player.dy = -player.speed;
          break;
        case 'ArrowDown':
          player.dy = player.speed;
          break;
      }
    });

    document.addEventListener('keyup', (e) => {
      switch (e.key) {
        case 'ArrowLeft':
        case 'ArrowRight':
          player.dx = 0;
          break;
        case 'ArrowUp':
        case 'ArrowDown':
          player.dy = 0;
          break;
      }
    });

    // Function to spawn a new enemy
    function spawnEnemy() {
      const enemy = {
        x: Math.random() * canvas.width,
        y: 0,
        width: 30,
        height: 30,
        color: 'red',
        dy: enemySpeed
      };
      enemies.push(enemy);
    }

    // Function to update the player's position
    function updatePlayer() {
      player.x += player.dx;
      player.y += player.dy;

      // Prevent player from moving out of bounds
      if (player.x < 0) player.x = 0;
      if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
      if (player.y < 0) player.y = 0;
      if (player.y + player.height > canvas.height) player.y = canvas.height - player.height;
    }

    // Function to update enemies' positions
    function updateEnemies() {
      for (let i = enemies.length - 1; i >= 0; i--) {
        const enemy = enemies[i];
        enemy.y += enemy.dy;

        // Remove enemy if it goes off-screen
        if (enemy.y > canvas.height) {
          enemies.splice(i, 1);
        }

        // Check for collision with the player
        if (
          player.x < enemy.x + enemy.width &&
          player.x + player.width > enemy.x &&
          player.y < enemy.y + enemy.height &&
          player.y + player.height > enemy.y
        ) {
          alert('Game Over!');
          document.location.reload();
        }
      }
    }

    // Function to draw the player
    function drawPlayer() {
      ctx.fillStyle = player.color;
      ctx.fillRect(player.x, player.y, player.width, player.height);
    }

    // Function to draw enemies
    function drawEnemies() {
      enemies.forEach((enemy) => {
        ctx.fillStyle = enemy.color;
        ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
      });
    }

    // Main game loop
    function gameLoop(timestamp) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Spawn enemies at regular intervals
      if (timestamp - lastEnemySpawnTime > enemySpawnInterval) {
        spawnEnemy();
        lastEnemySpawnTime = timestamp;
      }

      updatePlayer();
      updateEnemies();

      drawPlayer();
      drawEnemies();

      requestAnimationFrame(gameLoop);
    }

    // Start the game loop
    requestAnimationFrame(gameLoop);
  </script>
</body>
</html>
```
