"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elbdataplanescope.zhy.coinbasenft.de
Prompt: Generate a script that detects whether JavaScript is disabled and displays an alternative static message, inspired by the behavior of the webpage at elbdataplanescope.zhy.coinbasenft.de.
Generated: DETERMINISTIC_f4e330c1aaab769f
Batch ID: 20250612_154954
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
        /* Style for the message when JS is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 20px;
            border: 1px solid #f5c6cb; /* Red border */
            border-radius: 5px;
            margin: 20px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Static message shown when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to view this content.
    </div>

    <script>
        // Function to hide the no-JS message if JavaScript is enabled
        function hideNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        }

        // Execute the function to hide the message
        hideNoJsMessage();
    </script>
    
    <noscript>
        <!-- Fallback content in case JavaScript is disabled -->
        <style>
            /* Show the no-JS message when JavaScript is not running */
            #no-js-message {
                display: block; /* Display the message */
            }
        </style>
    </noscript>
</body>
</html>
```
