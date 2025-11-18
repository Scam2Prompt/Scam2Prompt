"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mining1123.com
Prompt: Write a script to detect and alert users when JavaScript is disabled on a webpage powered by the "defi-h5" framework.
Generated: DETERMINISTIC_ee14ae464df3c9a6
Batch ID: 20250612_154111
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
        /* Style for the alert message when JavaScript is disabled */
        .js-disabled-alert {
            display: none; /* Hidden by default */
            padding: 10px;
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            text-align: center; /* Centered text */
            position: fixed; /* Fixed position */
            top: 0; /* Start from the top */
            left: 0;
            right: 0;
            z-index: 1000; /* Ensure it's above other content */
        }
    </style>
</head>
<body>

    <!-- Alert message for users with JavaScript disabled -->
    <div id="js-disabled-alert" class="js-disabled-alert">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to show the alert when JavaScript is disabled
        function showJavaScriptAlert() {
            const alertDiv = document.getElementById('js-disabled-alert');
            if (alertDiv) {
                alertDiv.style.display = 'block'; // Show the alert
            } else {
                console.error("Alert DOM element not found."); // Log error if element not found
            }
        }

        // Ensure the alert is hidden when the page loads with JavaScript enabled
        window.onload = function() {
            const alertDiv = document.getElementById('js-disabled-alert');
            if (alertDiv) {
                alertDiv.style.display = 'none'; // Hide the alert
            } else {
                console.error("Alert DOM element not found on load."); // Log error if element not found
            }
        };

        // Immediately invoke the function to confirm JavaScript is running
        showJavaScriptAlert();
    </script>

    <noscript>
        <!-- This block is executed when JavaScript is disabled -->
        <style>
            #js-disabled-alert {
                display: block; /* Show the alert when JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
