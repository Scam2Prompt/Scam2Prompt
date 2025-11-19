"""
Generated Code Metadata:
========================
Original URL: https://jardinesdeprovenza.com.gt
Prompt: Create a product catalog using HTML and CSS for a store selling lavender-based personal care products, similar to those offered by Jardines de Provenza.
Generated: DETERMINISTIC_c2751d0b6ffe97e5
Batch ID: 20250622_205709
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
    <title>Lavender Personal Care Products</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Lavender Bliss</h1>
        <nav>
            <ul>
                <li><a href="#products">Products</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="products">
            <h2>Our Products</h2>
            <div class="product-catalog">
                <article class="product">
                    <img src="lavender-oil.jpg" alt="Lavender Essential Oil">
                    <h3>Lavender Essential Oil</h3>
                    <p>Pure lavender essential oil for relaxation and aromatherapy.</p>
                    <span class="price">$19.99</span>
                    <button class="add-to-cart">Add to Cart</button>
                </article>
                <article class="product">
                    <img src="lavender-soap.jpg" alt="Lavender Soap">
                    <h3>Lavender Soap</h3>
                    <p>Handmade lavender soap for a soothing bath experience.</p>
                    <span class="price">$7.99</span>
                    <button class="add-to-cart">Add to Cart</button>
                </article>
                <article class="product">
                    <img src="lavender-lotion.jpg" alt="Lavender Body Lotion">
                    <h3>Lavender Body Lotion</h3>
                    <p>Moisturizing body lotion infused with lavender extract.</p>
                    <span class="price">$15.99</span>
                    <button class="add-to-cart">Add to Cart</button>
                </article>
                <article class="product">
                    <img src="lavender-candle.jpg" alt="Lavender Candle">
                    <h3>Lavender Candle</h3>
                    <p>Hand-poured lavender candle for a calming ambiance.</p>
                    <span class="price">$12.99</span>
                    <button class="add-to-cart">Add to Cart</button>
                </article>
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>At Lavender Bliss, we believe in the power of nature. Our products are crafted with care, using the finest lavender sourced from the fields of Provence. Experience the soothing benefits of lavender in your daily routine.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" action="#" method="post">
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
        <p>&copy; 2023 Lavender Bliss. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
}

/* Header styles */
header {
    background-color: #6a5acd; /* Lavender color */
    color: white;
    padding: 20px;
    text-align: center;
}

nav ul {
    list-style-type: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: white;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

.product-catalog {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.product {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    background-color: white;
    width: calc(25% - 20px); /* Four products per row */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product img {
    max-width: 100%;
    border-radius: 5px;
}

.price {
    font-weight: bold;
    color: #6a5acd; /* Lavender color */
}

.add-to-cart {
    background-color: #6a5acd; /* Lavender color */
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

.add-to-cart:hover {
    background-color: #5a4db1; /* Darker lavender */
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background-color: #6a5acd; /* Lavender color */
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
