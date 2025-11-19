"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-metamesklogin.uteach.io
Prompt: Develop a simple HTML page that displays a user-friendly 404 error message, including options to contact support or return home, based on the Uteach example.
Generated: DETERMINISTIC_097096e665953fda
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <style>
        body {
            font-family: Arial, sans-serif; /* Use a clean sans-serif font */
            background-color: #f4f4f4; /* Light grey background */
            margin: 0; /* Remove default margin */
            padding: 0; /* Remove default padding */
            display: flex; /* Flexbox for centering content */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            height: 100vh; /* Full viewport height */
            text-align: center; /* Center text */
        }

        .container {
            background-color: #fff; /* White background for content */
            border-radius: 8px; /* Rounded corners */
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
            padding: 20px; /* Padding around the content */
            max-width: 400px; /* Maximum width for content */
        }

        h1 {
            color: #e74c3c; /* Red color for error message */
            font-size: 48px; /* Large font size for the header */
        }

        p {
            color: #333; /* Darker color for the paragraph */
            font-size: 16px; /* Standard font size */
        }

        a {
            display: inline-block; /* Make links block-level */
            margin: 10px 0; /* Margin around links */
            text-decoration: none; /* Remove underline */
            color: #3498db; /* Blue color for links */
            font-weight: bold; /* Bold weight for links */
        }

        a:hover {
            text-decoration: underline; /* Underline on hover */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1> <!-- Main error code -->
        <p>Oops! The page you are looking for does not exist.</p> <!-- Error message -->
        <p>
            <a href="/" title="Return to homepage">Return Home</a> <!-- Link to homepage -->
        </p>
        <p>
            <a href="mailto:support@example.com" title="Contact support">Contact Support</a> <!-- Link to support email -->
        </p>
    </div>
</body>
</html>
```
