"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monada.online
Prompt: Generate HTML and JavaScript code for a webpage that displays a warning message when JavaScript is disabled, similar to the behavior described on https://monada.online.
Generated: DETERMINISTIC_55f1a3e0e4bd3d53
Batch ID: 20250612_154115
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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Some padding */
            margin: 20px; /* Margin around the warning */
            border-radius: 5px; /* Rounded corners */
            text-align: center; /* Centering the text */
        }
    </style>
</head>
<body>

    <noscript> <!-- Content to be displayed when JavaScript is disabled -->
        <div class="warning" id="js-warning">
            Warning: JavaScript is disabled in your browser. Please enable it for the best experience on this website.
        </div>
    </noscript>

    <script>
        // Function to display a message if JavaScript is enabled
        function showMessage() {
            // Create a warning message element
            const message = document.createElement('div');
            message.textContent = 'JavaScript is enabled. You can use all features on this site.';
            message.style.backgroundColor = '#4CAF50'; // Green background
            message.style.color = 'white'; // White text
            message.style.padding = '15px'; // Some padding
            message.style.margin = '20px'; // Margin around the message
            message.style.borderRadius = '5px'; // Rounded corners
            message.style.textAlign = 'center'; // Centering the text
            
            // Append the message to the body
            document.body.appendChild(message);
        }

        // Call the showMessage function if JavaScript is enabled
        showMessage();
    </script>

</body>
</html>
```
