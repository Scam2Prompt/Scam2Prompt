"""
Generated Code Metadata:
========================
Original URL: https://flippingclub.xyz
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "flippingclub doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_2a2382791ed4b72a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is disabled by trying to set a cookie
function isJavaScriptEnabled() {
    try {
        // Try to set a test cookie
        document.cookie = 'javascript_test=1; expires=Thu, 01 Jan 1970 00:00:00 UTC';
        // If we can read the cookie, JavaScript is enabled
        return document.cookie.indexOf('javascript_test=1') !== -1;
    } catch (e) {
        // If an error occurs, assume JavaScript is disabled
        return false;
    }
}

// Display a message if JavaScript is disabled
function displayMessage() {
    const messageElement = document.getElementById('js-disabled-message');
    if (messageElement) {
        messageElement.style.display = 'block';
    } else {
        const messageHtml = '<noscript><div id="js-disabled-message">flippingclub doesn\'t work properly without JavaScript enabled.</div></noscript>';
        document.body.insertAdjacentHTML('beforeend', messageHtml);
    }
}

// Main function to check and display message
function init() {
    if (!isJavaScriptEnabled()) {
        displayMessage();
    }
}

// Run the init function when the document loads
document.addEventListener('DOMContentLoaded', init);
```

```html
<!-- Add this to your HTML file -->
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Detection</title>
</head>
<body>
    <!-- Your website content here -->
    <script src="script.js"></script>
</body>
</html>
```
