"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.si
Prompt: How do I create a fallback message for users who have JavaScript disabled when accessing the Blur.si domain details page?
Generated: DETERMINISTIC_612a626f924580db
Batch ID: 20250612_135637
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
  <title>Blur.si Domain Details</title>
  <style>
    /* Styling for fallback message */
    #no-js-message {
      display: none; /* Hidden when JavaScript is enabled */
      color: red;
      font-size: 1.2em;
      text-align: center;
      background: #f8d7da;
      padding: 1em;
      border: 1px solid #f5c6cb;
      max-width: 600px;
      margin: 20px auto;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <!-- Fallback message for users with JavaScript disabled -->
  <div id="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to view the Blur.si domain details page correctly.
  </div>

  <!-- Main content of the page -->
  <div id="content">
    <h1>Welcome to Blur.si Domain Details</h1>
    <p>Loading domain details...</p>
    <!-- More dynamic content will be loaded via JavaScript -->
  </div>

  <script>
    // JavaScript code to hide the fallback message when JS is enabled
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.getElementById('no-js-message');
      // If JavaScript runs successfully, hide the fallback message
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
