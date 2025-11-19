"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maximaseducao.fun
Prompt: What are the best practices for implementing a custom 404 error page in a web hosting environment?
Generated: DETERMINISTIC_1090f1c6d590fda9
Batch ID: 20250612_155952
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!-- Custom 404 Error Page: 404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f4f4f4;
        }
        h1 {
            font-size: 50px;
            color: #ff0000;
        }
        p {
            font-size: 20px;
        }
        a {
            text-decoration: none;
            color: #0066cc;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <p><a href="/">Go to Home Page</a></p>
</body>
</html>
```

```apache
# Apache Configuration: .htaccess

# Enable custom 404 error page
ErrorDocument 404 /404.html
```

```nginx
# Nginx Configuration: nginx.conf

server {
    # Other server configurations...

    # Set up custom error page for 404 errors
    error_page 404 /404.html;
    
    location = /404.html {
        internal; # Prevent direct access to the error page
    }
}
```

```javascript
// Optional JavaScript for tracking 404 error (analytics.js)

// Function to track 404 error
function track404Error() {
    // Perform tracking logic (e.g., sending data to analytics service)
    console.error('Page not found - 404 error tracked.');
}

// Call track404Error if the page is a 404
if (document.title === '404 Not Found') {
    track404Error();
}
```

```css
/* Optional CSS for additional styling: styles.css */

/* General styles for the error page (if using external CSS) */
body {
    background-color: #f9f9f9;
    color: #333;
}
```

```html
<!-- Include this in your main HTML file to link to the CSS -->
<link rel="stylesheet" href="styles.css">
``` 

```javascript
// Example of server-side handling (Node.js/Express)

const express = require('express');
const app = express();

// Middleware for serving static files
app.use(express.static('public'));

// Route for handling 404 errors
app.use((req, res, next) => {
    res.status(404).sendFile(__dirname + '/public/404.html');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

```json
{
    "name": "custom-404",
    "version": "1.0.0",
    "description": "A simple web app with a custom 404 error page",
    "main": "app.js",
    "scripts": {
        "start": "node app.js"
    },
    "dependencies": {
        "express": "^4.17.1"
    }
}
```
