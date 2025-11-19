"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: Generate a code snippet for a custom website design that enhances user engagement based on the services offered by DigiStrategy.
Generated: DETERMINISTIC_40b7f2203249073d
Batch ID: 20250612_162051
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
    <meta name="description" content="DigiStrategy - Enhance your digital presence with our tailored services.">
    <title>DigiStrategy - Digital Solutions</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="logo">DigiStrategy</h1>
            <nav class="navigation">
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Transform Your Digital Presence</h2>
            <p>We provide cutting-edge strategies to help your business thrive in the digital world.</p>
            <a href="#services" class="cta-button">Explore Services</a>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service-list">
                <div class="service-item">
                    <h3>SEO Optimization</h3>
                    <p>Boost your website's visibility and attract more organic traffic.</p>
                </div>
                <div class="service-item">
                    <h3>Social Media Marketing</h3>
                    <p>Engage with your audience and grow your brand on social platforms.</p>
                </div>
                <div class="service-item">
                    <h3>Web Development</h3>
                    <p>Create stunning, responsive websites tailored to your needs.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>DigiStrategy is a team of passionate digital experts dedicated to helping businesses succeed online.</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 DigiStrategy. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, input, textarea, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Header Styling */
.header {
    background: #0073e6;
    color: #fff;
    padding: 1rem 0;
}

.header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header .logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.header .navigation ul {
    list-style: none;
    display: flex;
}

.header .navigation ul li {
    margin: 0 1rem;
}

.header .navigation ul li a {
    color: #fff;
    text-decoration: none;
}

/* Hero Section */
.hero {
    background: #f4f4f4;
    text-align: center;
    padding: 2rem 0;
}

.hero h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.hero .cta-button {
    display: inline-block;
    background: #0073e6;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
}

/* Services Section */
.services {
    padding: 2rem 0;
    background: #fff;
}

.services .service-list {
    display: flex;
    justify-content: space-around;
}

.services .service-item {
    max-width: 30%;
    text-align: center;
}

/* About Section */
.about {
    padding: 2rem 0;
    background: #f4f4f4;
    text-align: center;
}

/* Contact Section */
.contact {
    padding: 2rem 0;
    background: #fff;
}

.contact form {
    max-width: 600px;
    margin: 0 auto;
}

.contact form label {
    display: block;
    margin-bottom: 0.5rem;
}

.contact form input, .contact form textarea {
    width: 100%;
    margin-bottom: 1rem;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.contact form button {
    background: #0073e6;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Footer Section */
.footer {
    background: #0073e6;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```

```javascript
// script.js

// Add event listener for form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation
    if (!name || !email || !message) {
        alert('Please fill out all fields.');
        return;
    }

    // Simulate form submission (replace with actual API call in production)
    alert(`Thank you, ${name}! Your message has been sent.`);
    this.reset(); // Reset the form
});
```
