"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-cftc-us25-eqq.pages.dev
Prompt: Generate a script that prompts users to enable JavaScript and cookies for a seamless experience, inspired by the verification process on namada.foundation.
Generated: DETERMINISTIC_05206447ec1899d3
Batch ID: 20250612_161134
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
    <title>Enable JavaScript and Cookies</title>
    <style>
        /* Basic styling for the message */
        .message-container {
            display: none;
            text-align: center;
            padding: 20px;
            margin: 20px auto;
            width: 80%;
            max-width: 600px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background-color: #f9f9f9;
            color: #333;
            font-family: Arial, sans-serif;
        }

        .error {
            color: #d9534f;
            font-weight: bold;
        }

        .success {
            color: #5cb85c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Placeholder messages -->
    <div id="javascriptMessage" class="message-container error">
        JavaScript is disabled in your browser. Please enable JavaScript for a seamless experience.
    </div>

    <div id="cookieMessage" class="message-container error">
        Cookies are disabled in your browser. Please enable cookies to use this site properly.
    </div>

    <div id="successMessage" class="message-container success">
        Thank you! JavaScript and cookies are enabled in your browser.
    </div>

    <noscript>
        <!-- Fallback message if JavaScript is entirely disabled -->
        <style>
            .message-container { display: block !important; }
        </style>
        <div class="message-container error">
            JavaScript is disabled in your browser. Please enable JavaScript for a seamless experience.
        </div>
    </noscript>

    <script>
        // Function to check if cookies are enabled
        function areCookiesEnabled() {
            try {
                // Test by setting a temporary cookie
                document.cookie = "testCookie=enabled; path=/";
                return document.cookie.indexOf("testCookie=enabled") !== -1;
            } catch (error) {
                return false; // Return false if cookies are blocked
            }
        }

        // Main function to handle the display logic
        function checkBrowserSettings() {
            const javascriptMessage = document.getElementById('javascriptMessage');
            const cookieMessage = document.getElementById('cookieMessage');
            const successMessage = document.getElementById('successMessage');

            // Hide all messages initially
            javascriptMessage.style.display = 'none';
            cookieMessage.style.display = 'none';
            successMessage.style.display = 'none';

            // Check if cookies are enabled
            const cookiesEnabled = areCookiesEnabled();

            if (!cookiesEnabled) {
                // Display cookie error message
                cookieMessage.style.display = 'block';
            } else {
                // JavaScript is enabled if we reach this point
                successMessage.style.display = 'block';
            }
        }

        // Execute the check on page load
        checkBrowserSettings();
    </script>
</body>
</html>
```
