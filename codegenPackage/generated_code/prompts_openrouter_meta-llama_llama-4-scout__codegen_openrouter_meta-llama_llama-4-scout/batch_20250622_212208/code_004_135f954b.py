"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Design a Webflow scroll progress indicator that displays 100% completion with an SVG and a "Back to Top" button.
Generated: DETERMINISTIC_135f954b802c8dd7
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Webflow Scroll Progress Indicator**
=====================================

### HTML
```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webflow Scroll Progress Indicator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="progress-container">
        <svg class="progress-svg" viewBox="0 0 100 100">
            <circle class="progress-circle" cx="50" cy="50" r="45" />
            <circle class="progress-fill" cx="50" cy="50" r="45" />
        </svg>
        <button class="back-to-top" aria-label="Back to Top">Back to Top</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (in styles.css file)
```css
/* styles.css */

.progress-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    display: flex;
    align-items: center;
}

.progress-svg {
    width: 100px;
    height: 100px;
}

.progress-circle {
    fill: none;
    stroke: #ccc;
    stroke-width: 10;
}

.progress-fill {
    fill: none;
    stroke: #333;
    stroke-width: 10;
    stroke-dasharray: 283;
    stroke-dashoffset: 283;
}

.back-to-top {
    margin-left: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #333;
    color: #fff;
    cursor: pointer;
}

.back-to-top:hover {
    background-color: #444;
}
```

### JavaScript (in script.js file)
```javascript
// script.js

// Get elements
const progressSvg = document.querySelector('.progress-svg');
const progressFill = document.querySelector('.progress-fill');
const backToTopButton = document.querySelector('.back-to-top');

// Set initial progress
let scrollProgress = 0;
let maxScrollHeight = document.body.offsetHeight - window.innerHeight;

// Update progress on scroll
window.addEventListener('scroll', () => {
    scrollProgress = (window.scrollY / maxScrollHeight) * 100;
    updateProgress();
});

// Update progress function
function updateProgress() {
    const dashOffset = 283 - (scrollProgress / 100) * 283;
    progressFill.style.strokeDashoffset = dashOffset;

    // Show/hide Back to Top button
    if (scrollProgress > 50) {
        backToTopButton.style.opacity = 1;
    } else {
        backToTopButton.style.opacity = 0;
    }

    // Update completion text
    const completionText = scrollProgress >= 100 ? '100% Complete' : `${Math.round(scrollProgress)}%`;
    // Optional: add a completion text element to display this text
}

// Back to Top button click handler
backToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
```
