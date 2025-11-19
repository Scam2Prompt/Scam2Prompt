"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsclayer.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a browser for BSC Layer?
Generated: DETERMINISTIC_1d1d5b6144766973
Batch ID: 20250612_163541
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
        /* Basic styling */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .js-disabled {
            display: none; /* Hide this message if JS is enabled */
        }
        .js-enabled {
            display: none; /* Hide this message initially */
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Message displayed if JavaScript is disabled -->
        <div class="js-disabled">
            <h1>JavaScript is Disabled</h1>
            <p>Please enable JavaScript in your browser to access full functionality.</p>
        </div>
    </noscript>

    <div class="js-enabled">
        <!-- Message displayed if JavaScript is enabled -->
        <h1>JavaScript is Enabled</h1>
        <p>Thank you for enabling JavaScript. Enjoy the features!</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Display the message for enabled JavaScript
                document.querySelector('.js-enabled').style.display = 'block';
            } catch (error) {
                console.error('Error displaying JavaScript enabled message:', error);
                // Fallback for error handling
                alert('An error occurred while checking JavaScript status.');
            }
        }

        // Run the check as soon as the script is loaded
        checkJavaScript();
    </script>
</body>
</html>
```
