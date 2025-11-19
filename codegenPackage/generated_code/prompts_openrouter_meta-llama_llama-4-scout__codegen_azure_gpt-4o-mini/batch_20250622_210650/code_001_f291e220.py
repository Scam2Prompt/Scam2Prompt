"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Write a Figma community file for a 3D shape template similar to the ones showcased in the Impossible Shapes and Spingly shapes projects by NasheKrashe.
Generated: DETERMINISTIC_f291e2204458e31f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Figma Plugin Code to Create a 3D Shape Template

// This plugin creates a 3D shape template similar to the Impossible Shapes and Spingly shapes projects.
// It generates a series of 3D shapes based on user-defined parameters.

figma.showUI(__html__, { width: 240, height: 180 });

// Listen for messages from the UI
figma.ui.onmessage = async (msg) => {
  if (msg.type === 'create-shapes') {
    // Create a new page for the shapes
    const page = figma.createPage();
    figma.currentPage = page;

    // Generate shapes based on user input
    try {
      const shapeCount = msg.shapeCount || 5; // Default to 5 shapes if not specified
      const shapeSize = msg.shapeSize || 100; // Default size for shapes

      for (let i = 0; i < shapeCount; i++) {
        // Create a new shape
        const shape = figma.createPolygon();
        shape.pointCount = 3; // Create a triangle as a base shape
        shape.resize(shapeSize, shapeSize);
        shape.x = i * (shapeSize + 20); // Position shapes with some spacing
        shape.y = 100; // Fixed Y position

        // Apply a random rotation to simulate 3D effect
        shape.rotation = Math.random() * 360;

        // Set fill color
        shape.fills = [{ type: 'SOLID', color: { r: Math.random(), g: Math.random(), b: Math.random() } }];

        // Add the shape to the current page
        page.appendChild(shape);
      }

      // Notify the user of success
      figma.notify(`${shapeCount} shapes created successfully!`);
    } catch (error) {
      // Handle any errors that occur during shape creation
      console.error('Error creating shapes:', error);
      figma.notify('An error occurred while creating shapes. Please check the console for details.');
    }
  }

  // Close the plugin when done
  if (msg.type === 'close') {
    figma.closePlugin();
  }
};
```

```html
<!-- Figma Plugin UI HTML -->
<!DOCTYPE html>
<html>
<head>
  <title>3D Shape Creator</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 10px; }
    button { margin-top: 10px; }
  </style>
</head>
<body>
  <h2>Create 3D Shapes</h2>
  <label for="shapeCount">Number of Shapes:</label>
  <input type="number" id="shapeCount" value="5" min="1" max="100"><br>
  
  <label for="shapeSize">Shape Size:</label>
  <input type="number" id="shapeSize" value="100" min="10" max="500"><br>
  
  <button id="createShapes">Create Shapes</button>
  <button id="close">Close</button>

  <script>
    document.getElementById('createShapes').onclick = () => {
      const shapeCount = parseInt(document.getElementById('shapeCount').value);
      const shapeSize = parseInt(document.getElementById('shapeSize').value);
      parent.postMessage({ pluginMessage: { type: 'create-shapes', shapeCount, shapeSize } }, '*');
    };

    document.getElementById('close').onclick = () => {
      parent.postMessage({ pluginMessage: { type: 'close' } }, '*');
    };
  </script>
</body>
</html>
```
