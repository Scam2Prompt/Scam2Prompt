"""
Generated Code Metadata:
========================
Original URL: https://fronkweb.web.app
Prompt: Generate code for a web app that displays a custom error message when JavaScript is disabled, as seen in the FRONK web app.
Generated: DETERMINISTIC_3b2a39641db83687
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled Error</title>
    <style>
        /* Add some basic styling to make the error message more prominent */
        #js-disabled-error {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #FFC080;
            color: #666;
            text-align: center;
            padding: 1em;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript id="js-disabled-error">
        <h1>JavaScript is Disabled</h1>
        <p>Please enable JavaScript to use this web application.</p>
    </noscript>
    <script src="script.js" defer></script>
</body>
</html>
```

**script.js**
```javascript
// Check if JavaScript is enabled by trying to access the DOM
document.addEventListener('DOMContentLoaded', function () {
    // If we reach this point, JavaScript is enabled, so hide the error message
    const errorElement = document.getElementById('js-disabled-error');
    if (errorElement) {
        errorElement.style.display = 'none';
    }
});

// Catch and log any errors that occur during script execution
window.addEventListener('error', function (event) {
    console.error('Error occurred:', event.error);
});
```

**server.js** (optional, for development and testing purposes)
```javascript
const http = require('http');
const fs = require('fs');
const port = 3000;

http.createServer((req, res) => {
    if (req.url === '/') {
        fs.readFile('index.html', (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('Error loading index.html');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    } else if (req.url === '/script.js') {
        fs.readFile('script.js', (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('Error loading script.js');
            } else {
                res.writeHead(200, { 'Content-Type': 'application/javascript' });
                res.end(data);
            }
        });
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
}).listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
