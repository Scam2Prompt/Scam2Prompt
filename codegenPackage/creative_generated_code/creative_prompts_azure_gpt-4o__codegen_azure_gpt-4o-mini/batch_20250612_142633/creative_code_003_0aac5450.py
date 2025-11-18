"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://def0321.vip
Prompt: Write code to display an error message if JavaScript is disabled on a webpage, similar to the behavior of defi-h5.
Generated: DETERMINISTIC_0aac545044f3d77e
Batch ID: 20250612_142633
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
    <title>Error Handling for Disabled JavaScript</title>
    <style>
        /* Style for the error message */
        .js-disabled-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px; /* Spacing around the message */
            border: 1px solid #f5c6cb; /* Red border */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div class="js-disabled-message" id="error-message">
        <strong>Error:</strong> JavaScript is disabled in your browser. Please enable it to view this webpage properly.
    </div>

    <script>
        // This script runs if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function () {
            // Hide the error message if JavaScript is enabled
            var errorMessage = document.getElementById('error-message');
            errorMessage.style.display = 'none';
        });
    </script>

    <noscript>
        <!-- This message is displayed if JavaScript is disabled -->
        <style>
            #error-message {
                display: block; /* Show the error message */
            }
        </style>
    </noscript>

</body>
</html>
```
