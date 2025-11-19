"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Generate a terms of service and privacy policy page using HTML, CSS, and JavaScript, similar to Linear Live Limited's website.
Generated: DETERMINISTIC_4cdd58f1106ca399
Batch ID: 20250622_205158
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
    <title>Terms of Service & Privacy Policy</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Terms of Service & Privacy Policy</h1>
        <nav>
            <ul>
                <li><a href="#terms">Terms of Service</a></li>
                <li><a href="#privacy">Privacy Policy</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="terms">
            <h2>Terms of Service</h2>
            <p>Welcome to our Terms of Service. By using our services, you agree to the following terms...</p>
            <!-- Add more detailed terms here -->
        </section>

        <section id="privacy">
            <h2>Privacy Policy</h2>
            <p>Your privacy is important to us. This policy outlines how we collect, use, and protect your information...</p>
            <!-- Add more detailed privacy information here -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Linear Live Limited. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007bff;
    color: #fff;
    padding: 20px;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 20px;
    background: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background: #007bff;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to handle smooth scrolling to sections
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        // Check if the target element exists
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        } else {
            console.error(`Element with ID ${targetId} not found.`);
        }
    });
});
```

This code provides a basic structure for a Terms of Service and Privacy Policy page, including HTML for layout, CSS for styling, and JavaScript for smooth scrolling navigation.
