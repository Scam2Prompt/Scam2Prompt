"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hingehealth.eu
Prompt: Write code to detect if JavaScript is disabled in a user's browser and display a custom message prompting them to enable it, similar to the behavior on the Hinge Health EU website.
Generated: DETERMINISTIC_4af81d72263b992e
Batch ID: 20250612_151438
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
    <title>JavaScript Detection</title>
    <style>
        /* Styles for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <!-- This message is shown if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block; /* Show message when JavaScript is disabled */
            }
        </style>
    </noscript>
</head>
<body>

    <!-- Message for users with JavaScript disabled -->
    <div class="no-js-message">
        <strong>JavaScript is disabled!</strong> For the best experience on our site, please enable JavaScript in your browser settings.
    </div>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to Our Website</h1>
        <p>This content is enhanced with JavaScript.</p>
    </div>

    <script>
        // JavaScript to enhance the user experience
        document.addEventListener('DOMContentLoaded', function () {
            try {
                // Example of JavaScript functionality (you can replace this with actual functionality)
                console.log("JavaScript is enabled and running!");
                // Further code to enhance the page goes here
            } catch (error) {
                console.error("An error occurred while running JavaScript:", error);
                // Handling if something goes wrong
                alert("An unexpected error occurred. Please reload the page.");
            }
        });
    </script>

</body>
</html>
```
