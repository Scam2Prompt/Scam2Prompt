"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getcoins.eu
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
Batch ID: 20250612_140107
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
            display: none; /* Hidden by default, will be shown by JavaScript */
        }
        .enabled {
            color: green;
        }
        .disabled {
            color: red;
        }
    </style>
</head>
<body>

    <div id="js-enabled" class="message enabled">JavaScript is enabled!</div>
    <div id="js-disabled" class="message disabled">JavaScript is disabled!</div>

    <noscript>
        <style>
            /* Style for no-script message */
            #js-disabled {
                display: block; /* Show if JavaScript is disabled */
            }
        </style>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            try {
                // Display the message indicating JavaScript is enabled
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                // Log the error (if any) and display a message
                console.error('Error checking JavaScript status:', error);
                document.getElementById('js-disabled').style.display = 'block';
            }
        }

        // Call the function to check JavaScript status
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
