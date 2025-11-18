"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea.vercel.app
Prompt: Generate JavaScript code to check whether JavaScript is enabled in a user's browser and display a custom message if it is disabled.
Generated: DETERMINISTIC_b7d8dd25da08ccab
Batch ID: 20250612_154635
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
    /* Style for the message displayed if JavaScript is disabled */
    .no-js-message {
      color: red;
      font-weight: bold;
    }
    .js-enabled-message {
      color: green;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Message displayed when JavaScript is disabled -->
  <noscript>
    <p class="no-js-message">JavaScript is disabled in your browser. Please enable it for a better experience.</p>
  </noscript>

  <!-- Placeholder for the message displayed when JavaScript is enabled -->
  <div id="js-enabled-placeholder"></div>

  <script>
    // Wrap the code in a try-catch block for error handling
    try {
      // Select the placeholder element
      const jsEnabledPlaceholder = document.getElementById('js-enabled-placeholder');
      
      // Display a custom message indicating JavaScript is enabled
      jsEnabledPlaceholder.innerHTML = '<p class="js-enabled-message">JavaScript is enabled in your browser.</p>';
    } catch (error) {
      // Log any unexpected errors to the console
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
