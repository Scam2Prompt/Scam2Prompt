"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pns.paladin.coinbaseindexfund.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message instructing the user to enable it, similar to the functionality described on `pns.paladin.coinbaseindexfund.com`.
Generated: DETERMINISTIC_1e247ced8ab9566c
Batch ID: 20250612_154842
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
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Styles for the message displayed when JavaScript is disabled */
    #js-disabled-message {
      display: none; /* Initially hidden */
      font-family: Arial, sans-serif;
      color: red;
      text-align: center;
      margin-top: 50px;
    }
  </style>
</head>
<body>
  <!-- Message shown only if JavaScript is disabled -->
  <noscript>
    <div id="js-disabled-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use the full functionality of this site.
    </div>
  </noscript>

  <!-- Content displayed when JavaScript is enabled -->
  <div id="main-content" style="display: none;">
    <h1>Welcome to the website!</h1>
    <p>JavaScript is enabled, and the site is functioning normally.</p>
  </div>

  <script>
    // JavaScript logic to hide the disabled message and show the main content
    // If JavaScript is enabled, the `main-content` div will be displayed
    try {
      const mainContent = document.getElementById('main-content');
      if (mainContent) {
        mainContent.style.display = 'block'; // Display the main content
      }
    } catch (error) {
      console.error('An error occurred while initializing the page:', error);
    }
  </script>
</body>
</html>
```
