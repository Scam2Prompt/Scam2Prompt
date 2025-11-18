"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-783--peaceful-nightingale-55a1b7.netlify.app
Prompt: Write code to dynamically enable JavaScript features in a web application and handle cases where JavaScript is disabled.
Generated: DETERMINISTIC_92531b9e37279e72
Batch ID: 20250612_151018
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
  <title>JavaScript Feature Enablement</title>
  <style>
    /* Styles for cases where JavaScript is disabled */
    .no-js {
      display: block;
      color: red;
    }

    .js-enabled {
      display: none;
    }
  </style>
  <script>
    // Dynamically enable features when JavaScript is active
    document.addEventListener("DOMContentLoaded", () => {
      // Replace 'no-js' elements with 'js-enabled' content
      const noJsElements = document.querySelectorAll('.no-js');
      const jsEnabledElements = document.querySelectorAll('.js-enabled');

      // Hide elements meant for when JS is disabled
      noJsElements.forEach((el) => {
        el.style.display = 'none';
      });

      // Show elements meant for when JS is enabled
      jsEnabledElements.forEach((el) => {
        el.style.display = 'block';
      });

      // Example dynamic functionality: Greet the user
      const dynamicContent = document.getElementById('dynamicContent');
      if (dynamicContent) {
        dynamicContent.textContent = 'Welcome! JavaScript is enabled.';
      }
    });
  </script>
</head>
<body>
  <!-- Content that appears only when JavaScript is disabled -->
  <noscript>
    <p class="no-js">JavaScript is disabled in your browser. Please enable JavaScript for full functionality.</p>
  </noscript>
  
  <!-- Content that appears when JavaScript is enabled -->
  <div class="js-enabled">
    <p id="dynamicContent">Loading dynamic features...</p>
  </div>
  
  <div>
    <h1>Static Content</h1>
    <p>This content is visible whether JavaScript is enabled or not.</p>
  </div>
</body>
</html>
```
