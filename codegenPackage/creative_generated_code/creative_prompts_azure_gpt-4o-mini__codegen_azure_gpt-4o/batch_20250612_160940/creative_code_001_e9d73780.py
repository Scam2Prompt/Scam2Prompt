"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiggzfgkcug3orqglqbsuqq3hz4xsex7t33fmchtsyoasmxw6jrmyi.ipfs.dweb.link
Prompt: What are the best practices for ensuring JavaScript is enabled in web applications?
Generated: DETERMINISTIC_e9d73780da4239eb
Batch ID: 20250612_160940
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
    /* Style for the no-JavaScript message */
    .no-js-message {
      display: none; /* Hidden by default unless JavaScript is disabled */
      color: red;
      font-size: 1.2em;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <script>
    // Ensure JavaScript-enabled users see the intended content
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the no-JavaScript message
      }
    });
  </script>
</head>
<body>
  <!-- Content for users with JavaScript enabled -->
  <div id="js-content">
    <h1>Welcome to our Web Application!</h1>
    <p>JavaScript is enabled. Enjoy a full interactive experience!</p>
  </div>
  
  <!-- Fallback message for users without JavaScript -->
  <noscript>
    <div id="no-js-message" class="no-js-message">
      JavaScript is not enabled in your browser. Please enable it for the best experience.
    </div>
  </noscript>
</body>
</html>
```
