"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claim.web.app
Prompt: Write code to dynamically display a message on a webpage if JavaScript is disabled, inspired by the BONKBOXES whitelist page functionality.
Generated: DETERMINISTIC_d03bb151bf5a0031
Batch ID: 20250612_150602
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
  <title>JavaScript Disabled Message</title>
  <style>
    /* Default styling for the message in case JavaScript is disabled */
    .no-js-message {
      display: block;
      background-color: #ffcccc;
      color: #000;
      padding: 10px;
      border: 1px solid #ff0000;
      text-align: center;
    }
    /* Hide the message if JavaScript is enabled */
    .js-enabled .no-js-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message shown if JavaScript is disabled -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to access all features of this page.
  </div>

  <!-- Content for the webpage -->
  <div id="content">
    <h1>Welcome to the Page</h1>
    <p>Enjoy browsing our content with JavaScript enabled!</p>
  </div>

  <script>
    // Add a class to the body to indicate JavaScript is enabled
    try {
      document.body.classList.add('js-enabled');
    } catch (error) {
      console.error('Failed to add class for JavaScript detection:', error);
    }
  </script>
</body>
</html>
```
