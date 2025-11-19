"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: Generate code to implement a cookie consent feature for a website, similar to the one described on celestia.solutions.
Generated: DETERMINISTIC_6ee9bc874d99672c
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
  <title>Cookie Consent</title>
  <style>
    /* Styling for the cookie consent banner */
    #cookieConsent {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #333;
      color: #fff;
      padding: 15px;
      font-size: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 1000;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
    }

    #cookieConsent button {
      background-color: #04AA6D;
      color: #fff;
      border: none;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      border-radius: 5px;
    }

    #cookieConsent button:hover {
      background-color: #037a54;
    }
  </style>
</head>
<body>
  <!-- Cookie consent banner -->
  <div id="cookieConsent" style="display: none;">
    <span>We use cookies to improve your experience on our website. By continuing, you agree to our use of cookies.</span>
    <button id="acceptCookies">Accept</button>
  </div>

  <script>
    // Function to set a cookie with a specified name, value, and expiration days
    function setCookie(name, value, days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      const expires = "expires=" + date.toUTCString();
      document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    // Function to get a cookie value by its name
    function getCookie(name) {
      const nameEQ = name + "=";
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.indexOf(nameEQ) === 0) {
          return cookie.substring(nameEQ.length, cookie.length);
        }
      }
      return null;
    }

    // Initialize the cookie consent banner
    window.onload = function() {
      const cookieConsent = getCookie("cookieConsent");
      
      // Show the banner only if the user hasn't already accepted cookies
      if (!cookieConsent) {
        document.getElementById("cookieConsent").style.display = "flex";
      }

      // Handle the click event on the "Accept" button
      document.getElementById("acceptCookies").addEventListener("click", function() {
        setCookie("cookieConsent", "true", 365); // Set a cookie valid for 1 year
        document.getElementById("cookieConsent").style.display = "none"; // Hide the banner
      });
    };
  </script>
</body>
</html>
```
