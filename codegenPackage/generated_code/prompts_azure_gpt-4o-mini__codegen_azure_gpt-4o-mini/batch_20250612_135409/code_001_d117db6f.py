"""
Generated Code Metadata:
========================
Original URL: https://extenso-mayotte.fr
Prompt: How can I implement a temporary maintenance page using HTML and CSS?
Generated: DETERMINISTIC_d117db6faf3aa15e
Batch ID: 20250612_135409
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
    <title>Maintenance Mode</title>
    <style>
        /* Basic reset for body and html */
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f4f4f4;
            color: #333;
        }

        /* Container for the maintenance message */
        .maintenance-container {
            text-align: center;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        /* Heading style */
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        /* Paragraph style */
        p {
            font-size: 1.2em;
            margin: 0;
        }

        /* Optional: Style for a return link */
        .return-link {
            margin-top: 20px;
            display: inline-block;
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
        }

        .return-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="maintenance-container">
        <h1>We'll Be Back Soon!</h1>
        <p>Our website is currently undergoing scheduled maintenance.</p>
        <p>We appreciate your patience and understanding.</p>
        <a href="/" class="return-link">Return to Homepage</a>
    </div>
</body>
</html>
```
