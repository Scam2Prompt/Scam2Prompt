"""
Generated Code Metadata:
========================
Original URL: https://haitwik.com
Prompt: Illustrate how to build a basic web page that showcases the phrase "I am haitwik" prominently, based on the content theme of haitwik.com.
Generated: DETERMINISTIC_f6cec6d286103197
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML file that showcases the phrase "I am haitwik" prominently:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I am haitwik</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        /* Main content container */
        .container {
            text-align: center;
            max-width: 800px;
            padding: 40px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        /* Main heading */
        h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            color: #2c3e50;
            font-weight: 700;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 2rem;
            }
            .container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>I am haitwik</h1>
    </div>
</body>
</html>
```
