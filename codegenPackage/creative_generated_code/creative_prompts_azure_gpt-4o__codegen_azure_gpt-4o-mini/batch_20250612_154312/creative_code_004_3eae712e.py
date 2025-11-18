"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeai.eu
Prompt: Write code for a JavaScript snippet that displays a custom error message when JavaScript is disabled, similar to the behavior described on the DogeAI website.
Generated: DETERMINISTIC_3eae712e5a38d7ae
Batch ID: 20250612_154312
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
        /* Style for the error message */
        #js-disabled-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <!-- Error message for when JavaScript is disabled -->
    <div id="js-disabled-message">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to show the error message
        function showErrorMessage() {
            const messageElement = document.getElementById("js-disabled-message");
            messageElement.style.display = "block"; // Show the message
        }

        // Call the function on page load
        showErrorMessage();
    </script>

    <noscript>
        <!-- Content within noscript tag is displayed when JavaScript is disabled -->
        <div id="js-disabled-message"> 
            <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

</body>
</html>
```
