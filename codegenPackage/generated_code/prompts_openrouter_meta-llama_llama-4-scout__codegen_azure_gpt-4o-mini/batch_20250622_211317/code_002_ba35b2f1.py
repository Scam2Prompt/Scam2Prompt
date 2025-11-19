"""
Generated Code Metadata:
========================
Original URL: https://onc188.vip
Prompt: Generate code to create a simple webpage that displays "defi-ETH" and prompts users to enable JavaScript for proper functionality, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_ba35b2f19a077953
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Defi-ETH</title>
    <style>
        /* Basic styling for the body and message */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        .message {
            text-align: center;
            padding: 20px;
            border: 2px solid #333;
            border-radius: 10px;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .js-enabled {
            display: none; /* Hide this by default */
        }
    </style>
</head>
<body>
    <div class="message">
        <p id="default-message">defi-ETH</p>
        <p class="js-enabled" id="js-message">JavaScript is enabled. Enjoy your experience!</p>
    </div>

    <script>
        // Function to display the message when JavaScript is enabled
        function enableJavaScriptMessage() {
            // Hide the default message
            document.getElementById('default-message').style.display = 'none';
            // Show the JavaScript enabled message
            document.getElementById('js-message').style.display = 'block';
        }

        // Execute the function to enable the JavaScript message
        try {
            enableJavaScriptMessage();
        } catch (error) {
            console.error('An error occurred while enabling the JavaScript message:', error);
        }
    </script>
</body>
</html>
```
