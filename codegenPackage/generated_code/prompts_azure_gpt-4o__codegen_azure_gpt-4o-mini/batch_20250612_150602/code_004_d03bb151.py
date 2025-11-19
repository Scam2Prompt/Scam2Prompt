"""
Generated Code Metadata:
========================
Original URL: https://bonkbox-claim.web.app
Prompt: Write code to dynamically display a message on a webpage if JavaScript is disabled, inspired by the BONKBOXES whitelist page functionality.
Generated: DETERMINISTIC_d03bb151bf5a0031
Batch ID: 20250612_150602
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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Style for the warning message */
        .js-disabled-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px; /* Padding around the message */
            border: 1px solid #f5c6cb; /* Border color */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <!-- Warning message for users with JavaScript disabled -->
    <div id="js-warning" class="js-disabled-warning">
        JavaScript is disabled in your browser. Please enable it for the best experience on this website.
    </div>

    <script>
        // Function to display the warning message if JavaScript is enabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            if (warningElement) {
                warningElement.style.display = 'none'; // Hide the warning if JS is enabled
            }
        }

        // Call the function to hide the warning
        showWarning();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            /* Ensure the warning message is displayed when JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning */
            }
        </style>
        <div id="js-warning" class="js-disabled-warning">
            JavaScript is disabled in your browser. Please enable it for the best experience on this website.
        </div>
    </noscript>

</body>
</html>
```
