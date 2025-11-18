"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applestorebali.com
Prompt: Create an HTML and CSS template for an e-commerce shop page that mimics the layout of the Apple Market Bali website, including sections for featured products and payment options.
Generated: DETERMINISTIC_ee90c8dab0ca2d1d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Shop Page</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <div class="logo">E-Shop</div>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="featured-products">
            <h2>Featured Products</h2>
            <div class="product-list">
                <div class="product-item">
                    <img src="product1.jpg" alt="Product 1">
                    <h3>Product 1</h3>
                    <p>$99.99</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-item">
                    <img src="product2.jpg" alt="Product 2">
                    <h3>Product 2</h3>
                    <p>$149.99</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-item">
                    <img src="product3.jpg" alt="Product 3">
                    <h3>Product 3</h3>
                    <p>$199.99</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-item">
                    <img src="product4.jpg" alt="Product 4">
                    <h3>Product 4</h3>
                    <p>$249.99</p>
                    <button>Add to Cart</button>
                </div>
            </div>
        </section>

        <section class="payment-options">
            <h2>Payment Options</h2>
            <div class="payment-icons">
                <img src="visa.png" alt="Visa">
                <img src="mastercard.png" alt="MasterCard">
                <img src="paypal.png" alt="PayPal">
                <img src="applepay.png" alt="Apple Pay">
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 E-Shop. All rights reserved.</p>
    </footer>
</body>

</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h2, h3, p {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background for the page */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

header .logo {
    font-size: 1.5em;
}

/* Navigation styling */
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

/* Main section styling */
main {
    padding: 20px;
}

/* Featured products section styling */
.featured-products {
    margin-bottom: 30px;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.product-item {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    text-align: center;
    width: calc(25% - 20px); /* Four products in each row */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-item img {
    width: 100%;
    height: auto;
}

/* Payment options section styling */
.payment-options {
    text-align: center;
}

.payment-icons img {
    width: 50px;
    margin: 0 10px;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 20px 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
