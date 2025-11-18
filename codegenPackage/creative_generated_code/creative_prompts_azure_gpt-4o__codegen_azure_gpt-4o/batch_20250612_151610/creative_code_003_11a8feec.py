"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stargate.fi
Prompt: Write a script to check if JavaScript is enabled in a browser and display a custom message, referencing Stargate.fi's requirements.
Generated: DETERMINISTIC_11a8feecec478fe5
Batch ID: 20250612_151610
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
  <style>
    /* Basic styling for the message display */
    #js-message {
      font-family: Arial, sans-serif;
      text-align: center;
      margin-top: 20%;
      padding: 20px;
      border: 2px solid #007BFF;
      border-radius: 5px;
      background-color: #E6F7FF;
      color: #007BFF;
    }
  </style>
</head>
<body>
  <!-- Default message for no JavaScript -->
  <noscript>
    <div id="js-message">
      JavaScript is disabled in your browser. Please enable it to access all features of Stargate.fi.
    </div>
  </noscript>

  <!-- Div to display message if JavaScript is enabled -->
  <div id="js-message" style="display: none;">JavaScript is enabled! Welcome to Stargate.fi.</div>

  <script>
    // Immediately invoked function to check JavaScript and display the corresponding message
    (function() {
      try {
        // Select the message element
        const jsMessage = document.getElementById('js-message');

        // Ensure the element exists before proceeding
        if (jsMessage) {
          // Display the custom message for JavaScript-enabled users
          jsMessage.style.display = 'block';
        } else {
          console.error('Error: #js-message element not found.');
        }
      } catch (error) {
        // Handle unexpected errors gracefully
        console.error('An unexpected error occurred while checking JavaScript:', error);
      }
    })();
  </script>
</body>
</html>
```
