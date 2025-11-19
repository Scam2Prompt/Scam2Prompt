"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: Generate code to implement a cookie consent feature for a website, similar to the one described on celestia.solutions.
Generated: DETERMINISTIC_6ee9bc874d99672c
Batch ID: 20250612_135538
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
  <title>Cookie Consent</title>
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
      text-align: center;
      z-index: 1000;
      display: none; /* Hidden by default */
    }

    #cookieConsentBanner button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      cursor: pointer;
      border-radius: 5px;
      margin-left: 10px;
    }

    #cookieConsentBanner button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Cookie Consent Banner -->
  <div id="cookieConsentBanner">
    <span>We use cookies to improve your experience on our website. By continuing, you agree to our use of cookies.</span>
    <button id="acceptCookies">Accept</button>
    <button id="declineCookies">Decline</button>
  </div>

  <script>
    // Function to check if the user has already made a cookie consent decision
    function hasCookieConsent() {
      return localStorage.getItem('cookieConsent') !== null;
    }

    // Function to show the cookie consent banner
    function showCookieConsentBanner() {
      const banner = document.getElementById('cookieConsentBanner');
      banner.style.display = 'block';
    }

    // Function to handle cookie consent acceptance
    function acceptCookies() {
      try {
        localStorage.setItem('cookieConsent', 'accepted');
        hideCookieConsentBanner();
        console.log('Cookies accepted.');
      } catch (error) {
        console.error('Error saving cookie consent:', error);
      }
    }

    // Function to handle cookie consent decline
    function declineCookies() {
      try {
        localStorage.setItem('cookieConsent', 'declined');
        hideCookieConsentBanner();
        console.log('Cookies declined.');
      } catch (error) {
        console.error('Error saving cookie consent:', error);
      }
    }

    // Function to hide the cookie consent banner
    function hideCookieConsentBanner() {
      const banner = document.getElementById('cookieConsentBanner');
      banner.style.display = 'none';
    }

    // Event listeners for the buttons
    document.getElementById('acceptCookies').addEventListener('click', acceptCookies);
    document.getElementById('declineCookies').addEventListener('click', declineCookies);

    // Show the banner only if the user hasn't made a decision yet
    if (!hasCookieConsent()) {
      showCookieConsentBanner();
    }
  </script>
</body>
</html>
```
