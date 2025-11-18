"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aubi.online
Prompt: Develop a script that redirects users to an error page if JavaScript is disabled, similar to the functionality required by "aubi.online."
Generated: DETERMINISTIC_c465c31b3327a77a
Batch ID: 20250612_154958
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
  <noscript>
    <!-- Redirect users to error.html if JavaScript is disabled -->
    <meta http-equiv="refresh" content="0; url=error.html">
    <!-- Display a fallback message for older browsers -->
    <style>
      body {
        display: none;
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Page Content -->
  <h1>Welcome to the Website</h1>
  <p>If you are seeing this, JavaScript is enabled!</p>
</body>
</html>
```

**Notes within the code:**
- The `<noscript>` tag handles cases where JavaScript is disabled by redirecting to `error.html`.
- A fallback `style` within `<noscript>` hides the main content if JavaScript is disabled.
- This solution is clean, unobtrusive, and ensures users with disabled JavaScript are redirected appropriately.
