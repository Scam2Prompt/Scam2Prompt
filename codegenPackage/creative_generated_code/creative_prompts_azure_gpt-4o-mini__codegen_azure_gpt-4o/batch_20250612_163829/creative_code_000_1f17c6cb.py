"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bot12.cc
Prompt: How can I enable JavaScript for better functionality on web applications?
Generated: DETERMINISTIC_1f17c6cb45772279
Batch ID: 20250612_163829
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
  <title>Enable JavaScript Example</title>
  <style>
    /* Style for the no-JavaScript warning message */
    .no-js-message {
      color: red;
      background-color: #f8f8f8;
      padding: 10px;
      border: 1px solid #ccc;
      display: none; /* Hidden by default */
    }
  </style>
</head>
<body>
  <!-- Message shown when JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is currently disabled. Please enable JavaScript in your browser for better functionality.
    </div>
  </noscript>

  <!-- Main content of the page -->
  <div id="app">
    <h1>Welcome to My Web Application</h1>
    <p>This content is enhanced with JavaScript functionality.</p>
  </div>

  <!-- JavaScript code -->
  <script>
    // Ensure the script runs only if JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      // Example functionality: Dynamically create a button and add interactivity
      try {
        const app = document.getElementById("app");

        // Create a new button
        const button = document.createElement("button");
        button.textContent = "Click Me!";
        button.style.padding = "10px";
        button.style.marginTop = "20px";

        // Add a click event listener to the button
        button.addEventListener("click", () => {
          alert("Thanks for clicking!");
        });

        // Append the button to the app container
        app.appendChild(button);
      } catch (error) {
        // Handle any errors in JavaScript execution
        console.error("An error occurred while initializing the application:", error);
      }
    });
  </script>
</body>
</html>
```
