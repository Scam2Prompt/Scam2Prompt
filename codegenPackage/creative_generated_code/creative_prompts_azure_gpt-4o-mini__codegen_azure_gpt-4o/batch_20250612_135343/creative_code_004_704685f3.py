"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synfutures.de
Prompt: How do I create a fallback for users who have JavaScript disabled on the SynFutures domain?
Generated: DETERMINISTIC_704685f30ffdb657
Batch ID: 20250612_135343
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
  <title>SynFutures</title>
  <style>
    /* Basic styling for the fallback content */
    .no-js-message {
      display: none; /* Hidden by default when JavaScript is active */
      background-color: #f8d7da;
      color: #842029;
      padding: 20px;
      border: 1px solid #f5c2c7;
      border-radius: 5px;
      font-family: Arial, sans-serif;
      margin: 20px;
    }
  </style>
  <noscript>
    <!-- Message shown if JavaScript is disabled -->
    <style>
      /* Ensure the fallback message is visible if JavaScript is disabled */
      .no-js-message {
        display: block;
      }
    </style>
  </noscript>
</head>
<body>

  <div class="no-js-message">
    JavaScript is disabled in your browser. For the best experience on SynFutures, please enable JavaScript.
    Alternatively, you may visit our <a href="/static-fallback-page">static fallback page</a>.
  </div>

  <!-- Main content of the site -->
  <div id="main-content">
    <!-- JavaScript-enabled content goes here -->
    <h1>Welcome to SynFutures</h1>
    <p>Your decentralized futures trading platform.</p>
  </div>

  <script>
    // JavaScript code to hide the fallback message when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.querySelector('.no-js-message');

      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the fallback message
      }
    });
  </script>

</body>
</html>
```
