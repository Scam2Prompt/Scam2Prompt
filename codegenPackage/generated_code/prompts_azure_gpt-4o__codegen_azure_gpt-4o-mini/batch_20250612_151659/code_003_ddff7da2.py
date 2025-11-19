"""
Generated Code Metadata:
========================
Original URL: https://full-mint-website-master.pages.dev
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message accordingly, as seen in the React app at https://full-mint-website-master.pages.dev.
Generated: DETERMINISTIC_ddff7da2e811d8c8
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to check if JavaScript is enabled in the browser
function checkJavaScriptEnabled() {
    // Create a div element to display the message
    const messageDiv = document.createElement('div');
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '0';
    messageDiv.style.left = '0';
    messageDiv.style.width = '100%';
    messageDiv.style.backgroundColor = '#f44336'; // Red background for visibility
    messageDiv.style.color = '#ffffff'; // White text color
    messageDiv.style.textAlign = 'center';
    messageDiv.style.padding = '10px';
    messageDiv.style.zIndex = '1000'; // Ensure it appears above other content

    // Message to display if JavaScript is enabled
    const jsEnabledMessage = 'JavaScript is enabled in your browser.';
    
    // Message to display if JavaScript is disabled
    const jsDisabledMessage = 'JavaScript is disabled in your browser. Please enable it for the best experience.';

    // Check if JavaScript is enabled by appending a message to the body
    document.body.appendChild(messageDiv);
    messageDiv.textContent = jsEnabledMessage;

    // If JavaScript is disabled, this message will be shown instead
    // This is achieved by using a <noscript> tag in the HTML
}

// Call the function to check JavaScript status
checkJavaScriptEnabled();
```

```html
<!-- Include this in your HTML file to handle the case when JavaScript is disabled -->
<noscript>
    <style>
        .noscript-message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #f44336; /* Red background for visibility */
            color: #ffffff; /* White text color */
            text-align: center;
            padding: 10px;
            z-index: 1000; /* Ensure it appears above other content */
        }
    </style>
    <div class="noscript-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>
</noscript>
```
