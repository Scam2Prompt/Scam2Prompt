"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Develop a simple JavaScript application that checks if JavaScript is enabled and displays a message similar to "You need to enable JavaScript to run this app."
Generated: DETERMINISTIC_565ba245807f5efc
Batch ID: 20250612_153648
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
    <title>JavaScript Check</title>
    <style>
        /* Basic styles for the message */
        .message {
            display: none;
            font-size: 20px;
            color: red;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <div class="message" id="js-disabled-message">
        You need to enable JavaScript to run this app.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showMessage() {
            const messageElement = document.getElementById('js-disabled-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // Check if JavaScript is enabled by running a test function
        (function checkJsEnabled() {
            try {
                // If this code runs, JavaScript is enabled
                console.log('JavaScript is enabled.');
            } catch (error) {
                // Log error if it occurs (should not happen in this case)
                console.error('An error occurred while checking JavaScript:', error);
                showMessage(); // Call function to show message
            }
        })();
    </script>

    <noscript>
        <!-- This HTML will only be displayed if JavaScript is disabled -->
        <style>
            #js-disabled-message {
                display: block; /* Show message when JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
