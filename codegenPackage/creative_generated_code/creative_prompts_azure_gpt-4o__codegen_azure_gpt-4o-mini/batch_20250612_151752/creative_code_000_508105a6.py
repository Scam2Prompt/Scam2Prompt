"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.fs.video
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, similar to the functionality described on the PancakeSwap FSV page.
Generated: DETERMINISTIC_508105a6e3d34b78
Batch ID: 20250612_151752
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
        /* Styles for the no-js message */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled!</strong> Please enable JavaScript for the best experience on this site.
    </div>
    
    <script>
        // Function to detect if JavaScript is enabled
        function detectJavaScript() {
            const noJsMessage = document.getElementById('no-js-message');
            // Display the no-JS message if this function is invoked
            noJsMessage.style.display = 'none'; // Hide the message if JS is enabled
        }

        // Calling the function to detect JavaScript
        detectJavaScript();
    </script>

    <noscript>
        <style>
            /* Styles for the no-JS message when JavaScript is disabled */
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>
</body>
</html>
```
