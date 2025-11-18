"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho-frontend.pages.dev
Prompt: Create a JavaScript function to check if JavaScript is enabled in a Morpho-based frontend application.
Generated: DETERMINISTIC_935e4dd7f256c9cf
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if JavaScript is enabled in the browser.
 * This function should be called on the page load to determine if JavaScript is active.
 * 
 * @returns {void}
 */
function checkJavaScriptEnabled() {
    // Create a <noscript> element to display a message if JavaScript is disabled
    const noScriptMessage = document.createElement('div');
    noScriptMessage.id = 'noscript-message';
    noScriptMessage.style.display = 'none'; // Hidden by default

    // Append the message to the body
    noScriptMessage.innerHTML = '<p style="color: red;">JavaScript is disabled in your browser. Please enable JavaScript to use this application.</p>';
    document.body.appendChild(noScriptMessage);

    // If JavaScript is enabled, remove the <noscript> message
    window.onload = function() {
        noScriptMessage.style.display = 'none'; // Make sure it's hidden
    };

    // Set a timeout to show the message if it is still present after some time
    setTimeout(() => {
        if (document.getElementById('noscript-message')) {
            noScriptMessage.style.display = 'block'; // Show the message if still present
        }
    }, 1000); // Wait for 1 second before checking
}

// Call the function to check if JavaScript is enabled
checkJavaScriptEnabled();
```
