"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hingehealth.eu
Prompt: Write code to detect if JavaScript is disabled in a user's browser and display a custom message prompting them to enable it, similar to the behavior on the Hinge Health EU website.
Generated: DETERMINISTIC_4af81d72263b992e
Batch ID: 20250612_151438
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
  <title>Enable JavaScript</title>
  <style>
    /* Style for the no-JavaScript message */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 20px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      text-align: center;
      font-family: Arial, sans-serif;
    }

    /* Ensures the message is visible only when JavaScript is disabled */
    .no-js-visible {
      display: block !important;
    }
  </style>
</head>
<body>
  <!-- Message to display if JavaScript is disabled -->
  <div id="no-js-message" class="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to view this website properly.
  </div>

  <!-- JavaScript logic -->
  <script>
    try {
      // Select the no-js-message element
      const noJsMessage = document.getElementById('no-js-message');

      // If JavaScript is running, hide the message (extra safety)
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    } catch (error) {
      // In case of unexpected errors, log them
      console.error('An error occurred while handling the JavaScript-enabled state:', error);
    }
  </script>
  <noscript>
    <!-- Fallback for browsers with JavaScript disabled -->
    <style>
      #no-js-message {
        display: block;
      }
    </style>
  </noscript>
</body>
</html>
```
