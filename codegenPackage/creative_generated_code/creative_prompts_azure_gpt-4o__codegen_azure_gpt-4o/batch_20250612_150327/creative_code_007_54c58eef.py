"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelvm.flowtrack.me
Prompt: Generate code for a drag-and-drop website builder using vanilla JavaScript, with functionality for adding headings, accordions, and text blocks.
Generated: DETERMINISTIC_54c58eef8f074eff
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
  <title>Drag-and-Drop Website Builder</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }

    #toolbar {
      display: flex;
      gap: 10px;
      padding: 10px;
      background-color: #f4f4f4;
      border-bottom: 1px solid #ccc;
    }

    #builder {
      min-height: 400px;
      border: 2px dashed #ddd;
      margin: 20px;
      padding: 10px;
      background-color: #fafafa;
    }

    .block {
      padding: 10px;
      border: 1px solid #ccc;
      margin: 5px;
      background-color: #fff;
      cursor: grab;
    }

    .accordion-content {
      display: none;
      padding: 10px;
      border-top: 1px solid #ccc;
      background-color: #f9f9f9;
    }

    .accordion-header {
      cursor: pointer;
    }

    .dragging {
      opacity: 0.5;
    }
  </style>
</head>
<body>
  <div id="toolbar">
    <button id="add-heading">Add Heading</button>
    <button id="add-text">Add Text Block</button>
    <button id="add-accordion">Add Accordion</button>
  </div>
  <div id="builder"></div>

  <script>
    // Select DOM elements
    const toolbar = document.getElementById('toolbar');
    const builder = document.getElementById('builder');

    // Drag-and-drop variables
    let draggedElement = null;

    // Utility function to create a block
    function createBlock(type) {
      const block = document.createElement('div');
      block.classList.add('block');
      block.setAttribute('draggable', true);

      switch (type) {
        case 'heading':
          block.innerHTML = '<h2 contenteditable="true">Heading</h2>';
          break;
        case 'text':
          block.innerHTML = '<p contenteditable="true">Text Block</p>';
          break;
        case 'accordion':
          block.innerHTML = `
            <div class="accordion-header">Accordion Header (Click me)</div>
            <div class="accordion-content">Accordion Content</div>
          `;
          block.querySelector('.accordion-header').addEventListener('click', () => {
            const content = block.querySelector('.accordion-content');
            content.style.display = content.style.display === 'none' ? 'block' : 'none';
          });
          break;
        default:
          throw new Error('Unknown block type');
      }

      // Add drag-and-drop listeners
      block.addEventListener('dragstart', handleDragStart);
      block.addEventListener('dragend', handleDragEnd);

      return block;
    }

    // Event listener - Add heading block
    document.getElementById('add-heading').addEventListener('click', () => {
      builder.appendChild(createBlock('heading'));
    });

    // Event listener - Add text block
    document.getElementById('add-text').addEventListener('click', () => {
      builder.appendChild(createBlock('text'));
    });

    // Event listener - Add accordion block
    document.getElementById('add-accordion').addEventListener('click', () => {
      builder.appendChild(createBlock('accordion'));
    });

    // Drag-and-drop functionality
    function handleDragStart(event) {
      draggedElement = this;
      this.classList.add('dragging');
      event.dataTransfer.effectAllowed = 'move';
      event.dataTransfer.setData('text/plain', '');
    }

    function handleDragEnd() {
      this.classList.remove('dragging');
      draggedElement = null;
    }

    builder.addEventListener('dragover', (event) => {
      event.preventDefault();
      event.dataTransfer.dropEffect = 'move';
    });

    builder.addEventListener('drop', (event) => {
      event.preventDefault();
      if (draggedElement) {
        builder.appendChild(draggedElement);
      }
    });

    // Error handling for unknown block types
    window.addEventListener('error', (event) => {
      console.error('An error occurred:', event.error.message);
    });
  </script>
</body>
</html>
```
