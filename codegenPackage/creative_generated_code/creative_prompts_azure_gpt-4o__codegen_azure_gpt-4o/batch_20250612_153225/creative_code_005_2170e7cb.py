"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Write code to display a message prompting users to enable JavaScript if it is disabled, as seen in the Moonbirds Q1 '24 Holder Survey webpage.
Generated: DETERMINISTIC_2170e7cba6dce9fe
Batch ID: 20250612_153225
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
  <title>Enable JavaScript Message</title>
  <style>
    /* Styling for the no-JavaScript message */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 20px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      text-align: center;
      font-family: Arial, sans-serif;
      margin: 20px;
    }
  </style>
</head>
<body>
  <!-- This message will only be shown if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to access this webpage fully.
    </div>
  </noscript>

  <!-- Main content of the webpage that requires JavaScript -->
  <div id="content">
    <h1>Welcome to the Moonbirds Q1 '24 Holder Survey</h1>
    <p>Please ensure JavaScript is enabled for the best experience.</p>
  </div>

  <script>
    // JavaScript is enabled, so we can hide the no-JavaScript message entirely
    // (This step is redundant in modern browsers since <noscript> elements are not shown if JavaScript is enabled).
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
