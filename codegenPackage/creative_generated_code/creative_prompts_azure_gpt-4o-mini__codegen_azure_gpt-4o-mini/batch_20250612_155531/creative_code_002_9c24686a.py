"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-explorer.skavel.cz
Prompt: Can you provide code snippets to check if JavaScript is enabled in a web browser for using Sonic Explorer?
Generated: DETERMINISTIC_9c24686ac80594a8
Batch ID: 20250612_155531
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
    <title>Sonic Explorer - JavaScript Check</title>
    <style>
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
        }
        /* Style for the message displayed when JavaScript is enabled */
        .js-message {
            display: none; /* Hide by default */
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to use Sonic Explorer.
        </div>
    </noscript>
    
    <div class="js-message">
        JavaScript is enabled. Welcome to Sonic Explorer!
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // If this script executes, JavaScript is enabled
                document.querySelector('.js-message').style.display = 'block'; // Show message
            } catch (error) {
                // Log the error for debugging purposes
                console.error('Error displaying JavaScript enabled message:', error);
            }
        }

        // Call the function to check JavaScript status
        checkJavaScript();
    </script>
</body>
</html>
```
