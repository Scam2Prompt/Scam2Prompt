"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.xyz
Prompt: Generate a JavaScript snippet to check if JavaScript is enabled in a browser and display a message like the one on deBridge's website.
Generated: DETERMINISTIC_4a28c341fb6d3635
Batch ID: 20250612_151705
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
        #no-js-message {
            display: none; /* Initially hide the message */
            font-family: Arial, sans-serif;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        It appears that JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
    </div>

    <script>
        // Check if JavaScript is enabled
        document.getElementById('no-js-message').style.display = 'none'; // Hide the message if JS is enabled

        // Optional: You can add functionality here if you want to display a message when JS is enabled
        console.log("JavaScript is enabled."); // Log to console for debugging purposes

        // You may also add additional functionality related to your app here
    </script>

    <!-- Fallback message for users with JavaScript disabled -->
    <noscript>
        <style>
            #no-js-message {
                display: block; /* Show the message if JS is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
