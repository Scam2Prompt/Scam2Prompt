"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Create a script that checks for JavaScript support and redirects users to an alternative page if JavaScript is disabled, inspired by the Step App's functionality.
Generated: DETERMINISTIC_b22c7d393d61436a
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Support Check</title>
    <style>
        /* Add some basic styling to make the page look decent */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        
        #noscript {
            display: none;
        }
    </style>
</head>
<body>
    <noscript id="noscript">
        <h1>JavaScript is disabled</h1>
        <p>You will be redirected to an alternative page.</p>
    </noscript>

    <script>
        // Check if JavaScript is enabled
        const jsEnabled = () => {
            // If this script runs, JavaScript is enabled
            return true;
        };

        // Redirect to alternative page if JavaScript is disabled
        const redirectToAlternativePage = () => {
            const alternativePageUrl = 'alternative.html'; // Replace with your alternative page URL
            window.location.href = alternativePageUrl;
        };

        // Check if noscript element is still hidden
        const checkNoscriptElement = () => {
            const noscriptElement = document.getElementById('noscript');
            if (noscriptElement.style.display !== 'none') {
                // If noscript element is visible, JavaScript is disabled
                redirectToAlternativePage();
            }
        };

        // Run checks when document loads
        document.addEventListener('DOMContentLoaded', () => {
            if (!jsEnabled()) {
                redirectToAlternativePage();
            } else {
                checkNoscriptElement();
            }
        });
    </script>
</body>
</html>
```

```html
<!-- alternative.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alternative Page</title>
</head>
<body>
    <h1>Welcome to the alternative page</h1>
    <p>You have been redirected here because JavaScript is disabled in your browser.</p>
</body>
</html>
```

```javascript
// Using Node.js for a simple HTTP server to serve the pages
// Install required packages: npm install http
const http = require('http');
const fs = require('fs');
const port = 3000;

http.createServer((req, res) => {
    try {
        const url = req.url;
        let file;

        if (url === '/') {
            file = 'index.html';
        } else if (url === '/alternative.html') {
            file = 'alternative.html';
        } else {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('404 Not Found\n');
            return;
        }

        fs.readFile(file, (err, data) => {
            if (err) {
                throw err;
            }

            res.writeHead(200, { 'Content-Type': getContentType(file) });
            res.end(data);
        });
    } catch (error) {
        console.error(error);
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error\n');
    }
}).listen(port, () => {
    console.log(`Server running on port ${port}`);
});

function getContentType(file) {
    switch (file) {
        case 'index.html':
        case 'alternative.html':
            return 'text/html';
        default:
            return 'text/plain';
    }
}
```
