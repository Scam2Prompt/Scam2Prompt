"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://localcamflings.com
Prompt: Write JavaScript code to detect if a user's browser has JavaScript enabled and display a message prompting them to enable it if disabled.
Generated: DETERMINISTIC_ec0976a13e02397d
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if JavaScript is enabled using the `<noscript>` tag.
// This code works in conjunction with HTML to detect if JavaScript is disabled.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Detection</title>
  <style>
    /* Styling for the no-JavaScript message */
    .noscript-message {
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Default message shown when JavaScript is disabled -->
  <noscript>
    <div class="noscript-message">
      JavaScript is disabled in your browser. Please enable JavaScript for a better browsing experience.
    </div>
  </noscript>

  <!-- Content for users with JavaScript enabled -->
  <div id="js-enabled-content">
    <h1>Welcome to the website!</h1>
    <p>JavaScript is enabled in your browser.</p>
  </div>

  <script>
    // Hide the content meant for users with JavaScript disabled
    // This is just a precaution since `<noscript>` tag handles it by default
    const noScriptMessage = document.querySelector('.noscript-message');
    if (noScriptMessage) {
      noScriptMessage.style.display = 'none';
    }

    // Additional functionality for browsers with JavaScript enabled can go here
    console.log('JavaScript is enabled in your browser.');
  </script>
</body>
</html>
```
