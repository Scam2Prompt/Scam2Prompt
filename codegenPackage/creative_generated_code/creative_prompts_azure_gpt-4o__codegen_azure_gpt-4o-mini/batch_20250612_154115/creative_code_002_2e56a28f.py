"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiacelestiia.com
Prompt: Create a script to detect whether JavaScript is enabled in a browser and display a message prompting users to enable it for "Glow Node" to work properly.
Generated: DETERMINISTIC_2e56a28f55ca2a7a
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
    <title>Glow Node Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide the message by default */
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
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript for "Glow Node" to function properly.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showMessage() {
            const messageElement = document.getElementById('no-js-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // Execute the showMessage function if JavaScript is not enabled
        window.onload = function() {
            // This script will run only if JavaScript is enabled
            // So we can safely hide the message element
            const messageElement = document.getElementById('no-js-message');
            messageElement.style.display = 'none'; // Hide the message for users with JS enabled
        };

        // Error handling for unexpected issues
        try {
            // This block can include any initialization code for "Glow Node"
            // For example: initializeGlowNode();
        } catch (error) {
            console.error('An error occurred while initializing Glow Node:', error);
        }
    </script>
</body>
</html>
```
