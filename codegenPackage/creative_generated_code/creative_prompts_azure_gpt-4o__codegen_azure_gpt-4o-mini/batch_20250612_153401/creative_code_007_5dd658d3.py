"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-drago.vercel.app
Prompt: Generate code for a JavaScript app that checks if the user has enabled JavaScript and displays content accordingly.
Generated: DETERMINISTIC_5dd658d3a4e5c752
Batch ID: 20250612_153401
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
    <title>JavaScript Check</title>
    <style>
        /* Basic styling for the messages */
        #js-enabled, #js-disabled {
            display: none; /* Initially hidden */
            font-size: 20px;
            margin: 20px;
            color: green;
        }
        #js-disabled {
            color: red;
        }
    </style>
</head>
<body>

    <!-- Message for when JavaScript is enabled -->
    <div id="js-enabled">JavaScript is enabled on your browser!</div>

    <!-- Message for when JavaScript is disabled -->
    <noscript>
        <div id="js-disabled">JavaScript is disabled in your browser. Please enable it to view the content.</div>
    </noscript>

    <script>
        // Function to display content if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Display the message for enabled JavaScript
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                // Log error if any issue occurs while accessing the DOM
                console.error('Error displaying JS enabled message:', error);
            }
        }

        // Call the function to check if JavaScript is enabled
        checkJavaScript();
    </script>

</body>
</html>
```
