"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foxylinea.presale.com
Prompt: Create a function that detects JavaScript support in a user's browser and displays a message if it's disabled.
Generated: DETERMINISTIC_77485abcf452a50c
Batch ID: 20250612_135152
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
  <title>JavaScript Detection</title>
  <style>
    /* Default message displayed if JavaScript is disabled */
    #js-disabled-message {
      display: none; /* Hide by default if JavaScript is enabled */
      color: red;
      font-size: 16px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <noscript>
    <!-- This will display only if JavaScript is disabled -->
    <p id="js-disabled-message">JavaScript is disabled in your browser. Please enable JavaScript for better functionality.</p>
  </noscript>
  <script>
    // Function to detect JavaScript support
    (function detectJavaScriptSupport() {
      try {
        // Since this script runs, JavaScript is clearly enabled
        const messageElement = document.getElementById('js-disabled-message');
        if (messageElement) {
          // Ensure the message stays hidden as JavaScript is enabled
          messageElement.style.display = 'none';
        }
      } catch (error) {
        // Handle any unexpected errors gracefully
        console.error('An error occurred while detecting JavaScript support:', error);
      }
    })();
  </script>
</body>
</html>
```
