"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Provide code to clear a drawing canvas with a "Clear Canvas" button, ensuring the functionality matches the description on Monad Whiteboard NFT.
Generated: DETERMINISTIC_77ff02471fa09892
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
  <title>Monad Whiteboard NFT - Clear Canvas</title>
  <style>
    /* Basic styles for the canvas and button */
    #drawingCanvas {
      border: 2px solid #000;
      display: block;
      margin: 20px auto;
    }
    #clearButton {
      display: block;
      margin: 20px auto;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 5px;
    }
    #clearButton:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>

  <!-- Canvas element for drawing -->
  <canvas id="drawingCanvas" width="800" height="400"></canvas>
  
  <!-- Button to clear the canvas -->
  <button id="clearButton">Clear Canvas</button>

  <script>
    // Get references to canvas and button elements
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    const clearButton = document.getElementById('clearButton');

    // Variable to track whether drawing is active
    let isDrawing = false;

    // Event listener for mouse down to start drawing
    canvas.addEventListener('mousedown', (event) => {
      isDrawing = true;
      ctx.beginPath();
      // Move the drawing cursor to the mouse's starting position
      ctx.moveTo(event.offsetX, event.offsetY);
    });

    // Event listener for mouse move to draw lines
    canvas.addEventListener('mousemove', (event) => {
      if (isDrawing) {
        // Draw a line to the current mouse position
        ctx.lineTo(event.offsetX, event.offsetY);
        ctx.stroke();
      }
    });

    // Event listener for mouse up to end drawing
    canvas.addEventListener('mouseup', () => {
      isDrawing = false;
    });

    // Event listener for mouse out to end drawing (if mouse leaves canvas)
    canvas.addEventListener('mouseout', () => {
      isDrawing = false;
    });

    // Event listener for the "Clear Canvas" button
    clearButton.addEventListener('click', () => {
      try {
        // Clear the canvas by resetting its state
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      } catch (error) {
        console.error('Error clearing the canvas:', error);
      }
    });
  </script>

</body>
</html>
```
