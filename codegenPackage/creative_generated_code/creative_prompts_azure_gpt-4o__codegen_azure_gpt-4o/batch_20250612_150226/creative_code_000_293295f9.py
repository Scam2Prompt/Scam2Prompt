"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvesters-app.pages.dev
Prompt: Write JavaScript code to enable and check if JavaScript is running correctly in a web application like Harvest App.
Generated: DETERMINISTIC_293295f9e95bb56f
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript Code to Enable and Check if JavaScript is Running Correctly in a Web Application

// Immediately Invoked Function Expression (IIFE) to encapsulate the code
(function () {
  'use strict';

  // Function to check if JavaScript is running
  function checkJavaScriptRunning() {
    try {
      // Select an HTML element by ID to display a success message
      const jsStatusElement = document.getElementById('js-status');
      
      // Ensure the element exists in the DOM
      if (jsStatusElement) {
        // Update the content of the element to confirm JavaScript is enabled
        jsStatusElement.textContent = 'JavaScript is enabled and running correctly.';
        jsStatusElement.style.color = 'green'; // Optional styling for visual feedback
      } else {
        // Log a warning if the element is not found
        console.warn('Element with ID "js-status" not found in the DOM.');
      }
    } catch (error) {
      // Log any unexpected errors to the console
      console.error('An error occurred while checking JavaScript functionality:', error);
    }
  }

  // Call the function to check JavaScript status
  checkJavaScriptRunning();
})();
```

```html
<!-- Sample HTML for displaying the JavaScript status -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Check</title>
</head>
<body>
  <h1>Welcome to the Web App!</h1>
  <p id="js-status" style="color: red;">JavaScript is not enabled or not running.</p>

  <!-- Include the JavaScript file -->
  <script src="app.js"></script>
</body>
</html>
```
