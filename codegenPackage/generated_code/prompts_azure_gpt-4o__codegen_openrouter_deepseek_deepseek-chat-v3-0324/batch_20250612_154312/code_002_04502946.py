"""
Generated Code Metadata:
========================
Original URL: https://dogeai.eu
Prompt: Generate code for a basic web application that checks for JavaScript support and redirects users to an error page if JavaScript is disabled, inspired by the DogeAI website's functionality.
Generated: DETERMINISTIC_045029468ea5f114
Batch ID: 20250612_154312
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
    <title>JavaScript Check</title>
    <script>
        // Immediately check for JavaScript support
        (function() {
            // If JavaScript is enabled, remove the no-js class
            document.documentElement.className = document.documentElement.className.replace(/\bno-js\b/, 'js');
        })();
    </script>
    <noscript>
        <meta http-equiv="refresh" content="0; url=/no-js.html">
    </noscript>
    <style>
        /* Basic styling for the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }
        
        .container {
            text-align: center;
            padding: 2rem;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: #333;
        }
        
        /* Hide content if JavaScript is disabled */
        .no-js .js-content {
            display: none;
        }
    </style>
</head>
<body class="no-js">
    <div class="container js-content">
        <h1>Welcome to Our Website</h1>
        <p>JavaScript is enabled. Enjoy your experience!</p>
    </div>
</body>
</html>
```

```html
<!-- no-js.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Required</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }
        
        .container {
            text-align: center;
            padding: 2rem;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
        }
        
        h1 {
            color: #d9534f;
        }
        
        p {
            color: #333;
            line-height: 1.6;
        }
        
        .instructions {
            margin-top: 1.5rem;
            text-align: left;
            padding: 1rem;
            background-color: #f8f9fa;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>JavaScript is Required</h1>
        <p>Our website requires JavaScript to function properly. Please enable JavaScript in your browser settings to continue.</p>
        
        <div class="instructions">
            <p><strong>How to enable JavaScript:</strong></p>
            <ul>
                <li><strong>Chrome:</strong> Settings → Privacy and security → Site Settings → JavaScript → Allowed</li>
                <li><strong>Firefox:</strong> Options → Privacy & Security → Permissions → Enable JavaScript</li>
                <li><strong>Safari:</strong> Preferences → Security → Enable JavaScript</li>
                <li><strong>Edge:</strong> Settings → Cookies and site permissions → JavaScript → Allowed</li>
            </ul>
        </div>
        
        <p>After enabling JavaScript, please <a href="/">refresh this page</a>.</p>
    </div>
</body>
</html>
```
