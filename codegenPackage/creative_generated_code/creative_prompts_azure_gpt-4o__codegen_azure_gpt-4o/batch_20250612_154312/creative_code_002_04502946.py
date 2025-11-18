"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeai.eu
Prompt: Generate code for a basic web application that checks for JavaScript support and redirects users to an error page if JavaScript is disabled, inspired by the DogeAI website's functionality.
Generated: DETERMINISTIC_045029468ea5f114
Batch ID: 20250612_154312
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
    // JavaScript is enabled, redirect to the main page
    window.location.href = "/main.html";
  </script>
  <!-- If JavaScript is disabled, this page will remain visible -->
  <noscript>
    <meta http-equiv="refresh" content="0; url=/error.html">
  </noscript>
</head>
<body>
  <!-- Fallback content for users with JavaScript disabled -->
  <h1>Redirecting...</h1>
</body>
</html>
```

```html
<!-- main.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Main Page</title>
</head>
<body>
  <h1>Welcome to the Main Page</h1>
  <p>JavaScript is enabled on your browser!</p>
</body>
</html>
```

```html
<!-- error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Disabled</title>
</head>
<body>
  <h1>Error: JavaScript Disabled</h1>
  <p>It seems like JavaScript is disabled in your browser. Please enable JavaScript to use this website.</p>
</body>
</html>
```
