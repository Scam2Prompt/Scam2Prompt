"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain.bike
Prompt: How can I enable JavaScript in my browser to use the Onchain-ETH features on onchain.bike?
Generated: DETERMINISTIC_1b52d6c00e44b540
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to check if JavaScript is enabled in the browser
// and display a message accordingly on onchain.bike.

document.addEventListener('DOMContentLoaded', function() {
    // Create a message element to inform the user
    const messageElement = document.createElement('div');
    
    // Check if JavaScript is enabled
    if (typeof window !== 'undefined' && window.document) {
        // JavaScript is enabled
        messageElement.textContent = 'JavaScript is enabled. You can now use Onchain-ETH features on onchain.bike!';
        messageElement.style.color = 'green';
    } else {
        // JavaScript is not enabled
        messageElement.textContent = 'JavaScript is disabled in your browser. Please enable it to use Onchain-ETH features.';
        messageElement.style.color = 'red';
    }

    // Append the message to the body of the document
    document.body.appendChild(messageElement);
});

// Fallback method to alert users to enable JavaScript
function showAlertForJavaScript() {
    alert("It seems JavaScript is disabled in your browser. Please enable it to use the full functionality of onchain.bike.");
}

// Call the function if JavaScript is not functioning correctly
window.onload = function() {
    if (document.body.innerHTML.indexOf('JavaScript is disabled') !== -1) {
        showAlertForJavaScript();
    }
};
```

```html
<!-- HTML structure to include the above JavaScript in a basic webpage -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Onchain-ETH JavaScript Check</title>
    <script src="script.js" defer></script> <!-- Link to the JavaScript file -->
</head>
<body>
    <noscript>
        <style>
            .noscript-message {
                color: red;
                font-weight: bold;
            }
        </style>
        <div class="noscript-message">
            JavaScript is disabled in your browser. Please enable it for the best experience on onchain.bike.
        </div>
    </noscript>
</body>
</html>
```
