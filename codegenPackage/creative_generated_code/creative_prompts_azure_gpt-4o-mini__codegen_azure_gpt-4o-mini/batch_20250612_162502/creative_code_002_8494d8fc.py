"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collab-land.de
Prompt: Can you provide code examples for detecting if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_8494d8fc428334b8
Batch ID: 20250612_162502
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
        /* Styles for the message display */
        .no-js {
            display: none; /* Hide the message by default */
        }
        .js {
            display: block; /* Show the message if JavaScript is enabled */
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is not enabled -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for a better experience.</p>
        </div>
    </noscript>

    <!-- Message to display if JavaScript is enabled -->
    <div class="js" id="js-enabled-message">
        <p>JavaScript is enabled in your browser. Enjoy the full experience!</p>
    </div>

    <script>
        // This script runs if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            try {
                // Log successful detection of JavaScript
                console.log("JavaScript is enabled."); // Log for debugging purposes

                // Optionally, manipulate the DOM or load additional resources here
                // e.g., load additional scripts or display dynamic content.

            } catch (error) {
                // Capture and log any errors that occur during execution
                console.error("An error occurred while detecting JavaScript:", error);
            }
        });
    </script>
</body>
</html>
```
