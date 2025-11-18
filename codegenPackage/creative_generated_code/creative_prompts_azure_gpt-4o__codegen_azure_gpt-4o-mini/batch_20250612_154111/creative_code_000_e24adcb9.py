"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitkuex-trade.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message like "BitExchangePro doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_e24adcb9f12d216a
Batch ID: 20250612_154111
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
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <!-- Message to display if JavaScript is disabled -->
    <div id="no-js-message" class="no-js-message">
        BitExchangePro doesn't work properly without JavaScript enabled.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function displayNoJsMessage() {
            const noJsMessage = document.getElementById("no-js-message");
            noJsMessage.style.display = "block"; // Show the message
        }

        // Call the function to display the message
        // It can be called as an inline script if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // If JavaScript is enabled, this function will run
            // We do not need to display any message
        });

        // If JavaScript is enabled, we can hide the message in case it was previously shown
        window.onload = () => {
            const noJsMessage = document.getElementById("no-js-message");
            noJsMessage.style.display = "none"; // Hide the message if JS is enabled
        };
    </script>

    <noscript>
        <!-- Display the message if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
