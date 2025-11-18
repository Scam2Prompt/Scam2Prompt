"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mokent.com
Prompt: Generate code to detect and alert users when JavaScript is disabled on a trading platform like MOKENT Trading.
Generated: DETERMINISTIC_8a78e7ddb708bf1a
Batch ID: 20250612_154145
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
    <title>MOKENT Trading - JavaScript Detection</title>
    <style>
        /* Style for the alert message */
        #js-disabled-alert {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the text */
            position: fixed; /* Fixed position */
            top: 0; /* At the top */
            width: 100%; /* Full width */
            text-align: center; /* Centered text */
            z-index: 1000; /* On top of other content */
        }
    </style>
</head>
<body>
    <!-- Alert message for disabled JavaScript -->
    <div id="js-disabled-alert">
        JavaScript is disabled in your browser. Please enable JavaScript to use MOKENT Trading features.
    </div>
    
    <noscript>
        <style>
            /* Ensures the alert is visible if JavaScript is disabled */
            #js-disabled-alert {
                display: block; /* Show the alert */
            }
        </style>
    </noscript>
    
    <script>
        // This script runs when JavaScript is enabled
        
        // Function to show the alert when JavaScript is enabled
        function showAlert() {
            const alertDiv = document.getElementById('js-disabled-alert');
            if (alertDiv) {
                alertDiv.style.display = 'none'; // Ensure alert is hidden
            }
        }
        
        // Execute function on page load
        window.onload = function() {
            showAlert(); // Call the alert function
        };
    </script>
</body>
</html>
```
