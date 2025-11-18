"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a user's browser and display a warning message.
Generated: DETERMINISTIC_664094980dca82b5
Batch ID: 20250612_150116
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
        /* Style for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Red border */
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>Warning:</strong> It seems that JavaScript is disabled in your browser. Please enable it to use all features of this site.
    </div>

    <script>
        // This function will be executed when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Show the warning message if JavaScript is enabled
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'none'; // Ensure it's hidden on JS enabled browsers
        });
    </script>

    <noscript>
        <!-- This will only be rendered if JavaScript is disabled in the browser -->
        <style>
            /* Ensure the warning message is displayed if JS is disabled */
            #js-warning {
                display: block; /* Show the warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
