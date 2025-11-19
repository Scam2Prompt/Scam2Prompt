"""
Generated Code Metadata:
========================
Original URL: https://sushiswap-suhii.weebly.com
Prompt: Generate code for a webpage that allows users to edit text directly on the site, drag and drop elements, and customize templates, similar to the functionality described on the Sushiswap-Suhii website.
Generated: DETERMINISTIC_2b27e25b91ae3310
Batch ID: 20250612_151811
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
    <title>Editable Webpage</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Editable Webpage</h1>
        <button id="addElementBtn">Add Text Element</button>
    </header>
    <main id="editableArea">
        <p class="draggable" contenteditable="true">Edit this text directly!</p>
    </main>
    <footer>
        <p>&copy; 2023 Editable Webpage</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the body and header */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    background: #007bff;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

#editableArea {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    background: white;
}

/* Draggable elements */
.draggable {
    padding: 10px;
    border: 1px dashed #007bff;
    margin: 10px 0;
    cursor: move;
}

/* Hover effect for draggable elements */
.draggable:hover {
    background-color: #e9ecef;
}
```

```javascript
// script.js

// Function to initialize drag and drop functionality
function makeDraggable(element) {
    element.setAttribute('draggable', true);

    element.addEventListener('dragstart', (e) => {
        e.dataTransfer.setData('text/plain', null); // Required for Firefox
        e.dataTransfer.setData('text/plain', e.target.innerHTML);
        e.target.classList.add('dragging');
    });

    element.addEventListener('dragend', () => {
        element.classList.remove('dragging');
    });
}

// Function to handle dropping of elements
function handleDrop(e) {
    e.preventDefault();
    const data = e.dataTransfer.getData('text/plain');
    const newElement = document.createElement('p');
    newElement.className = 'draggable';
    newElement.contentEditable = true;
    newElement.innerHTML = data || 'New editable text';
    makeDraggable(newElement);
    e.target.appendChild(newElement);
}

// Function to add a new text element
function addTextElement() {
    const newElement = document.createElement('p');
    newElement.className = 'draggable';
    newElement.contentEditable = true;
    newElement.innerHTML = 'New editable text';
    makeDraggable(newElement);
    document.getElementById('editableArea').appendChild(newElement);
}

// Event listeners for adding elements and handling drop
document.getElementById('addElementBtn').addEventListener('click', addTextElement);
document.getElementById('editableArea').addEventListener('dragover', (e) => e.preventDefault());
document.getElementById('editableArea').addEventListener('drop', handleDrop);

// Initialize the first draggable element
document.querySelectorAll('.draggable').forEach(makeDraggable);
```

This code creates a simple webpage that allows users to edit text directly, add new text elements, and drag and drop them within the editable area. The code is structured, well-commented, and follows best practices for HTML, CSS, and JavaScript.
