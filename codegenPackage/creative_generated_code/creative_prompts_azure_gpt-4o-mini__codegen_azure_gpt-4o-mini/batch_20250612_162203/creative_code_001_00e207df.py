"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aubi.online
Prompt: Write a JavaScript code snippet that checks if JavaScript is enabled on a webpage.
Generated: DETERMINISTIC_00e207df71b3d23b
Batch ID: 20250612_162203
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Styles for the message display */
        #js-enabled-message, #js-disabled-message {
            display: none; /* Initially hide both messages */
            font-size: 1.2em;
            margin: 20px;
        }
    </style>
</head>
<body>

    <div id="js-enabled-message">JavaScript is enabled on your browser!</div>
    <div id="js-disabled-message">JavaScript is disabled on your browser. Please enable it for better experience.</div>

    <noscript>
        <style>
            /* Show message if JavaScript is disabled */
            #js-disabled-message {
                display: block;
                color: red; /* Alerting color for disabled message */
            }
        </style>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            try {
                // Attempt to display the message indicating JavaScript is enabled
                document.getElementById('js-enabled-message').style.display = 'block';
            } catch (error) {
                // Log the error to the console if any unexpected issue arises
                console.error('An error occurred while checking JavaScript:', error);
            }
        }

        // Invoking the function to check if JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
    
</body>
</html>
```
