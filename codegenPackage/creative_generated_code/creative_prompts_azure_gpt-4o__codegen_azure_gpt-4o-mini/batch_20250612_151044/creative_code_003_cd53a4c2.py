"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check.wenser.e2p.xyz
Prompt: Provide code to detect and handle cases where JavaScript is disabled, inspired by the behavior of the domain-checking tool at https://check.wenser.e2p.xyz.
Generated: DETERMINISTIC_cd53a4c2098cf47d
Batch ID: 20250612_151044
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
        /* Styles for the message to display when JS is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #ffcccc;
            color: #ff0000;
            padding: 15px;
            border: 1px solid #ff0000;
            margin: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'block'; // Show message
            }
        }

        // Ensure the no-JS message is displayed if no JS execution occurs
        window.onload = function() {
            // Check if a specific JavaScript function has been executed
            if (!window.jsDetected) {
                showNoJsMessage();
            }
        };

        // This flag serves as an indicator that JavaScript is working
        window.jsDetected = true; // Set to true if JS is enabled

        // Example of JavaScript functionality
        function init() {
            // Here you can initialize your application
            console.log("JavaScript is enabled and running.");
            // Additional functionality can be added here
        }

        // Execute the init function to kickstart the application
        init();

    </script>
</body>
</html>
```
