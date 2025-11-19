"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinneon.com
Prompt: "Generate code for a cookie consent banner that complies with GDPR for a business website."
Generated: DETERMINISTIC_c5bb12ab59e67f12
Batch ID: 20250612_163828
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
  <title>Cookie Consent</title>
  <style>
    /* Styles for the cookie consent banner */
    #cookie-banner {
      position: fixed;
      bottom: 0;
      width: 100%;
      background-color: #222;
      color: #fff;
      padding: 15px;
      text-align: center;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
      font-size: 14px;
      z-index: 1000;
    }

    #cookie-banner button {
      margin-left: 10px;
      padding: 5px 10px;
      background-color: #4CAF50;
      border: none;
      color: white;
      cursor: pointer;
      font-size: 14px;
      border-radius: 3px;
    }

    #cookie-banner button:hover {
      background-color: #45a049;
    }

    #cookie-banner a {
      color: #4CAF50;
      text-decoration: underline;
    }

    #cookie-banner.hidden {
      display: none;
    }
  </style>
</head>
<body>
  
  <!-- Cookie Consent Banner -->
  <div id="cookie-banner">
    <span>We use cookies to improve your experience. By continuing to use our website, you agree to our <a href="/privacy-policy" target="_blank">Privacy Policy</a>.</span>
    <button id="accept-cookies">Accept</button>
    <button id="decline-cookies">Decline</button>
  </div>

  <script>
    // Function to set a cookie
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      const expires = "expires=" + date.toUTCString();
      document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    // Function to get a cookie value
    function getCookie(name) {
      const nameEQ = name + "=";
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim();
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
      }
      return null;
    }

    // Function to handle cookie consent actions
    function handleCookieConsent(action) {
      if (action === 'accept') {
        // Set a cookie indicating consent
        setCookie('cookieConsent', 'true', 365);
      } else if (action === 'decline') {
        // Set a cookie indicating decline
        setCookie('cookieConsent', 'false', 365);
      }
      // Hide the banner
      document.getElementById('cookie-banner').classList.add('hidden');
    }

    // Check if consent cookie already exists
    document.addEventListener('DOMContentLoaded', () => {
      const consentCookie = getCookie('cookieConsent');
      if (consentCookie === 'true' || consentCookie === 'false') {
        document.getElementById('cookie-banner').classList.add('hidden');
      } else {
        document.getElementById('accept-cookies').addEventListener('click', () => handleCookieConsent('accept'));
        document.getElementById('decline-cookies').addEventListener('click', () => handleCookieConsent('decline'));
      }
    });
  </script>

</body>
</html>
```
