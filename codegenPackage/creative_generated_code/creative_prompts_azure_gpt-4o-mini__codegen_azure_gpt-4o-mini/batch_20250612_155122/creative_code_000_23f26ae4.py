"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jumper-change.xyz
Prompt: Write a JavaScript function to check if a user has JavaScript enabled in their browser before loading content.
Generated: DETERMINISTIC_23f26ae4d9b6f0d0
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the user's browser.
 * It does this by creating a hidden <noscript> element and checking its presence in the DOM.
 * 
 * @returns {boolean} - Returns true if JavaScript is enabled, false otherwise.
 */
function isJavaScriptEnabled() {
    // Create a <noscript> element to check for JavaScript support
    const noScriptElement = document.createElement('noscript');
    noScriptElement.innerHTML = 'JavaScript is disabled.';
    
    // Append the <noscript> element to the body
    document.body.appendChild(noScriptElement);

    // Check if the <noscript> element is still in the DOM
    const isEnabled = !document.body.contains(noScriptElement);

    // Remove the <noscript> element to clean up the DOM
    document.body.removeChild(noScriptElement);

    return isEnabled;
}

// Usage example
if (isJavaScriptEnabled()) {
    console.log("JavaScript is enabled.");
    // Load additional content or execute scripts here
} else {
    console.log("JavaScript is disabled. Please enable it for a better experience.");
    // Optionally, load alternative content for users without JavaScript
}
```
