"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rainbnb.live
Prompt: Write a script to detect whether JavaScript is enabled in a user's browser and display a warning message if it is disabled, as seen on RainBNB.
Generated: DETERMINISTIC_766530d379239736
Batch ID: 20250612_150246
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
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hide by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Warning message for users with JavaScript disabled -->
    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience on this site.
    </div>

    <script>
        // Function to display the warning message if JavaScript is disabled
        function showWarning() {
            const warningDiv = document.getElementById('js-warning');
            if (warningDiv) {
                warningDiv.style.display = 'block'; // Show the warning
            } else {
                console.error('Warning div not found, cannot display warning message.');
            }
        }

        // Ensure the warning is displayed if JavaScript is disabled
        document.addEventListener('DOMContentLoaded', (event) => {
            // The warning will show up only if JavaScript is not enabled
        });
    </script>

    <noscript>
        <!-- Fallback content for browsers with JavaScript disabled -->
        <style>
            #js-warning {
                display: block; /* Show warning by default if JS is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
