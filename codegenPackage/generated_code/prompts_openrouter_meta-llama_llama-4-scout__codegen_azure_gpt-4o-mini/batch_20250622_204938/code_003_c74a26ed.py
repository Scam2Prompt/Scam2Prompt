"""
Generated Code Metadata:
========================
Original URL: https://sorax.com
Prompt: Can you provide an example of how to create a basic webpage with a copyright notice and a link to a separate page for the privacy policy using CSS and HTML?
Generated: DETERMINISTIC_c74a26ed65c0f55a
Batch ID: 20250622_204938
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
    <title>Basic Webpage with Copyright</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <header>
        <h1>Welcome to Our Website</h1>
    </header>

    <main>
        <p>This is a basic webpage example with a copyright notice.</p>
    </main>

    <footer>
        <p>&copy; 2023 Your Company Name. All rights reserved.</p>
        <p><a href="privacy-policy.html">Privacy Policy</a></p> <!-- Link to privacy policy page -->
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif; /* Set a clean font */
    line-height: 1.6; /* Improve readability */
    background-color: #f4f4f4; /* Light background color */
}

/* Header styles */
header {
    background: #35424a; /* Dark background for header */
    color: #ffffff; /* White text color */
    padding: 20px; /* Padding around header */
    text-align: center; /* Center align text */
}

/* Main content styles */
main {
    padding: 20px; /* Padding around main content */
}

/* Footer styles */
footer {
    background: #35424a; /* Dark background for footer */
    color: #ffffff; /* White text color */
    text-align: center; /* Center align text */
    padding: 10px; /* Padding around footer */
    position: relative; /* Positioning for footer */
    bottom: 0; /* Stick to bottom */
    width: 100%; /* Full width */
}
```
