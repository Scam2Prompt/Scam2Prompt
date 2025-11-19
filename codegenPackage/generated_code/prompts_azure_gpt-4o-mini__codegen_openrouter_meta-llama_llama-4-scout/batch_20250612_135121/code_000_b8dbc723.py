"""
Generated Code Metadata:
========================
Original URL: https://fuelvm.flowtrack.me
Prompt: How can I implement a drag-and-drop feature similar to the one described on fuelvm.flowtrack.me for a web application?
Generated: DETERMINISTIC_b8dbc723d1e106ae
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Drag-and-Drop Feature Implementation**
======================================

### HTML
```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drag-and-Drop Feature</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div id="draggable" class="draggable" draggable="true">Drag Me</div>
        <div id="dropzone" class="dropzone">Drop Zone</div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (in styles.css file)
```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

.container {
    width: 80%;
    margin: 40px auto;
    text-align: center;
}

.draggable {
    width: 100px;
    height: 100px;
    background-color: #f0f0f0;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    cursor: move; /* fallback if grab cursor is unsupported */
    cursor: grab;
}

.dropzone {
    width: 300px;
    height: 300px;
    background-color: #e0e0e0;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    margin: 20px auto;
}

.over {
    background-color: #ccc;
}
```

### JavaScript (in script.js file)
```javascript
// script.js

// Get elements
const draggableElement = document.getElementById('draggable');
const dropzoneElement = document.getElementById('dropzone');

// Define drag-and-drop variables
let dragItem = null;
let dragItemCenterX = 0;
let dragItemCenterY = 0;

// Add event listeners
document.addEventListener('dragstart', handleDragStart);
document.addEventListener('dragover', handleDragOver);
document.addEventListener('dragleave', handleDragLeave);
document.addEventListener('drop', handleDrop);

// Handle drag start
function handleDragStart(event) {
    // Set drag item
    dragItem = event.target;

    // Calculate center coordinates of the drag item
    dragItemCenterX = event.clientX;
    dragItemCenterY = event.clientY;

    // Set data transfer effect
    event.dataTransfer.effectAllowed = 'move';
    event.dataTransfer.setData('text', 'dragged-item');
}

// Handle drag over
function handleDragOver(event) {
    event.preventDefault();

    // Check if drag item is over dropzone
    if (event.target === dropzoneElement) {
        dropzoneElement.classList.add('over');
    }
}

// Handle drag leave
function handleDragLeave(event) {
    if (event.target === dropzoneElement) {
        dropzoneElement.classList.remove('over');
    }
}

// Handle drop
function handleDrop(event) {
    event.preventDefault();

    // Remove over class from dropzone
    dropzoneElement.classList.remove('over');

    // Check if drag item is not null and is being dropped on dropzone
    if (dragItem && event.target === dropzoneElement) {
        // Append drag item to dropzone
        dropzoneElement.appendChild(dragItem);
    }

    // Reset drag item
    dragItem = null;
}
```
