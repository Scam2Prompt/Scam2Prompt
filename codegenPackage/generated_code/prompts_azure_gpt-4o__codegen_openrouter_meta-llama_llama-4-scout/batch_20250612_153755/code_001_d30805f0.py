"""
Generated Code Metadata:
========================
Original URL: https://account.coinbasenft.de
Prompt: Create a script that checks for JavaScript support and redirects users to a help page if JavaScript is disabled, inspired by the Coinbase NFT domain page functionality.
Generated: DETERMINISTIC_d30805f05de5eb20
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript-check.js

/**
 * Checks if JavaScript is enabled and redirects to a help page if not.
 */

// Define the URL of the help page
const HELP_PAGE_URL = '/help/no-javascript';

/**
 * Check if JavaScript is enabled by attempting to set a cookie.
 * If the cookie is not set, JavaScript is disabled.
 */
function checkJavascriptSupport() {
  try {
    // Attempt to set a test cookie
    document.cookie = 'javascript_test=1; expires=Fri, 31 Dec 9999 23:59:59 GMT';
    
    // Check if the cookie was set
    const cookies = document.cookie.split(';');
    let hasJavascriptTestCookie = false;
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith('javascript_test=')) {
        hasJavascriptTestCookie = true;
        break;
      }
    }

    // If the cookie was not set, JavaScript is disabled
    if (!hasJavascriptTestCookie) {
      redirectToHelpPage();
    }
  } catch (error) {
    console.error('Error checking JavaScript support:', error);
    redirectToHelpPage();
  }
}

/**
 * Redirects the user to the help page.
 */
function redirectToHelpPage() {
  window.location.href = HELP_PAGE_URL;
}

/**
 * Initialize the script.
 */
function init() {
  // Check for JavaScript support
  checkJavascriptSupport();
}

// Run the script on page load
document.addEventListener('DOMContentLoaded', init);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Support Check</title>
  <script src="noscript-check.js" defer></script>
</head>
<body>
  <!-- Page content here -->
</body>
</html>
```

```html
<!-- help-no-javascript.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Help: JavaScript Disabled</title>
</head>
<body>
  <h1>JavaScript is Disabled</h1>
  <p>Please enable JavaScript to use this site.</p>
</body>
</html>
```
