"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkta.com
Prompt: Generate a code example to check if JavaScript is enabled in a browser and display an Ethereum pledge-related message if it is disabled.
Generated: DETERMINISTIC_50e1d00f1072a855
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
    <title>Check JavaScript</title>
    <style>
        #no-js-message {
            display: none; /* Hide message by default */
            color: red; /* Style for the message */
            font-weight: bold;
        }
    </style>
    <script>
        // Function to display message if JavaScript is enabled
        function showMessage() {
            const messageContainer = document.getElementById('js-message');
            messageContainer.style.display = 'block'; // Show message if JS is enabled
        }
    </script>
</head>
<body onload="showMessage()">

    <div id="js-message">
        <p>JavaScript is enabled in your browser.</p>
        <p>Consider making an Ethereum pledge to support our project!</p>
    </div>

    <noscript>
        <div id="no-js-message">
            <p>JavaScript is disabled in your browser.</p>
            <p>Please enable JavaScript to see our Ethereum pledge message.</p>
        </div>
    </noscript>

</body>
</html>
```
