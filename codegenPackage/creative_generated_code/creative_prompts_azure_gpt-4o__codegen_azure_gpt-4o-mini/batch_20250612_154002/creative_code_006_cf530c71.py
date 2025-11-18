"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqqh.com
Prompt: Create a JavaScript snippet to detect whether JavaScript is enabled in a browser and display a warning message for DeFi users if it is disabled.
Generated: DETERMINISTIC_cf530c716355b36b
Batch ID: 20250612_154002
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
        .warning {
            display: none; /* Hide by default */
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
    <div id="js-warning" class="warning">
        Warning: JavaScript is disabled in your browser. Please enable it for a better experience, especially for DeFi applications.
    </div>

    <script>
        // Function to display the warning message for users with JavaScript disabled
        function displayWarning() {
            const warningDiv = document.getElementById('js-warning');
            warningDiv.style.display = 'block'; // Show the warning message
        }

        // Check if JavaScript is enabled by using a timeout that executes immediately
        window.onload = function() {
            // Set a timeout to display the warning if the page loads too fast (indicating JS is disabled)
            setTimeout(() => {
                displayWarning(); // Show warning if the timeout is reached
            }, 100); // 100ms delay
        };
    </script>
</body>
</html>
```
