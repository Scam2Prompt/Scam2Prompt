"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrofunding-optimism-application5.pages.dev
Prompt: Provide an example of how to prompt users to enable JavaScript and cookies on a webpage.
Generated: DETERMINISTIC_f85f77131476a60b
Batch ID: 20250612_164319
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
        /* Basic styling for the message container */
        #jsCookiesMessage {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            border: 1px solid #f5c6cb; /* Border for the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div id="jsCookiesMessage">
        <strong>Notice:</strong> To enjoy the full functionality of this website, please enable JavaScript and allow cookies in your browser settings.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Show the message if JavaScript is enabled
            document.getElementById('jsCookiesMessage').style.display = 'block';
        }

        // Delay execution to allow the message to be shown if JavaScript is disabled
        window.onload = function() {
            checkJavaScript();
        };

        // Error handling for unsupported browsers
        try {
            // Check if cookies are enabled
            document.cookie = "testcookie=1; SameSite=Strict";
            if (document.cookie.indexOf("testcookie=") === -1) {
                throw new Error("Cookies are not enabled in your browser.");
            } else {
                // Clean up the test cookie
                document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            }
        } catch (error) {
            console.error("Error checking cookies:", error.message);
            document.getElementById('jsCookiesMessage').innerHTML += " Please enable cookies in your browser settings.";
            document.getElementById('jsCookiesMessage').style.display = 'block';
        }
    </script>
</body>
</html>
```
