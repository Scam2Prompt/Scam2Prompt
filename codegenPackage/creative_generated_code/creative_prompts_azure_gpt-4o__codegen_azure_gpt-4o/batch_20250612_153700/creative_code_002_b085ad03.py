"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponet.pro
Prompt: Generate JavaScript code to detect if JavaScript is disabled in a user's browser and display a message prompting them to enable it for accessing a presale application.
Generated: DETERMINISTIC_b085ad0352c358fa
Batch ID: 20250612_153700
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
  <title>Presale Application</title>
  <style>
    /* Styles for the no-JavaScript message */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 15px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px;
    }
  </style>
</head>
<body>
  <!-- This message will appear if JavaScript is disabled -->
  <div class="no-js-message" id="noJsMessage">
    JavaScript is disabled in your browser. Please enable JavaScript to access the presale application.
  </div>

  <script>
    // JavaScript automatically runs, so we hide the error message if JavaScript is enabled
    (function() {
      try {
        const noJsMessage = document.getElementById('noJsMessage');
        if (noJsMessage) {
          // Hide the message since JavaScript is enabled
          noJsMessage.style.display = 'none';
        }
      } catch (error) {
        // Log any unexpected errors for debugging
        console.error('Error hiding no-JavaScript message:', error);
      }
    })();
  </script>

  <noscript>
    <!-- Fallback message if JavaScript is disabled -->
    <style>
      #noJsMessage {
        display: block; /* Ensure the message is visible if JavaScript is disabled */
      }
    </style>
  </noscript>
</body>
</html>
```
