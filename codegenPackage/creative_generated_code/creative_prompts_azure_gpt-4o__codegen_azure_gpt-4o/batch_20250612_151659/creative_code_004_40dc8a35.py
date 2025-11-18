"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokensea-dapp.pages.dev
Prompt: Write code to detect if JavaScript is disabled in the browser and display a message like "You need to enable JavaScript to run this app."
Generated: DETERMINISTIC_40dc8a35eba92f51
Batch ID: 20250612_151659
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
  <title>JavaScript Detection</title>
  <style>
    /* Style for the message when JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default if JavaScript is enabled */
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Fallback message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js-message">
      You need to enable JavaScript to run this app.
    </div>
  </noscript>

  <!-- Main content of the app -->
  <div id="app">
    <h1>Welcome to the App!</h1>
    <p>This content is displayed only if JavaScript is enabled.</p>
  </div>

  <script>
    // Ensure any message meant for users with JavaScript disabled remains hidden
    // This is redundant as <noscript> handles it, but works as a fallback
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
