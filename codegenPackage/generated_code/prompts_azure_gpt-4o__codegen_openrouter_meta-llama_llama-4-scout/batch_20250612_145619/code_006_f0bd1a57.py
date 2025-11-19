"""
Generated Code Metadata:
========================
Original URL: https://imtixoken.com
Prompt: Provide a code example for enabling JavaScript detection and redirecting users to a help page if JavaScript is disabled.
Generated: DETERMINISTIC_f0bd1a571b78aa37
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <noscript>
        <meta http-equiv="refresh" content="0;url=help.html">
    </noscript>
</head>
<body>
    <h1>JavaScript is enabled</h1>
    <script src="script.js" defer></script>
</body>
</html>
```

```html
<!-- help.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Help Page - JavaScript Disabled</title>
</head>
<body>
    <h1>JavaScript is disabled. Please enable JavaScript to continue.</h1>
</body>
</html>
```

```javascript
// script.js

/**
 * Detect if JavaScript is enabled and redirect to help page if not.
 * This script is not strictly necessary but can be used for additional JavaScript detection.
 */
// Check if JavaScript is enabled
function isJavaScriptEnabled() {
    try {
        return navigator.userAgent.indexOf('JavaScript') !== -1 || 
               typeof window !== 'undefined' && typeof document !== 'undefined';
    } catch (error) {
        console.error('Error detecting JavaScript:', error);
        return false;
    }
}

// Redirect to help page if JavaScript is disabled
if (!isJavaScriptEnabled()) {
    window.location.href = 'help.html';
} else {
    console.log('JavaScript is enabled');
}

// Additional script to test JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    const testElement = document.createElement('div');
    testElement.textContent = 'JavaScript is working';
    document.body.appendChild(testElement);
});
```
