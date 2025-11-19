"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rectifydappfix.rf.gd
Prompt: Can you provide a code snippet that checks if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_208d526183894754
Batch ID: 20250612_155337
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Style for the message display */
        #js-enabled {
            display: none;
            font-size: 1.2em;
            color: green;
        }
        #js-disabled {
            font-size: 1.2em;
            color: red;
        }
    </style>
</head>
<body>

    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div id="js-disabled">JavaScript is disabled in your browser. Please enable it for the best experience.</div>
    </noscript>
    
    <div id="js-enabled">JavaScript is enabled in your browser.</div>

    <script>
        // Function to check if JavaScript is enabled and update the DOM accordingly
        function checkJavaScriptEnabled() {
            try {
                // Show the JavaScript enabled message
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                // Log an error message to the console if an error occurs
                console.error('An error occurred while checking JavaScript status: ', error);
            }
        }

        // Execute the check when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
    </script>
    
</body>
</html>
```
