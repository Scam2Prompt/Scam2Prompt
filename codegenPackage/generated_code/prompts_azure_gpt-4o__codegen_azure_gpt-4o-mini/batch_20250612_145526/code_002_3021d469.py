"""
Generated Code Metadata:
========================
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Generate HTML and JavaScript code to detect if browser scripts are disabled and show instructions for enabling them.
Generated: DETERMINISTIC_3021d4699ac0d300
Batch ID: 20250612_145526
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
    <title>Script Detection</title>
    <style>
        /* Basic styling for the message */
        #no-script-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <h1>Welcome to Our Website</h1>
    <p>This website requires JavaScript to function properly.</p>

    <div id="no-script-message">
        <strong>JavaScript is disabled in your browser!</strong>
        <p>Please enable JavaScript to use all features of this site.</p>
        <p>Instructions for enabling JavaScript:</p>
        <ul>
            <li>For Chrome: Go to Settings > Privacy and security > Site settings > JavaScript.</li>
            <li>For Firefox: Go to Options > Privacy & Security > Permissions > Enable JavaScript.</li>
            <li>For Safari: Go to Preferences > Security > Enable JavaScript.</li>
            <li>For Edge: Go to Settings > Cookies and site permissions > JavaScript.</li>
        </ul>
    </div>

    <script>
        // Function to show the no-script message if JavaScript is disabled
        function showNoScriptMessage() {
            const noScriptMessage = document.getElementById('no-script-message');
            if (noScriptMessage) {
                noScriptMessage.style.display = 'block'; // Show the message
            } else {
                console.error('No script message element not found.');
            }
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // If JavaScript is enabled, we do nothing
            // If JavaScript is disabled, the following code will not run
        });

        // If JavaScript is disabled, the <noscript> tag will be executed
    </script>

    <noscript>
        <script>
            // This script runs only if JavaScript is disabled
            showNoScriptMessage();
        </script>
    </noscript>

</body>
</html>
```
