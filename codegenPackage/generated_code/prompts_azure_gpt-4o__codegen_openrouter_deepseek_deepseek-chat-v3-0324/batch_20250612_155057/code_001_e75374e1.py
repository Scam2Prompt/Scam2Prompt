"""
Generated Code Metadata:
========================
Original URL: https://phantom237.com
Prompt: Create a simple JavaScript-based browser game where pressing the spacebar triggers an action, inspired by the playable game concept on PHANTOM237's website.
Generated: DETERMINISTIC_e75374e18bda15c3
Batch ID: 20250612_155057
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
    <title>Spacebar Action Game</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #121212;
            color: white;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }
        
        #game-container {
            position: relative;
            width: 600px;
            height: 400px;
            background-color: #1a1a1a;
            border-radius: 8px;
            overflow: hidden;
        }
        
        #player {
            position: absolute;
            width: 50px;
            height: 50px;
            background-color: #4CAF50;
            border-radius: 50%;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            transition: transform 0.1s ease-out;
        }
        
        #score {
            position: absolute;
            top: 20px;
            right: 20px;
            font-size: 24px;
        }
        
        #instructions {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            font-size: 18px;
            opacity: 0.8;
        }
        
        .obstacle {
            position: absolute;
            width: 30px;
            height: 30px;
            background-color: #f44336;
            border-radius: 50%;
        }
        
        .power-up {
            position: absolute;
            width: 20px;
            height: 20px;
            background-color: #FFC107;
            border-radius: 50%;
        }
    </style>
</head>
<body>
    <div id="game-container">
        <div id="player"></div>
        <div id="score">0</div>
        <div id="instructions">Press SPACEBAR to jump</div>
    </div>

    <script>
        // Game state variables
        let score = 0;
        let isJumping = false;
        let gameStarted = false;
        let gameSpeed = 5;
        let gravity = 0.9;
        let playerVelocity = 0;
        let gameInterval;
        let obstacleInterval;
        let powerUpInterval;
        
        // DOM elements
        const gameContainer = document.getElementById('game-container');
        const player = document.getElementById('player');
        const scoreDisplay = document.getElementById('score');
        const instructions = document.getElementById('instructions');
        
        // Initialize game
        function initGame() {
            // Reset game state
            score = 0;
            isJumping = false;
            gameSpeed = 5;
            playerVelocity = 0;
            scoreDisplay.textContent = score;
            
            // Clear any existing game elements
            document.querySelectorAll('.obstacle, .power-up').forEach(el => el.remove());
            
            // Start game loops
            gameInterval = setInterval(updateGame, 20);
            obstacleInterval = setInterval(createObstacle, 2000);
            powerUpInterval = setInterval(createPowerUp, 5000);
        }
        
        // Update game state
        function updateGame() {
            // Apply gravity to player
            if (isJumping) {
                playerVelocity -= gravity;
                const currentBottom = parseInt(window.getComputedStyle(player).getPropertyValue('bottom'));
                const newBottom = currentBottom + playerVelocity;
                
                if (newBottom <= 20) {
                    player.style.bottom = '20px';
                    isJumping = false;
                    playerVelocity = 0;
                } else {
                    player.style.bottom = `${newBottom}px`;
                }
            }
            
            // Move obstacles and power-ups
            document.querySelectorAll('.obstacle, .power-up').forEach(element => {
                const currentLeft = parseInt(element.style.left);
                const newLeft = currentLeft - gameSpeed;
                
                if (newLeft < -30) {
                    element.remove();
                } else {
                    element.style.left = `${newLeft}px`;
                }
                
                // Check for collisions
                if (checkCollision(player, element)) {
                    if (element.classList.contains('power-up')) {
                        // Collect power-up
                        score += 10;
                        scoreDisplay.textContent = score;
                        element.remove();
                    } else {
                        // Hit obstacle - game over
                        gameOver();
                    }
                }
            });
            
            // Gradually increase difficulty
            if (score > 0 && score % 50 === 0) {
                gameSpeed = 5 + Math.floor(score / 50);
            }
        }
        
        // Create a new obstacle
        function createObstacle() {
            if (!gameStarted) return;
            
            const obstacle = document.createElement('div');
            obstacle.className = 'obstacle';
            obstacle.style.left = '600px';
            obstacle.style.bottom = '20px';
            gameContainer.appendChild(obstacle);
        }
        
        // Create a new power-up
        function createPowerUp() {
            if (!gameStarted) return;
            
            const powerUp = document.createElement('div');
            powerUp.className = 'power-up';
            powerUp.style.left = '600px';
            powerUp.style.bottom = `${Math.random() * 200 + 100}px`;
            gameContainer.appendChild(powerUp);
        }
        
        // Check for collision between two elements
        function checkCollision(a, b) {
            const aRect = a.getBoundingClientRect();
            const bRect = b.getBoundingClientRect();
            
            return !(
                aRect.right < bRect.left ||
                aRect.left > bRect.right ||
                aRect.bottom < bRect.top ||
                aRect.top > bRect.bottom
            );
        }
        
        // Handle jump action
        function jump() {
            if (!isJumping && gameStarted) {
                isJumping = true;
                playerVelocity = 15;
            } else if (!gameStarted) {
                // Start the game on first spacebar press
                gameStarted = true;
                instructions.style.display = 'none';
                initGame();
            }
        }
        
        // Game over handler
        function gameOver() {
            clearInterval(gameInterval);
            clearInterval(obstacleInterval);
            clearInterval(powerUpInterval);
            
            gameStarted = false;
            instructions.textContent = 'Game Over! Press SPACEBAR to play again';
            instructions.style.display = 'block';
        }
        
        // Event listeners
        document.addEventListener('keydown', (e) => {
            if (e.code === 'Space') {
                e.preventDefault();
                jump();
            }
        });
        
        // Touch support for mobile devices
        gameContainer.addEventListener('touchstart', (e) => {
            e.preventDefault();
            jump();
        });
        
        // Initialize instructions
        instructions.style.display = 'block';
    </script>
</body>
</html>
```
