"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new-pay.starpay.top
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the behavior on the Starpay payment platform.
Generated: DETERMINISTIC_ffe81572003caf37
Batch ID: 20250612_155037
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
        /* Styles for the message container */
        #js-disabled-message {
            display: none; /* Hidden by default */
            background-color: #ffdddd; /* Light red background */
            color: #d8000c; /* Dark red text color */
            border: 1px solid #d8000c; /* Red border */
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <div id="js-disabled-message">
        <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript to use this site properly.
    </div>

    <script>
        // This function will be executed when the page is loaded
        window.onload = function() {
            // The following block will run only if JS is enabled
            document.getElementById('js-disabled-message').style.display = 'none';
        };

        // To ensure the message is displayed if JS is disabled, we use a <noscript> tag
    </script>

    <noscript>
        <style>
            /* Show the message when JS is disabled */
            #js-disabled-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>
</body>
</html>
```
