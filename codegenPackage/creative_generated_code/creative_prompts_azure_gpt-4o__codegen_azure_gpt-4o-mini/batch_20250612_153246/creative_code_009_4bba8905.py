"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Generate HTML and CSS code for a product page showcasing customized photo frames with detailed descriptions and "Add to Cart" functionality, inspired by Gvika's layout.
Generated: DETERMINISTIC_4bba89054c7d52e8
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
    <title>Customized Photo Frames</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Customized Photo Frames</h1>
        <nav>
            <ul>
                <li><a href="#frames">Frames</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main id="frames">
        <section class="product">
            <img src="frame1.jpg" alt="Elegant Wooden Frame" class="product-image">
            <div class="product-details">
                <h2>Elegant Wooden Frame</h2>
                <p class="description">A beautifully crafted wooden frame, perfect for displaying your cherished memories.</p>
                <p class="price">$49.99</p>
                <button class="add-to-cart" onclick="addToCart('Elegant Wooden Frame', 49.99)">Add to Cart</button>
            </div>
        </section>
        
        <section class="product">
            <img src="frame2.jpg" alt="Modern Acrylic Frame" class="product-image">
            <div class="product-details">
                <h2>Modern Acrylic Frame</h2>
                <p class="description">A sleek and stylish acrylic frame to enhance the look of your favorite photos.</p>
                <p class="price">$39.99</p>
                <button class="add-to-cart" onclick="addToCart('Modern Acrylic Frame', 39.99)">Add to Cart</button>
            </div>
        </section>
        
        <section class="product">
            <img src="frame3.jpg" alt="Vintage Metal Frame" class="product-image">
            <div class="product-details">
                <h2>Vintage Metal Frame</h2>
                <p class="description">A charming vintage metal frame that adds a touch of nostalgia to any room.</p>
                <p class="price">$59.99</p>
                <button class="add-to-cart" onclick="addToCart('Vintage Metal Frame', 59.99)">Add to Cart</button>
            </div>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 Customized Photo Frames. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic Reset */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Body Style */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header Style */
header {
    background: #35424a;
    color: #ffffff;
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
    color: #ffffff;
    text-decoration: none;
}

/* Main Product Section */
main {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 20px;
}

.product {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin: 15px;
    padding: 15px;
    width: 300px;
}

.product-image {
    width: 100%;
    border-radius: 8px;
}

.product-details {
    text-align: center;
}

.price {
    font-weight: bold;
    color: #e67e22;
}

.add-to-cart {
    background: #e67e22;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    padding: 10px;
    cursor: pointer;
}

/* Footer Style */
footer {
    text-align: center;
    padding: 20px;
    background: #35424a;
    color: #ffffff;
}
```

```javascript
// script.js

/**
 * Function to handle adding products to the cart
 * @param {string} productName - Name of the product to be added
 * @param {number} productPrice - Price of the product
 */
function addToCart(productName, productPrice) {
    // Simulate adding to cart logic
    try {
        // In a real application, you would integrate with a shopping cart system here
        console.log(`Added to cart: ${productName} - $${productPrice}`);
        alert(`${productName} has been added to your cart!`);
    } catch (error) {
        console.error("Error adding product to cart:", error);
        alert("There was an error adding the product to the cart.");
    }
}
```
