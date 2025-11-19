"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Generate a code snippet for a simple web application that incorporates cookie consent functionality, similar to what might be found on a site like Sensible Optimism.
Generated: DETERMINISTIC_a544ea990dd3a0bc
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Cookie Consent Web Application**
=====================================

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent Example</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Cookie Consent Example</h1>
    </header>
    <main>
        <p>This website uses cookies to improve your experience.</p>
        <button id="accept-cookies">Accept Cookies</button>
        <button id="decline-cookies">Decline Cookies</button>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

### styles.css
```css
body {
    font-family: Arial, sans-serif;
}

main {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}
```

### script.js
```javascript
// Get the cookie consent buttons
const acceptCookiesButton = document.getElementById('accept-cookies');
const declineCookiesButton = document.getElementById('decline-cookies');

// Set the cookie name
const COOKIE_NAME = 'cookie_consent';

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 86400 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
}

// Function to get a cookie
function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const [key, value] = cookie.split('=');
        if (key === name) {
            return value;
        }
    }
    return null;
}

// Function to show the cookie consent banner
function showCookieConsentBanner() {
    const cookieConsentBanner = document.createElement('div');
    cookieConsentBanner.innerHTML = `
        <p>This website uses cookies to improve your experience.</p>
        <button id="accept-cookies-banner">Accept Cookies</button>
        <button id="decline-cookies-banner">Decline Cookies</button>
    `;
    document.body.appendChild(cookieConsentBanner);

    const acceptCookiesBannerButton = document.getElementById('accept-cookies-banner');
    const declineCookiesBannerButton = document.getElementById('decline-cookies-banner');

    acceptCookiesBannerButton.addEventListener('click', () => {
        setCookie(COOKIE_NAME, 'accepted', 365);
        cookieConsentBanner.remove();
    });

    declineCookiesBannerButton.addEventListener('click', () => {
        setCookie(COOKIE_NAME, 'declined', 365);
        cookieConsentBanner.remove();
    });
}

// Check if the cookie consent cookie is set
if (!getCookie(COOKIE_NAME)) {
    showCookieConsentBanner();
}

// Add event listeners to the buttons
acceptCookiesButton.addEventListener('click', () => {
    setCookie(COOKIE_NAME, 'accepted', 365);
});

declineCookiesButton.addEventListener('click', () => {
    setCookie(COOKIE_NAME, 'declined', 365);
});
```

### server.js (using Node.js and Express.js)
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.static(__dirname));

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

### package.json
```json
{
    "name": "cookie-consent-example",
    "version": "1.0.0",
    "scripts": {
        "start": "node server.js"
    },
    "dependencies": {
        "express": "^4.17.1"
    }
}
```
