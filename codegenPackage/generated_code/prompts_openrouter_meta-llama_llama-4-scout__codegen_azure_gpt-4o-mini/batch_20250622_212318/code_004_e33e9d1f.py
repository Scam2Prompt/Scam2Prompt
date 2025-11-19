"""
Generated Code Metadata:
========================
Original URL: https://cafelc.com
Prompt: Develop a simple HTML and CSS template for a product page on an e-commerce website, inspired by the design of cafelc.com.
Generated: DETERMINISTIC_e33e9d1fef91aebf
Batch ID: 20250622_212318
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
    <title>Product Page - E-commerce</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Product Name</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#products">Products</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="product-details">
            <div class="product-image">
                <img src="product-image.jpg" alt="Product Image" />
            </div>
            <div class="product-info">
                <h2>Product Title</h2>
                <p class="price">$99.99</p>
                <p class="description">This is a brief description of the product. It highlights the key features and benefits.</p>
                <button class="add-to-cart">Add to Cart</button>
            </div>
        </section>

        <section class="related-products">
            <h3>Related Products</h3>
            <div class="product-list">
                <div class="product-item">
                    <img src="related-product1.jpg" alt="Related Product 1" />
                    <h4>Related Product 1</h4>
                    <p class="price">$79.99</p>
                </div>
                <div class="product-item">
                    <img src="related-product2.jpg" alt="Related Product 2" />
                    <h4>Related Product 2</h4>
                    <p class="price">$89.99</p>
                </div>
                <div class="product-item">
                    <img src="related-product3.jpg" alt="Related Product 3" />
                    <h4>Related Product 3</h4>
                    <p class="price">$69.99</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 E-commerce Website. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, h4, p {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
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

/* Main product details section */
.product-details {
    display: flex;
    justify-content: space-around;
    padding: 20px;
    background: #fff;
    margin: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Product image styling */
.product-image img {
    max-width: 100%;
    border-radius: 8px;
}

/* Product info styling */
.product-info {
    max-width: 400px;
}

.price {
    font-size: 1.5em;
    color: #e67e22;
}

.add-to-cart {
    background: #e67e22;
    color: #fff;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

/* Related products section */
.related-products {
    margin: 20px;
}

.product-list {
    display: flex;
    justify-content: space-around;
}

.product-item {
    background: #fff;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.product-item img {
    max-width: 100%;
    border-radius: 5px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
