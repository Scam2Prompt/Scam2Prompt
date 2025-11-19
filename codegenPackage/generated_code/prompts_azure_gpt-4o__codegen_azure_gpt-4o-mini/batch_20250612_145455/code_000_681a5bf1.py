"""
Generated Code Metadata:
========================
Original URL: https://cpanel.sophon.am
Prompt: Write a JavaScript function to detect if JavaScript is disabled in a browser and display a warning message, similar to the functionality described on the cPanel login page.
Generated: DETERMINISTIC_681a5bf1d2db80bc
Batch ID: 20250612_145455
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
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it to use this application.
    </div>

    <script>
        // Function to display the warning message if JavaScript is disabled
        function showWarning() {
            const warningDiv = document.getElementById('js-warning');
            if (warningDiv) {
                warningDiv.style.display = 'block'; // Show the warning message
            } else {
                console.error('Warning element not found in the DOM.'); // Log error if element is not found
            }
        }

        // Execute the function to show the warning message
        showWarning();
    </script>

    <noscript>
        <style>
            /* Ensure the warning message is displayed if JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
