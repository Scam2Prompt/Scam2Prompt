"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkta.com
Prompt: Write a code snippet that checks if JavaScript is enabled on a mobile device and displays a message if it is not.
Generated: DETERMINISTIC_df92765226b7eef0
Batch ID: 20250612_163840
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
    <title>JavaScript Check</title>
    <style>
        /* Default message styling for when JavaScript is disabled */
        #js-disabled-message {
            display: block;
            font-size: 18px;
            color: red;
            text-align: center;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- This message will be displayed if JavaScript is disabled -->
    <div id="js-disabled-message">
        JavaScript is disabled on your device. Please enable it for the best experience.
    </div>

    <script>
        // JavaScript is enabled, hide the message
        document.addEventListener("DOMContentLoaded", () => {
            const jsDisabledMessage = document.getElementById("js-disabled-message");

            if (jsDisabledMessage) {
                jsDisabledMessage.style.display = "none"; // Hide the message when JS is enabled
            }
        });
    </script>
</body>
</html>
```
