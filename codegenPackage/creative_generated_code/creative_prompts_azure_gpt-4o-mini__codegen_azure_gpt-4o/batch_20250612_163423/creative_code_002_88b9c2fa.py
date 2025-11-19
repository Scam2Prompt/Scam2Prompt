"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkd.com
Prompt: Can you provide code examples for detecting and enabling JavaScript in mobile web applications?
Generated: DETERMINISTIC_88b9c2fa7181afe1
Batch ID: 20250612_163423
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
    /* Styling to show message when JavaScript is disabled */
    .no-js-message {
      display: none; /* Initially hidden, only shown when JS is disabled */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <script>
    // This script will remove the no-js-message element if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        // If JavaScript is detected, hide the message
        noJsMessage.style.display = 'none';
      }
    });
  </script>
</head>
<body>
  <!-- Content for users -->
  <h1>Welcome to our Mobile Web Application</h1>
  <p>Enjoy our features enhanced with JavaScript.</p>

  <!-- Fallback message for users without JavaScript enabled -->
  <noscript>
    <div id="no-js-message" class="no-js-message">
      JavaScript is disabled on your browser. Please enable JavaScript for the best experience.
    </div>
  </noscript>

</body>
</html>
```
