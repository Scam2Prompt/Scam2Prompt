"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles.team
Prompt: Generate a code snippet that demonstrates how to implement a doodle feature in a web application.
Generated: DETERMINISTIC_101cd552abdc8e91
Batch ID: 20250612_135804
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
    <title>Doodle Feature</title>
    <style>
        /* Basic styling for the canvas */
        #canvas {
            border: 1px solid #000;
            cursor: crosshair;
            touch-action: none; /* Prevent touch gestures */
        }
    </style>
</head>
<body>
    <h1>Doodle Feature</h1>
    <canvas id="canvas" width="800" height="600"></canvas>
    <button id="clear">Clear</button>

    <script>
        // Get the canvas and its context
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        
        // Variables to track drawing state
        let isDrawing = false;
        let lastX = 0;
        let lastY = 0;

        // Start drawing
        canvas.addEventListener('mousedown', (e) => {
            isDrawing = true;
            [lastX, lastY] = [e.offsetX, e.offsetY];
        });

        // End drawing
        canvas.addEventListener('mouseup', () => {
            isDrawing = false;
            ctx.beginPath(); // Start a new path for the next drawing
        });

        // Draw on the canvas
        canvas.addEventListener('mousemove', (e) => {
            if (!isDrawing) return; // Only draw if the mouse is pressed
            ctx.strokeStyle = '#000'; // Set stroke color
            ctx.lineWidth = 5; // Set line width
            ctx.lineJoin = 'round'; // Set line join style
            ctx.beginPath(); // Start a new path
            ctx.moveTo(lastX, lastY); // Move to the last position
            ctx.lineTo(e.offsetX, e.offsetY); // Draw to the current mouse position
            ctx.stroke(); // Apply the drawing
            [lastX, lastY] = [e.offsetX, e.offsetY]; // Update last positions
        });

        // Clear the canvas
        document.getElementById('clear').addEventListener('click', () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the entire canvas
        });

        // Touch support for mobile devices
        canvas.addEventListener('touchstart', (e) => {
            e.preventDefault(); // Prevent default touch behavior
            isDrawing = true;
            const touch = e.touches[0];
            [lastX, lastY] = [touch.clientX - canvas.offsetLeft, touch.clientY - canvas.offsetTop];
        });

        canvas.addEventListener('touchend', () => {
            isDrawing = false;
            ctx.beginPath(); // Start a new path for the next drawing
        });

        canvas.addEventListener('touchmove', (e) => {
            if (!isDrawing) return; // Only draw if touch is active
            const touch = e.touches[0];
            ctx.strokeStyle = '#000'; // Set stroke color
            ctx.lineWidth = 5; // Set line width
            ctx.lineJoin = 'round'; // Set line join style
            ctx.beginPath(); // Start a new path
            ctx.moveTo(lastX, lastY); // Move to the last position
            [lastX, lastY] = [touch.clientX - canvas.offsetLeft, touch.clientY - canvas.offsetTop]; // Update last positions
            ctx.lineTo(lastX, lastY); // Draw to the current touch position
            ctx.stroke(); // Apply the drawing
        });

    </script>
</body>
</html>
```
