"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Write code to add a color picker and size adjustment tool for drawing on a canvas, similar to the customization options on Monad Whiteboard NFT.
Generated: DETERMINISTIC_cffbcb9869fafdea
Batch ID: 20250612_153854
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
  <title>Canvas Drawing Tool</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    #controls {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px;
      background-color: #f0f0f0;
      border-bottom: 2px solid #ccc;
    }
    #canvas {
      display: block;
      border: 1px solid #ccc;
      margin: 10px auto;
    }
  </style>
</head>
<body>
  <!-- Control Panel -->
  <div id="controls">
    <!-- Color Picker -->
    <label for="colorPicker">Color:</label>
    <input type="color" id="colorPicker" value="#000000">

    <!-- Size Adjustment -->
    <label for="sizePicker">Brush Size:</label>
    <input type="number" id="sizePicker" min="1" max="50" value="5">
  </div>

  <!-- Canvas Element -->
  <canvas id="canvas" width="800" height="500"></canvas>

  <script>
    // References to UI elements
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const colorPicker = document.getElementById('colorPicker');
    const sizePicker = document.getElementById('sizePicker');

    // State variables
    let drawing = false; // Tracks whether the user is drawing on the canvas
    let brushColor = colorPicker.value; // Current brush color
    let brushSize = parseInt(sizePicker.value, 10); // Current brush size

    // Event listener for color picker changes
    colorPicker.addEventListener('change', (e) => {
      brushColor = e.target.value; // Update brush color
    });

    // Event listener for brush size changes
    sizePicker.addEventListener('input', (e) => {
      brushSize = parseInt(e.target.value, 10); // Update brush size
    });

    // Start drawing when mouse is pressed
    canvas.addEventListener('mousedown', (e) => {
      drawing = true;
      draw(e); // Start drawing immediately
    });

    // Stop drawing when mouse is released
    canvas.addEventListener('mouseup', () => {
      drawing = false;
      ctx.beginPath(); // Reset path to prevent unintended line connections
    });

    // Draw on the canvas as the mouse moves
    canvas.addEventListener('mousemove', (e) => {
      if (drawing) {
        draw(e);
      }
    });

    /**
     * Draws a line segment on the canvas based on mouse movement.
     * @param {MouseEvent} e - The mouse event containing cursor position.
     */
    function draw(e) {
      // Get mouse position relative to the canvas
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left; // Calculate X coordinate
      const y = e.clientY - rect.top;  // Calculate Y coordinate

      // Configure drawing settings
      ctx.lineWidth = brushSize;
      ctx.lineCap = 'round'; // Smooth ends of lines
      ctx.strokeStyle = brushColor;

      // Draw line segment
      ctx.lineTo(x, y); // Add point to path
      ctx.stroke();     // Render the line
      ctx.beginPath();  // Start a new path
      ctx.moveTo(x, y); // Set the starting point of the new path
    }

    // Optionally, prevent context menu from opening on canvas (useful for smooth drawing experience)
    canvas.addEventListener('contextmenu', (e) => e.preventDefault());
  </script>
</body>
</html>
```
