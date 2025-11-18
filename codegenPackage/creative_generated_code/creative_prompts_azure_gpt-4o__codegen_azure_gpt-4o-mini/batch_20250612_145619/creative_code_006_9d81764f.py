"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethltt.com
Prompt: Create a script to notify users to enable JavaScript before interacting with an Ethereum pledge system on a website.
Generated: DETERMINISTIC_9d81764fc27fbf0d
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
    <title>Ethereum Pledge System</title>
    <style>
        /* Style for the notification banner */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            border: 1px solid #f5c6cb; /* Border color */
            margin: 20px;
            border-radius: 5px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="js-warning">
        <strong>Warning:</strong> Please enable JavaScript to interact with the Ethereum pledge system.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // If JavaScript runs, hide the warning
            document.getElementById('js-warning').style.display = 'none';
        }

        // Function to show warning if JavaScript is disabled
        function showWarning() {
            // Show the warning message in case JavaScript is disabled
            document.getElementById('js-warning').style.display = 'block';
        }

        // Execute the check on page load
        window.onload = function() {
            try {
                // Call the check function to confirm JavaScript is running
                checkJavaScriptEnabled();
            } catch (error) {
                console.error("An error occurred while checking JavaScript status:", error);
                // Show warning if an error occurs (indicating JS might be disabled)
                showWarning();
            }
        };
    </script>
</body>
</html>
```
