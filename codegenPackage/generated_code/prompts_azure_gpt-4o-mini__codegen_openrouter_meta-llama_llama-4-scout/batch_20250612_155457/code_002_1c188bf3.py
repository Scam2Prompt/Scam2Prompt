"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in a web browser.
 * 
 * This function uses a simple script tag to execute a JavaScript function.
 * If JavaScript is enabled, the function will return true; otherwise, it will return false.
 * 
 * @returns {boolean} True if JavaScript is enabled, false otherwise.
 */
function isJavaScriptEnabled() {
    try {
        // Create a script tag to execute a JavaScript function
        const script = document.createElement('script');
        script.text = 'window.jsEnabled = true;';
        document.head.appendChild(script);
        
        // Check if the JavaScript function was executed
        return window.jsEnabled === true;
    } catch (error) {
        // If an error occurs, JavaScript is likely disabled
        console.error('Error checking JavaScript enabled:', error);
        return false;
    } finally {
        // Clean up the script tag
        if (window.jsEnabled) {
            delete window.jsEnabled;
        }
    }
}

// Example usage:
document.addEventListener('DOMContentLoaded', function () {
    const jsEnabled = isJavaScriptEnabled();
    console.log('JavaScript enabled:', jsEnabled);
});
```
