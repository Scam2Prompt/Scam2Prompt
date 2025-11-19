"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockfe-cdn.godaddysites.com
Prompt: Generate a code snippet to implement cookie consent management for a website similar to BlockFi's photo gallery.
Generated: DETERMINISTIC_3d044ebbad92117e
Batch ID: 20250612_155349
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
    /* Basic styling for the cookie consent banner */
    #cookieConsentBanner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #333;
      color: #fff;
      padding: 15px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 1000;
    }
    #cookieConsentBanner button {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 20px;
      cursor: pointer;
      border-radius: 5px;
    }
    #cookieConsentBanner button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Cookie consent banner -->
  <div id="cookieConsentBanner" style="display:none;">
    <span>We use cookies to improve your experience. By continuing, you agree to our use of cookies. <a href="/cookie-policy" style="color: #007bff; text-decoration: underline;">Learn more</a></span>
    <button id="acceptCookies">Accept</button>
  </div>

  <script>
    // Utility function to set a cookie
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Expiration in days
      const expires = "expires=" + date.toUTCString();
      document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    // Utility function to get a cookie
    function getCookie(name) {
      const nameEQ = name + "=";
      const cookiesArray = document.cookie.split(';');
      for (let i = 0; i < cookiesArray.length; i++) {
        let cookie = cookiesArray[i].trim();
        if (cookie.indexOf(nameEQ) === 0) {
          return cookie.substring(nameEQ.length);
        }
      }
      return null;
    }

    // Function to handle cookie consent
    function handleCookieConsent() {
      const hasConsent = getCookie('cookieConsent'); // Check if consent was already given
      if (!hasConsent) {
        // Show the banner if consent not yet given
        const banner = document.getElementById('cookieConsentBanner');
        banner.style.display = 'flex'; // Make banner visible

        // Attach event listener to the Accept button
        const acceptButton = document.getElementById('acceptCookies');
        acceptButton.addEventListener('click', () => {
          setCookie('cookieConsent', 'true', 365); // Set consent cookie for 1 year
          banner.style.display = 'none'; // Hide the banner after accepting
        });
      }
    }

    // Initialize cookie consent management on page load
    document.addEventListener('DOMContentLoaded', handleCookieConsent);
  </script>
</body>
</html>
```
