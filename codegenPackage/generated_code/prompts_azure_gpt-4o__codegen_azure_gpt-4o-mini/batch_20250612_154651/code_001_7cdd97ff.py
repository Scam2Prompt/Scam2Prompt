"""
Generated Code Metadata:
========================
Original URL: https://webmail.ire-coinbase.com
Prompt: Create a script to check if a user is accessing a webpage using Internet Explorer 11 and display a message recommending an alternative browser, as mentioned in the cPanel Webmail login system.
Generated: DETERMINISTIC_7cdd97ff5bf0e7a8
Batch ID: 20250612_154651
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
        /* Basic styling for the warning message */
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
    You are using Internet Explorer 11. For a better experience, please consider using a modern browser such as Google Chrome, Mozilla Firefox, or Microsoft Edge.
</div>

<script>
    // Function to detect if the user is using Internet Explorer 11
    function isIE11() {
        // Check the user agent string for IE11
        return !!window.MSInputMethodContext && !!document.documentMode;
    }

    // Function to display the warning message if IE11 is detected
    function displayBrowserWarning() {
        if (isIE11()) {
            // Show the warning message
            document.getElementById('browser-warning').style.display = 'block';
        }
    }

    // Execute the browser check on page load
    window.onload = function() {
        try {
            displayBrowserWarning();
        } catch (error) {
            console.error('An error occurred while checking the browser:', error);
        }
    };
</script>

</body>
</html>
```
