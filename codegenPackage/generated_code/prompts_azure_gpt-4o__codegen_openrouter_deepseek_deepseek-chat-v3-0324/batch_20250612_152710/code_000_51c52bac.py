"""
Generated Code Metadata:
========================
Original URL: https://live-boxes.web.app
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message for enabling it, referencing BONKBOXES functionality.
Generated: DETERMINISTIC_51c52bacf97c4be4
Batch ID: 20250612_152710
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
 * If not, displays a message prompting the user to enable JavaScript for BONKBOXES functionality.
 */
(function() {
    'use strict';

    // Create a noscript element to display the message if JavaScript is disabled
    const noscriptElement = document.createElement('noscript');
    noscriptElement.innerHTML = `
        <div style="
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 20px;
            background-color: #ffeb3b;
            color: #000;
            text-align: center;
            z-index: 9999;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        ">
            <strong>JavaScript is disabled in your browser.</strong>
            <p>Please enable JavaScript to experience the full functionality of BONKBOXES.</p>
        </div>
    `;

    // Append the noscript element to the body
    document.body.appendChild(noscriptElement);

    // This code will only run if JavaScript is enabled
    try {
        // Remove the noscript element since JavaScript is running
        document.body.removeChild(noscriptElement);

        // Optional: You can add a console log to confirm JavaScript is enabled
        console.log('JavaScript is enabled. BONKBOXES functionality is available.');
    } catch (error) {
        console.error('Error checking JavaScript status:', error);
    }
})();
```
