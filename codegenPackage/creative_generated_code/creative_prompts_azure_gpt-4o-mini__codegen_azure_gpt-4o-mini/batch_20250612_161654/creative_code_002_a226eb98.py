"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptodrop.eu
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_161654
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
        /* Styles for the message indicating JavaScript is enabled */
        .js-enabled {
            display: none;
            color: green;
            font-weight: bold;
        }

        /* Styles for the message indicating JavaScript is disabled */
        .no-js {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Message to show if JavaScript is disabled -->
    <noscript>
        <div class="no-js">JavaScript is disabled in your browser.</div>
    </noscript>

    <!-- Message to show if JavaScript is enabled -->
    <div class="js-enabled">JavaScript is enabled in your browser.</div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // Check if the JavaScript is running
            try {
                // Show the message for JavaScript enabled
                document.querySelector('.js-enabled').style.display = 'block';
            } catch (error) {
                // Log error if any issue occurs
                console.error('Error displaying JavaScript enabled message:', error);
            }
        }

        // Run the check when the document is fully loaded
        document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
    </script>
</body>
</html>
```
