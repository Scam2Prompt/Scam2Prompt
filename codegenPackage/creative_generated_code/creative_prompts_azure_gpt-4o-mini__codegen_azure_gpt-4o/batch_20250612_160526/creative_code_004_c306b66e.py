"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogebox.link
Prompt: How can I create a user-friendly message for users who have JavaScript disabled, similar to the one on Dogebox?
Generated: DETERMINISTIC_c306b66ef3dfdd07
Batch ID: 20250612_160526
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
  <title>JavaScript Disabled Message Example</title>
  <style>
    /* Style for the no-js message */
    .no-js-message {
      display: none;
      color: #fff;
      background-color: #ff0000;
      padding: 15px;
      text-align: center;
      font-size: 16px;
      font-family: Arial, sans-serif;
    }
  </style>
</head>

<body>
  <!-- JavaScript Disabled Message -->
  <div class="no-js-message">
    <p>It seems that JavaScript is disabled in your browser. For the best experience, please enable JavaScript.</p>
  </div>

  <h1>Welcome to Our Website</h1>
  <p>This is a sample content that works only when JavaScript is enabled.</p>

  <script>
    // JavaScript will remove the no-js-message if it is enabled
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the message since JavaScript is enabled
      }
    });
  </script>
  
  <!-- No JavaScript Fallback -->
  <noscript>
    <style>
      /* Inline style to ensure visibility if JavaScript is disabled */
      .no-js-message {
        display: block;
      }
    </style>
  </noscript>
</body>

</html>
```
