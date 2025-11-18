"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jito.pro
Prompt: Write JavaScript code for a bubble-shooter game similar to the one described in the "Bubble-shooter" category on jito.pro, including collision detection and scoring mechanics.
Generated: DETERMINISTIC_c9f661e7f4eb6fdf
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Bubble Shooter Game

// Canvas setup
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Game constants
const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 600;
const BUBBLE_RADIUS = 20;
const BUBBLE_COLORS = ['red', 'green', 'blue', 'yellow', 'purple'];

canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;

// Game variables
let bubbles = [];
let score = 0;

// Bubble class
class Bubble {
    constructor(x, y, color) {
        this.x = x;
        this.y = y;
        this.color = color;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, BUBBLE_RADIUS, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }

    // Collision detection
    isColliding(other) {
        const dx = this.x - other.x;
        const dy = this.y - other.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        return distance < BUBBLE_RADIUS * 2;
    }
}

// Initialize game
function init() {
    // Generate random bubbles
    for (let i = 0; i < 10; i++) {
        const x = Math.random() * (CANVAS_WIDTH - BUBBLE_RADIUS * 2) + BUBBLE_RADIUS;
        const y = Math.random() * (CANVAS_HEIGHT - BUBBLE_RADIUS * 2) + BUBBLE_RADIUS;
        const color = BUBBLE_COLORS[Math.floor(Math.random() * BUBBLE_COLORS.length)];
        bubbles.push(new Bubble(x, y, color));
    }
    draw();
}

// Draw function
function draw() {
    // Clear the canvas
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

    // Draw bubbles
    bubbles.forEach(bubble => bubble.draw());

    // Draw score
    ctx.fillStyle = 'black';
    ctx.font = '20px Arial';
    ctx.fillText(`Score: ${score}`, 10, 30);
}

// Click event to shoot bubble
canvas.addEventListener('click', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    const shotBubble = new Bubble(x, y, BUBBLE_COLORS[Math.floor(Math.random() * BUBBLE_COLORS.length)]);
    checkCollisions(shotBubble);
});

// Check collisions with existing bubbles
function checkCollisions(shotBubble) {
    let matchedBubbles = [];

    bubbles.forEach((bubble, index) => {
        if (shotBubble.isColliding(bubble)) {
            matchedBubbles.push(index);
        }
    });

    // Update score and remove matched bubbles
    if (matchedBubbles.length > 0) {
        score += matchedBubbles.length;
        matchedBubbles.reverse().forEach(index => bubbles.splice(index, 1));
        draw();
    }
}

// Error handling for canvas not found
if (!canvas) {
    console.error('Canvas element not found. Please ensure the HTML contains an element with id "gameCanvas".');
}

// Start the game
init();
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bubble Shooter Game</title>
    <style>
        canvas {
            border: 1px solid black;
            display: block;
            margin: auto;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <script src="bubbleShooter.js"></script>
</body>
</html>
```
