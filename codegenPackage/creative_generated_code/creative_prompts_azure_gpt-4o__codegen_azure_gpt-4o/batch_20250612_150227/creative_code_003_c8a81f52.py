"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamausklogiixy.godaddysites.com
Prompt: Provide a step-by-step guide to setting up a cookie consent banner for a website, similar to the one described on Metamausklogiixy.
Generated: DETERMINISTIC_c8a81f52b1814e3a
Batch ID: 20250612_150227
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
  <style>
    /* Basic styles for the cookie banner */
    #cookie-banner {
      position: fixed;
      bottom: 0;
      width: 100%;
      background-color: #333;
      color: #fff;
      padding: 15px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
    }

    #cookie-banner button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
    }

    #cookie-banner button:hover {
      background-color: #45a049;
    }

    #cookie-banner.hidden {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Cookie Consent Banner -->
  <div id="cookie-banner">
    <span>
      We use cookies to personalize content and analyze our traffic. By clicking "Accept", you consent to the use of cookies.
    </span>
    <button id="accept-cookies">Accept</button>
  </div>

  <script>
    // Helper function to set a cookie
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // Set expiration in days
      const expires = "expires=" + date.toUTCString();
      document.cookie = `${name}=${value};${expires};path=/`;
    }

    // Helper function to get a cookie value
    function getCookie(name) {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
          return cookie.substring(name.length + 1);
        }
      }
      return null;
    }

    // Event listener for the "Accept" button
    document.getElementById('accept-cookies').addEventListener('click', () => {
      setCookie('cookieConsent', 'true', 365); // Store consent for 1 year
      document.getElementById('cookie-banner').classList.add('hidden'); // Hide the banner
    });

    // Check if consent has already been given
    window.onload = () => {
      const consent = getCookie('cookieConsent');
      if (consent === 'true') {
        document.getElementById('cookie-banner').classList.add('hidden'); // Hide banner if consent is present
      }
    };
  </script>
</body>
</html>
```
