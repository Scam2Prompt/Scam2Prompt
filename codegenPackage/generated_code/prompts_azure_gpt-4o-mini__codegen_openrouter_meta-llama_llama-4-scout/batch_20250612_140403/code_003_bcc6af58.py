"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: How can I implement a visual representation of an eye watching users in a web application, based on the themes from RED?
Generated: DETERMINISTIC_bcc6af58942efcf3
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// EyeWatcher.js
class EyeWatcher {
  /**
   * Creates an instance of EyeWatcher.
   * @param {HTMLElement} container - The container element for the eye.
   * @param {number} [pupilSize=20] - The size of the pupil.
   * @param {number} [eyeSize=100] - The size of the eye.
   */
  constructor(container, pupilSize = 20, eyeSize = 100) {
    this.container = container;
    this.pupilSize = pupilSize;
    this.eyeSize = eyeSize;
    this.eyeElement = null;
    this.pupilElement = null;

    this.init();
  }

  /**
   * Initializes the eye watcher.
   */
  init() {
    // Create the eye element
    this.eyeElement = document.createElement('div');
    this.eyeElement.classList.add('eye');
    this.eyeElement.style.width = `${this.eyeSize}px`;
    this.eyeElement.style.height = `${this.eyeSize}px`;
    this.eyeElement.style.position = 'relative';
    this.eyeElement.style.borderRadius = '50%';
    this.eyeElement.style.background = '#fff';
    this.eyeElement.style.border = '2px solid #000';

    // Create the pupil element
    this.pupilElement = document.createElement('div');
    this.pupilElement.classList.add('pupil');
    this.pupilElement.style.width = `${this.pupilSize}px`;
    this.pupilElement.style.height = `${this.pupilSize}px`;
    this.pupilElement.style.position = 'absolute';
    this.pupilElement.style.borderRadius = '50%';
    this.pupilElement.style.background = '#000';
    this.pupilElement.style.left = '50%';
    this.pupilElement.style.top = '50%';
    this.pupilElement.style.transform = 'translate(-50%, -50%)';

    // Add the eye and pupil elements to the container
    this.container.appendChild(this.eyeElement);
    this.eyeElement.appendChild(this.pupilElement);

    // Add event listener for mouse movement
    document.addEventListener('mousemove', this.handleMouseMove.bind(this));
  }

  /**
   * Handles mouse movement.
   * @param {MouseEvent} event - The mouse move event.
   */
  handleMouseMove(event) {
    // Calculate the mouse position relative to the container
    const rect = this.container.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Calculate the pupil position
    const pupilX = (x / this.eyeSize) * 100 - 50;
    const pupilY = (y / this.eyeSize) * 100 - 50;

    // Update the pupil position
    this.pupilElement.style.left = `calc(50% + ${pupilX}px)`;
    this.pupilElement.style.top = `calc(50% + ${pupilY}px)`;
  }
}

// Example usage
const container = document.getElementById('eye-container');
const eyeWatcher = new EyeWatcher(container);
```

```css
/* styles.css */
.eye {
  position: relative;
  margin: 20px;
}

.pupil {
  transition: 0.1s ease-in-out;
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eye Watcher</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="eye-container"></div>
  <script src="EyeWatcher.js"></script>
</body>
</html>
```
