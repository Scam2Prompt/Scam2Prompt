"""
Generated Code Metadata:
========================
Original URL: https://crystal.free.nf
Prompt: What libraries or tools can help detect JavaScript support on a webpage?
Generated: DETERMINISTIC_c7300cf0dce30d92
Batch ID: 20250612_163950
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Support Detection</title>
    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptSupport() {
            // Create a div element to test JavaScript functionality
            const testDiv = document.createElement('div');
            testDiv.id = 'js-support-test';
            testDiv.innerHTML = 'JavaScript is enabled!';
            document.body.appendChild(testDiv);
        }

        // Function to handle the case when JavaScript is not supported
        function handleNoJavaScript() {
            const noJsMessage = document.createElement('noscript');
            noJsMessage.innerHTML = '<style>body { background-color: #f8d7da; }</style>' +
                                    '<div style="color: red; font-weight: bold;">' +
                                    'JavaScript is not supported or is disabled in your browser.' +
                                    '</div>';
            document.body.appendChild(noJsMessage);
        }

        // Execute the check for JavaScript support
        window.onload = function() {
            try {
                checkJavaScriptSupport();
            } catch (error) {
                console.error('Error checking JavaScript support:', error);
                handleNoJavaScript();
            }
        };
    </script>
</head>
<body>
    <h1>JavaScript Support Detection</h1>
    <p>If you see the message below, JavaScript is enabled.</p>
    <div id="js-support-message"></div>
</body>
</html>
```
