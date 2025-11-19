"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getin.co.il
Prompt: Write a code snippet to gracefully degrade functionality for users with JavaScript disabled on a website.
Generated: DETERMINISTIC_08e5718beeb34cf0
Batch ID: 20250612_160309
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
  <title>Graceful Degradation Example</title>
  <style>
    /* Default styles for users with JavaScript disabled */
    .no-js-message {
      display: block; /* Visible only if JavaScript is disabled */
      color: red;
      font-weight: bold;
      margin: 20px 0;
    }

    .js-enabled-content {
      display: none; /* Hidden by default, shown if JavaScript is enabled */
    }
  </style>
  <script>
    // Detect JavaScript support and adjust content visibility
    document.addEventListener("DOMContentLoaded", function() {
      const noJsMessage = document.querySelector('.no-js-message');
      const jsEnabledContent = document.querySelector('.js-enabled-content');

      // Hide the "no-js-message" and show "js-enabled-content"
      if (noJsMessage && jsEnabledContent) {
        noJsMessage.style.display = 'none'; // Hide "JavaScript required" message
        jsEnabledContent.style.display = 'block'; // Show enhanced content
      }
    });
  </script>
</head>
<body>
  <!-- Message shown if JavaScript is disabled -->
  <div class="no-js-message">
    This website requires JavaScript for full functionality. Please enable JavaScript in your browser.
  </div>

  <!-- Content enhanced with JavaScript -->
  <div class="js-enabled-content">
    <h1>Welcome to the enhanced experience!</h1>
    <p>This content is only visible to users with JavaScript enabled.</p>
  </div>

  <!-- Additional static content available to all users -->
  <div class="fallback-content">
    <h2>Basic Information</h2>
    <p>This content is always displayed regardless of JavaScript availability.</p>
  </div>
</body>
</html>
```
