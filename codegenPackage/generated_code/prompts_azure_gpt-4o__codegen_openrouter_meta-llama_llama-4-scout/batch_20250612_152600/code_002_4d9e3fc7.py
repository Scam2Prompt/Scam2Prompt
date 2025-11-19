"""
Generated Code Metadata:
========================
Original URL: https://ethlast.com
Prompt: Create a script that checks for JavaScript support on a mobile device and redirects users to an alternative page if JavaScript is disabled, inspired by the ETH Pledge website functionality.
Generated: DETERMINISTIC_4d9e3fc7db80489a
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check for JavaScript support and redirect to alternative page if disabled

// Function to check for JavaScript support
function checkJavaScriptSupport() {
    // Create a hidden input element to store the JavaScript support status
    const jsSupportInput = document.createElement('input');
    jsSupportInput.type = 'hidden';
    jsSupportInput.id = 'js-support';
    jsSupportInput.value = 'unsupported';

    // Add the input element to the page
    document.body.appendChild(jsSupportInput);

    // If JavaScript is supported, update the input value
    jsSupportInput.value = 'supported';

    // Check the input value after 100ms to account for potential page reloads
    setTimeout(() => {
        if (jsSupportInput.value === 'unsupported') {
            // Redirect to alternative page if JavaScript is disabled
            redirectToAlternativePage();
        }
    }, 100);
}

// Function to redirect to alternative page
function redirectToAlternativePage() {
    // Define the alternative page URL
    const alternativePageUrl = '/alternative-page'; // Replace with your alternative page URL

    // Redirect to the alternative page
    window.location.href = alternativePageUrl;
}

// Check for JavaScript support on page load
document.addEventListener('DOMContentLoaded', () => {
    checkJavaScriptSupport();
});

// noscript element fallback for browsers that don't support JavaScript
document.write(`
    <noscript>
        <meta http-equiv="refresh" content="0;url=/alternative-page">
    </noscript>
`);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Support Check</title>
</head>
<body>
    <script src="script.js"></script>
</body>
</html>
```
