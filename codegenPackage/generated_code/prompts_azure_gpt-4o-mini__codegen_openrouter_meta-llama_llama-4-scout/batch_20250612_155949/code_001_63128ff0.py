"""
Generated Code Metadata:
========================
Original URL: https://methodsmoney.com
Prompt: How can I create a custom cursor effect for hover icons in a web application, based on the techniques mentioned on methodsmoney.com?
Generated: DETERMINISTIC_63128ff0d47adff6
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// customCursor.js

class CustomCursor {
  /**
   * Creates a custom cursor effect for hover icons.
   * @param {Document} document - The document object.
   * @param {Window} window - The window object.
   */
  constructor(document, window) {
    this.document = document;
    this.window = window;
    this.cursorElement = null;
    this.iconElements = [];
    this.isHovering = false;

    // Initialize the custom cursor element.
    this.initCursor();
    // Add event listeners to icon elements.
    this.addEventListeners();
  }

  /**
   * Initializes the custom cursor element.
   */
  initCursor() {
    // Create the custom cursor element.
    this.cursorElement = document.createElement('div');
    this.cursorElement.classList.add('custom-cursor');
    this.cursorElement.style.position = 'absolute';
    this.cursorElement.style.pointerEvents = 'none';
    this.cursorElement.style.width = '20px';
    this.cursorElement.style.height = '20px';
    this.cursorElement.style.borderRadius = '50%';
    this.cursorElement.style.background = '#333';
    this.cursorElement.style.transform = 'translate(-50%, -50%)';
    this.cursorElement.style.transition = '0.2s ease-out';

    // Add the custom cursor element to the body.
    this.document.body.appendChild(this.cursorElement);
  }

  /**
   * Adds event listeners to icon elements.
   */
  addEventListeners() {
    // Get all icon elements.
    this.iconElements = this.document.querySelectorAll('.icon');

    // Add event listeners to icon elements.
    this.iconElements.forEach((icon) => {
      icon.addEventListener('mouseover', (event) => this.handleMouseOver(event));
      icon.addEventListener('mouseout', (event) => this.handleMouseOut(event));
    });

    // Add a mousemove event listener to the document.
    this.document.addEventListener('mousemove', (event) => this.handleMouseMove(event));
  }

  /**
   * Handles the mouseover event.
   * @param {MouseEvent} event - The mouseover event.
   */
  handleMouseOver(event) {
    // Set the isHovering flag to true.
    this.isHovering = true;

    // Update the custom cursor position and scale.
    this.updateCursorPosition(event.clientX, event.clientY);
    this.cursorElement.style.transform = 'translate(-50%, -50%) scale(1.2)';
  }

  /**
   * Handles the mouseout event.
   * @param {MouseEvent} event - The mouseout event.
   */
  handleMouseOut(event) {
    // Set the isHovering flag to false.
    this.isHovering = false;

    // Reset the custom cursor scale.
    this.cursorElement.style.transform = 'translate(-50%, -50%) scale(1)';
  }

  /**
   * Handles the mousemove event.
   * @param {MouseEvent} event - The mousemove event.
   */
  handleMouseMove(event) {
    // Update the custom cursor position if not hovering.
    if (!this.isHovering) {
      this.updateCursorPosition(event.clientX, event.clientY);
    }
  }

  /**
   * Updates the custom cursor position.
   * @param {number} x - The x-coordinate.
   * @param {number} y - The y-coordinate.
   */
  updateCursorPosition(x, y) {
    // Update the custom cursor position.
    this.cursorElement.style.left = `${x}px`;
    this.cursorElement.style.top = `${y}px`;
  }
}

// Initialize the custom cursor.
const customCursor = new CustomCursor(document, window);
```

```css
/* styles.css */

.custom-cursor {
  position: absolute;
  pointer-events: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #333;
  transform: translate(-50%, -50%);
  transition: 0.2s ease-out;
}

.icon {
  cursor: pointer;
  transition: 0.2s ease-out;
}

.icon:hover {
  transform: scale(1.2);
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Custom Cursor Effect</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <script src="customCursor.js"></script>
  <div class="icon">Icon 1</div>
  <div class="icon">Icon 2</div>
  <div class="icon">Icon 3</div>
</body>
</html>
```
