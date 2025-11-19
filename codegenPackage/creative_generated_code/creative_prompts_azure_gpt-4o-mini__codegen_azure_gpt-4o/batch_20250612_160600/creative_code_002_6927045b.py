"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abubit.com
Prompt: How can I implement a cookie policy notification in my web application like the one on abubit.com?
Generated: DETERMINISTIC_6927045b0b17567a
Batch ID: 20250612_160600
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
  <title>Cookie Policy Notification</title>
  <style>
    /* Styling for the cookie notification banner */
    #cookie-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background-color: #333;
      color: #fff;
      padding: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 1000;
    }

    #cookie-banner p {
      margin: 0;
      font-size: 14px;
    }

    #cookie-banner button {
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      padding: 10px 15px;
      cursor: pointer;
      font-size: 14px;
    }

    #cookie-banner button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Cookie Notification Banner -->
  <div id="cookie-banner" style="display: none;">
    <p>We use cookies to improve your experience on our site. By using our site, you agree to our <a href="/cookie-policy" style="color: #4CAF50;">cookie policy</a>.</p>
    <button id="accept-cookies">Accept</button>
  </div>

  <script>
    // Function to check if cookies are already accepted
    function cookiesAccepted() {
      return localStorage.getItem('cookiesAccepted') === 'true';
    }

    // Function to show the cookie banner
    function showCookieBanner() {
      const banner = document.getElementById('cookie-banner');
      if (!cookiesAccepted()) {
        banner.style.display = 'flex';
      }
    }

    // Function to handle cookie acceptance
    function acceptCookies() {
      try {
        localStorage.setItem('cookiesAccepted', 'true');
        document.getElementById('cookie-banner').style.display = 'none';
      } catch (error) {
        console.error('Error saving cookie preference:', error);
      }
    }

    // Attach event listener to the Accept button
    document.getElementById('accept-cookies').addEventListener('click', acceptCookies);

    // Show the cookie banner when the page loads
    document.addEventListener('DOMContentLoaded', showCookieBanner);
  </script>
</body>
</html>
```
