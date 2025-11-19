"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrurnbridge.xyz
Prompt: Write a code snippet to enable JavaScript checks before accessing a web page.
Generated: DETERMINISTIC_66498cb8009a5dbe
Batch ID: 20250612_162511
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
    /* Hide content initially for users without JavaScript enabled */
    .no-js-message {
      display: block;
    }

    .content {
      display: none;
    }
  </style>
  <script>
    // Enable content visibility if JavaScript is active
    document.addEventListener("DOMContentLoaded", function() {
      const noJsMessage = document.querySelector(".no-js-message");
      const content = document.querySelector(".content");

      // Hide the "no-JS" message and show the main content
      if (noJsMessage && content) {
        noJsMessage.style.display = "none";
        content.style.display = "block";
      }
    });
  </script>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <div class="no-js-message">
    <p>JavaScript is required to access this page. Please enable it in your browser settings.</p>
  </div>
  
  <!-- Main content hidden by default -->
  <div class="content">
    <h1>Welcome to the JavaScript-enabled page!</h1>
    <p>Enjoy exploring this content.</p>
  </div>
</body>
</html>
```
