"""
Generated Code Metadata:
========================
Original URL: https://www.gardenpathquilts.com
Prompt: Generate a simple quilting pattern using JavaScript, focusing on geometric shapes commonly found in quilts.
Generated: DETERMINISTIC_adb14fbe4360e13d
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple Quilting Pattern Generator using HTML5 Canvas

// Set up the canvas and context
const canvas = document.getElementById('quiltCanvas');
const ctx = canvas.getContext('2d');

// Set canvas dimensions
canvas.width = 800;
canvas.height = 800;

// Function to draw a square
function drawSquare(x, y, size, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, size, size);
}

// Function to draw a triangle
function drawTriangle(x, y, size, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + size / 2, y - size);
    ctx.lineTo(x + size, y);
    ctx.closePath();
    ctx.fill();
}

// Function to draw a circle
function drawCircle(x, y, radius, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.closePath();
    ctx.fill();
}

// Function to generate a simple quilt pattern
function generateQuiltPattern(rows, cols, size) {
    const colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A1'];

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const x = col * size;
            const y = row * size;
            const shapeType = Math.floor(Math.random() * 3); // Randomly choose shape

            // Select a random color
            const color = colors[Math.floor(Math.random() * colors.length)];

            // Draw the selected shape
            switch (shapeType) {
                case 0:
                    drawSquare(x, y, size, color);
                    break;
                case 1:
                    drawTriangle(x, y, size, color);
                    break;
                case 2:
                    drawCircle(x + size / 2, y + size / 2, size / 2, color);
                    break;
                default:
                    console.error('Invalid shape type');
            }
        }
    }
}

// Error handling for canvas context
try {
    generateQuiltPattern(8, 8, 100); // Generate a quilt pattern with 8 rows and 8 columns
} catch (error) {
    console.error('Error generating quilt pattern:', error);
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quilt Pattern Generator</title>
    <style>
        canvas {
            border: 1px solid #000;
        }
    </style>
</head>
<body>
    <canvas id="quiltCanvas"></canvas>
    <script src="quiltPattern.js"></script>
</body>
</html>
```
