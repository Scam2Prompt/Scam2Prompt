"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeai.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "This app doesn't work properly without JavaScript enabled. Please enable it to continue," as seen on the DogeAI website.
Generated: DETERMINISTIC_fe1512dc2030ed56
Batch ID: 20250612_154312
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
        /* Style for the fallback message */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 20px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Fallback message for when JavaScript is disabled -->
    <div id="no-js-message" class="no-js-message">
        This app doesn't work properly without JavaScript enabled. Please enable it to continue.
    </div>

    <script>
        // Function to enable JavaScript detection
        function enableJavaScript() {
            // Hides the no-JS message if JavaScript is enabled
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        }

        // Call the function to enable JavaScript
        enableJavaScript();
    </script>

    <!-- Inline script to ensure the message is shown if JS is disabled -->
    <noscript>
        <style>
            /* Show the fallback message when JavaScript is disabled */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>
</body>
</html>
```
