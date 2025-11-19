"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Provide an example of a 100% scroll progress indicator using SVG in a Webflow project.
Generated: DETERMINISTIC_42a716c95cf3b3d7
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**SVG Scroll Progress Indicator**
=====================================

### HTML
```html
<!-- SVG container -->
<div id="scroll-progress-indicator">
  <svg id="progress-svg" viewBox="0 0 100 10">
    <rect id="progress-bar" x="0" y="0" width="0" height="10" fill="#3498db" />
  </svg>
</div>
```

### CSS
```css
/* Style the SVG container */
#scroll-progress-indicator {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
}

/* Style the SVG */
#progress-svg {
  width: 100%;
  height: 10px;
}

/* Style the progress bar */
#progress-bar {
  transition: width 0.3s ease-in-out;
}
```

### JavaScript
```javascript
// Get the progress bar element
const progressBar = document.getElementById('progress-bar');

// Calculate the scroll progress
function calculateScrollProgress() {
  const scrollPosition = window.scrollY;
  const documentHeight = document.body.offsetHeight;
  const windowHeight = window.innerHeight;
  const progress = (scrollPosition / (documentHeight - windowHeight)) * 100;
  return progress;
}

// Update the progress bar
function updateProgressBar() {
  const progress = calculateScrollProgress();
  progressBar.setAttribute('width', `${progress}%`);
}

// Handle scroll events
window.addEventListener('scroll', () => {
  requestAnimationFrame(updateProgressBar);
});

// Initialize the progress bar
updateProgressBar();
```

### Error Handling
```javascript
try {
  // Get the progress bar element
  const progressBar = document.getElementById('progress-bar');
  if (!progressBar) {
    throw new Error('Progress bar element not found');
  }
} catch (error) {
  console.error('Error initializing progress bar:', error);
}
```
