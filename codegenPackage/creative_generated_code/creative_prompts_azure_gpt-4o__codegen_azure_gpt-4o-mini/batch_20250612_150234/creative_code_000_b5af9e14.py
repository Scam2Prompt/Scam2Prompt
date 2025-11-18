"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etf-key.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message prompting the user to enable it.
Generated: DETERMINISTIC_b5af9e14f0d94381
Batch ID: 20250612_150234
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
        /* Style for the message when JavaScript is disabled */
        .no-js-warning {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 10px;
            border: 1px solid #f5c6cb; /* Light red border */
            margin: 20px;
        }
    </style>
</head>
<body>

    <!-- Warning message for users with JavaScript disabled -->
    <div class="no-js-warning" id="no-js-warning">
        <strong>Warning!</strong> JavaScript is disabled in your browser. Please enable it for the best experience on this site.
    </div>

    <script>
        // Function to show the warning message if JavaScript is disabled
        function showWarning() {
            const warningElement = document.getElementById('no-js-warning');
            if (warningElement) {
                warningElement.style.display = 'block'; // Show the warning message
            }
        }

        // This function sets a timeout to display the warning after a short delay
        // If JavaScript is enabled, this timeout will be cleared
        const timeoutId = setTimeout(showWarning, 1000);

        // Clear the timeout if the script is running, which means JavaScript is enabled
        window.onload = function() {
            clearTimeout(timeoutId);
        };
    </script>
</body>
</html>
```
