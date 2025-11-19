"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balticasopot.pl
Prompt: Generate a code snippet to create a cookie consent banner for a hotel website similar to Baltica Residence Sopot, ensuring compliance with GDPR.
Generated: DETERMINISTIC_07a91a3c63dcf6d2
Batch ID: 20250612_135829
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
  <title>Hotel Website</title>
  <style>
    /* Basic styling for the cookie consent banner */
    #cookie-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background-color: rgba(0, 0, 0, 0.9);
      color: #fff;
      padding: 15px;
      text-align: center;
      font-size: 14px;
      z-index: 1000;
    }

    #cookie-banner a {
      color: #4caf50;
      text-decoration: underline;
    }

    #cookie-banner button {
      margin-left: 15px;
      background-color: #4caf50;
      color: #fff;
      border: none;
      padding: 8px 12px;
      border-radius: 4px;
      cursor: pointer;
    }

    #cookie-banner button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <!-- Cookie Consent Banner -->
  <div id="cookie-banner" style="display: none;">
    <p>
      We use cookies to improve your browsing experience on our website. By using our site, you consent to the use of cookies.
      <a href="/cookie-policy" target="_blank">Learn more</a>
    </p>
    <button id="accept-cookies">Accept</button>
  </div>

  <script>
    // Function to check if cookies are already accepted
    function cookiesAccepted() {
      return localStorage.getItem('cookiesAccepted') === 'true';
    }

    // Function to handle accepting cookies
    function acceptCookies() {
      try {
        localStorage.setItem('cookiesAccepted', 'true');
        document.getElementById('cookie-banner').style.display = 'none';
      } catch (error) {
        console.error('Error saving cookie consent status:', error);
      }
    }

    // Event listener for the "Accept" button
    document.getElementById('accept-cookies').addEventListener('click', acceptCookies);

    // Display the banner if cookies are not accepted yet
    if (!cookiesAccepted()) {
      document.getElementById('cookie-banner').style.display = 'block';
    }
  </script>
</body>
</html>
```
