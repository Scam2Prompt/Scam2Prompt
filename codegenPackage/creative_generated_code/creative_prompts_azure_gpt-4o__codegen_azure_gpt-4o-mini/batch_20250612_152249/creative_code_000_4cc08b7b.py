"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mybonkbox.web.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the behavior of BONKBOXES.
Generated: DETERMINISTIC_4cc08b7b0ace4d3b
Batch ID: 20250612_152249
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
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message" id="no-js-message">
            <strong>JavaScript is disabled!</strong><br>
            Please enable JavaScript in your browser settings to use this site.
        </div>
    </noscript>

    <script>
        // JavaScript to enhance the user experience
        document.addEventListener("DOMContentLoaded", () => {
            // This function can be used to hide the no-js message if JS is enabled
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        });
    </script>
</body>
</html>
```
