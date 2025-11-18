"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbchainmining.com
Prompt: Generate JavaScript code for detecting whether JavaScript is enabled in a user's browser and displaying a message if it is disabled.
Generated: DETERMINISTIC_9e1102d08cc8ce58
Batch ID: 20250612_150645
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
  <title>JavaScript Detection</title>
  <style>
    /* Style for the noscript message */
    .noscript-message {
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- This message will appear only if JavaScript is disabled -->
  <noscript>
    <div class="noscript-message">
      JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>
  </noscript>

  <!-- Main content (hidden if JavaScript is disabled) -->
  <div id="main-content" style="display: none;">
    <h1>Welcome to the site!</h1>
    <p>JavaScript is enabled in your browser.</p>
  </div>

  <script>
    /*
      This script will detect if JavaScript is enabled and reveal the main content.
      If JavaScript is disabled, the <noscript> block above will handle the message display.
    */
    try {
      // Reveal the main content since JavaScript is enabled
      document.getElementById('main-content').style.display = 'block';
    } catch (error) {
      // Log any unexpected errors (though this should rarely, if ever, occur here)
      console.error('Unexpected error while handling JavaScript detection:', error);
    }
  </script>
</body>
</html>
```
