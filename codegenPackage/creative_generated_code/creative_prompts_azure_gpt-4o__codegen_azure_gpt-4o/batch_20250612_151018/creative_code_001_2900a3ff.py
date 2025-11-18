"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-783--peaceful-nightingale-55a1b7.netlify.app
Prompt: Create a script that checks for JavaScript support in a browser and redirects users to a fallback page if JavaScript is disabled.
Generated: DETERMINISTIC_2900a3ff568b41f1
Batch ID: 20250612_151018
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
  <script>
    // This script runs if JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      // JavaScript is enabled; no need to redirect.
      console.log("JavaScript is enabled.");
    });
  </script>
  <noscript>
    <!-- If JavaScript is disabled, redirect to the fallback page -->
    <meta http-equiv="refresh" content="0;url=/fallback.html">
  </noscript>
</head>
<body>
  <h1>Welcome to the Website</h1>
  <p>If you are seeing this message, JavaScript is enabled in your browser.</p>
</body>
</html>
```
