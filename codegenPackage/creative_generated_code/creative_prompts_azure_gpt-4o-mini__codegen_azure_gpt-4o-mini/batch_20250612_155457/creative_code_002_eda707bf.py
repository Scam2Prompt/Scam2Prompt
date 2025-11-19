"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethxoo.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a mobile web application?
Generated: DETERMINISTIC_eda707bf44fcb929
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
    <title>JavaScript Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <noscript>
        <style>
            /* Show the message when JavaScript is disabled */
            .no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

    <div class="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best user experience.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            console.log("JavaScript is enabled."); // Log message for debugging
        }

        // Call the function to indicate that JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
