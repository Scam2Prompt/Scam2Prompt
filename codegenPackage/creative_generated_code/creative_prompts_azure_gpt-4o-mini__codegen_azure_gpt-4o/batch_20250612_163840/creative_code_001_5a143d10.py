"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjya.com
Prompt: Write a code snippet that checks if JavaScript is enabled on a user's mobile device for a site focused on BTC pledges.
Generated: DETERMINISTIC_5a143d1096f7387d
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
  <title>BTC Pledge - JavaScript Check</title>
  <style>
    /* Basic styles for the message */
    .no-js-message {
      display: none;
      text-align: center;
      font-size: 1.2em;
      color: red;
      margin-top: 20px;
    }
    .js-enabled-message {
      display: none;
      text-align: center;
      font-size: 1.2em;
      color: green;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Default message for no JavaScript -->
  <div class="no-js-message" id="noJsMessage">
    JavaScript is disabled. Please enable JavaScript to use the BTC pledge site.
  </div>

  <!-- Message for JavaScript-enabled devices -->
  <div class="js-enabled-message" id="jsEnabledMessage">
    JavaScript is enabled! Enjoy the BTC pledge experience.
  </div>

  <script>
    // Error handling for ensuring DOM manipulation is safe
    try {
      // Hide the "No JavaScript" message since JS is enabled
      document.getElementById('noJsMessage').style.display = 'none';

      // Display the "JavaScript Enabled" message
      document.getElementById('jsEnabledMessage').style.display = 'block';
    } catch (error) {
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
