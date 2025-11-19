"""
Generated Code Metadata:
========================
Original URL: https://fantom.de
Prompt: Generate a code snippet for a basic website structure that includes sections for services, contact information, and terms of use, similar to the Fantom Internet Dienst website.
Generated: DETERMINISTIC_0b13f2fd4d05e130
Batch ID: 20250622_205030
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
    <meta name="description" content="Basic website structure for services, contact information, and terms of use.">
    <title>Basic Website Structure</title>
    <link rel="stylesheet" href="styles.css"> <!-- External CSS file -->
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Welcome to Our Website</h1>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#contact">Contact</a></li>
                    <li><a href="#terms">Terms of Use</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Services Section -->
    <section id="services">
        <div class="container">
            <h2>Our Services</h2>
            <p>We offer a variety of services to meet your needs:</p>
            <ul>
                <li>Service 1: Description of service 1.</li>
                <li>Service 2: Description of service 2.</li>
                <li>Service 3: Description of service 3.</li>
            </ul>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <p>If you have any questions, feel free to reach out:</p>
            <form action="/submit-contact" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
                
                <button type="submit">Submit</button>
            </form>
        </div>
    </section>

    <!-- Terms of Use Section -->
    <section id="terms">
        <div class="container">
            <h2>Terms of Use</h2>
            <p>By using this website, you agree to the following terms:</p>
            <ol>
                <li>Term 1: Description of term 1.</li>
                <li>Term 2: Description of term 2.</li>
                <li>Term 3: Description of term 3.</li>
            </ol>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Your Company Name. All rights reserved.</p>
        </div>
    </footer>

    <!-- External JavaScript file -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header Styles */
header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
}

header h1 {
    text-align: center;
}

header nav ul {
    list-style: none;
    padding: 0;
    text-align: center;
}

header nav ul li {
    display: inline;
    margin: 0 10px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section Styles */
section {
    padding: 2rem 0;
}

section h2 {
    text-align: center;
    margin-bottom: 1rem;
}

section p, section ul, section ol {
    margin: 0 auto;
    width: 70%;
}

/* Footer Styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}

/* Form Styles */
form {
    width: 70%;
    margin: auto;
}

form label {
    display: block;
    margin: 0.5rem 0 0.2rem;
}

form input, form textarea, form button {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
}

form button {
    background: #333;
    color: #fff;
    border: none;
    cursor: pointer;
}

form button:hover {
    background: #555;
}
```

```javascript
// script.js

// Example JavaScript functionality (optional)
// Add smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
```
