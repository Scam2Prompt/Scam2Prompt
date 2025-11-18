"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btccetc.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a user's browser and display a message prompting them to enable it for accessing BTC Pledge services.
Generated: DETERMINISTIC_c3b1984c79475e40
Batch ID: 20250612_152600
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
    <title>BTC Pledge Services</title>
    <style>
        /* Basic styles for the message */
        #js-message {
            display: none; /* Hidden by default */
            background-color: #ffcccc;
            color: #a00;
            padding: 15px;
            border: 1px solid #a00;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div id="js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to access BTC Pledge services.
</div>

<script>
    // Function to check if JavaScript is enabled
    function checkJavaScriptEnabled() {
        // Select the message element
        const messageElement = document.getElementById('js-message');
        
        // Display the message indicating JavaScript is disabled
        messageElement.style.display = 'block';
    }

    // Execute the function to check JavaScript
    checkJavaScriptEnabled();
</script>

<!-- This script will run only if JavaScript is enabled -->
<script>
    // Function to hide the JS disabled message when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
        const messageElement = document.getElementById('js-message');
        
        // Check if the message element exists
        if (messageElement) {
            // Hide the message if JavaScript is enabled
            messageElement.style.display = 'none';
        }
    });
</script>

</body>
</html>
```
