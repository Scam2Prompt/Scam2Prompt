"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade.94la.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on the Trade website.
Generated: DETERMINISTIC_c359e4bdbdafe144
Batch ID: 20250612_154741
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
            display: none; /* Hide by default */
            color: red;
            font-size: 18px;
            text-align: center;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <div id="no-js" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const noJsMessage = document.getElementById('no-js');
            if (noJsMessage) {
                noJsMessage.style.display = 'block'; // Show the message
            } else {
                console.error('No JavaScript message element not found.');
            }
        }

        // Run the function to show the message if this script executes
        showNoJsMessage();
    </script>

    <noscript>
        <!-- Fallback content for browsers with JavaScript disabled -->
        <style>
            #no-js {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
