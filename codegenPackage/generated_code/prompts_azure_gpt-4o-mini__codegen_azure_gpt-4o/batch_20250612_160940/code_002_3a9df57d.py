"""
Generated Code Metadata:
========================
Original URL: https://bafybeiggzfgkcug3orqglqbsuqq3hz4xsex7t33fmchtsyoasmxw6jrmyi.ipfs.dweb.link
Prompt: Can you provide code snippets for detecting if JavaScript is enabled in a browser?
Generated: DETERMINISTIC_3a9df57d1b94d83f
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Detection</title>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <p style="color: red;">JavaScript is disabled in your browser. Please enable it for full functionality.</p>
  </noscript>

  <!-- Message displayed if JavaScript is enabled -->
  <div id="js-enabled-message" style="display: none;">
    <p style="color: green;">JavaScript is enabled in your browser!</p>
  </div>

  <script>
    // Check if JavaScript is enabled and display the appropriate message
    document.addEventListener('DOMContentLoaded', () => {
      const jsEnabledMessage = document.getElementById('js-enabled-message');
      if (jsEnabledMessage) {
        // If JavaScript is enabled, show the message
        jsEnabledMessage.style.display = 'block';
      }
    });
  </script>
</body>
</html>
```
