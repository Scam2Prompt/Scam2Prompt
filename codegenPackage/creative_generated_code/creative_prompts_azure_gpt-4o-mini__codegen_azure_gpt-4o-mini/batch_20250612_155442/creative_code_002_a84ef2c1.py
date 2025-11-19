"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.sophon.am
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser for cPanel compatibility?
Generated: DETERMINISTIC_a84ef2c195a19f86
Batch ID: 20250612_155442
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
        /* Styles for the message display */
        #js-enabled {
            display: none; /* Hide by default */
            color: green;
            font-weight: bold;
        }
        #js-disabled {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Message to be shown if JavaScript is enabled -->
    <div id="js-enabled">JavaScript is enabled in your browser.</div>
    
    <!-- Message to be shown if JavaScript is disabled -->
    <noscript>
        <div id="js-disabled">JavaScript is disabled in your browser. Please enable it for full functionality.</div>
    </noscript>

    <script>
        // Immediately Invoked Function Expression (IIFE) to check JavaScript status
        (function() {
            try {
                // Display the message if JavaScript is enabled
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                // Log any errors to the console
                console.error('Error displaying JavaScript enabled message:', error);
            }
        })();
    </script>
</body>
</html>
```
