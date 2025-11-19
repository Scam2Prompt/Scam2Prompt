"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Design a simple e-commerce website using HTML and CSS to showcase and sell customized products like ecobags, canetas ecologicas, and squezzes personalizados."
Generated: DETERMINISTIC_a5e14c183dc22206
Batch ID: 20250622_210655
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
    <meta name="description" content="E-commerce website for customized eco-friendly products">
    <title>EcoShop - Customized Eco Products</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>EcoShop</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#products">Products</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container">
            <h2>Welcome to EcoShop</h2>
            <p>Your one-stop shop for customized eco-friendly products.</p>
            <a href="#products" class="btn">Shop Now</a>
        </div>
    </section>

    <!-- Products Section -->
    <section id="products" class="products">
        <div class="container">
            <h2>Our Products</h2>
            <div class="product-grid">
                <!-- Product 1 -->
                <div class="product-card">
                    <img src="images/ecobag.jpg" alt="Eco Bag">
                    <h3>Eco Bag</h3>
                    <p>Stylish and sustainable bags for everyday use.</p>
                    <button class="btn">Buy Now</button>
                </div>
                <!-- Product 2 -->
                <div class="product-card">
                    <img src="images/ecopen.jpg" alt="Eco Pen">
                    <h3>Eco Pen</h3>
                    <p>Eco-friendly pens made from recycled materials.</p>
                    <button class="btn">Buy Now</button>
                </div>
                <!-- Product 3 -->
                <div class="product-card">
                    <img src="images/squeeze.jpg" alt="Personalized Squeeze">
                    <h3>Personalized Squeeze</h3>
                    <p>Reusable bottles customized to your liking.</p>
                    <button class="btn">Buy Now</button>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>EcoShop is dedicated to providing eco-friendly, sustainable, and customizable products to help you reduce your environmental footprint.</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <form action="#" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
                <button type="submit" class="btn">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 EcoShop. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, img, button, input, textarea {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
header {
    background: #2c3e50;
    color: #fff;
    padding: 1rem 0;
}

header h1 {
    text-align: center;
    font-size: 2rem;
}

header nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
    margin-top: 0.5rem;
}

header nav ul li {
    margin: 0 1rem;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
    font-size: 1rem;
}

/* Hero Section */
.hero {
    background: #27ae60;
    color: #fff;
    text-align: center;
    padding: 2rem 0;
}

.hero h2 {
    font-size: 2.5rem;
}

.hero p {
    margin: 1rem 0;
}

.hero .btn {
    background: #fff;
    color: #27ae60;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
}

/* Products Section */
.products {
    padding: 2rem 0;
    background: #fff;
}

.products h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.product-grid {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.product-card {
    background: #f4f4f4;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    text-align: center;
    width: 300px;
}

.product-card img {
    max-width: 100%;
    border-radius: 5px;
}

.product-card h3 {
    margin: 0.5rem 0;
}

.product-card p {
    margin: 0.5rem 0;
}

.product-card .btn {
    background: #27ae60;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
}

/* About Section */
.about {
    padding: 2rem 0;
    background: #f4f4f4;
}

.about h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.about p {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

/* Contact Section */
.contact {
    padding: 2rem 0;
    background: #fff;
}

.contact h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.contact form {
    max-width: 600px;
    margin: 0 auto;
}

.contact form label {
    display: block;
    margin: 0.5rem 0 0.2rem;
}

.contact form input, .contact form textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.contact form .btn {
    background: #27ae60;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    display: block;
    width: 100%;
    text-align: center;
}

/* Footer */
footer {
    background: #2c3e50;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}

footer p {
    margin: 0;
}
```
