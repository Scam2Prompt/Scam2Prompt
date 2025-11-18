"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boredturtleyc.netlify.app
Prompt: Generate JavaScript code to detect if JavaScript is disabled in a user's browser and display an alert or message, as seen on the "Bored Turtle Yacht Club" site.
Generated: DETERMINISTIC_bdccdbe73647612e
Batch ID: 20250612_151044
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
        /* Styling for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #ffcccc;
            color: #d8000c;
            padding: 15px;
            border: 1px solid #d8000c;
            margin: 20px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Message to show when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled in your browser!</strong><br>
        Please enable JavaScript to view the content of this site properly.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // If JavaScript is enabled, hide the no-js message
        document.addEventListener('DOMContentLoaded', function() {
            const messageElement = document.getElementById('no-js-message');
            messageElement.style.display = 'none'; // Hide the message
        });
    </script>

    <!-- Fallback for browsers where JavaScript is disabled -->
    <noscript>
        <style>
            #no-js-message {
                display: block; /* Show the message in case of no JavaScript */
            }
        </style>
    </noscript>
</body>
</html>
```
