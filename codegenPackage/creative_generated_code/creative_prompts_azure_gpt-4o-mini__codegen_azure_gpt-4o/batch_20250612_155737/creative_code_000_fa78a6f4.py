"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wholygood.com
Prompt: Generate a code snippet that implements cookie consent management for a website, similar to the approach mentioned on wholygood.com.
Generated: DETERMINISTIC_fa78a6f4aa87fe88
Batch ID: 20250612_155737
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
  <title>Cookie Consent Management</title>
  <style>
    /* Styling for cookie consent banner */
    #cookie-consent-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #f8f9fa;
      color: #333;
      padding: 15px;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
      display: none; /* Initially hidden */
      text-align: center;
      font-family: Arial, sans-serif;
    }

    #cookie-consent-banner button {
      margin: 0 10px;
      padding: 8px 16px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    #cookie-consent-banner button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Cookie Consent Banner -->
  <div id="cookie-consent-banner">
    <span>We use cookies to improve your experience. By using our site, you accept our <a href="/privacy-policy" target="_blank">Privacy Policy</a>.</span>
    <button id="accept-cookies">Accept</button>
    <button id="decline-cookies">Decline</button>
  </div>

  <script>
    /**
     * Function to check if the user has already made a cookie consent decision.
     * @returns {string|null} - The stored cookie consent value, or null if not set.
     */
    function getCookie(name) {
      const cookies = document.cookie.split('; ');
      for (let cookie of cookies) {
        const [key, value] = cookie.split('=');
        if (key === name) return value;
      }
      return null;
    }

    /**
     * Function to set a cookie with a name, value, and expiration days.
     * @param {string} name - Name of the cookie.
     * @param {string} value - Value of the cookie.
     * @param {number} days - Number of days until the cookie expires.
     */
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/;SameSite=Strict`;
    }

    /**
     * Function to handle user decisions regarding cookie consent.
     * @param {boolean} isAccepted - Whether the user accepts cookies or not.
     */
    function handleCookieConsent(isAccepted) {
      if (isAccepted) {
        setCookie('cookieConsent', 'accepted', 365); // Set cookie for 1 year
        console.log('Cookies accepted.');
      } else {
        setCookie('cookieConsent', 'declined', 365); // Set cookie for 1 year
        console.log('Cookies declined.');
      }

      // Hide the cookie consent banner once the user makes a choice
      document.getElementById('cookie-consent-banner').style.display = 'none';
    }

    // Check if user has already made a cookie consent decision
    document.addEventListener('DOMContentLoaded', () => {
      const cookieConsent = getCookie('cookieConsent');
      if (!cookieConsent) {
        // Show the banner if no decision has been made
        document.getElementById('cookie-consent-banner').style.display = 'block';
      }
    });

    // Event listeners for Accept and Decline buttons
    document.getElementById('accept-cookies').addEventListener('click', () => handleCookieConsent(true));
    document.getElementById('decline-cookies').addEventListener('click', () => handleCookieConsent(false));
  </script>
</body>
</html>
```
