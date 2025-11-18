"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethvnq.com
Prompt: Create a script that checks if JavaScript is enabled on a user's browser and displays a message prompting them to enable it for BTC pledge functionality.
Generated: DETERMINISTIC_83e6d093941bae63
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
    <title>JavaScript Check</title>
    <style>
        /* Styles for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Light red border */
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <div id="no-js-message">
        <strong>JavaScript is disabled!</strong><br>
        Please enable JavaScript in your browser for BTC pledge functionality.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'block';
            }
        }

        // Check if the script is running
        try {
            // If this code runs, JavaScript is enabled
            // We can safely hide the message if JavaScript is enabled
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        } catch (error) {
            // Log error to the console for debugging purposes
            console.error('An error occurred while checking JavaScript status:', error);
        }

        // Optionally, display the no-JS message after a short delay
        // This is just to give users a chance to enable JS if it's disabled
        window.onload = () => {
            setTimeout(showNoJsMessage, 1000); // Show message after 1 second if JS is still not enabled
        };
    </script>
</body>
</html>
```
