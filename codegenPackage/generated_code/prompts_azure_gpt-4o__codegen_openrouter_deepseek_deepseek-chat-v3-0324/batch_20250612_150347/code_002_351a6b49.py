"""
Generated Code Metadata:
========================
Original URL: https://soneium.app
Prompt: Generate a JavaScript snippet to dynamically enable or check for JavaScript support in a web application.
Generated: DETERMINISTIC_351a6b49ca0c3ebe
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and optionally
 * executes a callback function if it is.
 * 
 * @param {function} [callback] - Optional callback to execute if JS is enabled
 * @returns {boolean} True if JavaScript is enabled, false otherwise
 */
function checkJavascriptSupport(callback) {
    try {
        // Create a test element to check for JS support
        const testElement = document.createElement('div');
        testElement.style.display = 'none';
        document.body.appendChild(testElement);

        // Attempt to modify the element via JavaScript
        testElement.style.display = 'block';
        const jsEnabled = testElement.style.display === 'block';

        // Clean up
        document.body.removeChild(testElement);

        // Execute callback if provided and JS is enabled
        if (jsEnabled && typeof callback === 'function') {
            callback();
        }

        return jsEnabled;
    } catch (error) {
        console.error('Error checking JavaScript support:', error);
        return false;
    }
}

/**
 * Adds a 'js-enabled' class to the document element if JavaScript is supported.
 * This allows for CSS styling based on JavaScript availability.
 */
function enableJavascriptStyles() {
    if (checkJavascriptSupport()) {
        document.documentElement.classList.add('js-enabled');
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    enableJavascriptStyles();
});
```
