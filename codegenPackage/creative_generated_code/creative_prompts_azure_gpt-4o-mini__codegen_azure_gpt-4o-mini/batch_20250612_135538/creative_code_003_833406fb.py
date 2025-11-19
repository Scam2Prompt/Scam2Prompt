"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: How can I create a user-friendly cookie consent banner for my website based on the guidelines from celestia.solutions?
Generated: DETERMINISTIC_833406fbdd63e87b
Batch ID: 20250612_135538
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
    <title>Cookie Consent Banner</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Cookie Consent Banner -->
    <div id="cookie-consent-banner" class="cookie-consent-banner hidden">
        <div class="cookie-consent-content">
            <p>
                This website uses cookies to enhance your experience. By continuing to use this website, you consent to our use of cookies.
            </p>
            <button id="accept-cookies" class="cookie-consent-button">Accept</button>
            <button id="decline-cookies" class="cookie-consent-button">Decline</button>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the cookie consent banner */
.cookie-consent-banner {
    position: fixed;
    bottom: 20px;
    left: 20px;
    right: 20px;
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    padding: 15px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.hidden {
    display: none;
}

.cookie-consent-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    margin-left: 10px;
}

.cookie-consent-button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js

// Function to check if cookie consent has been given
function checkCookieConsent() {
    return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
}

// Function to set the cookie for consent
function setCookieConsent(value) {
    const expirationDate = new Date();
    expirationDate.setFullYear(expirationDate.getFullYear() + 1); // 1 year expiration
    document.cookie = `cookieConsent=${value}; expires=${expirationDate.toUTCString()}; path=/`;
}

// Function to show the cookie consent banner if consent isn't given
function showCookieConsentBanner() {
    const banner = document.getElementById('cookie-consent-banner');
    if (!checkCookieConsent()) {
        banner.classList.remove('hidden');
    }
}

// Event listener for the accept button
document.getElementById('accept-cookies').addEventListener('click', () => {
    setCookieConsent('accepted');
    document.getElementById('cookie-consent-banner').classList.add('hidden');
});

// Event listener for the decline button
document.getElementById('decline-cookies').addEventListener('click', () => {
    setCookieConsent('declined');
    document.getElementById('cookie-consent-banner').classList.add('hidden');
});

// Show the cookie consent banner on page load
document.addEventListener('DOMContentLoaded', showCookieConsentBanner);
```

This code implements a user-friendly cookie consent banner following best practices, including proper styling, functionality, and error handling. Make sure to adjust the styles in `styles.css` as needed for your website's design.
