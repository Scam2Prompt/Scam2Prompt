"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketisillegal.com
Prompt: Generate code to integrate a cookie consent banner for a website similar to polymarketisillegal.com, ensuring compliance with data privacy regulations.
Generated: DETERMINISTIC_b6216149cb3ba571
Batch ID: 20250612_164046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent Banner Example</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <!-- Main content of the website -->
    <div class="content">
        <h1>Welcome to Our Website</h1>
        <p>This is a sample website that uses a cookie consent banner.</p>
    </div>

    <!-- Cookie Consent Banner -->
    <div id="cookieConsentBanner" class="cookie-consent-banner">
        <p>This website uses cookies to ensure you get the best experience on our website. <a href="/privacy-policy" target="_blank">Learn more</a>.</p>
        <button id="acceptCookies" class="consent-button">Accept</button>
        <button id="declineCookies" class="consent-button">Decline</button>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for styling */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Style for the cookie consent banner */
.cookie-consent-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #f1f1f1;
    padding: 20px;
    text-align: center;
    border-top: 1px solid #ccc;
    display: none; /* Hidden by default */
    z-index: 1000;
}

/* Style for buttons */
.consent-button {
    margin: 0 10px;
    padding: 10px 15px;
    border: none;
    background-color: #007bff;
    color: white;
    cursor: pointer;
}

.consent-button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js

// Function to show the cookie consent banner
function showCookieConsentBanner() {
    const banner = document.getElementById('cookieConsentBanner');
    banner.style.display = 'block';
}

// Function to set a cookie
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// Function to check if the user has already consented
function checkCookieConsent() {
    const consentCookie = document.cookie.split('; ').find(row => row.startsWith('cookieConsent='));
    if (consentCookie) {
        const consentValue = consentCookie.split('=')[1];
        return consentValue === 'accepted';
    }
    return false;
}

// Event listeners for buttons
document.addEventListener('DOMContentLoaded', () => {
    if (!checkCookieConsent()) {
        showCookieConsentBanner();
    }

    document.getElementById('acceptCookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'accepted', 30); // Set cookie for 30 days
        document.getElementById('cookieConsentBanner').style.display = 'none';
    });

    document.getElementById('declineCookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'declined', 30); // Set cookie for 30 days
        document.getElementById('cookieConsentBanner').style.display = 'none';
    });
});
```

This code comprises an HTML file, a CSS file for styling, and a JavaScript file to handle cookie consent logic. Each file includes comments and follows best practices for readability and maintainability.
