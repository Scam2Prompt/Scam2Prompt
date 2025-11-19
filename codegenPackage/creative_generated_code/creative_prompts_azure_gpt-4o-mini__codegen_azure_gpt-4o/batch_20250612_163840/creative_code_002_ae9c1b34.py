"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtlioken.com
Prompt: Can you provide code snippets for checking if JavaScript is enabled in a mobile web environment?
Generated: DETERMINISTIC_ae9c1b347ebe5a19
Batch ID: 20250612_163840
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
  <title>Check JavaScript Enabled</title>
  <noscript>
    <!-- HTML displayed if JavaScript is disabled -->
    <style>
      .no-js-message {
        display: block;
        color: red;
        font-size: 18px;
        text-align: center;
        margin-top: 20px;
      }
    </style>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable it for better experience.
    </div>
  </noscript>
</head>
<body>
  <div id="js-enabled-message" style="display: none;">
    <!-- This message will show if JavaScript is enabled -->
    <p style="color: green; font-size: 18px; text-align: center; margin-top: 20px;">
      JavaScript is enabled in your browser!
    </p>
  </div>

  <script>
    // Check if JavaScript is enabled by setting the display of the message element
    try {
      const jsEnabledMessage = document.getElementById('js-enabled-message');
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block'; // Make the message visible
      }
    } catch (error) {
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
