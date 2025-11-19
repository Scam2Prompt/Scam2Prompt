"""
Generated Code Metadata:
========================
Original URL: https://extenso-mayotte.fr
Prompt: Generate HTML and CSS code for a basic website template that displays a maintenance mode message, inspired by the design of extenso-mayotte.fr.
Generated: DETERMINISTIC_0813dc15dec9f78b
Batch ID: 20250622_205228
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="message">
            <h1>Maintenance Mode</h1>
            <p>We are currently performing scheduled maintenance. We will be back shortly.</p>
            <p>Thank you for your patience!</p>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Set the body to use a full viewport height */
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4; /* Light background color */
}

/* Container for the maintenance message */
.container {
    text-align: center;
    background-color: #ffffff; /* White background for the message box */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    padding: 20px; /* Padding around the text */
}

/* Styling for the main message heading */
.message h1 {
    color: #333; /* Dark text color */
    font-size: 2.5em; /* Larger font size for emphasis */
    margin-bottom: 10px; /* Space below the heading */
}

/* Styling for the paragraph text */
.message p {
    color: #666; /* Lighter text color for paragraphs */
    font-size: 1.2em; /* Slightly larger font size for readability */
    margin: 5px 0; /* Space between paragraphs */
}
```
