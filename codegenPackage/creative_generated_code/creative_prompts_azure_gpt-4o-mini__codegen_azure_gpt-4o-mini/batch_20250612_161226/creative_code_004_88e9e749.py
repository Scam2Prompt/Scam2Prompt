"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as.magiceden.eu
Prompt: How do I create a JavaScript function that checks for the presence of JavaScript on a webpage like Magic Eden?
Generated: DETERMINISTIC_88e9e7499f7cb5d8
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if JavaScript is enabled on the webpage.
 * It does so by attempting to manipulate the DOM and 
 * verifying that the changes persist. 
 *
 * @returns {boolean} - Returns true if JavaScript is enabled, false otherwise.
 */
function isJavaScriptEnabled() {
    // Create a test element
    const testElement = document.createElement('div');
    testElement.id = 'js-test';
    testElement.textContent = 'JavaScript is enabled';

    // Append the test element to the body
    document.body.appendChild(testElement);

    // Check if the element was added successfully
    const isJsEnabled = document.getElementById('js-test') !== null;

    // Clean up by removing the test element
    document.body.removeChild(testElement);

    return isJsEnabled;
}

// Usage
window.onload = function () {
    if (isJavaScriptEnabled()) {
        console.log('JavaScript is enabled on this webpage.');
    } else {
        console.log('JavaScript is not enabled on this webpage.');
    }
};
```
