"""
Generated Code Metadata:
========================
Original URL: https://greendotinstallerportaluat.crm.com
Prompt: Create JavaScript code to display a warning message if JavaScript is disabled, as seen in the GreenDot Installer Portal.
Generated: DETERMINISTIC_f181f9c8ecc67e73
Batch ID: 20250612_154250
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
    <title>JavaScript Warning</title>
    <style>
        /* Style for the warning message */
        .js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Light red border */
            padding: 15px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <!-- Warning message for users with JavaScript disabled -->
    <noscript>
        <div class="js-warning">
            Warning: JavaScript is disabled in your browser. Please enable JavaScript to use this application.
        </div>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Log a message to the console for debugging
            console.log("JavaScript is enabled.");
        }

        // Call the function to check JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```
