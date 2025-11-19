"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkind.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
Batch ID: 20250612_155457
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
        /* Basic styling for messages */
        .message {
            font-size: 20px;
            margin: 20px;
            padding: 10px;
            border: 1px solid;
        }
        .js-enabled {
            border-color: green;
            color: green;
        }
        .js-disabled {
            border-color: red;
            color: red;
        }
    </style>
</head>
<body>
    <div id="message" class="message"></div>

    <script>
        // Function to display message based on JavaScript availability
        function displayMessage(isEnabled) {
            const messageDiv = document.getElementById('message');
            if (isEnabled) {
                messageDiv.textContent = "JavaScript is enabled in your browser.";
                messageDiv.className = "message js-enabled"; // Apply CSS for JS enabled message
            } else {
                messageDiv.textContent = "JavaScript is disabled in your browser.";
                messageDiv.className = "message js-disabled"; // Apply CSS for JS disabled message
            }
        }

        // Check if JavaScript is enabled in the browser
        displayMessage(true); // If JavaScript runs, it's enabled
    </script>

    <noscript>
        <!-- Fallback message for users with JavaScript disabled -->
        <style>
            /* Hide message if JavaScript is enabled */
            .message {
                display: none;
            }
        </style>
        <div class="message js-disabled">JavaScript is disabled in your browser.</div>
    </noscript>
</body>
</html>
```
