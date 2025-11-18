"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapfinderbq.github.io
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "avedex-m doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_d0538c98a7b701f2
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the browser
 * and display a message if it is not.
 */
function checkJavaScriptEnabled() {
    // Create a div element to hold the message
    const messageDiv = document.createElement('div');

    // Set the message text
    messageDiv.textContent = "avedex-m doesn't work properly without JavaScript enabled.";

    // Style the message for visibility
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '0';
    messageDiv.style.left = '0';
    messageDiv.style.width = '100%';
    messageDiv.style.backgroundColor = '#ffcc00'; // Yellow background
    messageDiv.style.color = '#000'; // Black text
    messageDiv.style.textAlign = 'center';
    messageDiv.style.padding = '10px';
    messageDiv.style.zIndex = '1000'; // Ensure it is above other content

    // Append the message to the body
    document.body.appendChild(messageDiv);
}

// Call the function to check for JavaScript enabled
checkJavaScriptEnabled();
``` 

```html
<!-- Include a noscript tag to display a message when JavaScript is not enabled -->
<noscript>
    <style>
        .noscript-message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #ffcc00;
            color: #000;
            text-align: center;
            padding: 10px;
            z-index: 1000;
        }
    </style>
    <div class="noscript-message">
        avedex-m doesn't work properly without JavaScript enabled.
    </div>
</noscript>
```
