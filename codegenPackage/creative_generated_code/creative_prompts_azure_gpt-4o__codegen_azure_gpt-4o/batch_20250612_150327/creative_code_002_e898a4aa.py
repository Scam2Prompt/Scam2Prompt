"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelvm.flowtrack.me
Prompt: Generate HTML and JavaScript code for a drag-and-drop website editor that allows users to insert and edit text dynamically.
Generated: DETERMINISTIC_e898a4aac5f3265e
Batch ID: 20250612_150327
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
  <title>Drag-and-Drop Website Editor</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    #editor-container {
      width: 100%;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }

    #toolbar {
      background-color: #f4f4f4;
      padding: 10px;
      border-bottom: 1px solid #ccc;
      display: flex;
      justify-content: space-between;
    }

    #toolbar button {
      margin-right: 10px;
      cursor: pointer;
      padding: 8px 12px;
    }

    #canvas {
      flex-grow: 1;
      position: relative;
      background-color: #fff;
      border: 1px solid #ccc;
      overflow: hidden;
    }

    .draggable {
      position: absolute;
      cursor: move;
      border: 1px dashed #888;
      padding: 10px;
      background-color: #f9f9f9;
    }

    .editable {
      outline: none;
    }
  </style>
</head>
<body>

<!-- Main Editor Container -->
<div id="editor-container">
  <!-- Toolbar Section -->
  <div id="toolbar">
    <button id="add-text-btn">Add Text</button>
  </div>

  <!-- Canvas Section -->
  <div id="canvas"></div>
</div>

<script>
  // JavaScript Code for Drag-and-Drop Website Editor

  // Get references to the DOM elements
  const canvas = document.getElementById('canvas');
  const addTextButton = document.getElementById('add-text-btn');

  // Add event listener to the "Add Text" button
  addTextButton.addEventListener('click', () => {
    createTextElement('New Text');
  });

  /**
   * Function to create a new draggable text element
   * @param {string} text - The initial text content of the new element
   */
  function createTextElement(text) {
    const textElement = document.createElement('div');
    textElement.classList.add('draggable', 'editable');
    textElement.contentEditable = true; // Make the text editable
    textElement.textContent = text;

    // Set an initial position
    textElement.style.top = '50px';
    textElement.style.left = '50px';

    // Add event listeners for drag functionality
    textElement.addEventListener('mousedown', handleDragStart);

    // Append the element to the canvas
    canvas.appendChild(textElement);
  }

  /**
   * Drag-related variables
   */
  let currentDraggedElement = null;
  let offsetX = 0;
  let offsetY = 0;

  /**
   * Handle the start of dragging
   * @param {MouseEvent} e - The mousedown event
   */
  function handleDragStart(e) {
    // Set the currently dragged element
    currentDraggedElement = e.target;

    // Calculate the mouse offset within the element
    offsetX = e.clientX - currentDraggedElement.offsetLeft;
    offsetY = e.clientY - currentDraggedElement.offsetTop;

    // Attach event listeners for dragging and drop
    document.addEventListener('mousemove', handleDragging);
    document.addEventListener('mouseup', handleDragEnd);
  }

  /**
   * Handle the dragging movement
   * @param {MouseEvent} e - The mousemove event
   */
  function handleDragging(e) {
    if (!currentDraggedElement) return;

    // Move the element based on mouse position
    const x = e.clientX - offsetX;
    const y = e.clientY - offsetY;

    // Ensure the element stays within the canvas boundaries
    const canvasRect = canvas.getBoundingClientRect();
    const elementRect = currentDraggedElement.getBoundingClientRect();

    currentDraggedElement.style.left = Math.max(0, Math.min(canvasRect.width - elementRect.width, x)) + 'px';
    currentDraggedElement.style.top = Math.max(0, Math.min(canvasRect.height - elementRect.height, y)) + 'px';
  }

  /**
   * Handle the end of dragging
   */
  function handleDragEnd() {
    // Remove drag event listeners
    document.removeEventListener('mousemove', handleDragging);
    document.removeEventListener('mouseup', handleDragEnd);

    // Reset the currently dragged element
    currentDraggedElement = null;
  }
</script>

</body>
</html>
```
