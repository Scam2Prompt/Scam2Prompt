"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism-megadashboard.vercel.app
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like the Optimism Megadashboard?
Generated: DETERMINISTIC_9ce1727c28001b56
Batch ID: 20250612_162346
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
        /* Styles for the loading message */
        #no-js-message {
            display: none; /* Hide by default */
            color: red; /* Red color for visibility */
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is not enabled -->
    <div id="no-js-message">
        JavaScript is not enabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to display a message if JavaScript is not enabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'block'; // Show message
        }

        // Run when the window is fully loaded
        window.onload = function() {
            // If JavaScript is enabled, hide the no-JS message
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'none'; // Hide message by default
        };

        // Error handling for any potential issues
        try {
            // You can add any JavaScript functionality here
            console.log("JavaScript is enabled.");
        } catch (error) {
            console.error("An error occurred:", error); // Log any errors to console
            showNoJsMessage(); // Show no-JS message in case of error
        }
    </script>
</body>
</html>
```
