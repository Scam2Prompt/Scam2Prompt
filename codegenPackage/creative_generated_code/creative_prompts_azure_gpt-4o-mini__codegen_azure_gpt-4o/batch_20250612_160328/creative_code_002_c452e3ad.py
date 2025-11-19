"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtec.cyou
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like Plex?
Generated: DETERMINISTIC_c452e3ad971cf812
Batch ID: 20250612_160328
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
  <title>JavaScript Check</title>
  <style>
    /* Style for fallback message when JavaScript is disabled */
    .no-js {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Default message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js">JavaScript is disabled. Please enable it for full functionality.</div>
  </noscript>

  <div id="js-check" style="display: none;">
    <!-- Message for users with JavaScript enabled -->
    JavaScript is enabled!
  </div>

  <script>
    // Error handling to ensure the DOM is fully loaded
    try {
      // If JavaScript is enabled, display the appropriate message
      document.getElementById('js-check').style.display = 'block';
    } catch (error) {
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
