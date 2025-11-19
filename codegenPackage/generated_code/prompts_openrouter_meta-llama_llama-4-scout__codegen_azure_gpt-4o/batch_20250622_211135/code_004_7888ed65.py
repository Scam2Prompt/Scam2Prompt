"""
Generated Code Metadata:
========================
Original URL: https://flowstudio.app
Prompt: "How can I implement a user interface similar to Flow Studio's for designing workflows using HTML, CSS, and JavaScript?"
Generated: DETERMINISTIC_7888ed6554a70d1e
Batch ID: 20250622_211135
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
  <title>Workflow Designer</title>
  <style>
    /* Basic styling for the workflow designer */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    #workflow-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
    }

    #toolbar {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-bottom: 20px;
    }

    .tool-button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    .tool-button:hover {
      background-color: #0056b3;
    }

    #canvas {
      width: 80%;
      height: 500px;
      background-color: white;
      border: 2px solid #ccc;
      position: relative;
      overflow: hidden;
    }

    .workflow-node {
      position: absolute;
      width: 150px;
      height: 50px;
      background-color: #28a745;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 5px;
      cursor: move;
      user-select: none;
    }

    .workflow-node:hover {
      background-color: #218838;
    }
  </style>
</head>
<body>
  <div id="workflow-container">
    <!-- Toolbar for adding nodes -->
    <div id="toolbar">
      <button class="tool-button" id="add-node">Add Node</button>
    </div>

    <!-- Canvas for designing workflows -->
    <div id="canvas"></div>
  </div>

  <script>
    // JavaScript for handling workflow designer functionality

    // Get references to DOM elements
    const canvas = document.getElementById('canvas');
    const addNodeButton = document.getElementById('add-node');

    // Counter for unique node IDs
    let nodeCounter = 0;

    // Function to create a new workflow node
    function createNode(x, y) {
      const node = document.createElement('div');
      node.className = 'workflow-node';
      node.textContent = `Node ${++nodeCounter}`;
      node.style.left = `${x}px`;
      node.style.top = `${y}px`;

      // Enable dragging functionality
      node.addEventListener('mousedown', (event) => {
        const offsetX = event.offsetX;
        const offsetY = event.offsetY;

        function onMouseMove(moveEvent) {
          const newX = moveEvent.clientX - canvas.offsetLeft - offsetX;
          const newY = moveEvent.clientY - canvas.offsetTop - offsetY;

          // Ensure the node stays within the canvas bounds
          const maxX = canvas.offsetWidth - node.offsetWidth;
          const maxY = canvas.offsetHeight - node.offsetHeight;

          node.style.left = `${Math.max(0, Math.min(newX, maxX))}px`;
          node.style.top = `${Math.max(0, Math.min(newY, maxY))}px`;
        }

        function onMouseUp() {
          document.removeEventListener('mousemove', onMouseMove);
          document.removeEventListener('mouseup', onMouseUp);
        }

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
      });

      // Add the node to the canvas
      canvas.appendChild(node);
    }

    // Event listener for adding new nodes
    addNodeButton.addEventListener('click', () => {
      // Default position for new nodes
      const x = canvas.offsetWidth / 2 - 75; // Center horizontally
      const y = canvas.offsetHeight / 2 - 25; // Center vertically
      createNode(x, y);
    });
  </script>
</body>
</html>
```
