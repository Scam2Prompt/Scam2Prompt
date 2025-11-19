"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dueleth.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
Batch ID: 20250612_135829
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
        .enabled {
            color: green;
            border-color: green;
        }
        .disabled {
            color: red;
            border-color: red;
        }
    </style>
</head>
<body>
    <div id="js-check" class="message"></div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Get the message div
            const messageDiv = document.getElementById('js-check');

            // Update the message to indicate JavaScript is enabled
            messageDiv.textContent = "JavaScript is enabled!";
            messageDiv.classList.add('enabled');
        }

        // Call the check function
        checkJavaScript();

        // Fallback for when JavaScript is disabled
        window.onload = function() {
            // Create a fallback message to display if JavaScript is disabled
            const fallbackMessage = document.createElement('noscript');
            fallbackMessage.innerHTML = "<div class='message disabled'>JavaScript is disabled in your browser. Please enable it for a better experience.</div>";
            document.body.appendChild(fallbackMessage);
        };
    </script>
</body>
</html>
```
