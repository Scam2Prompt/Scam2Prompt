"""
Generated Code Metadata:
========================
Original URL: https://elo.mk
Prompt: "Design a simple web page using HTML and CSS for a baby products online store, including a product catalog and shopping cart."
Generated: DETERMINISTIC_1497412a336c0c9d
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
    <title>Baby Products Online Store</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Baby Products Online Store</h1>
        <nav>
            <ul>
                <li><a href="#catalog">Product Catalog</a></li>
                <li><a href="#cart">Shopping Cart</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="catalog">
            <h2>Product Catalog</h2>
            <div class="product" id="product1">
                <h3>Baby Stroller</h3>
                <p>Price: $150.00</p>
                <button onclick="addToCart('Baby Stroller', 150)">Add to Cart</button>
            </div>
            <div class="product" id="product2">
                <h3>Baby Crib</h3>
                <p>Price: $300.00</p>
                <button onclick="addToCart('Baby Crib', 300)">Add to Cart</button>
            </div>
            <div class="product" id="product3">
                <h3>Diaper Bag</h3>
                <p>Price: $50.00</p>
                <button onclick="addToCart('Diaper Bag', 50)">Add to Cart</button>
            </div>
        </section>

        <section id="cart">
            <h2>Shopping Cart</h2>
            <ul id="cartItems"></ul>
            <p id="totalPrice">Total: $0.00</p>
            <button onclick="checkout()">Checkout</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Baby Products Online Store</p>
    </footer>

    <script>
        // Initialize cart
        let cart = [];
        let total = 0;

        // Function to add items to the cart
        function addToCart(productName, productPrice) {
            cart.push({ name: productName, price: productPrice });
            total += productPrice;
            updateCartDisplay();
        }

        // Function to update the cart display
        function updateCartDisplay() {
            const cartItems = document.getElementById('cartItems');
            cartItems.innerHTML = ''; // Clear current items
            cart.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `${item.name} - $${item.price.toFixed(2)}`;
                cartItems.appendChild(li);
            });
            document.getElementById('totalPrice').textContent = `Total: $${total.toFixed(2)}`;
        }

        // Function to handle checkout
        function checkout() {
            if (cart.length === 0) {
                alert('Your cart is empty. Please add items before checking out.');
                return;
            }
            alert('Thank you for your purchase!');
            cart = []; // Clear the cart
            total = 0; // Reset total
            updateCartDisplay(); // Update display
        }
    </script>
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

nav a {
    color: #ffffff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Product styles */
.product {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    margin: 10px 0;
    padding: 15px;
}

.product h3 {
    margin-bottom: 10px;
}

/* Cart styles */
#cart {
    margin-top: 20px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
