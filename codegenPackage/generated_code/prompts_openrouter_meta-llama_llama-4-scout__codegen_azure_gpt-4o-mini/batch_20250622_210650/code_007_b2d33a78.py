"""
Generated Code Metadata:
========================
Original URL: https://samional.com
Prompt: "Generate code for a responsive web design that adapts to different screen sizes and devices, using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_b2d33a78decfff5d
Batch ID: 20250622_210650
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
    <title>Responsive Web Design</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Responsive Web Design Example</h1>
        <nav>
            <ul id="nav-list">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h2>Welcome to Our Website</h2>
            <p>This is a responsive web design example that adapts to different screen sizes.</p>
        </section>
        <section id="about">
            <h2>About Us</h2>
            <p>We are committed to providing the best service possible.</p>
        </section>
        <section id="services">
            <h2>Our Services</h2>
            <p>We offer a variety of services to meet your needs.</p>
        </section>
        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <button type="submit">Submit</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Responsive Web Design Example. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Set a base font size and family */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    padding: 0;
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
    margin: 20px 0;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem;
    background: #333;
    color: #fff;
}

/* Responsive styles */
@media (max-width: 600px) {
    nav ul li {
        display: block;
        margin: 10px 0;
    }
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    // Basic validation
    if (!name || !email) {
        alert('Please fill in all fields.');
        return;
    }

    // Simulate form submission (e.g., send data to a server)
    console.log('Form submitted:', { name, email });

    // Reset the form
    this.reset();
    alert('Thank you for your submission!');
});
```
