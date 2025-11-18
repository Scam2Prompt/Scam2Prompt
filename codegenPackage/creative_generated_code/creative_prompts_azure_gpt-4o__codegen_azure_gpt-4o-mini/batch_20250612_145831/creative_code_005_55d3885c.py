"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simons-17h.pages.dev
Prompt: Develop HTML and CSS code for a "colour-in" feature inspired by Simon's Cat, where users can digitally colour Simon's Cat characters.
Generated: DETERMINISTIC_55d3885cb4d5c144
Batch ID: 20250612_145831
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
    <title>Simon's Cat Colour-In Feature</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <h1>Colour Simon's Cat!</h1>
    <div class="color-palette">
        <label for="colorPicker">Choose a color:</label>
        <input type="color" id="colorPicker" value="#000000">
        <button id="clearButton">Clear All</button>
    </div>
    <div class="canvas-container">
        <canvas id="catCanvas" width="500" height="500"></canvas>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
}

/* Styling for the color palette section */
.color-palette {
    margin-bottom: 20px;
}

/* Canvas container styling */
.canvas-container {
    border: 2px solid #ccc;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

```javascript
// script.js

// Get references to the canvas and context
const canvas = document.getElementById('catCanvas');
const ctx = canvas.getContext('2d');

// Set default fill style
let fillColor = '#000000';

// Add event listener for color picker
document.getElementById('colorPicker').addEventListener('input', (event) => {
    fillColor = event.target.value;
});

// Function to draw the outline of Simon's Cat
function drawCatOutline() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.moveTo(250, 100); // Start position
    ctx.bezierCurveTo(200, 50, 300, 50, 250, 100); // Head
    // Draw body and other features...
    ctx.lineWidth = 5;
    ctx.strokeStyle = 'black';
    ctx.stroke();
}

// Event listener for canvas click to fill color
canvas.addEventListener('mousedown', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Simple fill logic (for demonstration, expands to any area would require more logic)
    ctx.fillStyle = fillColor;
    ctx.fillRect(x - 10, y - 10, 20, 20); // Example area to fill
});

// Add clear button functionality
document.getElementById('clearButton').addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawCatOutline(); // Redraw the outline
});

// Initial call to draw the cat outline
drawCatOutline();
```

This code consists of three files: `index.html`, `styles.css`, and `script.js`. The HTML sets up the structure, the CSS styles it, and the JavaScript implements the functionality for the colouring feature.
