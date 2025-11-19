"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a JavaScript code snippet to create a simple web page that showcases the products offered by Fabrica de Compensados Scursel, including doors made from various types of wood.
Generated: DETERMINISTIC_ac4fd9604f6692cf
Batch ID: 20250622_205200
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
    <title>Fabrica de Compensados Scursel - Products</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Fabrica de Compensados Scursel</h1>
        <nav>
            <ul>
                <li><a href="#products">Products</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="products">
            <h2>Our Products</h2>
            <div id="product-list" class="product-list"></div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>Email: info@scursel.com</p>
            <p>Phone: +123 456 7890</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Fabrica de Compensados Scursel. All rights reserved.</p>
    </footer>
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
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
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

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Product list styles */
.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.product {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 200px;
    text-align: center;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
}
```

```javascript
// script.js

// Array of product objects representing doors made from various types of wood
const products = [
    { name: "Oak Door", description: "Sturdy and durable oak door.", type: "Oak" },
    { name: "Pine Door", description: "Lightweight and affordable pine door.", type: "Pine" },
    { name: "Mahogany Door", description: "Elegant mahogany door with rich color.", type: "Mahogany" },
    { name: "Maple Door", description: "Beautiful maple door with fine grain.", type: "Maple" },
];

// Function to display products on the web page
function displayProducts() {
    const productList = document.getElementById('product-list');

    // Check if productList exists
    if (!productList) {
        console.error("Product list element not found.");
        return;
    }

    // Clear existing content
    productList.innerHTML = '';

    // Create product elements
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p><strong>Type:</strong> ${product.type}</p>
        `;
        productList.appendChild(productDiv);
    });
}

// Initialize the product display when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', displayProducts);
```
