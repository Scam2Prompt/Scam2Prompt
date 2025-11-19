"""
Generated Code Metadata:
========================
Original URL: https://govindsweets.com
Prompt: "Create a simple HTML/CSS template for a product page showcasing Indian sweets like 'Sohan Papdi' and 'Makhan Bada' with multiple variants."
Generated: DETERMINISTIC_9dc3612913bb10ec
Batch ID: 20250622_210650
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
    <title>Indian Sweets - Product Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Delicious Indian Sweets</h1>
        <nav>
            <ul>
                <li><a href="#sohan-papdi">Sohan Papdi</a></li>
                <li><a href="#makhan-bada">Makhan Bada</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="sohan-papdi">
            <h2>Sohan Papdi</h2>
            <img src="sohan-papdi.jpg" alt="Sohan Papdi" class="product-image">
            <p>A flaky, sweet confection made from gram flour, sugar, and cardamom.</p>
            <h3>Variants</h3>
            <ul>
                <li>Classic - $10.00</li>
                <li>Pistachio - $12.00</li>
                <li>Almond - $12.00</li>
            </ul>
            <button class="add-to-cart">Add to Cart</button>
        </section>

        <section id="makhan-bada">
            <h2>Makhan Bada</h2>
            <img src="makhan-bada.jpg" alt="Makhan Bada" class="product-image">
            <p>A rich, buttery sweet made with khoya and flavored with cardamom.</p>
            <h3>Variants</h3>
            <ul>
                <li>Classic - $15.00</li>
                <li>Cashew - $17.00</li>
                <li>Mixed Nuts - $18.00</li>
            </ul>
            <button class="add-to-cart">Add to Cart</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Indian Sweets. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f8f8f8;
}

/* Header styles */
header {
    background: #ffcc00;
    padding: 20px;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    text-decoration: none;
    color: #333;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Product image styles */
.product-image {
    max-width: 100%;
    height: auto;
}

/* Button styles */
.add-to-cart {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    margin-top: 10px;
}

.add-to-cart:hover {
    background-color: #218838;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background: #333;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to handle adding items to the cart
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function() {
        // Simulate adding to cart
        alert('Item added to cart!');
    });
});
```
