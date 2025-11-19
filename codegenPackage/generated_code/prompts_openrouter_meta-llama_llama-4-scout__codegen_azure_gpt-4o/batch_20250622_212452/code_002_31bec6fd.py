"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: "Generate a JavaScript code to create a simple game for a Ropes Obstacle Course, similar to the one at Playland Kenya."
Generated: DETERMINISTIC_31bec6fda3f05a1c
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Ropes Obstacle Course Game
// This game simulates a simple obstacle course where the player navigates through ropes.
// The player must avoid obstacles and reach the finish line to win.

// Game Configuration
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
canvas.width = 800; // Width of the game area
canvas.height = 400; // Height of the game area

// Player Configuration
const player = {
  x: 50, // Starting X position
  y: canvas.height / 2, // Starting Y position
  width: 30, // Player width
  height: 30, // Player height
  color: "blue", // Player color
  speed: 5, // Movement speed
};

// Obstacles Configuration
const obstacles = [];
const obstacleFrequency = 100; // Frequency of obstacle generation
const obstacleSpeed = 3; // Speed of obstacles
const obstacleWidth = 20; // Width of obstacles
const obstacleHeight = 100; // Height of obstacles

// Game State
let isGameRunning = true;
let score = 0;

// Event Listener for Player Movement
document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowUp" && player.y > 0) {
    player.y -= player.speed;
  } else if (event.key === "ArrowDown" && player.y < canvas.height - player.height) {
    player.y += player.speed;
  }
});

// Function to Draw the Player
function drawPlayer() {
  ctx.fillStyle = player.color;
  ctx.fillRect(player.x, player.y, player.width, player.height);
}

// Function to Generate Obstacles
function generateObstacle() {
  const obstacleY = Math.random() * (canvas.height - obstacleHeight);
  obstacles.push({ x: canvas.width, y: obstacleY, width: obstacleWidth, height: obstacleHeight });
}

// Function to Draw Obstacles
function drawObstacles() {
  ctx.fillStyle = "red";
  obstacles.forEach((obstacle) => {
    ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
  });
}

// Function to Update Obstacles
function updateObstacles() {
  obstacles.forEach((obstacle) => {
    obstacle.x -= obstacleSpeed;
  });

  // Remove obstacles that go off-screen
  obstacles = obstacles.filter((obstacle) => obstacle.x + obstacle.width > 0);
}

// Function to Check for Collisions
function checkCollisions() {
  obstacles.forEach((obstacle) => {
    if (
      player.x < obstacle.x + obstacle.width &&
      player.x + player.width > obstacle.x &&
      player.y < obstacle.y + obstacle.height &&
      player.y + player.height > obstacle.y
    ) {
      isGameRunning = false; // End the game if collision occurs
    }
  });
}

// Function to Update the Score
function updateScore() {
  score += 1; // Increment score
}

// Function to Display the Score
function displayScore() {
  ctx.fillStyle = "black";
  ctx.font = "20px Arial";
  ctx.fillText(`Score: ${score}`, 10, 30);
}

// Main Game Loop
function gameLoop() {
  if (!isGameRunning) {
    ctx.fillStyle = "black";
    ctx.font = "40px Arial";
    ctx.fillText("Game Over!", canvas.width / 2 - 100, canvas.height / 2);
    return; // Stop the game loop
  }

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw and update game elements
  drawPlayer();
  drawObstacles();
  updateObstacles();
  checkCollisions();
  updateScore();
  displayScore();

  // Generate obstacles periodically
  if (score % obstacleFrequency === 0) {
    generateObstacle();
  }

  // Request the next frame
  requestAnimationFrame(gameLoop);
}

// Start the Game
gameLoop();
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ropes Obstacle Course Game</title>
  <style>
    canvas {
      border: 2px solid black;
      display: block;
      margin: 0 auto;
    }
  </style>
</head>
<body>
  <canvas id="gameCanvas"></canvas>
  <script src="game.js"></script>
</body>
</html>
```
