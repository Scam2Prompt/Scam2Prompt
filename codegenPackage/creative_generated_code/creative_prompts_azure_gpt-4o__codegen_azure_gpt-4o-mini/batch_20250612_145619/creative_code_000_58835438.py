"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobken.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a mobile browser and display a message prompting the user to enable it for the "ETH Pledge" website.
Generated: DETERMINISTIC_588354382ebb0578
Batch ID: 20250612_145619
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
    <title>ETH Pledge</title>
    <style>
        /* Style for the warning message */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            margin: 20px;
            border: 1px solid #f5c6cb; /* Border to match the background */
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to access the ETH Pledge website.
    </div>

    <script>
        // Function to display the message when JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Check if JavaScript is enabled
        window.onload = function() {
            // Hide the message if JavaScript is enabled
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'none'; // Ensure the message is hidden
        };

        // Error handling to ensure the message is updated correctly
        try {
            // Additional logic can be placed here if necessary
        } catch (error) {
            console.error('An error occurred while checking JavaScript status:', error);
        }
    </script>
</body>
</html>
```
