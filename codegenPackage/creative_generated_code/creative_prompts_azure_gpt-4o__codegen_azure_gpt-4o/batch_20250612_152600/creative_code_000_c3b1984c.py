"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btccetc.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a user's browser and display a message prompting them to enable it for accessing BTC Pledge services.
Generated: DETERMINISTIC_c3b1984c79475e40
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BTC Pledge Services</title>
  <style>
    /* Basic styling for the warning message */
    #js-warning {
      display: none; /* Hidden by default */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <noscript>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <div style="color: red; font-weight: bold; text-align: center; margin-top: 20px;">
      JavaScript is disabled in your browser. Please enable JavaScript to access BTC Pledge services.
    </div>
  </noscript>

  <!-- JavaScript-enabled message container -->
  <div id="js-warning">
    JavaScript is enabled. You can access BTC Pledge services.
  </div>

  <script>
    // Check if the JavaScript is running (which implies it's enabled)
    try {
      // Find the warning element
      const jsWarning = document.getElementById('js-warning');
      
      // Display the message for JavaScript-enabled browsers
      jsWarning.style.display = 'block';
    } catch (error) {
      // Log any unexpected error (shouldn't occur in this scenario)
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
