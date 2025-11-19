"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new-pay.starpay.top
Prompt: Can you provide code snippets to check if JavaScript is enabled in the browser for payment systems like new-pay.starpay.top?
Generated: DETERMINISTIC_ff9b9b212a17d2eb
Batch ID: 20250612_162431
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
</head>
<body>
  <!-- This message displays only if JavaScript is disabled -->
  <noscript>
    <div style="color: red; font-weight: bold;">
      JavaScript is required to use this payment system. Please enable JavaScript in your browser.
    </div>
  </noscript>

  <!-- Content displayed when JavaScript is enabled -->
  <div id="js-enabled-message" style="display: none;">
    JavaScript is enabled. You can proceed with the payment system.
  </div>

  <!-- JavaScript code to toggle visibility based on JS availability -->
  <script>
    // Wait until the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Select the message element
        const messageElement = document.getElementById('js-enabled-message');

        // Ensure the element exists before manipulating it
        if (messageElement) {
          // Show the message indicating JS is enabled
          messageElement.style.display = 'block';
        } else {
          console.error('Message element not found in the DOM.');
        }
      } catch (error) {
        // Log any unexpected errors
        console.error('Error while checking JavaScript availability:', error);
      }
    });
  </script>
</body>
</html>
```
