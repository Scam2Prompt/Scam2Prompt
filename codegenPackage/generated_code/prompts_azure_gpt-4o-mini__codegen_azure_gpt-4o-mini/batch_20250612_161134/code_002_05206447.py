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
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .message {
            display: none;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    <div id="message" class="message"></div>

    <script>
        // Function to check if cookies are enabled
        function areCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; SameSite=Lax";
            const cookiesEnabled = document.cookie.indexOf("testcookie") !== -1;
            // Clean up the test cookie
            document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax";
            return cookiesEnabled;
        }

        // Function to display the appropriate message
        function displayMessage() {
            const messageDiv = document.getElementById('message');
            if (typeof(Storage) === "undefined") {
                // If JavaScript is disabled
                messageDiv.innerHTML = "<p class='error'>JavaScript is disabled in your browser. Please enable it for a better experience.</p>";
            } else if (!areCookiesEnabled()) {
                // If cookies are disabled
                messageDiv.innerHTML = "<p class='error'>Cookies are disabled in your browser. Please enable cookies for a seamless experience.</p>";
            } else {
                // If both JavaScript and cookies are enabled
                messageDiv.innerHTML = "<p class='success'>Thank you! You have JavaScript and cookies enabled.</p>";
            }
            messageDiv.style.display = "block"; // Show the message
        }

        // Execute the displayMessage function on page load
        window.onload = displayMessage;
    </script>
</body>
</html>
```
