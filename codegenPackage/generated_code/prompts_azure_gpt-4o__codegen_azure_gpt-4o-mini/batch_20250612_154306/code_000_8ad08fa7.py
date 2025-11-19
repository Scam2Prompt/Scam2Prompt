"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, as suggested by the functionality described on the Step App domain page.
Generated: DETERMINISTIC_8ad08fa70cebd9a2
Batch ID: 20250612_154306
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
    <title>JavaScript Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
    <noscript>
        <style>
            /* Show the message when JavaScript is disabled */
            .no-js-message {
                display: block; /* Show when JS is disabled */
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this application.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Log a message to the console for debugging
            console.log("JavaScript is enabled.");
        }

        // Call the function to indicate JavaScript is running
        checkJavaScript();
    </script>
</body>
</html>
```
