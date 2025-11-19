"""
Generated Code Metadata:
========================
Original URL: https://webmail.dexodoor.com
Prompt: Create a script that checks for Internet Explorer 11 usage and displays a message recommending users to switch browsers, as mentioned on the Dexodoor Webmail login page.
Generated: DETERMINISTIC_8385b55d999fa969
Batch ID: 20250612_152441
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
    <title>Browser Check</title>
    <style>
        #browser-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div id="browser-warning">
    <strong>Warning:</strong> You are using Internet Explorer 11. For a better experience, please switch to a modern browser such as Chrome, Firefox, or Edge.
</div>

<script>
    /**
     * Function to detect if the user is using Internet Explorer 11
     * @returns {boolean} - True if the browser is IE11, otherwise false
     */
    function isIE11() {
        return !!window.MSInputMethodContext && !!document.documentMode;
    }

    /**
     * Function to display a warning message if the user is on IE11
     */
    function checkBrowser() {
        try {
            if (isIE11()) {
                // Show the warning message
                document.getElementById('browser-warning').style.display = 'block';
            }
        } catch (error) {
            console.error('Error checking browser:', error);
        }
    }

    // Run the browser check on page load
    window.onload = checkBrowser;
</script>

</body>
</html>
```
