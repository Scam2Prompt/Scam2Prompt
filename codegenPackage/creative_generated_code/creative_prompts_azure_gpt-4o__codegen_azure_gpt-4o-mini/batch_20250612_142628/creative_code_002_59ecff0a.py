"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinwallets.xyz
Prompt: Write JavaScript code to detect if a user’s browser has JavaScript disabled and display a custom message prompting them to enable it for a cryptocurrency wallet app.
Generated: DETERMINISTIC_59ecff0a66fe4715
Batch ID: 20250612_142628
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
    <title>Crypto Wallet App</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Initially hidden */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
        }
    </style>
</head>
<body>

    <!-- Message for users with JavaScript disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use the cryptocurrency wallet app.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'block'; // Show the message
            } else {
                console.error('No JavaScript message element not found.');
            }
        }

        // Show the message if JavaScript is disabled
        window.onload = function() {
            // If JavaScript is enabled, remove the no-JS message
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        };

        // Execute the function to display the message
        showNoJsMessage();
    </script>
</body>
</html>
```
