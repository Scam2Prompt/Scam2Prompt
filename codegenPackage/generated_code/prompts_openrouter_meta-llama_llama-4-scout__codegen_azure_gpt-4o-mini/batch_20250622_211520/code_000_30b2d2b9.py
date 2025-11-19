"""
Generated Code Metadata:
========================
Original URL: https://wallmemes.com
Prompt: Design an e-commerce website homepage using HTML, CSS, and JavaScript that showcases various products with images, prices, and discounts, similar to wallmemes.com.
Generated: DETERMINISTIC_30b2d2b939bd5ac2
Batch ID: 20250622_211520
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
    <title>E-Commerce Homepage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our E-Commerce Store</h1>
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
            <h2>Featured Products</h2>
            <div class="product-grid">
                <!-- Product Item -->
                <div class="product-item">
                    <img src="product1.jpg" alt="Product 1">
                    <h3>Product 1</h3>
                    <p class="price">$19.99 <span class="discount">20% off</span></p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
                <!-- Product Item -->
                <div class="product-item">
                    <img src="product2.jpg" alt="Product 2">
                    <h3>Product 2</h3>
                    <p class="price">$29.99 <span class="discount">10% off</span></p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
                <!-- Product Item -->
                <div class="product-item">
                    <img src="product3.jpg" alt="Product 3">
                    <h3>Product 3</h3>
                    <p class="price">$39.99 <span class="discount">15% off</span></p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
                <!-- Product Item -->
                <div class="product-item">
                    <img src="product4.jpg" alt="Product 4">
                    <h3>Product 4</h3>
                    <p class="price">$49.99 <span class="discount">5% off</span></p>
                    <button class="add-to-cart">Add to Cart</button>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 E-Commerce Store. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
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
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
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

/* Product grid styles */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
}

/* Product item styles */
.product-item {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
    text-align: center;
}

.product-item img {
    max-width: 100%;
    height: auto;
}

.price {
    font-size: 1.2em;
    color: #333;
}

.discount {
    color: red;
    font-weight: bold;
}

/* Button styles */
.add-to-cart {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
}

.add-to-cart:hover {
    background: #218838;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to handle adding products to the cart
function addToCart(event) {
    const productName = event.target.parentElement.querySelector('h3').innerText;
    alert(`${productName} has been added to your cart!`);
}

// Attach event listeners to all "Add to Cart" buttons
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', addToCart);
});
```

This code provides a simple e-commerce homepage layout with a header, product grid, and footer. Each product has an image, name, price, discount, and an "Add to Cart" button that triggers a JavaScript alert when clicked. The CSS styles ensure a clean and responsive design.
