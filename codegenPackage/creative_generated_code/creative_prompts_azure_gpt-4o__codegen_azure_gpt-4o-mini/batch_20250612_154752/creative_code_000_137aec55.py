"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarecrew-app.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message like the one on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_137aec55ec9f8b30
Batch ID: 20250612_154752
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
        /* Basic styling for the error message */
        .no-js-message {
            display: none; /* Hide the message by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 20px;
            border: 1px solid #f5c6cb; /* Red border */
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="no-js-message">
        <strong>Error:</strong> JavaScript is disabled in your browser. Please enable JavaScript to use this application.
    </div>

    <noscript>
        <style>
            /* Show the error message when JavaScript is disabled */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>

    <script>
        // Check if JavaScript is enabled
        (function() {
            // This function runs only if JavaScript is enabled
            console.log("JavaScript is enabled."); // Log for debugging

            // Additional application logic can be added here
            // For example, initializing the app or loading resources
        })();
    </script>

</body>
</html>
```
