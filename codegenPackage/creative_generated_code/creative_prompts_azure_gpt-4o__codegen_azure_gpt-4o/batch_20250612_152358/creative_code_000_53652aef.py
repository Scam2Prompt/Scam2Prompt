"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibonkgifts.web.app
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting users to enable it, similar to the functionality described on the Shibonk Gang Whitelist webpage.
Generated: DETERMINISTIC_53652aef557e0038
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Check</title>
  <style>
    /* Basic styling for the message */
    #no-js-message {
      display: none; /* Hidden by default as JavaScript will enable it */
      font-family: Arial, sans-serif;
      color: red;
      font-size: 16px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Fallback message for browsers without JavaScript enabled -->
  <noscript>
    <div id="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to access this website properly.
    </div>
  </noscript>

  <!-- Main content of the webpage -->
  <div id="main-content">
    <h1>Welcome to Our Website</h1>
    <p>This content requires JavaScript to be fully functional.</p>
  </div>

  <script>
    // JavaScript code to ensure a seamless experience
    (function() {
      try {
        // Select the fallback message using its ID
        const noJsMessage = document.getElementById('no-js-message');
        
        // Ensure the fallback message remains hidden if JavaScript is enabled
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }
        
        // Additional initialization logic can be added here
        console.log("JavaScript is enabled and running smoothly.");
      } catch (error) {
        // Error handling for any unexpected runtime issues
        console.error("An error occurred while checking JavaScript functionality:", error);
      }
    })();
  </script>
</body>
</html>
```
