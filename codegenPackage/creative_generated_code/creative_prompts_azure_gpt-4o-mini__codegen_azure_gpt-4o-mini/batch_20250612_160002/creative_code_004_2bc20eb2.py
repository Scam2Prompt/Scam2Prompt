"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeiairdrope888.pages.dev
Prompt: How do I implement a feature that prompts users to enable JavaScript and cookies on my website?
Generated: DETERMINISTIC_2bc20eb2d0177e21
Batch ID: 20250612_160002
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
        /* Styles for the popup notification */
        .notification {
            display: none; /* Initially hidden */
            position: fixed; /* Fixed position */
            top: 20px; /* Distance from top */
            left: 50%; /* Center horizontally */
            transform: translateX(-50%); /* Adjust centering */
            background-color: #ffcc00; /* Background color */
            color: #333; /* Text color */
            padding: 15px; /* Padding */
            border-radius: 5px; /* Rounded corners */
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Shadow effect */
            z-index: 1000; /* Ensure it appears above other elements */
        }
    </style>
    <noscript>
        <style>
            /* Show the notification if JavaScript is disabled */
            .notification {
                display: block; /* Display the notification */
            }
        </style>
    </noscript>
</head>
<body>
    <div class="notification" id="js-cookie-warning">
        <strong>Important:</strong> Please enable JavaScript and cookies in your browser settings to ensure the best experience on our website.
    </div>

    <script>
        // Function to check if cookies are enabled
        function areCookiesEnabled() {
            // Attempt to set and delete a test cookie
            document.cookie = "testcookie=1";
            const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;
            document.cookie = "testcookie=;expires=Thu, 01 Jan 1970 00:00:00 GMT"; // Clean up the test cookie
            return cookiesEnabled;
        }

        // Function to display warning if cookies are not enabled
        function checkCookies() {
            if (!areCookiesEnabled()) {
                const warningDiv = document.getElementById('js-cookie-warning');
                warningDiv.innerHTML += " Cookies are not enabled in your browser.";
                warningDiv.style.display = "block"; // Show the warning
            }
        }

        // Run the check when the script loads
        checkCookies();
    </script>
</body>
</html>
```
