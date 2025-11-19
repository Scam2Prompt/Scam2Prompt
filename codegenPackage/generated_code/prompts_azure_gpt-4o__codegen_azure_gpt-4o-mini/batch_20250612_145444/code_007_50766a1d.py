"""
Generated Code Metadata:
========================
Original URL: https://morpho-frontend.pages.dev
Prompt: Develop a JavaScript snippet to display a warning message if JavaScript is disabled in a Morpho-based app.
Generated: DETERMINISTIC_50766a1d11192944
Batch ID: 20250612_145444
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
    <title>JavaScript Warning</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Light red border */
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="warningMessage" class="warning">
        Warning: JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to display the warning message
        function displayWarning() {
            const warningElement = document.getElementById('warningMessage');
            if (warningElement) {
                warningElement.style.display = 'block'; // Show the warning message
            } else {
                console.error('Warning element not found in the DOM.'); // Log error if element is not found
            }
        }

        // Check if JavaScript is enabled
        window.onload = function() {
            // If JavaScript is enabled, hide the warning message
            const warningElement = document.getElementById('warningMessage');
            if (warningElement) {
                warningElement.style.display = 'none'; // Hide the warning message
            } else {
                console.error('Warning element not found in the DOM.'); // Log error if element is not found
            }
        };
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            #warningMessage {
                display: block; /* Show the warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
