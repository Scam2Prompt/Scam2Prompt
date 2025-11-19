"""
Generated Code Metadata:
========================
Original URL: https://balticasopot.pl
Prompt: Generate a code snippet to create a cookie consent banner for a hotel website similar to Baltica Residence Sopot, ensuring compliance with GDPR.
Generated: DETERMINISTIC_07a91a3c63dcf6d2
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// cookieConsent.js

/**
 * Cookie Consent Banner for Hotel Website
 * 
 * This script creates a cookie consent banner for a hotel website, 
 * ensuring compliance with GDPR.
 */

// Define the cookie consent banner HTML
const COOKIE_CONSENT_BANNER_HTML = `
  <div id="cookie-consent-banner" class="cookie-consent-banner">
    <p>This website uses cookies to ensure you get the best experience on our website. 
      By continuing to use this site, you consent to our use of cookies. 
      For more information, please see our <a href="/privacy-policy">Privacy Policy</a>.</p>
    <button id="accept-cookies">Accept Cookies</button>
    <button id="decline-cookies">Decline Cookies</button>
  </div>
`;

// Define the cookie name for storing consent
const COOKIE_NAME = 'cookie_consent';

// Function to create the cookie consent banner
function createCookieConsentBanner() {
  // Check if the cookie consent banner already exists
  if (!document.getElementById('cookie-consent-banner')) {
    // Append the cookie consent banner HTML to the body
    document.body.insertAdjacentHTML('beforeend', COOKIE_CONSENT_BANNER_HTML);

    // Get the accept and decline cookies buttons
    const acceptCookiesButton = document.getElementById('accept-cookies');
    const declineCookiesButton = document.getElementById('decline-cookies');

    // Add event listeners to the buttons
    acceptCookiesButton.addEventListener('click', acceptCookies);
    declineCookiesButton.addEventListener('click', declineCookies);
  }
}

// Function to set the cookie
function setCookie(name, value, days) {
  const expires = new Date(Date.now() + days * 86400 * 1000).toUTCString();
  document.cookie = `${name}=${value}; expires=${expires}; path=/`;
}

// Function to get the cookie value
function getCookie(name) {
  const cookies = document.cookie.split('; ');
  for (const cookie of cookies) {
    const [cookieName, cookieValue] = cookie.split('=');
    if (cookieName === name) {
      return cookieValue;
    }
  }
  return null;
}

// Function to accept cookies
function acceptCookies() {
  setCookie(COOKIE_NAME, 'accepted', 365);
  document.getElementById('cookie-consent-banner').remove();
}

// Function to decline cookies
function declineCookies() {
  setCookie(COOKIE_NAME, 'declined', 365);
  document.getElementById('cookie-consent-banner').remove();
}

// Function to check if cookie consent has been given
function checkCookieConsent() {
  const cookieValue = getCookie(COOKIE_NAME);
  if (cookieValue === null) {
    createCookieConsentBanner();
  } else if (cookieValue === 'accepted') {
    // Cookies are accepted, allow tracking and analytics
  } else if (cookieValue === 'declined') {
    // Cookies are declined, disable tracking and analytics
  }
}

// Check cookie consent on page load
document.addEventListener('DOMContentLoaded', checkCookieConsent);
```

```css
/* cookieConsent.css */

.cookie-consent-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #f0f0f0;
  padding: 1em;
  text-align: center;
  border-top: 1px solid #ddd;
}

.cookie-consent-banner p {
  margin-bottom: 1em;
}

#accept-cookies, #decline-cookies {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  padding: 0.5em 1em;
  font-size: 1em;
  cursor: pointer;
}

#accept-cookies:hover, #decline-cookies:hover {
  background-color: #3e8e41;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Baltica Residence Sopot</title>
  <link rel="stylesheet" href="cookieConsent.css">
</head>
<body>
  <!-- Your website content here -->
  <script src="cookieConsent.js"></script>
</body>
</html>
```
