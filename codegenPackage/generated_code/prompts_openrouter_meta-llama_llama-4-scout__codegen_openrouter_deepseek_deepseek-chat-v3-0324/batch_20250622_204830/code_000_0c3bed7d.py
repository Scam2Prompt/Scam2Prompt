"""
Generated Code Metadata:
========================
Original URL: https://duoiudf-dsdds-chy.pages.dev
Prompt: Write a simple webpage that displays a message asking users to enable JavaScript and cookies.
Generated: DETERMINISTIC_0c3bed7de81e3416
Batch ID: 20250622_204830
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
    <title>Enable JavaScript and Cookies</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        .message-box {
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
        }
        h1 {
            color: #d32f2f;
            margin-top: 0;
        }
        p {
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }
        .instructions {
            text-align: left;
            margin: 1.5rem 0;
            padding: 0;
        }
        li {
            margin-bottom: 0.5rem;
        }
    </style>
    <noscript>
        <meta http-equiv="refresh" content="0;url=/nojs">
    </noscript>
</head>
<body>
    <div class="message-box">
        <h1>JavaScript and Cookies Required</h1>
        <p>This website requires JavaScript and cookies to function properly.</p>
        
        <div class="instructions">
            <p>Please enable both in your browser settings:</p>
            <ul>
                <li><strong>JavaScript:</strong> Check your browser settings or extensions that might be blocking JavaScript</li>
                <li><strong>Cookies:</strong> Ensure cookies are enabled in your privacy settings</li>
            </ul>
        </div>
        
        <p>After enabling these features, please refresh this page.</p>
    </div>

    <script>
        // Check if cookies are enabled
        function areCookiesEnabled() {
            try {
                document.cookie = 'testcookie=1';
                return document.cookie.indexOf('testcookie=') !== -1;
            } catch (e) {
                return false;
            }
        }

        // Redirect if cookies are disabled
        if (!areCookiesEnabled()) {
            window.location.href = '/nocookies';
        }
    </script>
</body>
</html>
```
