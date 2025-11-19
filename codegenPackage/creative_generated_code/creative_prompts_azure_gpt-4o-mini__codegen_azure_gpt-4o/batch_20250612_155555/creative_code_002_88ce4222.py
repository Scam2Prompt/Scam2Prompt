"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.everclear.pk
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser for a webmail login page?
Generated: DETERMINISTIC_88ce42226509f7e5
Batch ID: 20250612_155555
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
  <title>Webmail Login</title>
  <style>
    /* Basic styling for messages */
    .no-js-message {
      display: none;
      color: red;
      font-size: 1.2em;
      text-align: center;
      margin-top: 20px;
    }
    .js-enabled-message {
      display: none;
      color: green;
      font-size: 1.2em;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <noscript>
    <!-- Display a message if JavaScript is disabled -->
    <style>
      .no-js-message {
        display: block;
      }
    </style>
    <div class="no-js-message">JavaScript is required to use this page. Please enable JavaScript in your browser settings.</div>
  </noscript>
</head>
<body>
  <div class="js-enabled-message">JavaScript is enabled. You can proceed with the login.</div>

  <form id="login-form" action="/login" method="post">
    <h1>Login</h1>
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password" required><br><br>
    <button type="submit">Login</button>
  </form>

  <script>
    /**
     * If JavaScript is enabled, display a message to the user
     * and ensure the login form works as expected.
     */
    document.addEventListener("DOMContentLoaded", () => {
      const jsEnabledMessage = document.querySelector('.js-enabled-message');
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }
    });
  </script>
</body>
</html>
```
