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
        /* Style for the no-JavaScript message */
        #no-js-message {
            display: none; /* Hidden by default; shown if JS is disabled */
            text-align: center;
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            font-family: Arial, sans-serif;
            margin: 20px;
        }
    </style>
    <noscript>
        <!-- This message is displayed only if JavaScript is disabled -->
        <div id="no-js-message">
            JavaScript is disabled on your browser. Please enable JavaScript for the best experience.
        </div>
    </noscript>
</head>
<body>
    <h1>Welcome to Our Mobile Site</h1>
    <p>This site uses JavaScript to provide a better experience.</p>

    <script>
        // JavaScript is enabled, so we ensure the no-js-message does not appear
        document.addEventListener('DOMContentLoaded', () => {
            const noJsMessage = document.getElementById('no-js-message');
            
            // Safeguard: Check if element exists before attempting to manipulate it
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
