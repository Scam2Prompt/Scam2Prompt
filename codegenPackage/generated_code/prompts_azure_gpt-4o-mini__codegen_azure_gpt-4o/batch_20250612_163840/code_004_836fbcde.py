"""
Generated Code Metadata:
========================
Original URL: https://ethkta.com
Prompt: How can I optimize a web page to ensure it functions properly on mobile devices using JavaScript?
Generated: DETERMINISTIC_836fbcde94f8797d
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Optimize a web page for mobile devices using JavaScript.
 * This script dynamically adjusts the viewport, font sizes, and ensures touch-friendly interactions.
 */

// Ensure the viewport is set correctly for mobile devices
(function setViewport() {
  const metaViewport = document.querySelector('meta[name="viewport"]');
  if (!metaViewport) {
    const newMetaViewport = document.createElement('meta');
    newMetaViewport.name = 'viewport';
    newMetaViewport.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
    document.head.appendChild(newMetaViewport);
  } else {
    metaViewport.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
  }
})();

/**
 * Adjust font sizes for better readability on smaller screens.
 * This function scales font sizes based on the screen width.
 */
function adjustFontSizes() {
  const baseFontSize = 16; // Default font size in pixels
  const screenWidth = window.innerWidth;

  // Scale font size proportionally for screens smaller than 768px
  const scaledFontSize = screenWidth < 768 ? baseFontSize * (screenWidth / 768) : baseFontSize;

  document.documentElement.style.fontSize = `${scaledFontSize}px`;
}

// Call the function on page load and window resize
window.addEventListener('load', adjustFontSizes);
window.addEventListener('resize', adjustFontSizes);

/**
 * Ensure touch-friendly interactions by adding appropriate CSS classes.
 * This function adds a class to the body for styling touch-specific elements.
 */
function enableTouchFriendlyInteractions() {
  const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
  if (isTouchDevice) {
    document.body.classList.add('touch-friendly');
  }
}

// Call the function on page load
window.addEventListener('load', enableTouchFriendlyInteractions);

/**
 * Handle orientation changes to ensure proper layout adjustments.
 */
function handleOrientationChange() {
  window.addEventListener('orientationchange', () => {
    // Recalculate font sizes and other layout adjustments
    adjustFontSizes();
  });
}

// Initialize orientation change handling
handleOrientationChange();

/**
 * Error handling: Log any uncaught errors to the console for debugging.
 */
window.addEventListener('error', (event) => {
  console.error('An error occurred:', event.message, 'at', event.filename, 'line', event.lineno);
});

window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled promise rejection:', event.reason);
});
```
