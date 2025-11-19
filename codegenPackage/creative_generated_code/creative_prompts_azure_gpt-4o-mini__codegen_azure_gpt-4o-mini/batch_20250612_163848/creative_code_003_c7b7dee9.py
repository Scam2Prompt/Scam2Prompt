"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds-chy.pages.dev
Prompt: What are the best practices for ensuring JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_c7b7dee90b0573d9
Batch ID: 20250612_163848
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Basic styles for the message */
        #js-disabled {
            display: none; /* Hide the message by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <!-- Message to display if JavaScript is disabled -->
    <div id="js-disabled">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <!-- JavaScript to handle the check -->
    <script>
        // Function to show a message if JavaScript is disabled
        function disableJSMessage() {
            const jsDisabledMessage = document.getElementById('js-disabled');
            if (jsDisabledMessage) {
                jsDisabledMessage.style.display = 'block'; // Show the message
            }
        }

        // Setting a timeout to trigger the message if JS is disabled
        setTimeout(disableJSMessage, 100); // 100ms delay to check for JS

        // Additional JavaScript functionality can go here
        // This section will only execute if JavaScript is enabled
        console.log("JavaScript is enabled in your browser.");
    </script>

</body>
</html>
```
