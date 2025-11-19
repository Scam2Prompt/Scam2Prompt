"""
Generated Code Metadata:
========================
Original URL: https://notio.ltd
Prompt: Generate a simple webpage content that includes a copyright notice and a link to a privacy policy, similar to notio.ltd.
Generated: DETERMINISTIC_4361ce726e643062
Batch ID: 20250622_204641
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
    <title>Simple Webpage</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to Our Website</h1>
    </header>

    <main>
        <p>This is a simple webpage demonstrating a copyright notice and a link to a privacy policy.</p>
    </main>

    <footer>
        <div class="footer-content">
            <!-- Copyright notice -->
            <p>&copy; <span id="current-year"></span> Your Company Name. All rights reserved.</p>
            <!-- Link to privacy policy -->
            <p><a href="privacy-policy.html" target="_blank" rel="noopener noreferrer">Privacy Policy</a></p>
        </div>
    </footer>

    <script>
        // Function to set the current year in the copyright notice
        function setCurrentYear() {
            const year = new Date().getFullYear();
            document.getElementById('current-year').textContent = year;
        }

        // Call the function to set the current year on page load
        window.onload = setCurrentYear;
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    padding: 20px;
}

/* Header styling */
header {
    background: #f4f4f4;
    padding: 10px 0;
    text-align: center;
}

/* Footer styling */
footer {
    margin-top: 20px;
    padding: 10px 0;
    text-align: center;
    background: #f4f4f4;
}

/* Link styling */
footer a {
    color: #007BFF;
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}
```
