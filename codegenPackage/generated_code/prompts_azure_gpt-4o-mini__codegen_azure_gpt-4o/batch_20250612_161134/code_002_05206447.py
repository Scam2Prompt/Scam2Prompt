"""
Generated Code Metadata:
========================
Original URL: https://cloudflare-cftc-us25-eqq.pages.dev
Prompt: Generate a script that prompts users to enable JavaScript and cookies for a seamless experience, inspired by the verification process on namada.foundation.
Generated: DETERMINISTIC_05206447ec1899d3
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Enable JavaScript and Cookies</title>
  <style>
    /* Basic styling for the message container */
    .message-container {
      display: none; /* Hidden by default */
      text-align: center;
      margin: 50px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
      max-width: 400px;
      font-family: Arial, sans-serif;
    }
    .error {
      color: red;
      font-weight: bold;
    }
    .success {
      color: green;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Message container -->
  <div id="message" class="message-container">
    <p id="message-text"></p>
  </div>

  <script>
    // Function to check if cookies are enabled
    function areCookiesEnabled() {
      try {
        // Attempt to set and read a test cookie
        document.cookie = "testcookie=1";
        const cookiesEnabled = document.cookie.indexOf("testcookie=1") !== -1;
        // Clean up the test cookie
        document.cookie = "testcookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
        return cookiesEnabled;
      } catch (error) {
        console.error("Error checking cookies:", error);
        return false;
      }
    }

    // Function to display a message to the user
    function displayMessage(message, isError = false) {
      const messageContainer = document.getElementById("message");
      const messageText = document.getElementById("message-text");

      // Set the message text and style
      messageText.textContent = message;
      messageText.className = isError ? "error" : "success";

      // Show the message container
      messageContainer.style.display = "block";
    }

    // Main script logic
    (function () {
      // Check if JavaScript is enabled (always true if this script runs)
      const isJavaScriptEnabled = true;

      // Check if cookies are enabled
      const isCookiesEnabled = areCookiesEnabled();

      // Display appropriate messages
      if (isJavaScriptEnabled && isCookiesEnabled) {
        displayMessage("JavaScript and cookies are enabled. You are good to go!");
      } else if (!isCookiesEnabled) {
        displayMessage("Please enable cookies in your browser for a seamless experience.", true);
      }
    })();
  </script>
</body>
</html>
```
