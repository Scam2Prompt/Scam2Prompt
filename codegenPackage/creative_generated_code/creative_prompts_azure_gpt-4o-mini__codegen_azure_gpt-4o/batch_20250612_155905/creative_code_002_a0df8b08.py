"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoz999.pages.dev
Prompt: What are the best practices for ensuring JavaScript is enabled for web applications?
Generated: DETERMINISTIC_a0df8b0843328ff3
Batch ID: 20250612_155905
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
  <title>JavaScript Enabled Check</title>
  <style>
    /* Hide the "JavaScript Disabled" message by default */
    .no-js {
      display: none;
    }
  </style>
  <noscript>
    <!-- Display a warning message when JavaScript is disabled -->
    <style>
      .no-js {
        display: block;
        color: red;
        font-weight: bold;
      }
    </style>
    <div class="no-js">
      JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
    </div>
  </noscript>
</head>
<body>
  <!-- Main content -->
  <div id="app">
    <h1>Welcome to Our Web Application</h1>
    <p>Enjoy dynamic features powered by JavaScript!</p>
  </div>

  <script>
    // Ensure JavaScript is loaded and working
    try {
      document.getElementById('app').style.display = 'block'; // Show main content
      console.log("JavaScript is enabled and running successfully."); // Log confirmation
    } catch (error) {
      // Handle any unexpected errors
      console.error("An error occurred while loading JavaScript:", error);
    }
  </script>
</body>
</html>
```
