"""
Generated Code Metadata:
========================
Original URL: https://cpanel.arbitrium.adv.br
Prompt: Write a JavaScript function to detect if JavaScript is disabled and redirect users to an informational page explaining how to enable it for cPanel functionality.
Generated: DETERMINISTIC_82f22e3eab5339de
Batch ID: 20250612_145619
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
    <title>JavaScript Detection</title>
    <style>
        /* Basic styles for the informational page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
    </style>
    <noscript>
        <meta http-equiv="refresh" content="0; url=javascript-disabled.html">
    </noscript>
</head>
<body>
    <h1>Welcome to cPanel</h1>
    <p>If you see this message, JavaScript is enabled.</p>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Redirect to the informational page if JavaScript is disabled
            window.location.href = 'javascript-disabled.html';
        }

        // Execute the function to check JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```

```html
<!-- javascript-disabled.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled</title>
    <style>
        /* Basic styles for the informational page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
    </style>
</head>
<body>
    <h1>JavaScript is Disabled</h1>
    <p>It appears that JavaScript is disabled in your browser. To use cPanel functionality, please enable JavaScript.</p>
    <h2>How to Enable JavaScript:</h2>
    <ul>
        <li>For Chrome: Go to Settings > Privacy and security > Site settings > JavaScript and enable it.</li>
        <li>For Firefox: Go to Options > Privacy & Security > Permissions > Enable JavaScript.</li>
        <li>For Safari: Go to Preferences > Security > Enable JavaScript.</li>
        <li>For Edge: Go to Settings > Cookies and site permissions > JavaScript and enable it.</li>
    </ul>
    <p>After enabling JavaScript, please refresh the page.</p>
</body>
</html>
```
