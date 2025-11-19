"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autorectifytoken.rf.gd
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_162658
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
        /* Styles for the message indicating JavaScript is disabled */
        .js-disabled {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
        }
        
        .js-enabled {
            display: none; /* Hide by default */
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div class="js-disabled">
            JavaScript is disabled in your browser. Please enable it for a better experience.
        </div>
    </noscript>
    
    <div class="js-enabled">
        JavaScript is enabled in your browser. Enjoy your visit!
    </div>

    <script>
        // Function to show the appropriate message based on JavaScript status
        function detectJavaScript() {
            try {
                // If this script runs, JavaScript is enabled
                document.querySelector('.js-enabled').style.display = 'block';
            } catch (error) {
                // Log the error to the console for debugging
                console.error('Error detecting JavaScript support:', error);
            }
        }

        // Call the function to detect JavaScript
        detectJavaScript();
    </script>
</body>
</html>
```
