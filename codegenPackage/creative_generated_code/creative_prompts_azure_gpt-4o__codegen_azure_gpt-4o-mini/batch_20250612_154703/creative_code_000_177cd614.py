"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getbonus.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message instructing them to enable it, similar to the functionality described on the GetBonus domain details page.
Generated: DETERMINISTIC_177cd614adcf41b4
Batch ID: 20250612_154703
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
            display: none; /* Hide this message by default */
            background-color: #ffcccc;
            color: #d8000c;
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            border: 1px solid #d8000c;
            margin: 20px;
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong>
        <p>Please enable JavaScript for a better experience on this site.</p>
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            document.getElementById('no-js-message').style.display = 'block';
        }

        // Ensure that the message is hidden when JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Hide no JavaScript message if JS is enabled
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });

        // Show the message after a short delay to give time for page load
        setTimeout(showNoJsMessage, 100);
    </script>

</body>
</html>
```
