"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greendotinstallerportaluat.crm.com
Prompt: Generate JavaScript code to check if JavaScript is enabled in a browser and display a message, similar to the GreenDot Installer Portal's functionality.
Generated: DETERMINISTIC_a9d62fb160190ae2
Batch ID: 20250612_154250
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
        /* Basic styling for the message */
        .message {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #cce5ff;
            border: 1px solid #b8daff;
            border-radius: 5px;
            display: none; /* Initially hidden */
        }
    </style>
</head>
<body>

    <noscript>
        <!-- Message for users with JavaScript disabled -->
        <div class="message">
            JavaScript is disabled in your browser. Please enable it to use this application.
        </div>
    </noscript>

    <div id="js-message" class="message">
        JavaScript is enabled in your browser. Welcome!
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Display the message for enabled JavaScript
                const messageElement = document.getElementById('js-message');
                
                // Ensure element is found before attempting to modify it
                if (messageElement) {
                    messageElement.style.display = 'block'; // Show the message
                } else {
                    // Log error if element is not found
                    console.error('Message element not found in the DOM.');
                }
            } catch (error) {
                // Log any unexpected errors
                console.error('An error occurred while checking JavaScript:', error);
            }
        }

        // Call the function to check for JavaScript
        checkJavaScript();
    </script>

</body>
</html>
```
