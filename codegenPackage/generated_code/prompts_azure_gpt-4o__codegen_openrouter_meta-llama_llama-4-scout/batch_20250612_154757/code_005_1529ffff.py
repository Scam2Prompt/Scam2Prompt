"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: How can I implement a no-jank scroll progress indicator in Webflow using SVG, as described on the Scroll Progress Indicator webpage?
Generated: DETERMINISTIC_1529ffff44d79ecf
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**No-Jank Scroll Progress Indicator in Webflow using SVG**

### HTML
```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No-Jank Scroll Progress Indicator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="progress-indicator">
        <svg class="progress-svg" viewBox="0 0 100 10">
            <rect class="progress-bar" x="0" y="0" width="0" height="10" fill="#ccc" />
            <rect class="progress-fill" x="0" y="0" width="0" height="10" fill="#333" />
        </svg>
    </div>
    <div class="content">
        <!-- Your Webflow content here -->
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        <!-- Add more content here to test the scroll progress indicator -->
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (in styles.css file)
```css
/* styles.css */

.progress-indicator {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 10px;
    z-index: 1000;
}

.progress-svg {
    width: 100%;
    height: 100%;
    display: block;
}

.progress-bar {
    stroke: none;
}

.progress-fill {
    stroke: none;
}

.content {
    padding-top: 20px;
}
```

### JavaScript (in script.js file)
```javascript
// script.js

// Get the progress indicator elements
const progressIndicator = document.querySelector('.progress-fill');

// Get the content element
const contentElement = document.querySelector('.content');

// Calculate the scroll progress
function calculateScrollProgress() {
    const scrollTop = window.scrollY;
    const scrollHeight = contentElement.offsetHeight - window.innerHeight;
    const progress = (scrollTop / scrollHeight) * 100;

    // Update the progress indicator
    progressIndicator.setAttribute('width', `${progress}%`);
}

// Handle scroll events
window.addEventListener('scroll', () => {
    requestAnimationFrame(calculateScrollProgress);
});

// Initialize the progress indicator
calculateScrollProgress();
```
