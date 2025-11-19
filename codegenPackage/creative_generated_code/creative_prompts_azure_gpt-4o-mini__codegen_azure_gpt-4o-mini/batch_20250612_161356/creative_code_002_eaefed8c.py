"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suibiolab.rf.gd
Prompt: Can you provide code examples for checking if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_eaefed8c9e3f3b65
Batch ID: 20250612_161356
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
            display: none;
            color: red;
            font-weight: bold;
        }
        /* Style for the message when JavaScript is enabled */
        .js-message {
            display: none;
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Message to display when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <!-- Message to display when JavaScript is enabled -->
    <div class="js-message" id="js-message">
        JavaScript is enabled in your browser. You can now use all features.
    </div>

    <noscript>
        <style>
            /* Ensure the no-JS message is visible when JavaScript is disabled */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>

    <script>
        // Function to handle the display of messages based on JS availability
        function checkJavaScript() {
            try {
                // Display the JS enabled message
                document.getElementById('js-message').style.display = 'block';
            } catch (error) {
                console.error('Error displaying JavaScript enabled message:', error);
            }
        }

        // Call the function to check for JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```
