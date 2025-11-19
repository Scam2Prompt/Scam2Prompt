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
    <meta name="description" content="Terms of Service and Privacy Policy page for our website.">
    <title>Terms of Service & Privacy Policy</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="#terms">Terms of Service</a></li>
                <li><a href="#privacy">Privacy Policy</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- Terms of Service Section -->
        <section id="terms">
            <h1>Terms of Service</h1>
            <p>Welcome to our website. By accessing or using our services, you agree to be bound by the following terms and conditions:</p>
            <ul>
                <li>Users must comply with all applicable laws and regulations.</li>
                <li>Unauthorized use of the website is prohibited.</li>
                <li>We reserve the right to modify these terms at any time.</li>
            </ul>
        </section>

        <!-- Privacy Policy Section -->
        <section id="privacy">
            <h1>Privacy Policy</h1>
            <p>Your privacy is important to us. This policy explains how we collect, use, and protect your information:</p>
            <ul>
                <li>We collect personal information only when necessary.</li>
                <li>Your data will not be shared with third parties without your consent.</li>
                <li>We use cookies to improve your experience on our website.</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Your Company Name. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, p, ul, li {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
    padding: 0 20px;
}

/* Header Styling */
header {
    background-color: #4CAF50;
    padding: 10px 20px;
    color: white;
}

.nav-links {
    list-style: none;
    display: flex;
    justify-content: space-around;
}

.nav-links li a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

.nav-links li a:hover {
    text-decoration: underline;
}

/* Main Content Styling */
main {
    margin: 20px 0;
}

section {
    margin-bottom: 20px;
    padding: 20px;
    background: white;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-bottom: 10px;
    color: #4CAF50;
}

ul {
    list-style: disc;
    margin-left: 20px;
}

/* Footer Styling */
footer {
    text-align: center;
    padding: 10px 0;
    background-color: #4CAF50;
    color: white;
    margin-top: 20px;
}
```

```javascript
// script.js

// Ensure the DOM is fully loaded before running scripts
document.addEventListener("DOMContentLoaded", () => {
    // Example: Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault(); // Prevent default anchor behavior

            const targetId = link.getAttribute("href").substring(1); // Get the target section ID
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                // Smooth scroll to the target section
                targetSection.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
```
