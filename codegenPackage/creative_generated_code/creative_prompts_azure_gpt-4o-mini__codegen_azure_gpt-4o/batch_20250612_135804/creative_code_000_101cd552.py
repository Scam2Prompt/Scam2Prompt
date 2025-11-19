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
    /* Canvas styling */
    #doodleCanvas {
      border: 1px solid #000;
      cursor: crosshair;
    }
    /* Container styling for layout */
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 20px;
    }
    .buttons {
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <canvas id="doodleCanvas" width="800" height="600"></canvas>
    <div class="buttons">
      <button id="clearBtn">Clear Canvas</button>
      <button id="saveBtn">Save Doodle</button>
    </div>
  </div>

  <script>
    // Select DOM elements
    const canvas = document.getElementById('doodleCanvas');
    const clearBtn = document.getElementById('clearBtn');
    const saveBtn = document.getElementById('saveBtn');
    const ctx = canvas.getContext('2d');

    // Variables to track drawing state
    let isDrawing = false;
    let prevX = 0;
    let prevY = 0;

    /**
     * Starts the drawing process when the user presses the mouse button.
     * @param {MouseEvent} event - The mouse event.
     */
    canvas.addEventListener('mousedown', (event) => {
      isDrawing = true;
      prevX = event.offsetX;
      prevY = event.offsetY;
    });

    /**
     * Draws on the canvas as the user moves the mouse while holding down the button.
     * @param {MouseEvent} event - The mouse event.
     */
    canvas.addEventListener('mousemove', (event) => {
      if (!isDrawing) return;
      
      const currentX = event.offsetX;
      const currentY = event.offsetY;

      // Draw a line from the previous position to the current position
      ctx.beginPath();
      ctx.moveTo(prevX, prevY);
      ctx.lineTo(currentX, currentY);
      ctx.strokeStyle = 'black'; // Line color
      ctx.lineWidth = 2; // Line thickness
      ctx.stroke();
      ctx.closePath();

      // Update previous position
      prevX = currentX;
      prevY = currentY;
    });

    /**
     * Stops the drawing process when the user releases the mouse button.
     */
    canvas.addEventListener('mouseup', () => {
      isDrawing = false;
    });

    /**
     * Stops the drawing process if the user moves the mouse out of the canvas.
     */
    canvas.addEventListener('mouseout', () => {
      isDrawing = false;
    });

    /**
     * Clears the canvas when the "Clear Canvas" button is clicked.
     */
    clearBtn.addEventListener('click', () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    });

    /**
     * Saves the doodle as an image when the "Save Doodle" button is clicked.
     */
    saveBtn.addEventListener('click', () => {
      const image = canvas.toDataURL('image/png');
      
      // Create a temporary link for downloading the image
      const link = document.createElement('a');
      link.href = image;
      link.download = 'doodle.png';
      link.click();
    });
  </script>
</body>
</html>
```
