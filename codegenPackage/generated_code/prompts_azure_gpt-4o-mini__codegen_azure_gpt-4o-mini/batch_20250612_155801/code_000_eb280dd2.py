"""
Generated Code Metadata:
========================
Original URL: https://phainton.com
Prompt: Generate code to display a welcome message on a newly created website using HTML and CSS.
Generated: DETERMINISTIC_eb280dd2cc78d55e
Batch ID: 20250612_155801
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
    <title>Welcome Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
    <style>
        /* Basic reset for margin and padding */
        body, h1 {
            margin: 0;
            padding: 0;
        }

        /* Styling for the body */
        body {
            font-family: Arial, sans-serif; /* Set a clean font */
            background-color: #f0f8ff; /* Light background color */
            display: flex; /* Use flexbox for centering */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            height: 100vh; /* Full viewport height */
        }

        /* Styling for the welcome message */
        .welcome-message {
            background-color: #ffffff; /* White background for the message */
            border: 2px solid #007bff; /* Blue border */
            border-radius: 10px; /* Rounded corners */
            padding: 20px; /* Padding inside the box */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
            text-align: center; /* Center text */
        }

        /* Styling for the heading */
        h1 {
            color: #007bff; /* Blue text color */
            font-size: 2.5em; /* Large font size */
        }
    </style>
</head>
<body>
    <div class="welcome-message">
        <h1>Welcome to Our Website!</h1> <!-- Welcome message -->
        <p>We are glad to have you here. Enjoy your stay!</p> <!-- Additional message -->
    </div>
</body>
</html>
```
