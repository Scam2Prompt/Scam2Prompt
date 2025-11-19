"""
Generated Code Metadata:
========================
Original URL: https://m.coinbasenft.eu
Prompt: Generate JavaScript code to redirect users to a "JavaScript Required" page if JavaScript is disabled in their browser settings.
Generated: DETERMINISTIC_acd358ac5013cdb2
Batch ID: 20250612_155032
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
 * Redirects users to a "JavaScript Required" page if JavaScript is disabled.
 */

// Define the URL of the "JavaScript Required" page
const javascriptRequiredPage = '/javascript-required';

/**
 * Check if JavaScript is enabled by attempting to set a cookie.
 * If the cookie is not set, it means JavaScript is disabled.
 */
function isJavaScriptEnabled() {
  try {
    // Attempt to set a test cookie
    document.cookie = 'javascriptEnabled=true; expires=Fri, 31 Dec 9999 23:59:59 GMT';
    // Check if the cookie was set successfully
    return document.cookie.includes('javascriptEnabled=true');
  } catch (error) {
    // If an error occurs, assume JavaScript is disabled
    return false;
  }
}

/**
 * Redirects the user to the "JavaScript Required" page.
 */
function redirectToJavaScriptRequiredPage() {
  // Use the window.location object to redirect the user
  window.location.href = javascriptRequiredPage;
}

// Check if JavaScript is enabled on page load
document.addEventListener('DOMContentLoaded', () => {
  if (!isJavaScriptEnabled()) {
    // If JavaScript is disabled, redirect the user
    redirectToJavaScriptRequiredPage();
  }
});
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
    <meta http-equiv="refresh" content="0;url=/javascript-required">
  </noscript>
</head>
<body>
  <!-- Your website content here -->
  <script src="noscript.js" defer></script>
</body>
</html>
```

```html
<!-- javascript-required.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Required</title>
</head>
<body>
  <h1>JavaScript Required</h1>
  <p>Please enable JavaScript in your browser settings to access this website.</p>
</body>
</html>
```
