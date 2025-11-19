"""
Generated Code Metadata:
========================
Original URL: https://adamhome.vn
Prompt: "Design a UI component for a painting services website that allows customers to select colors and visualize their painting project, inspired by the color selection tools on adamhome.vn."
Generated: DETERMINISTIC_c27c7d9a4d477976
Batch ID: 20250622_210703
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
    <title>Color Selection Tool</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Visualize Your Painting Project</h1>
        <div class="color-selection">
            <label for="colorPicker">Choose a color:</label>
            <input type="color" id="colorPicker" value="#ffffff">
        </div>
        <div class="preview">
            <h2>Preview</h2>
            <div id="previewBox" class="preview-box"></div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.color-selection {
    margin-bottom: 20px;
}

.preview {
    margin-top: 20px;
}

.preview-box {
    width: 100%;
    height: 200px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #ffffff;
}
```

```javascript
// script.js

// Function to initialize the color picker and set up event listeners
function initColorPicker() {
    const colorPicker = document.getElementById('colorPicker');
    const previewBox = document.getElementById('previewBox');

    // Set the initial color of the preview box
    previewBox.style.backgroundColor = colorPicker.value;

    // Event listener for color change
    colorPicker.addEventListener('input', (event) => {
        try {
            // Update the preview box color based on the selected color
            previewBox.style.backgroundColor = event.target.value;
        } catch (error) {
            console.error('Error updating color:', error);
        }
    });
}

// Initialize the color picker on page load
document.addEventListener('DOMContentLoaded', initColorPicker);
```

This code provides a simple UI component for a painting services website, allowing users to select colors and visualize their painting project. The HTML, CSS, and JavaScript are structured to ensure clarity, maintainability, and responsiveness.
