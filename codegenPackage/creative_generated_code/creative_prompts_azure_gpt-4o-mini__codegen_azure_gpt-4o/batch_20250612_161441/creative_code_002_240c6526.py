"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-five.vercel.app
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like Linea?
Generated: DETERMINISTIC_240c6526a807c2d2
Batch ID: 20250612_161441
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
  <title>JavaScript Enabled Check</title>
  <style>
    /* CSS Rule to hide the "JavaScript Disabled" message by default */
    #no-js-message {
      display: none;
      color: red;
      font-weight: bold;
    }
  </style>
  <script>
    // JavaScript function to hide the "JavaScript Disabled" message if JS is enabled
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.getElementById("no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none"; // Hide the message since JS is enabled
      }
    });
  </script>
</head>
<body>
  <!-- Message will be visible only when JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">JavaScript is disabled in your browser. Please enable it to use this web application.</div>
  </noscript>

  <h1>Welcome to the Web Application</h1>
  <p>If you are seeing this, JavaScript is enabled!</p>
</body>
</html>
```
