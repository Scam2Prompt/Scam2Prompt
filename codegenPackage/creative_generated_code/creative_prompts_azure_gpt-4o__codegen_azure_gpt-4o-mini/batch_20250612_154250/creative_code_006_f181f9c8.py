"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greendotinstallerportaluat.crm.com
Prompt: Create JavaScript code to display a warning message if JavaScript is disabled, as seen in the GreenDot Installer Portal.
Generated: DETERMINISTIC_f181f9c8ecc67e73
Batch ID: 20250612_154250
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
    <title>JavaScript Warning</title>
    <style>
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Red border */
            padding: 15px; /* Padding around the text */
            margin: 20px; /* Margin around the warning box */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <!-- Warning message container -->
    <div id="js-warning">
        <strong>Warning!</strong> JavaScript is disabled in your browser. Please enable JavaScript to use this application.
    </div>

    <script>
        // Function to display the warning message if JavaScript is disabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'block'; // Show the warning message
        }

        // Immediately invoked function to check if JavaScript is enabled
        (function() {
            try {
                // If this function runs, JavaScript is enabled
                console.log('JavaScript is enabled.');
            } catch (error) {
                // If an error occurs, log it and show the warning
                console.error('An error occurred:', error);
                showWarning(); // Show warning if there's an error
            }
        })();
    </script>

    <noscript>
        <!-- Fallback content for browsers with JavaScript disabled -->
        <style>
            /* Ensure the warning is shown if JavaScript is disabled */
            #js-warning {
                display: block;
            }
        </style>
    </noscript>

</body>
</html>
```
