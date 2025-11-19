"""
Generated Code Metadata:
========================
Original URL: https://earndrop.eu
Prompt: Write a basic JavaScript code snippet that checks if JavaScript is enabled in a browser, inspired by the approach used on EarnDrop.
Generated: DETERMINISTIC_de40d496cd8638fa
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser.
 * Inspired by EarnDrop's approach.
 * 
 * @returns {boolean} True if JavaScript is enabled, false otherwise.
 */
function isJavaScriptEnabled() {
    try {
        // Create a noscript element to test against
        const testElement = document.createElement('noscript');
        testElement.textContent = 'JavaScript is disabled';
        document.body.appendChild(testElement);

        // Check if the noscript content remains (indicates JS is disabled)
        const isDisabled = document.body.textContent.includes('JavaScript is disabled');
        
        // Clean up
        document.body.removeChild(testElement);
        
        return !isDisabled;
    } catch (error) {
        console.error('Error checking JavaScript status:', error);
        return false; // Assume JS is disabled if there's an error
    }
}

// Example usage:
if (isJavaScriptEnabled()) {
    console.log('JavaScript is enabled');
} else {
    console.log('JavaScript is disabled');
}
```
