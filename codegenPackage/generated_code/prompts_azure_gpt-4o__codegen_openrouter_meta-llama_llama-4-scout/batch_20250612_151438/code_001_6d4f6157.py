"""
Generated Code Metadata:
========================
Original URL: https://hingehealth.eu
Prompt: Create a script that checks for JavaScript support and redirects users to an alternative page if JavaScript is disabled, as seen on the Hinge Health EU domain.
Generated: DETERMINISTIC_6d4f6157b3b0777d
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check for JavaScript support and redirect to alternative page if disabled

// Set the URL of the alternative page for users with JavaScript disabled
const alternativePageUrl = '/no-javascript.html';

// Function to check for JavaScript support
function checkJavaScriptSupport() {
    // Create a hidden element to test for JavaScript support
    const jsTestElement = document.createElement('div');
    jsTestElement.style.behavior = 'url(#javascript:void(0))';

    // Check if the element is supported (i.e., JavaScript is enabled)
    const isJavaScriptSupported = jsTestElement.style.behavior !== '';

    return isJavaScriptSupported;
}

// Function to redirect to alternative page if JavaScript is disabled
function redirectToAlternativePage() {
    // Check if JavaScript support is enabled
    if (!checkJavaScriptSupport()) {
        // Redirect to alternative page
        window.location.href = alternativePageUrl;
    }
}

// Run the redirect function on page load
document.addEventListener('DOMContentLoaded', redirectToAlternativePage);
```

```html
<!-- no-javascript.html (alternative page) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No JavaScript Support</title>
</head>
<body>
    <h1>JavaScript is required to use this website.</h1>
    <p>Please enable JavaScript in your browser settings to continue.</p>
</body>
</html>
```

```html
<!-- index.html (main page) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main Page</title>
</head>
<body>
    <!-- Main page content here -->
    <script src="script.js"></script>
</body>
</html>
```
