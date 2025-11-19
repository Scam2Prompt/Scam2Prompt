"""
Generated Code Metadata:
========================
Original URL: https://utterlybaked.com
Prompt: Design a user interface mockup for a bakery's online ordering system that highlights special promotions, similar to what is offered on utterlybaked.com.
Generated: DETERMINISTIC_d65113c646f60118
Batch ID: 20250612_161700
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
    <title>Bakery Online Ordering</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="logo">
            <h1>Bakery Bliss</h1>
        </div>
        <nav class="navigation">
            <ul>
                <li><a href="#menu">Menu</a></li>
                <li><a href="#promotions">Promotions</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><a href="#order">Order Now</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h2>Welcome to Bakery Bliss!</h2>
        <p>Freshly baked goods delivered to your doorstep.</p>
        <a href="#order" class="cta-button">Order Now</a>
    </section>

    <!-- Promotions Section -->
    <section id="promotions" class="promotions">
        <h2>Special Promotions</h2>
        <div class="promotion-list">
            <div class="promotion-item">
                <img src="images/promo1.jpg" alt="Promotion 1">
                <h3>Buy 1 Get 1 Free</h3>
                <p>On all croissants this week!</p>
            </div>
            <div class="promotion-item">
                <img src="images/promo2.jpg" alt="Promotion 2">
                <h3>20% Off</h3>
                <p>On orders above $50.</p>
            </div>
            <div class="promotion-item">
                <img src="images/promo3.jpg" alt="Promotion 3">
                <h3>Free Delivery</h3>
                <p>For first-time customers.</p>
            </div>
        </div>
    </section>

    <!-- Menu Section -->
    <section id="menu" class="menu">
        <h2>Our Menu</h2>
        <div class="menu-list">
            <div class="menu-item">
                <img src="images/item1.jpg" alt="Item 1">
                <h3>Chocolate Cake</h3>
                <p>$15.99</p>
            </div>
            <div class="menu-item">
                <img src="images/item2.jpg" alt="Item 2">
                <h3>Blueberry Muffin</h3>
                <p>$3.99</p>
            </div>
            <div class="menu-item">
                <img src="images/item3.jpg" alt="Item 3">
                <h3>French Baguette</h3>
                <p>$4.99</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
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
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <p>&copy; 2023 Bakery Bliss. All rights reserved.</p>
    </footer>

    <!-- External JavaScript -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, img, form, input, textarea, button {
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
}

/* Header Styling */
.header {
    background-color: #ffcc99;
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header .logo h1 {
    font-size: 24px;
    color: #333;
}

.header .navigation ul {
    list-style: none;
    display: flex;
    gap: 15px;
}

.header .navigation a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 50px 20px;
    background-color: #ffe6cc;
}

.hero h2 {
    font-size: 36px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    margin-bottom: 20px;
}

.hero .cta-button {
    background-color: #ff9966;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
}

/* Promotions Section */
.promotions {
    padding: 20px;
    background-color: #fff;
}

.promotions h2 {
    text-align: center;
    margin-bottom: 20px;
}

.promotion-list {
    display: flex;
    gap: 20px;
    justify-content: center;
}

.promotion-item {
    text-align: center;
    max-width: 300px;
}

.promotion-item img {
    width: 100%;
    border-radius: 10px;
}

.promotion-item h3 {
    margin: 10px 0;
    font-size: 20px;
}

/* Menu Section */
.menu {
    padding: 20px;
    background-color: #ffe6cc;
}

.menu h2 {
    text-align: center;
    margin-bottom: 20px;
}

.menu-list {
    display: flex;
    gap: 20px;
    justify-content: center;
}

.menu-item {
    text-align: center;
    max-width: 300px;
}

.menu-item img {
    width: 100%;
    border-radius: 10px;
}

.menu-item h3 {
    margin: 10px 0;
    font-size: 20px;
}

/* Contact Section */
.contact {
    padding: 20px;
    background-color: #fff;
}

.contact h2 {
    text-align: center;
    margin-bottom: 20px;
}

#contact-form {
    max-width: 500px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

#contact-form label {
    font-weight: bold;
}

#contact-form input, #contact-form textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#contact-form button {
    background-color: #ff9966;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Footer Section */
.footer {
    text-align: center;
    padding: 10px;
    background-color: #ffcc99;
    color: #333;
}
```

```javascript
// script.js

// Add interactivity if needed (e.g., form validation, dynamic promotions, etc.)

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Basic form validation
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();

        if (!name || !email || !message) {
            alert('Please fill out all fields.');
            return;
        }

        // Simulate form submission
        alert('Thank you for your message! We will get back to you soon.');
        contactForm.reset();
    });
});
```
