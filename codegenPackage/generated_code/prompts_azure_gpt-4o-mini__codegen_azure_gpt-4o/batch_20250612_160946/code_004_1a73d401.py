"""
Generated Code Metadata:
========================
Original URL: https://magpiexyz.click
Prompt: Provide an example of an HTML page that can be used as a default message for a web server when no website is hosted.
Generated: DETERMINISTIC_1a73d4017e689cdf
Batch ID: 20250612_160946
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
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Default Server Page</title>
    <style>
        /* Basic styling for the default page */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background-color: #fff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 10px;
        }

        p {
            font-size: 1rem;
            margin-bottom: 20px;
        }

        .footer {
            font-size: 0.9rem;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Main message displayed to the user -->
        <h1>Welcome to the Server</h1>
        <p>No website is currently hosted at this address.</p>
        <p>If you are the administrator, please upload your website files to the server.</p>
        <!-- Footer information -->
        <div class="footer">
            <p>&copy; <span id="year"></span> Your Server Name. All rights reserved.</p>
        </div>
    </div>

    <script>
        // Dynamically set the current year in the footer
        document.getElementById('year').textContent = new Date().getFullYear();
    </script>
</body>
</html>
```
