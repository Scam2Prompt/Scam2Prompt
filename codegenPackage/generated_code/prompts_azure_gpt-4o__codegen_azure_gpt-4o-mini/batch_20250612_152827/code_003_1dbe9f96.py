"""
Generated Code Metadata:
========================
Original URL: https://khuga-mint.pages.dev
Prompt: Build a simple HTML and JavaScript-based landing page that displays a message to enable JavaScript, similar to the "Mint" page behavior.
Generated: DETERMINISTIC_1dbe9f968923ea03
Batch ID: 20250612_152827
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
    <title>JavaScript Required</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
        }
        .message {
            display: none; /* Hidden by default */
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .fallback {
            display: block; /* Show fallback message */
        }
    </style>
</head>
<body>
    <div class="fallback">
        <h1>JavaScript is Disabled</h1>
        <p>Please enable JavaScript in your browser settings to view this page.</p>
    </div>
    <div class="message" id="js-message">
        <h1>Welcome!</h1>
        <p>JavaScript is enabled. Enjoy your experience!</p>
    </div>

    <script>
        // Function to display the message when JavaScript is enabled
        function showMessage() {
            try {
                // Hide the fallback message
                document.querySelector('.fallback').style.display = 'none';
                // Show the main message
                document.getElementById('js-message').style.display = 'block';
            } catch (error) {
                console.error('Error displaying the message:', error);
            }
        }

        // Call the function to show the message
        showMessage();
    </script>
</body>
</html>
```
