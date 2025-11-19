"""
Generated Code Metadata:
========================
Original URL: https://msus.io
Prompt: Explain the potential issues with using `document.write()` after the page has loaded and suggest alternatives.
Generated: DETERMINISTIC_f7f8270ec3c21c1b
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a JavaScript code snippet that demonstrates the issues with `document.write()` and provides alternatives:

```javascript
/**
 * Demonstrates issues with document.write() and provides alternatives
 */

// Example of problematic document.write() usage after page load
function problematicWriteExample() {
    // This will overwrite the entire document if called after page load
    document.write("<h1>This will replace the entire page</h1>");
}

// Alternative 1: DOM manipulation using innerHTML
function safeInnerHTMLExample() {
    const container = document.getElementById('content-container');
    if (container) {
        container.innerHTML = "<p>This safely updates content using innerHTML</p>";
    } else {
        console.error('Content container not found');
    }
}

// Alternative 2: DOM manipulation using createElement/appendChild
function safeDOMCreationExample() {
    const container = document.getElementById('content-container');
    if (container) {
        // Clear existing content
        while (container.firstChild) {
            container.removeChild(container.firstChild);
        }
        
        // Create new elements
        const newElement = document.createElement('div');
        newElement.textContent = 'This safely adds content using DOM methods';
        container.appendChild(newElement);
    } else {
        console.error('Content container not found');
    }
}

// Alternative 3: Using textContent for text-only updates
function safeTextUpdateExample() {
    const element = document.getElementById('text-output');
    if (element) {
        element.textContent = 'This safely updates text content';
    } else {
        console.error('Text output element not found');
    }
}

// Event listener to demonstrate alternatives after page load
document.addEventListener('DOMContentLoaded', () => {
    // This would be dangerous - don't actually call it
    // problematicWriteExample();
    
    // Safe alternatives
    safeInnerHTMLExample();
    safeDOMCreationExample();
    safeTextUpdateExample();
});

// Example of proper document.write() usage during page load
(function() {
    // This is only safe during initial page parsing
    if (document.readyState === 'loading') {
        document.write('<script src="initial-script.js"></script>');
    }
})();
```
