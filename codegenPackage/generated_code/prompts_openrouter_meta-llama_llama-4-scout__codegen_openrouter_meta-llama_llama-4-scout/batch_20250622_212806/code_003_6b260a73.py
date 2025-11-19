"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Create a simple online game using JavaScript that can be embedded in a webpage like Square Bear's, which features fun and games.
Generated: DETERMINISTIC_6b260a73cf036a0e
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html is assumed to be in the same directory as this script
// and should contain a canvas element with id 'gameCanvas'

/**
 * Simple Online Game: Square Bear Clone
 */

// Get the canvas element
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Set canvas dimensions
canvas.width = 400;
canvas.height = 400;

// Game variables
let bearX = canvas.width / 2;
let bearY = canvas.height / 2;
let bearSpeedX = 2;
let bearSpeedY = 2;
let bearSize = 50;
let score = 0;

// Game loop
function draw() {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the bear
    ctx.fillStyle = 'yellow';
    ctx.fillRect(bearX, bearY, bearSize, bearSize);

    // Update bear position
    bearX += bearSpeedX;
    bearY += bearSpeedY;

    // Bounce off edges
    if (bearX < 0 || bearX > canvas.width - bearSize) {
        bearSpeedX *= -1;
    }
    if (bearY < 0 || bearY > canvas.height - bearSize) {
        bearSpeedY *= -1;
    }

    // Update score
    score++;
    document.getElementById('score').innerHTML = `Score: ${score}`;

    // Request next frame
    requestAnimationFrame(draw);
}

// Event listeners
canvas.addEventListener('click', () => {
    // Reset game
    bearX = canvas.width / 2;
    bearY = canvas.height / 2;
    score = 0;
    document.getElementById('score').innerHTML = `Score: ${score}`;
});

// Start the game
draw();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Square Bear Game</title>
    <style>
        /* Add some basic styling */
        canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <p id="score">Score: 0</p>
    <script src="script.js"></script>
</body>
</html>
```
