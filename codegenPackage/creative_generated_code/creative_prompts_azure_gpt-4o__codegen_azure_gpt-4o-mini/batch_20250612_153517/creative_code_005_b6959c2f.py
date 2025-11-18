"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchlawinc.com
Prompt: Provide code for a product listing page that showcases DIY legal forms, including descriptions and pricing, modeled after Launch Law's offerings.
Generated: DETERMINISTIC_b6959c2f8cdd494a
Batch ID: 20250612_153517
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
    <title>DIY Legal Forms - Product Listing</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>DIY Legal Forms</h1>
        <nav>
            <ul>
                <li><a href="#forms">Forms</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="forms">
            <h2>Our Products</h2>
            <div class="product-list">
                <!-- Product Item Template -->
                <div class="product-item">
                    <h3>Basic Will</h3>
                    <p>A simple will template to help you outline your final wishes.</p>
                    <p class="price">$29.99</p>
                    <button onclick="addToCart('Basic Will', 29.99)">Add to Cart</button>
                </div>

                <div class="product-item">
                    <h3>Power of Attorney</h3>
                    <p>Document granting someone the authority to act on your behalf.</p>
                    <p class="price">$34.99</p>
                    <button onclick="addToCart('Power of Attorney', 34.99)">Add to Cart</button>
                </div>

                <div class="product-item">
                    <h3>Living Trust</h3>
                    <p>A legal document that places your assets into a trust for your benefit during your lifetime.</p>
                    <p class="price">$49.99</p>
                    <button onclick="addToCart('Living Trust', 49.99)">Add to Cart</button>
                </div>

                <div class="product-item">
                    <h3>Lease Agreement</h3>
                    <p>A comprehensive lease template for residential or commercial properties.</p>
                    <p class="price">$39.99</p>
                    <button onclick="addToCart('Lease Agreement', 39.99)">Add to Cart</button>
                </div>
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>We provide easy-to-use legal forms for individuals seeking to manage their own legal affairs.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>If you have any questions, please reach out to us at support@diylegalforms.com.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 DIY Legal Forms. All rights reserved.</p>
    </footer>

    <script>
        /**
         * Adds a product to the shopping cart.
         * @param {string} productName - The name of the product to add.
         * @param {number} productPrice - The price of the product.
         */
        function addToCart(productName, productPrice) {
            try {
                // Simulate adding to cart (in a real application, this would also involve backend communication)
                console.log(`${productName} has been added to your cart for $${productPrice.toFixed(2)}.`);
                alert(`${productName} has been added to your cart!`);
            } catch (error) {
                console.error('Error adding product to cart:', error);
                alert('An error occurred while adding the product to the cart. Please try again.');
            }
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
}

header {
    background-color: #333;
    color: white;
    padding: 15px 20px;
}

header h1 {
    margin: 0;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin-right: 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

main {
    padding: 20px;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.product-item {
    border: 1px solid #ddd;
    background-color: white;
    padding: 15px;
    border-radius: 5px;
    width: 200px;
    text-align: center;
}

.price {
    font-weight: bold;
    color: green;
}

footer {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
