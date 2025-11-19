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
// This game simulates a simple ropes obstacle course where the player must jump over obstacles.

class Obstacle {
    constructor(x, y, width, height) {
        this.x = x; // X position of the obstacle
        this.y = y; // Y position of the obstacle
        this.width = width; // Width of the obstacle
        this.height = height; // Height of the obstacle
        this.isVisible = true; // Visibility status of the obstacle
    }

    // Draw the obstacle on the canvas
    draw(ctx) {
        if (this.isVisible) {
            ctx.fillStyle = 'brown';
            ctx.fillRect(this.x, this.y, this.width, this.height);
        }
    }

    // Check for collision with the player
    checkCollision(player) {
        if (this.isVisible && 
            player.x < this.x + this.width &&
            player.x + player.width > this.x &&
            player.y < this.y + this.height &&
            player.y + player.height > this.y) {
            return true; // Collision detected
        }
        return false; // No collision
    }
}

class Player {
    constructor(x, y, width, height) {
        this.x = x; // X position of the player
        this.y = y; // Y position of the player
        this.width = width; // Width of the player
        this.height = height; // Height of the player
        this.jumpHeight = 100; // Height of the jump
        this.isJumping = false; // Jumping status
    }

    // Draw the player on the canvas
    draw(ctx) {
        ctx.fillStyle = 'blue';
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }

    // Make the player jump
    jump() {
        if (!this.isJumping) {
            this.isJumping = true;
            this.y -= this.jumpHeight; // Move player up
            setTimeout(() => {
                this.y += this.jumpHeight; // Move player down after jump
                this.isJumping = false;
            }, 500); // Duration of the jump
        }
    }
}

// Game class to manage the game state
class Game {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.player = new Player(50, this.canvas.height - 60, 30, 30);
        this.obstacles = [];
        this.score = 0;
        this.isGameOver = false;

        // Start the game loop
        this.startGame();
    }

    // Start the game loop
    startGame() {
        this.generateObstacles();
        this.gameLoop();
        this.setupControls();
    }

    // Generate obstacles at random intervals
    generateObstacles() {
        setInterval(() => {
            const obstacleWidth = Math.random() * 50 + 20;
            const obstacleHeight = Math.random() * 20 + 20;
            const obstacleX = this.canvas.width;
            const obstacleY = this.canvas.height - obstacleHeight - 30; // Ground level
            this.obstacles.push(new Obstacle(obstacleX, obstacleY, obstacleWidth, obstacleHeight));
        }, 2000); // New obstacle every 2 seconds
    }

    // Main game loop
    gameLoop() {
        if (this.isGameOver) return;

        this.update();
        this.draw();
        requestAnimationFrame(() => this.gameLoop());
    }

    // Update game state
    update() {
        // Move obstacles to the left
        this.obstacles.forEach(obstacle => {
            obstacle.x -= 5; // Speed of obstacles
            if (obstacle.x + obstacle.width < 0) {
                obstacle.isVisible = false; // Remove off-screen obstacles
                this.score++; // Increase score
            }
            // Check for collision
            if (obstacle.checkCollision(this.player)) {
                this.isGameOver = true; // End game on collision
                alert('Game Over! Your score: ' + this.score);
            }
        });
        // Filter out invisible obstacles
        this.obstacles = this.obstacles.filter(obstacle => obstacle.isVisible);
    }

    // Draw everything on the canvas
    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height); // Clear canvas
        this.player.draw(this.ctx); // Draw player
        this.obstacles.forEach(obstacle => obstacle.draw(this.ctx)); // Draw obstacles
        this.ctx.fillStyle = 'black';
        this.ctx.fillText('Score: ' + this.score, 10, 20); // Display score
    }

    // Setup controls for the game
    setupControls() {
        document.addEventListener('keydown', (event) => {
            if (event.code === 'Space') {
                this.player.jump(); // Jump on space key press
            }
        });
    }
}

// Initialize the game when the window loads
window.onload = () => {
    const game = new Game('gameCanvas');
};
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ropes Obstacle Course Game</title>
    <style>
        canvas {
            border: 1px solid black;
            display: block;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="800" height="400"></canvas>
    <script src="game.js"></script>
</body>
</html>
```

This code creates a simple ropes obstacle course game where the player can jump over obstacles using the spacebar. The game keeps track of the score and ends when the player collides with an obstacle.
