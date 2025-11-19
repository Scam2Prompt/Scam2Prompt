"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-05.vip
Prompt: How do I create a JavaScript function to detect and alert users if JavaScript is disabled on a webpage?
Generated: DETERMINISTIC_4b3710b07ff06656
Batch ID: 20250612_155705
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
        /* Style for the alert message */
        #js-disabled-alert {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the text */
            position: fixed; /* Fixed position */
            top: 0; /* At the top */
            width: 100%; /* Full width */
            z-index: 1000; /* Ensure it is on top */
        }
    </style>
</head>
<body>

    <div id="js-disabled-alert">
        JavaScript is disabled in your browser. Please enable it for optimal experience.
    </div>

    <script>
        // Function to detect if JavaScript is enabled
        function detectJavaScript() {
            // Select the alert element
            const alertElement = document.getElementById('js-disabled-alert');
            
            // Show alert if JavaScript is disabled
            if (!alertElement) {
                console.error("Alert element not found.");
                return;
            }
            alertElement.style.display = 'none'; // Hide the alert if JS is enabled
        }

        // Call the function to check JavaScript status
        detectJavaScript();
    </script>

    <noscript>
        <style>
            /* Show the alert message if JavaScript is disabled */
            #js-disabled-alert {
                display: block; /* Make it visible */
            }
        </style>
    </noscript>

</body>
</html>
```
