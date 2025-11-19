"""
Generated Code Metadata:
========================
Original URL: https://mateimsklogi-usa.godaddysites.com
Prompt: How can I implement a cookie consent banner like the one on mateimsklogi-usa.godaddysites.com using JavaScript and HTML?
Generated: DETERMINISTIC_54dcf6c10dfb6089
Batch ID: 20250622_211158
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
  <title>Cookie Consent Banner</title>
  <style>
    /* Basic styling for the cookie consent banner */
    #cookie-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: #333;
      color: #fff;
      padding: 15px;
      text-align: center;
      box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
      display: none; /* Hidden by default */
    }

    #cookie-banner button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      margin-left: 10px;
      cursor: pointer;
      border-radius: 5px;
    }

    #cookie-banner button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Cookie Consent Banner -->
  <div id="cookie-banner">
    <span>We use cookies to improve your experience. By using our site, you agree to our use of cookies.</span>
    <button id="accept-cookies">Accept</button>
  </div>

  <script>
    // Function to check if the user has already accepted cookies
    function hasAcceptedCookies() {
      return localStorage.getItem('cookiesAccepted') === 'true';
    }

    // Function to show the cookie banner
    function showCookieBanner() {
      const banner = document.getElementById('cookie-banner');
      banner.style.display = 'block';
    }

    // Function to hide the cookie banner
    function hideCookieBanner() {
      const banner = document.getElementById('cookie-banner');
      banner.style.display = 'none';
    }

    // Function to handle cookie acceptance
    function acceptCookies() {
      try {
        // Save the user's consent in localStorage
        localStorage.setItem('cookiesAccepted', 'true');
        // Hide the cookie banner
        hideCookieBanner();
      } catch (error) {
        console.error('Error saving cookie consent:', error);
      }
    }

    // Event listener for the "Accept" button
    document.getElementById('accept-cookies').addEventListener('click', acceptCookies);

    // Check if cookies have already been accepted
    if (!hasAcceptedCookies()) {
      // Show the cookie banner if consent has not been given
      showCookieBanner();
    }
  </script>
</body>
</html>
```
