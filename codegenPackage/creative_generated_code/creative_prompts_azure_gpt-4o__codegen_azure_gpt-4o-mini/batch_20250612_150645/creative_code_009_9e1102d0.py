"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbchainmining.com
Prompt: Generate JavaScript code for detecting whether JavaScript is enabled in a user's browser and displaying a message if it is disabled.
Generated: DETERMINISTIC_9e1102d08cc8ce58
Batch ID: 20250612_150645
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
        /* Style for the message */
        #js-disabled-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <div id="js-disabled-message">
            JavaScript is disabled in your browser. Please enable it for a better experience.
        </div>
    </noscript>

    <script>
        // Function to show a message if JavaScript is enabled
        function showJsEnabledMessage() {
            console.log("JavaScript is enabled.");
            // Optionally, we can display a message on the page if needed
        }

        // Execute the function to confirm JavaScript is enabled
        showJsEnabledMessage();
    </script>
</body>
</html>
```
