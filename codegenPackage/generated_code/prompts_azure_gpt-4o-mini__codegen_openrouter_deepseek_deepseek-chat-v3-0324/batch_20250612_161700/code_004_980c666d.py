"""
Generated Code Metadata:
========================
Original URL: https://valentina-rossi.com
Prompt: How do I set up a temporary maintenance page using HTML and CSS?
Generated: DETERMINISTIC_980c666d9b2d3ed6
Batch ID: 20250612_161700
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
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        /* Maintenance container */
        .maintenance-container {
            max-width: 600px;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Header styles */
        h1 {
            color: #e74c3c;
            margin-bottom: 1rem;
            font-size: 2.5rem;
        }

        /* Content styles */
        p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }

        /* Animation for the spinner */
        .spinner {
            border: 5px solid #f3f3f3;
            border-top: 5px solid #e74c3c;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1.5rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .maintenance-container {
                margin: 0 1rem;
                padding: 1.5rem;
            }

            h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="maintenance-container">
        <div class="spinner"></div>
        <h1>Under Maintenance</h1>
        <p>We're currently performing scheduled maintenance. We'll be back online shortly.</p>
        <p>Thank you for your patience.</p>
        <p><small>Estimated downtime: 1 hour</small></p>
    </div>
</body>
</html>
```
