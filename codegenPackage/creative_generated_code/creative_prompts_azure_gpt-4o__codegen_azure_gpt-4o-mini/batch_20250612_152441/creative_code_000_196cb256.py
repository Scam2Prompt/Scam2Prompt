"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.dexodoor.com
Prompt: Write JavaScript code to detect if a user's browser has JavaScript disabled and display a warning message similar to the one on the Dexodoor Webmail login page.
Generated: DETERMINISTIC_196cb256f8c85020
Batch ID: 20250612_152441
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
        .js-warning {
            display: none; /* Hide by default */
            background-color: #ffcc00; /* Light yellow background */
            color: #333; /* Dark text color */
            padding: 15px; /* Padding around the message */
            border: 1px solid #cc9900; /* Darker border color */
            margin: 20px; /* Margin around the message */
            font-family: Arial, sans-serif; /* Font style */
        }
    </style>
</head>
<body>

    <div class="js-warning" id="js-warning">
        Warning: Your browser has JavaScript disabled. Please enable JavaScript to use this website.
    </div>

    <script>
        // Function to display the warning message if JavaScript is disabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            if (warningElement) {
                warningElement.style.display = 'block'; // Show the warning message
            }
        }

        // Execute the showWarning function on page load
        document.addEventListener('DOMContentLoaded', () => {
            showWarning(); // This will only be reached if JavaScript is enabled
        });

        // If JavaScript is enabled, remove the warning message
        document.getElementById('js-warning').style.display = 'none'; // Hide warning by default
    </script>

    <!--
    The following noscript tag will display content if JavaScript is disabled
    -->
    <noscript>
        <style>
            /* Ensure the warning message is shown if JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
