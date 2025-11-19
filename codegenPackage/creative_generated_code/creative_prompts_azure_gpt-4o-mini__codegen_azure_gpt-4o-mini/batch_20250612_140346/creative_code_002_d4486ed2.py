"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cry-ht.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like the one on cry-ht.com?
Generated: DETERMINISTIC_d4486ed24deeb912
Batch ID: 20250612_140346
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
        /* Styles for the message when JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <!-- Main content of the application -->
    <div id="main-content">
        <h1>Welcome to the Web Application</h1>
        <p>JavaScript is enabled!</p>
    </div>

    <script>
        // This script runs when the page is loaded
        
        // Function to hide the no-JavaScript message
        function hideNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        }

        // Execute the function to hide the message
        hideNoJsMessage();
    </script>
</body>
</html>
```
