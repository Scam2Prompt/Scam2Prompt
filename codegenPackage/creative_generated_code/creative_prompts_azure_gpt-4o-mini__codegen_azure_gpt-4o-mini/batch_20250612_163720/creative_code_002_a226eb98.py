"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo777-axe.pages.dev
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_163720
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
        JavaScript is enabled in your browser!
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Show the message indicating JavaScript is enabled
                document.querySelector('.js-enabled').style.display = 'block';
            } catch (error) {
                // Log any errors that occur while checking JavaScript
                console.error("An error occurred while checking JavaScript status: ", error);
            }
        }

        // Invoke the function to check JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```
