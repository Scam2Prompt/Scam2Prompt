"""
Generated Code Metadata:
========================
Original URL: https://combo.magiceden.nl
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on the Magic Eden NL domain details page.
Generated: DETERMINISTIC_6f5d1f8455c31d50
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and hide the no-js message if it is
document.addEventListener('DOMContentLoaded', function() {
    // Remove the 'no-js' class from the HTML element if JavaScript is enabled
    document.documentElement.classList.remove('no-js');
    
    // Hide the no-js message element if it exists
    const noJsMessage = document.getElementById('no-js-message');
    if (noJsMessage) {
        noJsMessage.style.display = 'none';
    }
});

// Create a noscript fallback message in case JavaScript is disabled
(function() {
    // Create the noscript element
    const noscriptElement = document.createElement('noscript');
    
    // Create the message div
    const messageDiv = document.createElement('div');
    messageDiv.id = 'no-js-message';
    messageDiv.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 1rem;
        background-color: #ffeb3b;
        color: #000;
        text-align: center;
        z-index: 9999;
        font-family: Arial, sans-serif;
    `;
    messageDiv.textContent = 'JavaScript is disabled in your browser. Some features may not work properly.';
    
    // Append the message to the noscript element
    noscriptElement.appendChild(messageDiv);
    
    // Insert the noscript element at the beginning of the body
    document.body.insertBefore(noscriptElement, document.body.firstChild);
    
    // Add no-js class to HTML element initially
    document.documentElement.classList.add('no-js');
})();
```

```html
<!-- Example HTML structure that would work with this script -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <style>
        /* Basic styling for when JavaScript is disabled */
        .no-js #main-content {
            display: none;
        }
    </style>
</head>
<body>
    <div id="main-content">
        <!-- Your normal page content goes here -->
        <h1>Welcome to our website</h1>
        <p>This content requires JavaScript to function properly.</p>
    </div>
</body>
</html>
```
