"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
Batch ID: 20250612_163647
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Basic styling for messages */
        .message {
            font-size: 20px;
            margin: 20px;
            display: none; /* Hidden by default, will be shown by JavaScript */
        }
        .enabled {
            color: green;
        }
        .disabled {
            color: red;
        }
    </style>
</head>
<body>

    <div id="js-enabled" class="message enabled">JavaScript is enabled!</div>
    <div id="js-disabled" class="message disabled">JavaScript is disabled!</div>

    <noscript>
        <style>
            /* Style for the no-script warning */
            #js-enabled {
                display: none; /* Hide the JavaScript enabled message */
            }
            #js-disabled {
                display: block; /* Show the JavaScript disabled message */
            }
        </style>
    </noscript>

    <script>
        // Check if JavaScript is enabled and display appropriate message
        document.addEventListener("DOMContentLoaded", function () {
            try {
                // Show the JavaScript enabled message
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                console.error("An error occurred while checking JavaScript status: ", error);
                // Optionally show a fallback message or log the error
            }
        });
    </script>
    
</body>
</html>
```
