"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamosklogi.godaddysites.com
Prompt: How do I create a cookie policy for my website that complies with privacy regulations?
Generated: DETERMINISTIC_828f01db5fbfd0e7
Batch ID: 20250612_161035
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
  <title>Cookie Policy</title>
  <style>
    /* Basic styles for the cookie banner */
    #cookie-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #f9f9f9;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
      padding: 15px;
      text-align: center;
      font-size: 14px;
      display: none; /* Hidden by default */
    }

    #cookie-banner button {
      background-color: #4caf50;
      color: white;
      border: none;
      padding: 10px 20px;
      margin-left: 10px;
      border-radius: 5px;
      cursor: pointer;
    }

    #cookie-banner button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Cookie Banner -->
  <div id="cookie-banner">
    We use cookies to improve your experience on our website. By continuing to use this site, you agree to our use of cookies. For more information, please read our <a href="/cookie-policy" target="_blank">Cookie Policy</a>.
    <button id="accept-cookies">Accept</button>
    <button id="decline-cookies">Decline</button>
  </div>

  <!-- Content of your website -->
  <h1>Welcome to Our Website</h1>
  <p>Enjoy browsing our content!</p>

  <script>
    // Function to set a cookie
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
    }

    // Function to get a cookie by name
    function getCookie(name) {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.indexOf(name + "=") === 0) {
          return cookie.substring((name + "=").length, cookie.length);
        }
      }
      return null;
    }

    // Display cookie banner if no cookie preference is set
    const cookiePreference = getCookie("cookieConsent");
    if (!cookiePreference) {
      document.getElementById("cookie-banner").style.display = "block";
    }

    // Handle "Accept" button click
    document.getElementById("accept-cookies").addEventListener("click", () => {
      setCookie("cookieConsent", "accepted", 365); // Set cookie for 1 year
      document.getElementById("cookie-banner").style.display = "none";
    });

    // Handle "Decline" button click
    document.getElementById("decline-cookies").addEventListener("click", () => {
      setCookie("cookieConsent", "declined", 365); // Set cookie for 1 year
      document.getElementById("cookie-banner").style.display = "none";
    });
  </script>
</body>
</html>
```
