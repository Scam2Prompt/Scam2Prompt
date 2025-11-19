"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqep.com
Prompt: How do I create a fallback for users who have JavaScript disabled when accessing DCQEP?
Generated: DETERMINISTIC_6a91189c1ead4f95
Batch ID: 20250612_155739
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
  <title>DCQEP Fallback Example</title>
  <!-- Inline CSS for basic styling -->
  <style>
    .no-js-message {
      display: none; /* Default: hidden if JavaScript is enabled */
      color: red;
      font-size: 1.2em;
      text-align: center;
      margin: 20px;
    }

    .js-enabled {
      display: none; /* Hide fallback content when JavaScript is disabled */
    }
  </style>
</head>
<body>

  <!-- Fallback message for users without JavaScript -->
  <div class="no-js-message">
    JavaScript is disabled or unavailable. Please enable JavaScript to access DCQEP's features.
  </div>

  <!-- Content visible only when JavaScript is enabled -->
  <div class="js-enabled">
    <h1>Welcome to DCQEP</h1>
    <p>This content is visible because JavaScript is enabled.</p>
  </div>

  <!-- Script to handle fallback -->
  <script>
    // Immediately invoked function to check JavaScript availability
    (function() {
      // Hide fallback message and show JavaScript-enabled content
      const noJsMessage = document.querySelector('.no-js-message');
      const jsEnabledContent = document.querySelector('.js-enabled');

      if (noJsMessage) noJsMessage.style.display = 'none';
      if (jsEnabledContent) jsEnabledContent.style.display = 'block';
    })();
  </script>

</body>
</html>
```
