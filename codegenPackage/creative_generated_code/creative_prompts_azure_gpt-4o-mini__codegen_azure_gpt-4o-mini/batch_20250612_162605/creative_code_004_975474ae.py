"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnetarnask-portfolio.com
Prompt: How can I configure my website to ensure it properly handles JavaScript requirements for users?
Generated: DETERMINISTIC_975474ae94378aa2
Batch ID: 20250612_162605
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
    <title>JavaScript Configuration</title>
    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            const jsEnabledElement = document.getElementById('js-enabled');
            const jsDisabledElement = document.getElementById('js-disabled');

            // If JavaScript is enabled, show the corresponding message
            if (jsEnabledElement && jsDisabledElement) {
                jsEnabledElement.style.display = 'block'; // Show JS enabled message
                jsDisabledElement.style.display = 'none'; // Hide JS disabled message
            }
        }

        // Call the function to check JavaScript status on page load
        window.onload = checkJavaScript;
    </script>
    <style>
        /* Simple styles to differentiate the messages */
        #js-enabled, #js-disabled {
            display: none; /* Hide both by default */
            padding: 10px;
            border: 1px solid #ccc;
            margin: 10px 0;
        }
        #js-enabled {
            background-color: #d4edda;
            color: #155724;
        }
        #js-disabled {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div id="js-disabled">
            JavaScript is disabled in your browser. Please enable it to experience the full functionality of this website.
        </div>
    </noscript>

    <!-- Message displayed when JavaScript is enabled -->
    <div id="js-enabled">
        JavaScript is enabled. Welcome to the full experience of our website!
    </div>

    <h1>Website Configuration for JavaScript</h1>
    <p>This website is configured to check for JavaScript support. Please ensure it is enabled for optimal performance.</p>
</body>
</html>
```
