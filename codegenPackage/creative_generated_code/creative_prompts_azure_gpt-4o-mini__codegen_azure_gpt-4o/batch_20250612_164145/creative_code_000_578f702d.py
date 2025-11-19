"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomware.net
Prompt: Generate a code snippet that demonstrates how to implement cookie consent management in a web application, similar to the practices mentioned on phantomware.net.
Generated: DETERMINISTIC_578f702dcc6d621f
Batch ID: 20250612_164145
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
    /* Styling for the cookie consent banner */
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
    }
    #cookie-consent-banner button {
      margin: 5px;
      padding: 10px 20px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 5px;
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
    <p>We use cookies to enhance your browsing experience. By clicking "Accept", you agree to our use of cookies. <a href="/privacy-policy" style="color: #fff; text-decoration: underline;">Learn more</a></p>
    <button id="accept-cookies">Accept</button>
    <button id="reject-cookies">Decline</button>
  </div>

  <script>
    // Helper function to set a cookie
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      const expires = `expires=${date.toUTCString()}`;
      document.cookie = `${name}=${value};${expires};path=/`;
    }

    // Helper function to get a cookie by name
    function getCookie(name) {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const c = cookies[i].trim();
        if (c.startsWith(name + '=')) {
          return c.substring(name.length + 1);
        }
      }
      return null;
    }

    // Initialize cookie consent management
    document.addEventListener('DOMContentLoaded', () => {
      const cookieConsentBanner = document.getElementById('cookie-consent-banner');
      const acceptCookiesButton = document.getElementById('accept-cookies');
      const rejectCookiesButton = document.getElementById('reject-cookies');

      // Check if consent has already been given or declined
      const consentStatus = getCookie('cookieConsent');
      if (!consentStatus) {
        // Show the cookie consent banner only if no preference is saved
        cookieConsentBanner.style.display = 'block';
      }

      // Event listener for the "Accept" button
      acceptCookiesButton.addEventListener('click', () => {
        setCookie('cookieConsent', 'accepted', 365); // Save consent for 1 year
        cookieConsentBanner.style.display = 'none';
      });

      // Event listener for the "Decline" button
      rejectCookiesButton.addEventListener('click', () => {
        setCookie('cookieConsent', 'declined', 365); // Save declined status for 1 year
        cookieConsentBanner.style.display = 'none';
      });
    });
  </script>
</body>
</html>
```
