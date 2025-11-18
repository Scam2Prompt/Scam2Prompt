"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.ire-coinbase.com
Prompt: Create a script to check if a user is accessing a webpage using Internet Explorer 11 and display a message recommending an alternative browser, as mentioned in the cPanel Webmail login system.
Generated: DETERMINISTIC_7cdd97ff5bf0e7a8
Batch ID: 20250612_154651
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
  <title>Browser Check</title>
  <style>
    /* Basic styling for the message displayed to the user */
    #browser-warning {
      display: none;
      margin: 20px;
      padding: 15px;
      border: 1px solid #ccc;
      background-color: #f8d7da;
      color: #721c24;
      border-radius: 5px;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <div id="browser-warning">
    You are using Internet Explorer 11, which is outdated and may not work well on this site. Please consider using an alternative browser like Google Chrome, Mozilla Firefox, or Microsoft Edge for a better experience.
  </div>

  <script>
    /**
     * Function to check the browser version and display a warning for Internet Explorer 11
     */
    (function checkBrowser() {
      try {
        // The user agent string for Internet Explorer 11 contains "Trident/7.0"
        const isIE11 = !!window.MSInputMethodContext && !!document.documentMode;
        
        if (isIE11) {
          // If the browser is IE11, display the warning message
          const warningElement = document.getElementById('browser-warning');
          warningElement.style.display = 'block';
        }
      } catch (error) {
        // Log any unexpected errors to the console
        console.error('An error occurred while checking the browser:', error);
      }
    })();
  </script>
</body>
</html>
```
