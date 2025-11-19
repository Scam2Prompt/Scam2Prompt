"""
Generated Code Metadata:
========================
Original URL: https://imetobken.com
Prompt: Create a script that checks for JavaScript support on mobile devices and redirects users to an alternative page if JavaScript is disabled, specifically for the "ETH Pledge" platform.
Generated: DETERMINISTIC_5c5fc8a2b115d64b
Batch ID: 20250612_145619
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
    <title>ETH Pledge</title>
    <style>
        /* Fallback message for users with JavaScript disabled */
        .no-js-message {
            display: none;
        }
        .js-message {
            display: none;
        }
    </style>
    <noscript>
        <style>
            /* Show this message if JavaScript is disabled */
            .no-js-message {
                display: block;
                color: red;
                font-weight: bold;
                text-align: center;
                margin-top: 20px;
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript or use a different browser to access the ETH Pledge platform.
    </div>
    <div class="js-message">
        <!-- Content for users with JavaScript enabled -->
        <h1>Welcome to the ETH Pledge Platform</h1>
        <p>Your journey starts here!</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptSupport() {
            // Redirect to an alternative page if JavaScript is disabled
            if (!window.navigator.javaEnabled()) {
                window.location.href = "alternative-page.html"; // Redirect URL
            } else {
                // Show content for users with JavaScript enabled
                document.querySelector('.js-message').style.display = 'block';
            }
        }

        // Execute the function to check for JavaScript support
        try {
            checkJavaScriptSupport();
        } catch (error) {
            console.error("An error occurred while checking JavaScript support:", error);
            // Optionally, redirect to an error page or show a user-friendly message
            window.location.href = "error-page.html"; // Error handling redirect
        }
    </script>
</body>
</html>
```
