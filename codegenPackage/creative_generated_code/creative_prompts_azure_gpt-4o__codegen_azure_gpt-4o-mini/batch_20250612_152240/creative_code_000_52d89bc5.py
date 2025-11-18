"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5h656h56h.pages.dev
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message like "Dexalot requires JavaScript enabled to function properly."
Generated: DETERMINISTIC_52d89bc588dac906
Batch ID: 20250612_152240
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
    <title>Dexalot JavaScript Detection</title>
    <style>
        /* Style for the message that will be displayed if JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide the message by default */
            background-color: #ffcccc; /* Light red background */
            color: #900; /* Dark red text */
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            border: 1px solid #900;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        Dexalot requires JavaScript enabled to function properly.
    </div>

    <script>
        // Function to display the warning message if JavaScript is enabled
        function showMessage() {
            const messageElement = document.getElementById('no-js-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // Calling the function to ensure it runs when the page loads
        showMessage();
    </script>

    <noscript>
        <!-- The no-script tag will be rendered if JavaScript is disabled. -->
        <style>
            #no-js-message {
                display: block; /* Show the message when JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
