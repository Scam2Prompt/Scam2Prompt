"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Generate a JavaScript snippet to detect if JavaScript is enabled in the browser, inspired by Tim Mansell's website functionality.
Generated: DETERMINISTIC_58a3a1e20d07a620
Batch ID: 20250612_151018
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
        /* Styles for the message display */
        #js-enabled {
            display: none; /* Hidden by default */
            color: green;
            font-weight: bold;
        }
        #js-disabled {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="js-enabled">JavaScript is enabled in your browser.</div>
    <div id="js-disabled">JavaScript is disabled in your browser. Please enable it for the best experience.</div>

    <script>
        // Function to display messages based on JavaScript availability
        function checkJavaScript() {
            try {
                // If this script runs, it means JavaScript is enabled
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                // Log the error for debugging purposes
                console.error('Error while checking JavaScript:', error);
                // Display the disabled message in case of an error
                document.getElementById('js-disabled').style.display = 'block';
            }
        }

        // Execute the function to check for JavaScript
        checkJavaScript();
    </script>

    <!-- The <noscript> tag will display if JavaScript is disabled -->
    <noscript>
        <style>
            /* Styles for the no-script display */
            #js-enabled {
                display: none; /* Hide JavaScript enabled message */
            }
        </style>
        <div id="js-disabled">JavaScript is disabled in your browser. Please enable it for the best experience.</div>
    </noscript>
</body>
</html>
```
