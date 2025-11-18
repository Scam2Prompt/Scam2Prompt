"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lrt-sym.biotic.fi
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "This app doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_6dad29d76354783c
Batch ID: 20250612_152006
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
        /* Style for the message that appears when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 20px; /* Padding for aesthetics */
            text-align: center; /* Center the text */
            font-family: Arial, sans-serif; /* Font styling */
            position: fixed; /* Fixed position on the screen */
            top: 0; /* Align to the top */
            left: 0; /* Align to the left */
            right: 0; /* Align to the right */
            z-index: 1000; /* Ensure it is above other content */
        }
    </style>
</head>
<body>

    <!-- Message for users with JavaScript disabled -->
    <div class="no-js-message" id="js-disabled-message">
        This app doesn't work properly without JavaScript enabled.
    </div>

    <script>
        // This script will run if JavaScript is enabled
        // Hide the no-JS message if JavaScript is active
        document.addEventListener('DOMContentLoaded', function() {
            const messageElement = document.getElementById('js-disabled-message');
            if (messageElement) {
                messageElement.style.display = 'none'; // Hide the message
            }
        });
    </script>

    <noscript>
        <!-- The <noscript> tag is used to display content when JavaScript is disabled -->
        <style>
            #js-disabled-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
