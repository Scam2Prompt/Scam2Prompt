"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stargate.fi
Prompt: Write a script to check if JavaScript is enabled in a browser and display a custom message, referencing Stargate.fi's requirements.
Generated: DETERMINISTIC_11a8feecec478fe5
Batch ID: 20250612_151610
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
        /* Styles for the message display */
        #js-enabled {
            display: none;
            color: green;
            font-size: 20px;
            margin-top: 20px;
        }
        #js-disabled {
            color: red;
            font-size: 20px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <noscript>
        <!-- Display a message when JavaScript is disabled -->
        <div id="js-disabled">
            JavaScript is disabled in your browser. Please enable it to use the full functionality of this site.
        </div>
    </noscript>

    <div id="js-enabled">
        JavaScript is enabled in your browser. Welcome to Stargate.fi!
    </div>

    <script>
        // Function to display message if JavaScript is enabled
        function displayJsEnabledMessage() {
            try {
                // Show the message for enabled JavaScript
                const jsEnabledDiv = document.getElementById('js-enabled');
                jsEnabledDiv.style.display = 'block';
            } catch (error) {
                // Log the error for debugging purposes
                console.error('An error occurred while displaying the message:', error);
            }
        }

        // Call the function to display the message
        displayJsEnabledMessage();
    </script>

</body>
</html>
```
