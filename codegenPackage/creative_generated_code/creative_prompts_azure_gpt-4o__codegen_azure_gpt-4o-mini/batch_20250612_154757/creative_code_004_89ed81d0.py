"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercufc.com
Prompt: Write code to detect if JavaScript is disabled in a browser and display a message prompting users to enable JavaScript for an Ethereum 2.0 application.
Generated: DETERMINISTIC_89ed81d0ac1185ab
Batch ID: 20250612_154757
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
        /* Styling for the message to prompt users */
        .js-disabled-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 20px;
            margin: 10px 0;
            border: 1px solid #f5c6cb; /* Red border */
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div class="js-disabled-message" id="js-disabled-message">
    <strong>JavaScript is disabled!</strong> Please enable JavaScript in your browser settings for the Ethereum 2.0 application to function properly.
</div>

<script>
    // This script runs when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", function() {
        // Hide the message if JavaScript is enabled
        const message = document.getElementById('js-disabled-message');
        message.style.display = 'none'; // Ensures the message is hidden
    });
</script>

<noscript>
    <!-- This block is displayed only if JavaScript is disabled -->
    <style>
        #js-disabled-message {
            display: block; /* Show the message */
        }
    </style>
</noscript>

</body>
</html>
```
