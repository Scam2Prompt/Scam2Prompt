"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exodusn.com
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and displays a message if it is not, similar to the warning on ExodusN.
Generated: DETERMINISTIC_54de12eca1c151bf
Batch ID: 20250612_155421
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
        /* Style for the warning message */
        .js-warning {
            display: none; /* Hidden by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Red text color */
            border: 1px solid #d8000c; /* Red border */
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Warning message for users with JavaScript disabled -->
    <div class="js-warning" id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. 
        Please enable JavaScript for a better experience.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Get the warning message element
            const warningMessage = document.getElementById('js-warning');
            // Show the warning message since JavaScript is enabled
            warningMessage.style.display = 'none'; // Hide the warning
        }

        // Call the function to check JavaScript
        checkJavaScript();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            /* Show warning message if JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning */
            }
        </style>
    </noscript>
</body>
</html>
```
