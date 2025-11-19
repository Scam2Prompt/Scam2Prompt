"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialmelaniatrump.me
Prompt: What are the best practices for ensuring a website displays a message when JavaScript is disabled, as seen on the Melania Trump official page?
Generated: DETERMINISTIC_39ed80c6a0fc4bd3
Batch ID: 20250612_155959
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
  <title>JavaScript Disabled Notification</title>
  <style>
    /* Style for the message */
    .no-js-message {
      display: none; /* Hide by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 10px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      text-align: center;
      margin: 20px;
    }
  </style>
</head>
<body>
  <!-- Message for users with JavaScript disabled -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to view this site properly.
  </div>

  <!-- Content when JavaScript is enabled -->
  <div class="main-content">
    <h1>Welcome to the site!</h1>
    <p>Enjoy browsing the content of this website.</p>
  </div>

  <script>
    // Select the element with the "no-js-message" class
    const noJsMessage = document.querySelector('.no-js-message');
    
    // If JavaScript is enabled, hide the no-js message
    if (noJsMessage) {
      noJsMessage.style.display = 'none';
    }
  </script>

  <!-- Noscript tag for additional fallback (if desired) -->
  <noscript>
    <style>
      /* Ensure the message is visible when JavaScript is disabled */
      .no-js-message {
        display: block !important;
      }
    </style>
  </noscript>
</body>
</html>
```
