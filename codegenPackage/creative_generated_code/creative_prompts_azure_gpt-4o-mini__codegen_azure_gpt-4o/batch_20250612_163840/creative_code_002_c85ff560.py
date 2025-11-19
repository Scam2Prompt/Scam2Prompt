"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltoiken.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a mobile browser for a web app?
Generated: DETERMINISTIC_c85ff560440e68e5
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
  <title>JavaScript Enabled Check</title>
  <style>
    /* Default message if JavaScript is not enabled */
    .js-enabled-message {
      display: none; /* Hide message since JavaScript is enabled */
    }

    .no-js-message {
      display: block; /* Show message if JavaScript is disabled */
      color: red;
      font-size: 1.2em;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Fallback message for browsers with JavaScript disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled. Please enable JavaScript for the best experience.
    </div>
  </noscript>

  <!-- Container for the JavaScript check message -->
  <div id="js-enabled" class="js-enabled-message">
    JavaScript is enabled on your browser. Welcome!
  </div>

  <script>
    // Check if JavaScript is enabled 
    // Using JavaScript to display the appropriate message
    try {
      const jsEnabledMessage = document.getElementById('js-enabled');
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block'; // Show the message indicating JavaScript is enabled
      }
    } catch (error) {
      console.error('Error displaying JavaScript enabled message:', error);
    }
  </script>
</body>
</html>
```
