"""
Generated Code Metadata:
========================
Original URL: https://webmail.everclear.pk
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the Webmail login page of https://webmail.everclear.pk.
Generated: DETERMINISTIC_6f4a62cffe5f1077
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <noscript>
        <style>
            /* Show the warning message if JavaScript is disabled */
            #js-warning {
                display: block; /* Display the warning */
            }
        </style>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Get the warning message element
            const warningElement = document.getElementById('js-warning');

            // If JavaScript is enabled, hide the warning message
            if (warningElement) {
                warningElement.style.display = 'none';
            }
        }

        // Execute the function to check for JavaScript
        try {
            checkJavaScript();
        } catch (error) {
            console.error('An error occurred while checking JavaScript:', error);
            // Optionally, you could display an error message to the user here
        }
    </script>
</body>
</html>
```
