"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloud.barchin.com
Prompt: Write a script to check if JavaScript is enabled before loading a Nextcloud application.
Generated: DETERMINISTIC_c4fc831b35d25209
Batch ID: 20250612_154632
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
  <title>Nextcloud Application</title>

  <!-- Inline CSS for quick styling -->
  <style>
    /* Display message if JavaScript is disabled */
    #no-js-message {
      display: none;
      font-family: Arial, sans-serif;
      color: red;
      text-align: center;
      margin-top: 20px;
    }
    #app-content {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message for users without JavaScript -->
  <noscript>
    <p id="no-js-message">JavaScript is disabled. Please enable JavaScript in your browser to use this application.</p>
  </noscript>

  <!-- Main application content -->
  <div id="app-content">
    <h1>Welcome to the Nextcloud Application</h1>
    <p>Loading...</p>
  </div>

  <!-- JavaScript to detect and handle enabled JavaScript -->
  <script>
    // Ensure the script runs once the DOM is ready
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // If JavaScript is enabled, show the application content
        const appContent = document.getElementById('app-content');
        appContent.style.display = 'block';
      } catch (error) {
        // Log any unexpected errors to the console
        console.error('Error while loading the application:', error);
      }
    });
  </script>
</body>
</html>
```
