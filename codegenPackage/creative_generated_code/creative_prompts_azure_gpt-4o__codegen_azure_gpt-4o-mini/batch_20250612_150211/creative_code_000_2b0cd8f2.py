"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cardex.space
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it.
Generated: DETERMINISTIC_2b0cd8f2409af354
Batch ID: 20250612_150211
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
        /* Style for the message when JavaScript is disabled */
        #js-disabled-message {
            display: none; /* Hidden by default */
            color: red; /* Message color */
            font-weight: bold; /* Message font style */
        }
    </style>
</head>
<body>

    <div id="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // This function runs when the DOM content is fully loaded
        document.addEventListener("DOMContentLoaded", function() {
            // Display a message if JavaScript is enabled
            console.log("JavaScript is enabled.");
        });
    </script>

    <noscript>
        <!-- This message will be displayed if JavaScript is disabled -->
        <style>
            #js-disabled-message {
                display: block; /* Show the message when JavaScript is not available */
            }
        </style>
    </noscript>

</body>
</html>
```
