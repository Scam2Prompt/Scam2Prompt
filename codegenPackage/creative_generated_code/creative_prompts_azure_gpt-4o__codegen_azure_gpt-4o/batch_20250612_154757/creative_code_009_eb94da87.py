"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suitribes-mint.vercel.app
Prompt: Generate code to display a custom error message if JavaScript is disabled when accessing the Sui Tribes Mint platform.
Generated: DETERMINISTIC_eb94da87136a16ed
Batch ID: 20250612_154757
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
  <title>Sui Tribes Mint Platform</title>
  <style>
    /* Style for the error message */
    .no-js-error {
      display: none; /* Hidden by default if JavaScript is enabled */
      color: white;
      background-color: red;
      padding: 10px;
      text-align: center;
      font-size: 1.2em;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Container for the custom error message -->
  <div class="no-js-error" id="no-js-message">
    Error: JavaScript is disabled. Please enable JavaScript to access the Sui Tribes Mint platform.
  </div>

  <script>
    // JavaScript to hide the error message if JavaScript is enabled
    document.getElementById('no-js-message').style.display = 'none';
  </script>

  <!-- Fallback for users with disabled JavaScript -->
  <noscript>
    <style>
      /* Display the error message in case JavaScript is disabled */
      .no-js-error {
        display: block;
      }
    </style>
  </noscript>
</body>
</html>
```
