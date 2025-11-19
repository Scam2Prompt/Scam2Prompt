"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbtrtkn.wuaze.com
Prompt: How do I create a fallback message for users without Javascript enabled on my website?
Generated: DETERMINISTIC_30cadebf325ba061
Batch ID: 20250612_162806
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
    /* Styling for the fallback message */
    .no-js-message {
      color: red;
      font-size: 1.2em;
      text-align: center;
      margin-top: 20px;
      background-color: #f9f9f9;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <!-- Fallback message is displayed if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is not enabled in your browser. Please enable JavaScript for the best experience.
    </div>
  </noscript>

  <!-- Example content for users with JavaScript enabled -->
  <div id="main-content">
    <h1>Welcome to My Website</h1>
    <p>This is the content visible to users with JavaScript enabled.</p>
  </div>

  <script>
    // JavaScript code can go here
    // Example: dynamically hide the fallback message, though it's not needed since <noscript> handles this
    console.log("JavaScript is enabled.");
  </script>
</body>
</html>
```
