"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greendotinstallerportaluat.crm.com
Prompt: Generate JavaScript code to check if JavaScript is enabled in a browser and display a message, similar to the GreenDot Installer Portal's functionality.
Generated: DETERMINISTIC_a9d62fb160190ae2
Batch ID: 20250612_154250
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
  <title>JavaScript Enabled Check</title>
  <style>
    /* Styling for the message container */
    #js-check-message {
      font-family: Arial, sans-serif;
      font-size: 16px;
      color: #333;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      width: 80%;
      margin: 20px auto;
      text-align: center;
      background-color: #f9f9f9;
    }
    #js-check-message.error {
      border-color: #e74c3c;
      background-color: #fbeee6;
      color: #e74c3c;
    }
    #js-check-message.success {
      border-color: #2ecc71;
      background-color: #eafaf1;
      color: #2ecc71;
    }
  </style>
</head>
<body>
  <noscript>
    <!-- Message displayed when JavaScript is disabled -->
    <div id="js-check-message" class="error">
      JavaScript is disabled in your browser. Please enable it to use this application.
    </div>
  </noscript>
  <!-- Message container for when JavaScript is enabled -->
  <div id="js-check-message" class="success" style="display: none;">
    JavaScript is enabled in your browser. You can use this application.
  </div>

  <script>
    // Wrap the code in a try-catch block for error safety
    try {
      // Select the message container
      const jsCheckMessage = document.getElementById('js-check-message');

      // Ensure the element exists before attempting to modify it
      if (jsCheckMessage) {
        // Update the message and display it
        jsCheckMessage.style.display = 'block';
        jsCheckMessage.textContent = 'JavaScript is enabled in your browser. You can use this application.';
        jsCheckMessage.classList.add('success');
      }
    } catch (error) {
      // Log any errors for debugging purposes
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
