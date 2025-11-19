"""
Generated Code Metadata:
========================
Original URL: https://imetobken.com
Prompt: Create a script that checks for JavaScript support on mobile devices and redirects users to an alternative page if JavaScript is disabled, specifically for the "ETH Pledge" platform.
Generated: DETERMINISTIC_5c5fc8a2b115d64b
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// No JavaScript redirect script for ETH Pledge platform

// Check if JavaScript is enabled by attempting to set a cookie
function checkJavaScriptSupport() {
    try {
        // Attempt to set a test cookie
        document.cookie = 'js_test=1; expires=Fri, 31 Dec 9999 23:59:59 GMT';
        
        // Check if the cookie was set successfully
        const cookies = document.cookie.split(';');
        let jsEnabled = false;
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith('js_test=1')) {
                jsEnabled = true;
                break;
            }
        }
        
        // If the cookie was not set, JavaScript is disabled
        if (!jsEnabled) {
            redirectToAlternativePage();
        }
    } catch (error) {
        console.error('Error checking JavaScript support:', error);
        redirectToAlternativePage();
    }
}

// Redirect to alternative page if JavaScript is disabled
function redirectToAlternativePage() {
    const alternativePageUrl = '/no-javascript'; // Update with desired URL
    window.location.href = alternativePageUrl;
}

// Run the check on page load
document.addEventListener('DOMContentLoaded', checkJavaScriptSupport);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETH Pledge</title>
</head>
<body>
    <!-- Page content here -->
    <script src="script.js"></script>
</body>
</html>
```

```html
<!-- no-javascript.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled</title>
</head>
<body>
    <h1>JavaScript is required to access this platform.</h1>
    <p>Please enable JavaScript in your browser settings to continue.</p>
</body>
</html>
```
