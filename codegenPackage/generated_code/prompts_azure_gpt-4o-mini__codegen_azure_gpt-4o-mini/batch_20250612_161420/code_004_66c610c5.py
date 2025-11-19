"""
Generated Code Metadata:
========================
Original URL: https://dulcedelarosa.com
Prompt: Write a code snippet in HTML and CSS that reflects user-centric design principles, similar to those applied by Dulce De La Rosa in her frontend development work at Devex.
Generated: DETERMINISTIC_66c610c57bc1abb0
Batch ID: 20250612_161420
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
    <title>User-Centric Design Example</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our User-Centric Design</h1>
        <nav>
            <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="features">
            <h2>Features</h2>
            <div class="feature-card">
                <h3>Intuitive Navigation</h3>
                <p>Our design ensures that users can easily find what they need.</p>
            </div>
            <div class="feature-card">
                <h3>Responsive Design</h3>
                <p>Our website adapts to any screen size for a seamless experience.</p>
            </div>
            <div class="feature-card">
                <h3>Accessibility</h3>
                <p>We prioritize accessibility to ensure everyone can use our site.</p>
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>We are committed to creating user-friendly experiences that cater to all users.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" action="#" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 User-Centric Design. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
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
    padding: 20px 0;
    text-align: center;
}

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

/* Main section styles */
main {
    padding: 20px;
}

/* Feature card styles */
.feature-card {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin: 10px 0;
}

/* Form styles */
form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

/* Button styles */
button {
    background: #007bff;
    color: #fff;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #007bff;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
