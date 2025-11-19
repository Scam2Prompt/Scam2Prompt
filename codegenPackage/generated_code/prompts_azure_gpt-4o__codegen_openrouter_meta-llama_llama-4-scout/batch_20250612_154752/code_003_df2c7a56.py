"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: Generate JavaScript code to redirect users to a help page if JavaScript is disabled, inspired by the Rarecrew app's handling of JavaScript requirements.
Generated: DETERMINISTIC_df2c7a56179d30ad
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript.js

/**
 * Redirects users to a help page if JavaScript is disabled.
 */

// Check if JavaScript is enabled by checking for a specific cookie
function isJavaScriptEnabled() {
    // Create a test cookie
    const testCookieName = 'javascript_test';
    document.cookie = `${testCookieName}=1; expires=${new Date(Date.now() + 1000).toUTCString()}; path=/`;
    
    // Check if the cookie was set
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const [name, value] = cookie.split('=');
        if (name === testCookieName && value === '1') {
            // If the cookie was set, delete it
            document.cookie = `${testCookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
            return true;
        }
    }
    return false;
}

// Redirect to help page if JavaScript is disabled
function redirectToHelpPage() {
    const helpPageUrl = '/help/javascript-required';
    // Use the browser's built-in navigation to redirect
    window.location.href = helpPageUrl;
}

// Main function
function main() {
    try {
        // Check if JavaScript is enabled
        if (!isJavaScriptEnabled()) {
            // If not, redirect to help page
            redirectToHelpPage();
        }
    } catch (error) {
        // Log any errors that occur during execution
        console.error('Error checking JavaScript enabled:', error);
        // If an error occurs, still try to redirect to help page
        redirectToHelpPage();
    }
}

// Run the main function on page load
document.addEventListener('DOMContentLoaded', main);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Required</title>
    <noscript>
        <meta http-equiv="refresh" content="0;url=/help/javascript-required">
    </noscript>
</head>
<body>
    <!-- Page content here -->
    <script src="noscript.js" defer></script>
</body>
</html>
```
