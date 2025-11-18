"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: Write a script to display a custom error message if a user tries to access a web app without enabling JavaScript, similar to the Honey App's requirement.
Generated: DETERMINISTIC_7cfb9939a0641ea0
Batch ID: 20250612_153401
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
  <title>JavaScript Required</title>
  <style>
    /* Basic styling for the error message */
    #no-js-message {
      display: none; /* Hidden by default, only shown if JavaScript is disabled */
      color: white;
      background-color: red;
      padding: 20px;
      text-align: center;
      font-size: 18px;
      font-family: Arial, sans-serif;
    }
  </style>
</head>

<body>
  <!-- Message shown if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      JavaScript is required to access this application. Please enable JavaScript in your browser settings and reload the page.
    </div>
  </noscript>

  <!-- Main content -->
  <div id="app-content">
    <h1>Welcome to the Web App</h1>
    <p>This is the main content of the application.</p>
  </div>

  <script>
    // Error handling in case JavaScript fails to load or an issue occurs.
    try {
      // Ensure "noscript" fallback isn't visible when JavaScript is enabled
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }

      // Logic for initializing the app can go here
      console.log('JavaScript is enabled, proceeding with app initialization...');
    } catch (error) {
      console.error('An unexpected error occurred:', error);
      alert('An error occurred while loading the application. Please try again.');
    }
  </script>
</body>

</html>
```
