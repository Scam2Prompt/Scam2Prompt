"""
Generated Code Metadata:
========================
Original URL: https://lingus.fun
Prompt: "Generate a basic webpage structure with a copyright notice and privacy policy link using HTML and CSS."
Generated: DETERMINISTIC_6e7721eec26d1011
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Webpage Structure</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main content area -->
    <main>
        <!-- Add main content here -->
        <h1>Welcome to our website</h1>
        <p>This is a basic webpage structure.</p>
    </main>
    
    <!-- Footer section -->
    <footer>
        <p>&copy; <?php echo date("Y"); ?> Our Company. All rights reserved.</p>
        <p><a href="privacy-policy.html">Privacy Policy</a></p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Main content area styles */
main {
    display: block;
    width: 80%;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Footer section styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
    clear: both;
}

footer a {
    color: #fff;
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}
```

**privacy-policy.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main>
        <h1>Privacy Policy</h1>
        <p>This is a sample privacy policy page.</p>
        <!-- Add privacy policy content here -->
    </main>
</body>
</html>
```
