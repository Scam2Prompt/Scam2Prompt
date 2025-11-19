"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds-chy.pages.dev
Prompt: What are the best practices for ensuring JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_c7b7dee90b0573d9
Batch ID: 20250612_163848
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Hide the "JavaScript is disabled" message by default */
        #no-js-message {
            display: none;
            color: red;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>

<body>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <noscript>
        <div id="no-js-message">
            JavaScript is disabled in your browser. Please enable it to view this website properly.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to My Website</h1>
        <p>JavaScript is enabled in your browser!</p>
    </div>

    <script>
        // Ensure proper handling if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function () {
            try {
                // Hide the message displayed by <noscript> if JavaScript is enabled
                const noJsMessage = document.getElementById("no-js-message");
                if (noJsMessage) {
                    noJsMessage.style.display = "none";
                }

                // Additional code can be added here to initialize your application
                console.log("JavaScript is enabled and working properly.");
            } catch (error) {
                // Log errors to the console and notify the user if something goes wrong
                console.error("An error occurred while checking JavaScript status:", error);
                alert("An error occurred. Please refresh the page.");
            }
        });
    </script>
</body>

</html>
```
