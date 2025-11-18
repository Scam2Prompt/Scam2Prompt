"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equinix.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it.
Generated: DETERMINISTIC_2b0cd8f2409af354
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
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Style for the message displayed when JavaScript is disabled */
    #no-js-message {
      display: none; /* Initially hidden since JavaScript will enable it */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Message to display when JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>

  <!-- Content of the page -->
  <div id="content">
    <h1>Welcome to Our Website</h1>
    <p>This page works best with JavaScript enabled!</p>
  </div>

  <script>
    // JavaScript enabled: Hide the "no-js-message" element
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });

    // Error handling in case DOMContentLoaded fails (unlikely)
    window.onload = () => {
      try {
        const noJsMessage = document.getElementById('no-js-message');
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }
      } catch (error) {
        console.error("An error occurred while trying to hide the no-js message:", error);
      }
    };
  </script>
</body>
</html>
```
