"""
Generated Code Metadata:
========================
Original URL: https://debridge.xyz
Prompt: Generate a JavaScript snippet to check if JavaScript is enabled in a browser and display a message like the one on deBridge's website.
Generated: DETERMINISTIC_4a28c341fb6d3635
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled in the browser
function checkJavascriptEnabled() {
    // Create a container element to display the message
    const jsEnabledContainer = document.createElement('div');
    jsEnabledContainer.id = 'js-enabled-container';

    // Check if JavaScript is enabled by trying to access the body element
    try {
        // If JavaScript is enabled, this line will execute without errors
        document.body.appendChild(jsEnabledContainer);
        
        // Display a message if JavaScript is enabled
        jsEnabledContainer.innerHTML = `
            <style>
                #js-enabled-container {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    background-color: #f2f2f2;
                    border-bottom: 1px solid #ccc;
                    padding: 10px;
                    text-align: center;
                    font-family: Arial, sans-serif;
                }
            </style>
            <p>JavaScript is enabled in your browser.</p>
        `;
    } catch (error) {
        // If an error occurs, it means JavaScript is disabled
        console.error('JavaScript is disabled in the browser:', error);
    }
}

// Run the check on page load
document.addEventListener('DOMContentLoaded', checkJavascriptEnabled);
```
