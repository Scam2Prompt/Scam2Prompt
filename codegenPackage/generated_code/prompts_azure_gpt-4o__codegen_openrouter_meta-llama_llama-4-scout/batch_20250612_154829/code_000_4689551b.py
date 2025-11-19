"""
Generated Code Metadata:
========================
Original URL: https://as.magiceden.eu
Prompt: Write code to detect if JavaScript is disabled in a user's browser and display a custom message prompting them to enable it.
Generated: DETERMINISTIC_4689551b0f3bb70f
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// No JavaScript code is needed for detection, 
// but we will use it to dynamically update the page.
// Detection is done via <noscript> tag in HTML.

```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <style>
        /* Add some basic styling to make the message more readable */
        #js-disabled-message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #f44336;
            color: #ffffff;
            padding: 1em;
            text-align: center;
            z-index: 1000;
        }
    </style>
</head>
<body>

<noscript>
    <div id="js-disabled-message">
        <h2>JavaScript is Disabled</h2>
        <p>Please enable JavaScript in your browser to use this website.</p>
    </div>
</noscript>

<script>
// If JavaScript is enabled, dynamically remove the message
document.addEventListener('DOMContentLoaded', function() {
    const jsDisabledMessage = document.getElementById('js-disabled-message');
    if (jsDisabledMessage) {
        jsDisabledMessage.style.display = 'none';
    }
});
</script>

</body>
</html>
```
