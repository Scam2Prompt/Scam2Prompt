"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imftokoen.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a mobile browser and display a message prompting the user to enable it.
Generated: DETERMINISTIC_a3c4479d3f4deae9
Batch ID: 20250612_145619
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
        /* Style for the message when JS is disabled */
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #ffcc00; /* Warning color */
            color: #333;
            padding: 15px;
            text-align: center;
            font-size: 18px;
            border: 1px solid #cc9900;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this application.
    </div>

    <script>
        // This function will be executed once the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", function() {
            // Hide the no-JS message if JavaScript is enabled
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'none';
        });
    </script>

    <noscript>
        <!-- This block will be rendered if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message if JS is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
