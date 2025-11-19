"""
Generated Code Metadata:
========================
Original URL: https://utterlybaked.com
Prompt: Design a user interface mockup for a bakery's online ordering system that highlights special promotions, similar to what is offered on utterlybaked.com.
Generated: DETERMINISTIC_d65113c646f60118
Batch ID: 20250612_161700
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
    <title>Bakery Online Ordering System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Bakery!</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#menu">Menu</a></li>
                <li><a href="#promotions">Promotions</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="promotions">
            <h2>Special Promotions</h2>
            <div class="promotion-card">
                <h3>Buy One Get One Free!</h3>
                <p>On all cupcakes every Friday!</p>
                <button onclick="orderNow('cupcakes')">Order Now</button>
            </div>
            <div class="promotion-card">
                <h3>20% Off on Bread</h3>
                <p>Every Wednesday, enjoy 20% off on all types of bread.</p>
                <button onclick="orderNow('bread')">Order Now</button>
            </div>
            <div class="promotion-card">
                <h3>Free Delivery on Orders Over $50</h3>
                <p>Get free delivery for orders above $50!</p>
                <button onclick="orderNow('delivery')">Order Now</button>
            </div>
        </section>

        <section id="menu">
            <h2>Our Menu</h2>
            <p>Explore our delicious offerings!</p>
            <!-- Menu items would be listed here -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Our Bakery. All rights reserved.</p>
        <p><a href="#contact">Contact Us</a></p>
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

/* Promotion card styles */
.promotion-card {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    margin: 20px;
    text-align: center;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background: #333;
    color: #fff;
}
```

```javascript
// script.js

/**
 * Function to handle the order action for promotions.
 * @param {string} item - The item to order.
 */
function orderNow(item) {
    try {
        // Simulate an order process
        console.log(`Ordering: ${item}`);
        alert(`You have successfully ordered: ${item}`);
    } catch (error) {
        console.error('Error while processing the order:', error);
        alert('There was an error processing your order. Please try again later.');
    }
}
```
