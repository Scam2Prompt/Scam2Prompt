"""
Generated Code Metadata:
========================
Original URL: https://cow-swap-dao.org
Prompt: Generate a code example that demonstrates how to enable JavaScript and cookies in a web application to improve user experience, inspired by Cow Swap DAO.
Generated: DETERMINISTIC_8a51f6f95d7861da
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Enabling JavaScript and Cookies in a Web Application**
===========================================================

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cow Swap DAO</title>
</head>
<body>
    <!-- Cookie and JavaScript enabled check -->
    <script src="script.js"></script>
</body>
</html>
```

### script.js
```javascript
// Check if JavaScript is enabled
function isJavaScriptEnabled() {
    try {
        return navigator.userAgent.toString().indexOf('JavaScript') !== -1;
    } catch (error) {
        console.error('Error checking JavaScript enabled:', error);
        return false;
    }
}

// Check if cookies are enabled
function areCookiesEnabled() {
    try {
        const date = new Date();
        document.cookie = `testCookie=${date.toUTCString()}; max-age=1`;
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            if (cookie.includes('testCookie')) {
                document.cookie = 'testCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
                return true;
            }
        }
        document.cookie = 'testCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
        return false;
    } catch (error) {
        console.error('Error checking cookies enabled:', error);
        return false;
    }
}

// Enable JavaScript and cookies if not already enabled
function enableJavaScriptAndCookies() {
    if (!isJavaScriptEnabled()) {
        // Display a message prompting the user to enable JavaScript
        const jsEnabledMessage = document.createElement('div');
        jsEnabledMessage.textContent = 'Please enable JavaScript to improve your experience.';
        document.body.appendChild(jsEnabledMessage);
    }

    if (!areCookiesEnabled()) {
        // Display a message prompting the user to enable cookies
        const cookiesEnabledMessage = document.createElement('div');
        cookiesEnabledMessage.textContent = 'Please enable cookies to improve your experience.';
        document.body.appendChild(cookiesEnabledMessage);
    }
}

// Run the enableJavaScriptAndCookies function on page load
document.addEventListener('DOMContentLoaded', enableJavaScriptAndCookies);
```

### cookie-handler.js
```javascript
// Set a cookie
function setCookie(name, value, days) {
    try {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = `expires=${date.toUTCString()}`;
        document.cookie = `${name}=${value}; ${expires}; path=/`;
    } catch (error) {
        console.error('Error setting cookie:', error);
    }
}

// Get a cookie
function getCookie(name) {
    try {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (cookieName === name) {
                return cookieValue;
            }
        }
        return null;
    } catch (error) {
        console.error('Error getting cookie:', error);
        return null;
    }
}

// Delete a cookie
function deleteCookie(name) {
    try {
        document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
    } catch (error) {
        console.error('Error deleting cookie:', error);
    }
}

// Example usage:
// Set a cookie that expires in 30 days
setCookie('exampleCookie', 'exampleValue', 30);

// Get the value of a cookie
const cookieValue = getCookie('exampleCookie');
console.log(cookieValue);

// Delete a cookie
deleteCookie('exampleCookie');
```
