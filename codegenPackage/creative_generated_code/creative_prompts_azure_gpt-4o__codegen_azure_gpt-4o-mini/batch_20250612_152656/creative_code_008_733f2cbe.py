"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wen-drop.web.app
Prompt: Write a script to check if JavaScript is enabled on a user's browser and display a message prompting them to enable it, as required by Wen Exchange.
Generated: DETERMINISTIC_733f2cbe1297c184
Batch ID: 20250612_152656
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
        /* Style for the message */
        .js-disabled {
            display: none; /* Hide the message by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            text-align: center; /* Center the text */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <!-- Message to be displayed if JavaScript is disabled -->
    <div id="js-disabled-message" class="js-disabled">
        JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showJSDisabledMessage() {
            var messageElement = document.getElementById('js-disabled-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Display the message
            } else {
                console.error("Message element not found."); // Error logging if element is not found
            }
        }

        // Simulating a condition to demonstrate JavaScript functionality
        document.addEventListener("DOMContentLoaded", function() {
            // If this code runs, JavaScript is enabled; hence no action needed
            console.log("JavaScript is enabled."); // Log confirmation to console
        });

        // Assume JavaScript is not enabled
        // In practice, a <noscript> tag is used to handle this case
    </script>

    <noscript>
        <style>
            /* Style for the <noscript> message */
            #js-disabled-message {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
