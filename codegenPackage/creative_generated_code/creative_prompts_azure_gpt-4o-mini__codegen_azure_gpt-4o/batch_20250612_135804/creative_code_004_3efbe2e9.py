"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles.team
Prompt: Create a simple HTML and JavaScript example to build a doodle canvas for user interaction.
Generated: DETERMINISTIC_3efbe2e98fe4e9a4
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
  <title>Doodle Canvas</title>
  <style>
    /* Style for the canvas element */
    #doodleCanvas {
      border: 2px solid #000; /* Border around canvas */
      display: block; /* Block-level element */
      margin: auto; /* Center horizontally */
      cursor: crosshair; /* Crosshair cursor for drawing */
    }
    /* Style for the container and instructions */
    .container {
      text-align: center; /* Center content */
      padding: 20px;
    }
    .instructions {
      margin: 10px 0;
      font-size: 1.2em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Doodle Canvas</h1>
    <p class="instructions">Click and drag to draw on the canvas.</p>
    <canvas id="doodleCanvas" width="800" height="600"></canvas>
  </div>

  <script>
    // Select the canvas element
    const canvas = document.getElementById('doodleCanvas');
    const context = canvas.getContext('2d');

    // Initialize variables for tracking drawing state
    let isDrawing = false; // Flag indicating whether the user is drawing
    let lastX = 0; // Last mouse X coordinate
    let lastY = 0; // Last mouse Y coordinate

    // Function to start drawing
    canvas.addEventListener('mousedown', (event) => {
      isDrawing = true; // Set drawing flag
      // Record initial mouse position
      [lastX, lastY] = [event.offsetX, event.offsetY];
    });

    // Function to draw on the canvas
    canvas.addEventListener('mousemove', (event) => {
      if (!isDrawing) return; // Exit if not drawing
      
      // Draw a line from the last position to the current position
      context.beginPath(); // Start a new path
      context.moveTo(lastX, lastY); // Move to the previous position
      context.lineTo(event.offsetX, event.offsetY); // Draw to the current position
      context.strokeStyle = '#000'; // Set line color
      context.lineWidth = 2; // Set line thickness
      context.stroke(); // Render the line
      context.closePath(); // Close the path

      // Update last position
      [lastX, lastY] = [event.offsetX, event.offsetY];
    });

    // Function to stop drawing
    canvas.addEventListener('mouseup', () => {
      isDrawing = false; // Reset drawing flag
    });

    // Handle mouse leaving the canvas (stop drawing if outside)
    canvas.addEventListener('mouseleave', () => {
      isDrawing = false; // Reset drawing flag
    });

    // Optional: Add error handling for unexpected cases
    try {
      if (!canvas || !context) {
        throw new Error('Canvas element or context could not be initialized.');
      }
    } catch (error) {
      console.error('An error occurred:', error.message);
      alert('An error occurred while initializing the doodle canvas.');
    }
  </script>
</body>
</html>
```
