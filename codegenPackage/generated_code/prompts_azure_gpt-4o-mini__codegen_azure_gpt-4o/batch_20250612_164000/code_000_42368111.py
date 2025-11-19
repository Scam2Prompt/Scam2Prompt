"""
Generated Code Metadata:
========================
Original URL: https://hnu.co.id
Prompt: Generate a code snippet to create an e-commerce product page for herbal supplements similar to those offered by Habbasyi Niaga Utama, focusing on Habbatussauda and its health benefits.
Generated: DETERMINISTIC_42368111f533e57f
Batch ID: 20250612_164000
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
    <meta name="description" content="Discover the health benefits of Habbatussauda herbal supplements. Shop high-quality products for your wellness journey.">
    <title>Habbatussauda Herbal Supplements</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Habbatussauda Herbal Supplements</h1>
            <p>Empowering your health with nature's best remedies.</p>
        </div>
    </header>

    <!-- Product Section -->
    <main>
        <div class="container">
            <section class="product">
                <h2>Habbatussauda Capsules</h2>
                <img src="habbatussauda.jpg" alt="Habbatussauda Capsules" class="product-image">
                <p>
                    Habbatussauda, also known as black seed, is renowned for its numerous health benefits, including boosting immunity, improving digestion, and supporting overall wellness.
                </p>
                <ul>
                    <li>100% natural and organic</li>
                    <li>Rich in antioxidants</li>
                    <li>Supports immune system health</li>
                    <li>Promotes healthy skin and hair</li>
                </ul>
                <p class="price">$19.99</p>
                <button class="btn-add-to-cart">Add to Cart</button>
            </section>
        </div>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Habbasyi Niaga Utama. All rights reserved.</p>
            <nav>
                <ul>
                    <li><a href="#privacy-policy">Privacy Policy</a></li>
                    <li><a href="#terms-of-service">Terms of Service</a></li>
                    <li><a href="#contact-us">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </footer>

    <!-- External JavaScript -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
    color: #333;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
header {
    background-color: #4CAF50;
    color: white;
    padding: 20px 0;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 2.5em;
}

header p {
    margin: 10px 0 0;
    font-size: 1.2em;
}

/* Product Section */
.product {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
}

.product-image {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

.product h2 {
    font-size: 2em;
    margin: 10px 0;
}

.product p {
    font-size: 1em;
    margin: 10px 0;
}

.product ul {
    list-style-type: none;
    padding: 0;
    margin: 10px 0;
}

.product ul li {
    margin: 5px 0;
}

.price {
    font-size: 1.5em;
    color: #4CAF50;
    margin: 10px 0;
}

.btn-add-to-cart {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    border-radius: 5px;
}

.btn-add-to-cart:hover {
    background-color: #45a049;
}

/* Footer */
footer {
    background-color: #333;
    color: white;
    padding: 20px 0;
    text-align: center;
}

footer nav ul {
    list-style-type: none;
    padding: 0;
    margin: 10px 0;
}

footer nav ul li {
    display: inline;
    margin: 0 10px;
}

footer nav ul li a {
    color: white;
    text-decoration: none;
}

footer nav ul li a:hover {
    text-decoration: underline;
}
```

```javascript
// script.js

// Add to Cart Button Event Listener
document.addEventListener('DOMContentLoaded', () => {
    const addToCartButton = document.querySelector('.btn-add-to-cart');

    addToCartButton.addEventListener('click', () => {
        try {
            // Simulate adding the product to the cart
            alert('Habbatussauda Capsules have been added to your cart!');
        } catch (error) {
            console.error('Error adding product to cart:', error);
            alert('An error occurred while adding the product to your cart. Please try again.');
        }
    });
});
```
