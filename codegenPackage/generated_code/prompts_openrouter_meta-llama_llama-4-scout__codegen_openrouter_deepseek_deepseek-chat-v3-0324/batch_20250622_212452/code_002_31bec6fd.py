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
/**
 * Ropes Obstacle Course Game
 * A simple 2D game simulating a ropes obstacle course.
 * Inspired by Playland Kenya's ropes course.
 */

// Game constants
const GAME_WIDTH = 800;
const GAME_HEIGHT = 600;
const PLAYER_WIDTH = 30;
const PLAYER_HEIGHT = 50;
const OBSTACLE_WIDTH = 20;
const OBSTACLE_GAP = 200;
const GRAVITY = 0.5;
const JUMP_FORCE = -10;
const ROPE_WIDTH = 5;
const ROPE_COLOR = '#8B4513';
const PLAYER_COLOR = '#FF0000';
const OBSTACLE_COLOR = '#00FF00';
const BACKGROUND_COLOR = '#87CEEB';

// Game state
let player = {
    x: 100,
    y: GAME_HEIGHT / 2,
    width: PLAYER_WIDTH,
    height: PLAYER_HEIGHT,
    velocityY: 0,
    isJumping: false,
    onRope: false,
    ropeIndex: -1
};

let ropes = [];
let obstacles = [];
let score = 0;
let gameOver = false;
let gameStarted = false;

// Initialize canvas
const canvas = document.createElement('canvas');
canvas.width = GAME_WIDTH;
canvas.height = GAME_HEIGHT;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');

// Event listeners
canvas.addEventListener('click', handleClick);
document.addEventListener('keydown', handleKeyDown);

// Initialize game elements
initializeGame();

/**
 * Initialize game elements (ropes and obstacles)
 */
function initializeGame() {
    // Create ropes
    for (let i = 0; i < 5; i++) {
        ropes.push({
            x: 150 + i * 150,
            y: 200 + Math.random() * 200,
            length: 100 + Math.random() * 100
        });
    }

    // Create initial obstacles
    for (let i = 0; i < 3; i++) {
        createObstacle(300 + i * OBSTACLE_GAP);
    }
}

/**
 * Create a new obstacle at given x position
 * @param {number} x - x position of the obstacle
 */
function createObstacle(x) {
    obstacles.push({
        x: x,
        y: 300 + Math.random() * 200,
        width: OBSTACLE_WIDTH,
        height: OBSTACLE_WIDTH,
        passed: false
    });
}

/**
 * Handle click events
 * @param {Event} e - Click event
 */
function handleClick(e) {
    if (!gameStarted) {
        gameStarted = true;
        requestAnimationFrame(gameLoop);
    } else if (gameOver) {
        resetGame();
    }
}

/**
 * Handle keydown events
 * @param {Event} e - Keydown event
 */
function handleKeyDown(e) {
    if (gameStarted && !gameOver) {
        if (e.code === 'Space') {
            jump();
        }
    }
}

/**
 * Make the player jump
 */
function jump() {
    if (!player.isJumping || player.onRope) {
        player.velocityY = JUMP_FORCE;
        player.isJumping = true;
        player.onRope = false;
    }
}

/**
 * Main game loop
 */
function gameLoop() {
    if (gameOver) return;

    update();
    render();

    if (!gameOver) {
        requestAnimationFrame(gameLoop);
    }
}

/**
 * Update game state
 */
function update() {
    if (!gameStarted) return;

    // Apply gravity
    if (!player.onRope) {
        player.velocityY += GRAVITY;
        player.y += player.velocityY;
    }

    // Check rope collisions
    checkRopeCollisions();

    // Check obstacle collisions
    checkObstacleCollisions();

    // Check boundaries
    if (player.y > GAME_HEIGHT - player.height) {
        player.y = GAME_HEIGHT - player.height;
        player.velocityY = 0;
        player.isJumping = false;
    }

    if (player.y < 0) {
        player.y = 0;
        player.velocityY = 0;
    }

    // Move obstacles
    obstacles.forEach(obstacle => {
        obstacle.x -= 2;

        // Score when passing obstacles
        if (obstacle.x + obstacle.width < player.x && !obstacle.passed) {
            obstacle.passed = true;
            score++;
        }
    });

    // Remove off-screen obstacles and add new ones
    obstacles = obstacles.filter(obstacle => obstacle.x + obstacle.width > 0);
    if (obstacles[obstacles.length - 1].x < GAME_WIDTH - OBSTACLE_GAP) {
        createObstacle(GAME_WIDTH);
    }
}

/**
 * Check collisions with ropes
 */
function checkRopeCollisions() {
    player.onRope = false;
    player.ropeIndex = -1;

    ropes.forEach((rope, index) => {
        if (player.x + player.width > rope.x - ROPE_WIDTH / 2 &&
            player.x < rope.x + ROPE_WIDTH / 2 &&
            player.y + player.height > rope.y &&
            player.y < rope.y + rope.length) {
            
            player.onRope = true;
            player.ropeIndex = index;
            player.velocityY = 0;
            player.y = rope.y + rope.length - player.height;
        }
    });
}

/**
 * Check collisions with obstacles
 */
function checkObstacleCollisions() {
    obstacles.forEach(obstacle => {
        if (player.x < obstacle.x + obstacle.width &&
            player.x + player.width > obstacle.x &&
            player.y < obstacle.y + obstacle.height &&
            player.y + player.height > obstacle.y) {
            
            gameOver = true;
        }
    });
}

/**
 * Render game elements
 */
function render() {
    // Clear canvas
    ctx.fillStyle = BACKGROUND_COLOR;
    ctx.fillRect(0, 0, GAME_WIDTH, GAME_HEIGHT);

    // Draw ropes
    ropes.forEach(rope => {
        ctx.fillStyle = ROPE_COLOR;
        ctx.fillRect(rope.x - ROPE_WIDTH / 2, rope.y, ROPE_WIDTH, rope.length);
    });

    // Draw obstacles
    obstacles.forEach(obstacle => {
        ctx.fillStyle = OBSTACLE_COLOR;
        ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
    });

    // Draw player
    ctx.fillStyle = PLAYER_COLOR;
    ctx.fillRect(player.x, player.y, player.width, player.height);

    // Draw score
    ctx.fillStyle = '#000000';
    ctx.font = '24px Arial';
    ctx.fillText(`Score: ${score}`, 20, 30);

    // Draw start/game over message
    if (!gameStarted) {
        ctx.fillStyle = '#000000';
        ctx.font = '36px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Click to Start', GAME_WIDTH / 2, GAME_HEIGHT / 2);
        ctx.textAlign = 'left';
    } else if (gameOver) {
        ctx.fillStyle = '#000000';
        ctx.font = '36px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Game Over - Click to Restart', GAME_WIDTH / 2, GAME_HEIGHT / 2);
        ctx.textAlign = 'left';
    }
}

/**
 * Reset game state
 */
function resetGame() {
    player = {
        x: 100,
        y: GAME_HEIGHT / 2,
        width: PLAYER_WIDTH,
        height: PLAYER_HEIGHT,
        velocityY: 0,
        isJumping: false,
        onRope: false,
        ropeIndex: -1
    };

    obstacles = [];
    score = 0;
    gameOver = false;
    gameStarted = false;

    // Create initial obstacles
    for (let i = 0; i < 3; i++) {
        createObstacle(300 + i * OBSTACLE_GAP);
    }

    render();
}

// Initial render
render();
```
