"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethrtc.com
Prompt: Write a script to detect if JavaScript is disabled in a browser and display a warning for Ethereum-based applications.
Generated: DETERMINISTIC_05bdf6b20dc9fec7
Batch ID: 20250612_152600
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
    <title>Ethereum Application Warning</title>
    <style>
        /* Styles for the warning message */
        #warning {
            display: none; /* Initially hidden */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Darker red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 15px; /* Padding around the text */
            margin: 20px; /* Margin from other elements */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div id="warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable JavaScript to use this Ethereum-based application.
    </div>

    <script>
        // Function to show the warning message
        function showWarning() {
            const warningDiv = document.getElementById('warning');
            warningDiv.style.display = 'block'; // Make the warning visible
        }

        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // If this script runs, it means JavaScript is enabled
            return true; // JavaScript is enabled
        }

        // Run the check
        if (!checkJavaScriptEnabled()) {
            showWarning(); // Show warning if JavaScript is disabled
        }
    </script>

    <noscript>
        <style>
            /* Ensure warning is shown when JavaScript is disabled */
            #warning {
                display: block; /* Show the warning */
            }
        </style>
    </noscript>

</body>
</html>
```
