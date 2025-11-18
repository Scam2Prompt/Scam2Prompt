"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aubi.online
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the behavior on the "aubi.online" domain details page.
Generated: DETERMINISTIC_f37adcfbec78c53f
Batch ID: 20250612_154958
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
        /* Basic styles for the message */
        #js-disabled-message {
            display: none; /* Hidden by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <noscript>
        <div id="js-disabled-message">
            JavaScript is disabled in your browser. Please enable it for the best experience on this site.
        </div>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        (function() {
            // Attempt to change a document property
            if (document.body) {
                // If JavaScript is enabled, this will run
                console.log("JavaScript is enabled.");
            } else {
                // If this block is executed, something went wrong
                console.error("JavaScript is not functioning as expected.");
            }
        })();
    </script>

</body>
</html>
```
