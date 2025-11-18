"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.dexodoor.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the cPanel login page.
Generated: DETERMINISTIC_97abd30422102dc4
Batch ID: 20250612_152441
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
    <title>JavaScript Disabled Detection</title>
    <style>
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Warning message element -->
    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable JavaScript to use this site properly.
    </div>

    <script>
        // Function to display the warning message
        function displayWarning() {
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'block'; // Show the warning message
        }

        // Attempt to hide the warning if JavaScript is enabled
        window.onload = function() {
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'none'; // Hide warning since JS is enabled
        };

        // Create a <noscript> tag to show a warning message if JS is disabled
        const noScriptMessage = document.createElement('noscript');
        noScriptMessage.innerHTML = `
            <style>
                /* Ensures the warning displays only when JS is disabled */
                #js-warning {
                    display: block; /* Show warning when JS is disabled */
                }
            </style>
        `;
        document.head.appendChild(noScriptMessage);
    </script>
</body>
</html>
```
