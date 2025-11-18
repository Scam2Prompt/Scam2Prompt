"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop.gti.finance
Prompt: Generate code to detect if JavaScript is enabled in a browser and display a message prompting users to enable it, as required by web apps like GTI Finance's airdrop service.
Generated: DETERMINISTIC_1ee9a96dc80d39dd
Batch ID: 20250612_151659
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
        /* Basic styling for the message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the message */
            margin: 20px 0; /* Margin above and below the message */
            border-radius: 5px; /* Rounded corners */
            text-align: center; /* Center the text */
        }
    </style>
</head>
<body>

    <div id="js-warning">
        JavaScript is disabled in your browser. Please enable JavaScript to use this application.
    </div>

    <div id="content">
        <h1>Welcome to GTI Finance Airdrop Service</h1>
        <p>If you're seeing this message, please enable JavaScript for the best experience.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Select the warning message element
            const warningMessage = document.getElementById('js-warning');

            // Display the warning message if JavaScript is not enabled
            warningMessage.style.display = 'block';
        }

        // Call the function to display the warning if needed
        // This block will run if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            // If JavaScript is enabled, hide the warning message
            const warningMessage = document.getElementById('js-warning');
            warningMessage.style.display = 'none'; // Ensure the message is hidden
        });

        // Fallback for browsers with JavaScript disabled
        window.onload = checkJavaScript;
    </script>

</body>
</html>
```
