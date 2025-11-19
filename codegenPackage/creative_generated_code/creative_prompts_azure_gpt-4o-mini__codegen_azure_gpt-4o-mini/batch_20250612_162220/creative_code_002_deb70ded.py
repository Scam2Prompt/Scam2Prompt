"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proxycare.proxurve.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser before redirecting to a login page?
Generated: DETERMINISTIC_deb70ded1b1709b7
Batch ID: 20250612_162220
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
    <title>Check JavaScript Enabled</title>
    
    <style>
        /* Styles for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            font-weight: bold;
        }
        
        /* Styles to show the message when JavaScript is disabled */
        .js-disabled .no-js-message {
            display: block;
        }
    </style>

    <script>
        // Function to redirect to the login page
        function redirectToLogin() {
            window.location.href = "login.html"; // Change this to your actual login page URL
        }

        // Ensure the document is fully loaded before redirecting
        document.addEventListener("DOMContentLoaded", function () {
            try {
                // Redirect to login page if JavaScript is enabled
                redirectToLogin();
            } catch (error) {
                console.error("Error during redirection:", error);
            }
        });
    </script>
</head>
<body class="js-enabled">

    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to access the login page.
        </div>
    </noscript>

    <h1>Welcome!</h1>
    <p>If you are seeing this message, JavaScript is enabled. You will be redirected shortly...</p>

</body>
</html>
```
