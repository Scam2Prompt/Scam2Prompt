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

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Consent Example</title>
  <style>
    /* Basic styling for the cookie consent banner */
    #cookie-consent-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #333;
      color: #fff;
      padding: 15px;
      text-align: center;
      display: none; /* Hidden by default */
      z-index: 1000;
    }
    #cookie-consent-banner button {
      margin-left: 10px;
      padding: 5px 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }
    #cookie-consent-banner button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Cookie Consent Banner -->
  <div id="cookie-consent-banner">
    <span>We use cookies to improve your experience. By using our site, you agree to our use of cookies.</span>
    <button id="accept-cookies">Accept</button>
    <button id="decline-cookies">Decline</button>
  </div>

  <script>
    // Function to check if the user has already made a cookie consent decision
    function hasCookieConsent() {
      return document.cookie.split(';').some((cookie) => cookie.trim().startsWith('cookieConsent='));
    }

    // Function to set a cookie with a specified name, value, and expiration days
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
    }

    // Function to handle cookie consent acceptance
    function acceptCookies() {
      setCookie('cookieConsent', 'accepted', 365); // Set cookie for 1 year
      hideCookieBanner();
    }

    // Function to handle cookie consent decline
    function declineCookies() {
      setCookie('cookieConsent', 'declined', 365); // Set cookie for 1 year
      hideCookieBanner();
    }

    // Function to hide the cookie consent banner
    function hideCookieBanner() {
      const banner = document.getElementById('cookie-consent-banner');
      banner.style.display = 'none';
    }

    // Initialize the cookie consent functionality
    function initCookieConsent() {
      if (!hasCookieConsent()) {
        const banner = document.getElementById('cookie-consent-banner');
        banner.style.display = 'block'; // Show the banner if no consent decision has been made
      }
    }

    // Event listeners for the Accept and Decline buttons
    document.getElementById('accept-cookies').addEventListener('click', acceptCookies);
    document.getElementById('decline-cookies').addEventListener('click', declineCookies);

    // Initialize the cookie consent functionality on page load
    window.onload = initCookieConsent;
  </script>
</body>
</html>
```
