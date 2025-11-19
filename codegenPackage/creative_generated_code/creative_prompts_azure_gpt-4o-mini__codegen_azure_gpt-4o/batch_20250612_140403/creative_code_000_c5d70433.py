"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://red.game
Prompt: Generate a code snippet for a browser-based game that incorporates surveillance themes similar to those found in RED's TRON concept.
Generated: DETERMINISTIC_c5d70433cfc879a6
Batch ID: 20250612_140403
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
  <title>Surveillance Game</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      background: #000;
      color: #FFF;
      font-family: Arial, sans-serif;
    }

    canvas {
      display: block;
    }

    #game-over {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      display: none;
    }

    #game-over h1 {
      font-size: 48px;
      margin: 0;
    }

    #restart-button {
      font-size: 24px;
      padding: 10px 20px;
      background: #222;
      color: #FFF;
      border: none;
      cursor: pointer;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <canvas id="gameCanvas"></canvas>
  <div id="game-over">
    <h1>Game Over</h1>
    <button id="restart-button">Restart</button>
  </div>
  <script>
    // Constants for game dimensions
    const canvas = document.getElementById('gameCanvas'); 
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Player and surveillance drone properties
    const player = { x: canvas.width / 2, y: canvas.height - 50, size: 20, speed: 5 };
    const drones = [];
    const droneSpeed = 2;
    const droneSpawnInterval = 2000; // milliseconds
    let isGameRunning = true;

    // Game Over UI components
    const gameOverScreen = document.getElementById('game-over');
    const restartButton = document.getElementById('restart-button');

    // Add event listeners
    document.addEventListener('keydown', handlePlayerMovement);
    restartButton.addEventListener('click', restartGame);

    // Error handling for game loop
    try {
      // Game loop
      function gameLoop() {
        if (!isGameRunning) return;
        updateGameState();
        renderGame();
        requestAnimationFrame(gameLoop);
      }
      
      // Update Drone positions and handle collisions
      function updateGameState() {
        drones.forEach(drone => {
          drone.y += droneSpeed;
          if (isColliding(player, drone)) {
            endGame();
          }
        });
      }
