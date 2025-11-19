"""
Generated Code Metadata:
========================
Original URL: https://doodles.team
Prompt: Generate a code snippet that demonstrates how to implement a doodle feature in a web application.
Generated: DETERMINISTIC_101cd552abdc8e91
Batch ID: 20250612_135804
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
  <title>Doodle Feature</title>
  <style>
    /* Basic styling for the canvas */
    canvas {
      border: 1px solid #000;
      cursor: crosshair;
    }
  </style>
</head>
<body>
  <h1>Doodle Feature</h1>
  <p>Draw on the canvas below:</p>
  <canvas id="doodleCanvas" width="800" height="400"></canvas>
  <button id="clearCanvas">Clear Canvas</button>

  <script>
    // Select the canvas and button elements
    const canvas = document.getElementById('doodleCanvas');
    const clearButton = document.getElementById('clearCanvas');
    const ctx = canvas.getContext('2d');

    // Variables to track drawing state
    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;

    // Function to start drawing
    canvas.addEventListener('mousedown', (e) => {
      isDrawing = true;
      [lastX, lastY] = [e.offsetX, e.offsetY];
    });

    // Function to draw on the canvas
    canvas.addEventListener('mousemove', (e) => {
      if (!isDrawing) return; // Exit if not drawing
      ctx.beginPath();
      ctx.moveTo(lastX, lastY); // Start from the last position
      ctx.lineTo(e.offsetX, e.offsetY); // Draw to the current position
      ctx.strokeStyle = '#000'; // Set the stroke color
      ctx.lineWidth = 2; // Set the line width
      ctx.stroke(); // Render the line
      [lastX, lastY] = [e.offsetX, e.offsetY]; // Update the last position
    });

    // Function to stop drawing
    canvas.addEventListener('mouseup', () => {
      isDrawing = false;
    });

    // Handle mouse leaving the canvas (stop drawing)
    canvas.addEventListener('mouseleave', () => {
      isDrawing = false;
    });

    // Clear the canvas when the button is clicked
    clearButton.addEventListener('click', () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the entire canvas
    });

    // Error handling: Ensure the canvas context is available
    if (!ctx) {
      console.error('Failed to get canvas context. Please check your browser compatibility.');
    }
  </script>
</body>
</html>
```
