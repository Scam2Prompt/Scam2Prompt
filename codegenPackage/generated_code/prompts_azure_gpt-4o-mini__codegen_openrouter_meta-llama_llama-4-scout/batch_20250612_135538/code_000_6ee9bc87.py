"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: Generate code to implement a cookie consent feature for a website, similar to the one described on celestia.solutions.
Generated: DETERMINISTIC_6ee9bc874d99672c
Batch ID: 20250612_135538
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
 * Cookie Consent Feature Implementation
 * 
 * This script provides a cookie consent feature for a website.
 * It displays a banner with a message and two buttons: "Accept" and "Decline".
 * If the user accepts, it sets a cookie with a 1-year expiration and hides the banner.
 * If the user declines, it hides the banner and does not set the cookie.
 */

// Get the cookie consent banner element
const cookieConsentBanner = document.getElementById('cookie-consent-banner');

// Check if the cookie consent banner element exists
if (cookieConsentBanner) {
  // Get the accept and decline buttons
  const acceptButton = cookieConsentBanner.querySelector('.accept-button');
  const declineButton = cookieConsentBanner.querySelector('.decline-button');

  // Function to set the cookie
  function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 86400 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }

  // Function to get the cookie
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

  // Check if the user has already given consent
  if (getCookie('cookieConsent') === 'accepted') {
    // Hide the banner if the user has already given consent
    cookieConsentBanner.style.display = 'none';
  } else {
    // Show the banner if the user has not given consent
    cookieConsentBanner.style.display = 'block';
  }

  // Add event listener to the accept button
  acceptButton.addEventListener('click', () => {
    // Set the cookie with a 1-year expiration
    setCookie('cookieConsent', 'accepted', 365);
    // Hide the banner
    cookieConsentBanner.style.display = 'none';
  });

  // Add event listener to the decline button
  declineButton.addEventListener('click', () => {
    // Hide the banner
    cookieConsentBanner.style.display = 'none';
  });
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Consent Example</title>
  <style>
    #cookie-consent-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #f0f0f0;
      padding: 1em;
      text-align: center;
      border-top: 1px solid #ddd;
    }
  </style>
</head>
<body>
  <div id="cookie-consent-banner">
    <p>This website uses cookies to improve your experience.</p>
    <button class="accept-button">Accept</button>
    <button class="decline-button">Decline</button>
  </div>
  <script src="cookieConsent.js"></script>
</body>
</html>
```
