"""
Generated Code Metadata:
========================
Original URL: https://peipeiairdrope888.pages.dev
Prompt: Create a simple webpage using HTML, CSS, and JavaScript that checks for cookie and JavaScript settings.
Generated: DETERMINISTIC_4383f029071d618a
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie and JavaScript Settings Checker</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Cookie and JavaScript Settings Checker</h1>
    <div id="cookie-status"></div>
    <div id="javascript-status"></div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css**
```css
body {
    font-family: Arial, sans-serif;
}

#cookie-status, #javascript-status {
    margin-bottom: 20px;
}

.enabled {
    color: green;
}

.disabled {
    color: red;
}
```

**script.js**
```javascript
// Check if cookies are enabled
function checkCookies() {
    try {
        const cookieName = 'testCookie';
        const cookieValue = 'testValue';

        // Set a test cookie
        document.cookie = `${cookieName}=${cookieValue}; expires=Fri, 31 Dec 9999 23:59:59 GMT`;

        // Check if the cookie was set successfully
        const cookies = document.cookie.split(';');
        const cookieExists = cookies.some(cookie => cookie.trim().startsWith(`${cookieName}=`));

        // Delete the test cookie
        document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 GMT`;

        return cookieExists;
    } catch (error) {
        console.error('Error checking cookies:', error);
        return false;
    }
}

// Check if JavaScript is enabled
function checkJavaScript() {
    return true; // JavaScript is always enabled if this script is running
}

// Update the UI with the results
function updateUI() {
    const cookieStatusElement = document.getElementById('cookie-status');
    const javascriptStatusElement = document.getElementById('javascript-status');

    const cookiesEnabled = checkCookies();
    const javascriptEnabled = checkJavaScript();

    cookieStatusElement.textContent = `Cookies: ${cookiesEnabled ? 'Enabled' : 'Disabled'}`;
    cookieStatusElement.className = cookiesEnabled ? 'enabled' : 'disabled';

    javascriptStatusElement.textContent = `JavaScript: ${javascriptEnabled ? 'Enabled' : 'Disabled'}`;
    javascriptStatusElement.className = javascriptEnabled ? 'enabled' : 'disabled';
}

// Run the checks on page load
document.addEventListener('DOMContentLoaded', updateUI);
```
