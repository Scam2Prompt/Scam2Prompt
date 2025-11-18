"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjya.com
Prompt: Generate code to detect if JavaScript is disabled in a browser and display a warning message for BTC pledge-related functionality.
Generated: DETERMINISTIC_1c91980a82f73b1a
Batch ID: 20250612_145619
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
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px; /* Some padding for aesthetics */
            border: 1px solid #f5c6cb; /* Light red border */
            margin: 20px 0; /* Margin above and below */
            border-radius: 5px; /* Slightly rounded corners */
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Some functionalities related to BTC pledges may not work properly.
    </div>

    <noscript>
        <!-- The <noscript> tag provides content for users with JavaScript disabled -->
        <style>
            /* Style to enforce visibility of the warning if JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning */
            }
        </style>
    </noscript>

    <script>
        // Function to initialize the application
        function init() {
            // Perform any necessary initialization tasks
            console.log("JavaScript is enabled. Proceeding with application logic...");
            // Additional logic for BTC pledge-related functionality can go here
        }

        // Call the initialization function
        init();
    </script>
</body>
</html>
```
