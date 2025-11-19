"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: "Design a website for an e-commerce business, including a custom design, online payment integration, and product management, using Henfruit's web design expertise."
Generated: DETERMINISTIC_d7d1ecadd09069e5
Batch ID: 20250622_210703
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
    <title>Henfruit E-Commerce</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Henfruit E-Commerce</h1>
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
            <div class="product-list" id="product-list">
                <!-- Products will be dynamically loaded here -->
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>Welcome to Henfruit, your go-to place for quality products!</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" onsubmit="return handleContactForm(event)">
                <label for="name">Name:</label>
                <input type="text" id="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" required>
                <label for="message">Message:</label>
                <textarea id="message" required></textarea>
                <button type="submit">Send</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Henfruit E-Commerce. All rights reserved.</p>
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
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

header h1 {
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
}

nav ul li {
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

/* Product list styles */
.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```

```javascript
// script.js

// Sample product data
const products = [
    { id: 1, name: "Product 1", price: 29.99 },
    { id: 2, name: "Product 2", price: 39.99 },
    { id: 3, name: "Product 3", price: 49.99 },
];

// Function to load products into the product list
function loadProducts() {
    const productList = document.getElementById('product-list');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price.toFixed(2)}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
}

// Function to handle adding products to the cart
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        alert(`${product.name} has been added to your cart.`);
    } else {
        console.error('Product not found:', productId);
    }
}

// Function to handle contact form submission
function handleContactForm(event) {
    event.preventDefault(); // Prevent default form submission
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Simple validation
    if (!name || !email || !message) {
        alert('Please fill in all fields.');
        return false;
    }

    // Simulate form submission
    console.log('Form submitted:', { name, email, message });
    alert('Thank you for your message!');

    // Reset form
    document.getElementById('contact-form').reset();
    return false; // Prevent actual form submission
}

// Load products on page load
window.onload = loadProducts;
``` 

This code provides a basic structure for an e-commerce website, including product display, a contact form, and basic styling. It is designed to be clean, efficient, and ready for further development and integration with backend services for payment processing and product management.
