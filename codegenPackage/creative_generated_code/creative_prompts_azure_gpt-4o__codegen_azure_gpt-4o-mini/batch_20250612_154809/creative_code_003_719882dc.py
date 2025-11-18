"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.co.za
Prompt: Write JavaScript code to display a warning message when JavaScript is disabled, styled using CSS, for a webpage like coinbase.co.za.
Generated: DETERMINISTIC_719882dc3584a025
Batch ID: 20250612_154809
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
        .js-warning {
            display: none; /* Hidden by default */
            position: fixed; /* Fixed position to stay on screen */
            top: 0; /* Align to the top */
            left: 0; /* Align to the left */
            width: 100%; /* Full width */
            padding: 20px; /* Padding around the text */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            text-align: center; /* Centered text */
            font-family: Arial, sans-serif; /* Font styling */
            z-index: 1000; /* High z-index to appear above other elements */
        }
    </style>
</head>
<body>
    <!-- Warning message to be displayed if JavaScript is disabled -->
    <noscript>
        <div class="js-warning">
            Warning: JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <script>
        // Function to display a warning message if JavaScript is disabled
        function displayWarning() {
            const warningMessage = document.querySelector('.js-warning');
            if (warningMessage) {
                warningMessage.style.display = 'block'; // Show the warning message
            }
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Call the function to display the warning message
            displayWarning();
        });
    </script>
</body>
</html>
```
