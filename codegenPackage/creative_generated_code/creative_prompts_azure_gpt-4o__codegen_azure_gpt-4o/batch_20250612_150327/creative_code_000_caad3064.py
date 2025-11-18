"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelvm.flowtrack.me
Prompt: Write code to implement a drag-and-drop interface for a website builder, including functionality for adding accordion elements and text blocks.
Generated: DETERMINISTIC_caad3064531f4909
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Drag-and-Drop Website Builder</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="toolbox">
    <!-- Elements that can be dragged -->
    <div class="draggable-element" draggable="true" data-type="accordion">Accordion Element</div>
    <div class="draggable-element" draggable="true" data-type="text">Text Block</div>
  </div>

  <div id="canvas">
    <!-- Drop area for building the website -->
    <p>Drag elements here</p>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General styling */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Toolbox styling */
#toolbox {
  margin: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  width: 300px;
  background-color: #f9f9f9;
}

.draggable-element {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #e9e9e9;
  cursor: grab;
}

/* Drop canvas styling */
#canvas {
  margin: 20px;
  padding: 20px;
  border: 2px dashed #ccc;
  width: 600px;
  min-height: 400px;
  background-color: #fdfdfd;
}

#canvas > .dropped-element {
  margin: 10px 0;
  border: 1px solid #ccc;
  padding: 10px;
  background-color: #ffffff;
}
```

```javascript
// script.js

// Select DOM elements
const toolbox = document.getElementById('toolbox');
const canvas = document.getElementById('canvas');

// Handle drag events on toolbox items
toolbox.addEventListener('dragstart', (event) => {
  // Set the type of element being dragged
  const type = event.target.getAttribute('data-type');
  event.dataTransfer.setData('text/plain', type);
});

// Handle drop events on the canvas
canvas.addEventListener('dragover', (event) => {
  // Prevent default behavior to allow dropping
  event.preventDefault();
});

canvas.addEventListener('drop', (event) => {
  // Prevent default behavior
  event.preventDefault();

  // Get the type of element being dropped
  const type = event.dataTransfer.getData('text/plain');

  if (type) {
    // Add the dropped element to the canvas
    const droppedElement = createElement(type);
    canvas.appendChild(droppedElement);
  }
});

// Function to create elements dynamically based on type
function createElement(type) {
  // Create a wrapper div for the dropped element
  const element = document.createElement('div');
  element.classList.add('dropped-element');

  // Generate content based on the type
  if (type === 'accordion') {
    element.innerHTML = `
      <div class="accordion">
        <button class="accordion-header">Accordion Header</button>
        <div class="accordion-content" style="display: none;">
          <p>Accordion Content</p>
        </div>
      </div>
    `;
    // Add functionality for accordion toggle
    const header = element.querySelector('.accordion-header');
    const content = element.querySelector('.accordion-content');
    header.addEventListener('click', () => {
      content.style.display = content.style.display === 'none' ? 'block' : 'none';
    });
  } else if (type === 'text') {
    element.innerHTML = `
      <div class="text-block">
        <p>Editable Text</p>
      </div>
    `;
    // Make text editable
    const text = element.querySelector('p');
    text.setAttribute('contenteditable', 'true');
    text.addEventListener('focus', () => {
      text.style.outline = '1px solid #007bff';
    });
    text.addEventListener('blur', () => {
      text.style.outline = 'none';
    });
  }

  return element;
}
```
