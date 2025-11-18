"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarecrew-app.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message like the one on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_137aec55ec9f8b30
Batch ID: 20250612_154752
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
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Style for the warning message */
    .js-error {
      display: none; /* Initially hidden, shown if JS is disabled */
      font-family: Arial, sans-serif;
      color: white;
      background-color: #ff4c4c;
      padding: 15px;
      border-radius: 5px;
      text-align: center;
      margin: 20px;
    }
  </style>
</head>
<body>
  <!-- Custom error message for JavaScript-disabled browsers -->
  <div class="js-error">
    JavaScript is disabled in your browser. Please enable JavaScript to continue using this website.
  </div>

  <!-- Script to hide the error message if JavaScript is enabled -->
  <script>
    try {
      // Select the error message element
      const jsErrorMessage = document.querySelector('.js-error');
      if (jsErrorMessage) {
        // Hide the message if JavaScript is enabled
        jsErrorMessage.style.display = 'none';
      }
    } catch (error) {
      console.error('Error occurred while checking for JavaScript support:', error);
    }
  </script>
</body>
</html>
```
