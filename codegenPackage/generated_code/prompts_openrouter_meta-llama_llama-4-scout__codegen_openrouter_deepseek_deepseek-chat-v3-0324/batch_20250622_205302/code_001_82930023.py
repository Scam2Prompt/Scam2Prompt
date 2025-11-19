"""
Generated Code Metadata:
========================
Original URL: https://gala.red
Prompt: Generate a basic HTML page that displays a copyright notice for a given year and website, similar to what is seen on gala.red.
Generated: DETERMINISTIC_8293002315fc6a3b
Batch ID: 20250622_205302
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
    <title>Copyright Notice</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f5f5f5;
            color: #333;
        }
        .copyright-container {
            text-align: center;
            padding: 2rem;
            max-width: 800px;
        }
        .copyright-notice {
            font-size: 0.9rem;
            color: #666;
            margin-top: 1rem;
        }
        .website-name {
            font-weight: bold;
            color: #000;
        }
    </style>
</head>
<body>
    <div class="copyright-container">
        <div class="copyright-notice">
            &copy; <span id="copyright-year"></span> <span class="website-name" id="website-name"></span>. All rights reserved.
        </div>
    </div>

    <script>
        // Set current year and website name
        document.getElementById('copyright-year').textContent = new Date().getFullYear();
        document.getElementById('website-name').textContent = window.location.hostname || 'Our Website';
    </script>
</body>
</html>
```
