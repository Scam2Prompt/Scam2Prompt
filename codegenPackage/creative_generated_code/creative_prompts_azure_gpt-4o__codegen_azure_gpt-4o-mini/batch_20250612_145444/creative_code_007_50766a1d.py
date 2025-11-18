"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho-frontend.pages.dev
Prompt: Develop a JavaScript snippet to display a warning message if JavaScript is disabled in a Morpho-based app.
Generated: DETERMINISTIC_50766a1d11192944
Batch ID: 20250612_145444
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
    <title>Warning Message Example</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none; /* Hide by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 10px;
            margin: 20px 0;
            border-radius: 5px; /* Rounded corners for better appearance */
        }
    </style>
</head>
<body>

    <div class="warning" id="warningMessage">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the full functionality of this application.
    </div>

    <noscript>
        <style>
            /* Show warning message if JavaScript is disabled */
            #warningMessage {
                display: block;
            }
        </style>
    </noscript>

    <script>
        // Function to display warning message if JavaScript is disabled
        function displayWarning() {
            const warningDiv = document.getElementById('warningMessage');

            // Check if the warningDiv exists
            if (warningDiv) {
                warningDiv.style.display = 'block';  // Show the warning message
            } else {
                console.error('Warning message element not found!'); // Log error if warning element is missing
            }
        }

        // Call the function to display the warning message
        displayWarning();
    </script>

</body>
</html>
```
