"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://login.futurx.live
Prompt: Develop a script to redirect users to an error page if JavaScript is disabled, similar to the functionality observed on the FuturX login page.
Generated: DETERMINISTIC_6ea5613148f20dcc
Batch ID: 20250612_145626
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
  <title>FuturX Login</title>
  <noscript>
    <!-- If JavaScript is disabled, the user will be redirected to the error page -->
    <meta http-equiv="refresh" content="0;url=/errorpage.html">
  </noscript>
  <style>
    /* Optional: Hide the main content if JavaScript is disabled */
    body {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Main content of the page -->
  <h1>Welcome to FuturX</h1>
  <p>Please log in to continue.</p>

  <script>
    // Enable rendering of the body only if JavaScript is enabled
    document.body.style.display = 'block';
  </script>
</body>
</html>
```
