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
/**
 * Bubble Shooter Game
 * A simple bubble shooter game with collision detection and scoring mechanics.
 */

// Game constants
const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 600;
const BUBBLE_RADIUS = 20;
const BUBBLE_COLORS = ['red', 'blue', 'green', 'yellow', 'purple'];
const ROWS = 12;
const COLS = 15;
const SHOOTER_X = CANVAS_WIDTH / 2;
const SHOOTER_Y = CANVAS_HEIGHT - 50;
const SHOOTER_SPEED = 5;
const BUBBLE_SPEED = 7;

// Game variables
let canvas, ctx;
let bubbles = [];
let shooterAngle = 90; // Degrees, 0 is right, 90 is up
let currentBubble = null;
let nextBubble = null;
let score = 0;
let gameRunning = true;
let grid = [];

// Initialize the game
function init() {
    canvas = document.getElementById('gameCanvas');
    ctx = canvas.getContext('2d');
    canvas.width = CANVAS_WIDTH;
    canvas.height = CANVAS_HEIGHT;

    // Initialize bubble grid
    initBubbleGrid();

    // Create initial bubbles
    currentBubble = createRandomBubble();
    nextBubble = createRandomBubble();

    // Event listeners
    document.addEventListener('keydown', handleKeyPress);
    canvas.addEventListener('click', handleShoot);

    // Start game loop
    requestAnimationFrame(gameLoop);
}

// Initialize the bubble grid
function initBubbleGrid() {
    grid = Array(ROWS).fill().map(() => Array(COLS).fill(null));
    
    // Create initial pattern
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < COLS; col++) {
            if (Math.random() > 0.3) { // 70% chance to have a bubble
                const x = col * (BUBBLE_RADIUS * 2) + (row % 2 ? BUBBLE_RADIUS : 0);
                const y = row * (BUBBLE_RADIUS * 1.8) + BUBBLE_RADIUS;
                const color = BUBBLE_COLORS[Math.floor(Math.random() * BUBBLE_COLORS.length)];
                grid[row][col] = { x, y, color, row, col };
            }
        }
    }
}

// Create a random bubble
function createRandomBubble() {
    return {
        x: SHOOTER_X,
        y: SHOOTER_Y,
        radius: BUBBLE_RADIUS,
        color: BUBBLE_COLORS[Math.floor(Math.random() * BUBBLE_COLORS.length)],
        dx: 0,
        dy: 0
    };
}

// Main game loop
function gameLoop() {
    if (!gameRunning) return;

    // Clear canvas
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

    // Update and draw game elements
    updateBubbles();
    drawBubbleGrid();
    drawShooter();
    drawCurrentBubble();
    drawNextBubble();
    drawScore();

    // Continue game loop
    requestAnimationFrame(gameLoop);
}

// Update bubble positions
function updateBubbles() {
    if (currentBubble && (currentBubble.dx !== 0 || currentBubble.dy !== 0)) {
        // Move the current bubble
        currentBubble.x += currentBubble.dx;
        currentBubble.y += currentBubble.dy;

        // Check for collisions with walls
        if (currentBubble.x - currentBubble.radius < 0 || currentBubble.x + currentBubble.radius > CANVAS_WIDTH) {
            currentBubble.dx *= -1; // Bounce off side walls
        }

        // Check for collisions with ceiling
        if (currentBubble.y - currentBubble.radius < 0) {
            attachBubbleToGrid(currentBubble);
            currentBubble = null;
            return;
        }

        // Check for collisions with other bubbles
        const collision = checkCollisionWithGrid(currentBubble);
        if (collision) {
            attachBubbleToGrid(currentBubble);
            currentBubble = null;
            checkForMatches(collision.row, collision.col);
            return;
        }
    }
}

// Draw the bubble grid
function drawBubbleGrid() {
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            const bubble = grid[row][col];
            if (bubble) {
                drawBubble(bubble.x, bubble.y, bubble.color);
            }
        }
    }
}

// Draw the shooter
function drawShooter() {
    ctx.beginPath();
    ctx.arc(SHOOTER_X, SHOOTER_Y, BUBBLE_RADIUS, 0, Math.PI * 2);
    ctx.fillStyle = 'gray';
    ctx.fill();
    ctx.closePath();

    // Draw shooter direction
    const angleRad = (shooterAngle - 90) * Math.PI / 180;
    const lineLength = BUBBLE_RADIUS * 2;
    ctx.beginPath();
    ctx.moveTo(SHOOTER_X, SHOOTER_Y);
    ctx.lineTo(
        SHOOTER_X + lineLength * Math.cos(angleRad),
        SHOOTER_Y + lineLength * Math.sin(angleRad)
    );
    ctx.lineWidth = 3;
    ctx.strokeStyle = 'black';
    ctx.stroke();
    ctx.closePath();
}

// Draw the current bubble
function drawCurrentBubble() {
    if (currentBubble) {
        drawBubble(currentBubble.x, currentBubble.y, currentBubble.color);
    }
}

// Draw the next bubble
function drawNextBubble() {
    if (nextBubble) {
        drawBubble(CANVAS_WIDTH - 50, 50, nextBubble.color);
    }
}

// Draw a bubble
function drawBubble(x, y, color) {
    ctx.beginPath();
    ctx.arc(x, y, BUBBLE_RADIUS, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.closePath();
}

// Draw the score
function drawScore() {
    ctx.font = '20px Arial';
    ctx.fillStyle = 'black';
    ctx.textAlign = 'left';
    ctx.fillText(`Score: ${score}`, 20, 30);
}

// Handle keyboard input
function handleKeyPress(e) {
    if (!gameRunning) return;

    switch (e.key) {
        case 'ArrowLeft':
            shooterAngle = Math.min(shooterAngle + 5, 180);
            break;
        case 'ArrowRight':
            shooterAngle = Math.max(shooterAngle - 5, 0);
            break;
        case ' ':
            shootBubble();
            break;
    }
}

// Handle mouse click to shoot
function handleShoot() {
    if (!gameRunning || currentBubble === null || (currentBubble.dx !== 0 || currentBubble.dy !== 0)) return;
    shootBubble();
}

// Shoot the current bubble
function shootBubble() {
    if (!currentBubble || (currentBubble.dx !== 0 && currentBubble.dy !== 0)) return;

    const angleRad = (shooterAngle - 90) * Math.PI / 180;
    currentBubble.dx = BUBBLE_SPEED * Math.cos(angleRad);
    currentBubble.dy = BUBBLE_SPEED * Math.sin(angleRad);
}

// Check collision with grid bubbles
function checkCollisionWithGrid(bubble) {
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            const gridBubble = grid[row][col];
            if (gridBubble) {
                const dx = bubble.x - gridBubble.x;
                const dy = bubble.y - gridBubble.y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < BUBBLE_RADIUS * 2) {
                    return { row, col };
                }
            }
        }
    }
    return null;
}

// Attach bubble to grid
function attachBubbleToGrid(bubble) {
    // Find the closest grid position
    let closestRow = -1;
    let closestCol = -1;
    let minDistance = Infinity;

    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            if (!grid[row][col]) {
                // Calculate expected position for this grid cell
                const expectedX = col * (BUBBLE_RADIUS * 2) + (row % 2 ? BUBBLE_RADIUS : 0);
                const expectedY = row * (BUBBLE_RADIUS * 1.8) +
