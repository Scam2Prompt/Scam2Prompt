"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dl8.xyz
Prompt: How can I create a fallback for users who have JavaScript disabled when accessing a site like DL8?
Generated: DETERMINISTIC_5ae365a7a1d512e0
Batch ID: 20250612_155753
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
  <title>Fallback for No JavaScript</title>
  <style>
    /* Basic styling for the fallback message */
    .no-js-message {
      display: none; /* Hide this by default */
      color: #fff;
      background-color: #f44336;
      padding: 10px;
      text-align: center;
      font-family: Arial, sans-serif;
      font-size: 16px;
    }
    .js-enabled .no-js-message {
      display: none; /* Ensure it's hidden if JS is enabled */
    }
  </style>
  <noscript>
    <!-- Fallback for users who have JavaScript disabled -->
    <style>
      .no-js-message {
        display: block; /* Show the fallback message if JavaScript is disabled */
      }
    </style>
  </noscript>
</head>
<body class="js-enabled">
  <!-- Fallback message -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to access all features of this site.
  </div>

  <!-- Main content -->
  <h1>Welcome to DL8</h1>
  <p>This site requires JavaScript for full functionality.</p>

  <script>
    // JavaScript to mark JavaScript as enabled
    // This ensures no-js-message is hidden if JS is running
    document.body.classList.remove('js-enabled');
  </script>
</body>
</html>
```
