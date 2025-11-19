"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.si
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser for the Blur.si domain?
Generated: DETERMINISTIC_516baff47d933ff0
Batch ID: 20250612_135637
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
        /* Basic styles for the message display */
        #js-message {
            display: none;
            font-size: 18px;
            color: green;
        }
        #no-js-message {
            display: none;
            font-size: 18px;
            color: red;
        }
    </style>
</head>
<body>
    <div id="js-message">JavaScript is enabled!</div>
    <div id="no-js-message">JavaScript is disabled. Please enable it for the best experience on Blur.si.</div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Display the JavaScript enabled message
            document.getElementById('js-message').style.display = 'block';
        }

        // Execute on page load
        window.onload = function() {
            try {
                // If this function runs, JavaScript is enabled
                checkJavaScript();
            } catch (error) {
                // Log the error in case of failure
                console.error('An error occurred while checking JavaScript status:', error);
            }
        };
    </script>

    <!-- Noscript tag to handle the case when JavaScript is disabled -->
    <noscript>
        <style>
            #no-js-message {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
