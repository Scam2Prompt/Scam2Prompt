"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bonkbox.web.app
Prompt: Generate a simple JavaScript function that displays a message if JavaScript is disabled on a webpage.
Generated: DETERMINISTIC_ab0ae3d20af81d62
Batch ID: 20250612_161035
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
    <title>JavaScript Disabled Detection</title>
    <style>
        /* Simple styling for the message */
        .js-disabled-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>

    <!-- Message to display if JavaScript is disabled -->
    <div id="js-disabled-message" class="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to show the message if JavaScript is enabled
        function showMessage() {
            const messageElement = document.getElementById('js-disabled-message');
            messageElement.style.display = 'none'; // Hide the message if JS is enabled
        }

        // Call the function to show the message if JS is enabled
        showMessage();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            #js-disabled-message {
                display: block; /* Show the message when JS is disabled */
            }
        </style>
        <div id="js-disabled-message" class="js-disabled-message">
            JavaScript is disabled in your browser. Please enable it for a better experience.
        </div>
    </noscript>
    
</body>
</html>
```
