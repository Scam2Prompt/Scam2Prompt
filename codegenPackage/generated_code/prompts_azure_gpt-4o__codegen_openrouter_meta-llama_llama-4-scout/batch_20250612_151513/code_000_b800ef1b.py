"""
Generated Code Metadata:
========================
Original URL: https://ethff.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message if it is disabled, similar to the behavior described on the ETH 2.0 website.
Generated: DETERMINISTIC_b800ef1bc402efa4
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled in the browser
function checkJavaScriptEnabled() {
    // Create a noscript element to display a message if JavaScript is disabled
    const noscriptElement = document.createElement('noscript');
    
    // Set the text content of the noscript element
    noscriptElement.textContent = `
        <style>
            /* Style the noscript element to display a prominent message */
            noscript {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background-color: #FFC080;
                color: #666;
                text-align: center;
                padding: 1em;
                font-weight: bold;
            }
        </style>
        JavaScript is disabled. Please enable JavaScript to view this site properly.
    `;

    // Append the noscript element to the body of the HTML document
    document.body.appendChild(noscriptElement);
}

// Call the function to check JavaScript enabled status
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Enabled Check</title>
</head>
<body>
    <script src="script.js"></script>
</body>
</html>
```
