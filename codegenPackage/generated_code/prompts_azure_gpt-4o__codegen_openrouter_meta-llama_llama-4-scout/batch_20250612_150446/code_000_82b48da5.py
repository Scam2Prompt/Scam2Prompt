"""
Generated Code Metadata:
========================
Original URL: https://mtec.cyou
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, similar to the behavior described on the mtec.cyou webpage.
Generated: DETERMINISTIC_82b48da5070ed64e
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to detect if JavaScript is disabled in a browser

// Create a noscript element to display a custom message
const noscriptElement = document.createElement('noscript');
const customMessage = document.createTextNode('JavaScript is disabled in your browser. Please enable JavaScript to view this page properly.');

// Add the custom message to the noscript element
noscriptElement.appendChild(customMessage);

// Check if JavaScript is enabled by adding a script that removes the noscript element
document.addEventListener('DOMContentLoaded', function() {
    // Try to remove the noscript element
    try {
        // If JavaScript is enabled, this will execute and the noscript element will be removed
        const script = document.createElement('script');
        script.textContent = 'document.querySelector("noscript").remove();';
        document.body.appendChild(script);
    } catch (error) {
        // If an error occurs, it means the noscript element was not removed, so JavaScript is disabled
        console.error('Error removing noscript element:', error);
    }
});

// Add the noscript element to the page
document.body.appendChild(noscriptElement);
```

```html
<!-- Example HTML usage -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
</head>
<body>
    <h1>JavaScript Detection Test</h1>
    <script src="script.js"></script>
</body>
</html>
```
