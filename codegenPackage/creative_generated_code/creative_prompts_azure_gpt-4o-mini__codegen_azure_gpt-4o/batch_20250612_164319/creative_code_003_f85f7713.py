"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrofunding-optimism-application5.pages.dev
Prompt: Provide an example of how to prompt users to enable JavaScript and cookies on a webpage.
Generated: DETERMINISTIC_f85f77131476a60b
Batch ID: 20250612_164319
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
  <title>Enable JavaScript and Cookies</title>
  <style>
    /* Styles for the warning messages */
    .warning {
      display: none; /* Hidden by default */
      padding: 20px;
      color: #fff;
      background-color: #f44336;
      text-align: center;
      font-size: 1.2rem;
    }
  </style>
</head>
<body>
  <!-- Warning message for JavaScript -->
  <noscript>
    <div class="warning">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>

  <!-- Warning message for cookies -->
  <div id="cookieWarning" class="warning">
    Cookies are disabled in your browser. Please enable cookies to use this website.
  </div>

  <!-- Main content -->
  <div id="mainContent">
    <h1>Welcome to Our Website</h1>
    <p>This is the main content of the webpage.</p>
  </div>

  <script>
    // Function to check if cookies are enabled
    function areCookiesEnabled() {
      try {
        // Attempt to set and read a test cookie
        document.cookie = "testcookie=1";
        return document.cookie.includes("testcookie=1");
      } catch (e) {
        return false; // Return false if there is an error
      }
    }

    // If cookies are disabled, show the warning message
    if (!areCookiesEnabled()) {
      const cookieWarningElement = document.getElementById('cookieWarning');
      cookieWarningElement.style.display = 'block';

      // Optionally hide the main content if cookies are required
      const mainContentElement = document.getElementById('mainContent');
      mainContentElement.style.display = 'none';
    }
  </script>
</body>
</html>
```
