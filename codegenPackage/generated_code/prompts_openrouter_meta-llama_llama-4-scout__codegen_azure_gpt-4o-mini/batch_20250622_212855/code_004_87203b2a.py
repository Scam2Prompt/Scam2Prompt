"""
Generated Code Metadata:
========================
Original URL: https://teslax.in
Prompt: Create a simple webpage using HTML, CSS, and JavaScript that displays a message when JavaScript is disabled, similar to the message seen on teslax.in.
Generated: DETERMINISTIC_87203b2a5a76dc57
Batch ID: 20250622_212855
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
    <title>JavaScript Disabled Message</title>
    <style>
        /* Basic styling for the body */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
            padding: 50px;
        }

        /* Styling for the message when JavaScript is enabled */
        #js-enabled {
            display: none; /* Hidden by default */
        }

        /* Styling for the message when JavaScript is disabled */
        #js-disabled {
            display: block; /* Shown by default */
            background-color: #ffdddd;
            border: 1px solid #f44336;
            padding: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <div id="js-disabled">
        <h1>JavaScript is Disabled</h1>
        <p>Please enable JavaScript in your browser settings to view the content of this page.</p>
    </div>

    <!-- Message displayed when JavaScript is enabled -->
    <div id="js-enabled">
        <h1>Welcome!</h1>
        <p>JavaScript is enabled. Enjoy the full experience of our website!</p>
    </div>

    <script>
        // Function to show the message for enabled JavaScript
        function showJsEnabledMessage() {
            document.getElementById('js-disabled').style.display = 'none'; // Hide the disabled message
            document.getElementById('js-enabled').style.display = 'block'; // Show the enabled message
        }

        // Execute the function to show the enabled message
        showJsEnabledMessage();
    </script>
</body>
</html>
```
