"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getin.co.il
Prompt: Write JavaScript code to detect if a user's browser supports JavaScript and display a custom message if it does not, similar to the functionality described on the website https://getin.co.il.
Generated: DETERMINISTIC_8756a4e8b5aa1fb9
Batch ID: 20250612_150417
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
    <title>JavaScript Support Detection</title>
    <style>
        /* Styling for the message */
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #ffdddd; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 10px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is not supported -->
    <div id="no-js-message">
        Your browser does not support JavaScript. Please enable JavaScript to access all features of this website.
    </div>

    <script>
        // Function to check if JavaScript is supported
        function checkJavaScriptSupport() {
            // Select the message element
            const noJsMessage = document.getElementById('no-js-message');

            // Check if the element exists and is currently hidden
            if (noJsMessage) {
                // If JavaScript is running, hide the message
                noJsMessage.style.display = 'none';
            } else {
                // If not, show the message
                noJsMessage.style.display = 'block';
            }
        }

        // Call the function to check JavaScript support
        checkJavaScriptSupport();
    </script>
</body>
</html>
```
