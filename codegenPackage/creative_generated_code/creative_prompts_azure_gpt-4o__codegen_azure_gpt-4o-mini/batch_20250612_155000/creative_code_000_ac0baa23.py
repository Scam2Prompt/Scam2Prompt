"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: Write code for a basic e-commerce website using HTML, CSS, and JavaScript, incorporating features mentioned by La Guarida, such as product listings and a shopping cart.
Generated: DETERMINISTIC_ac0baa230ac21b4c
Batch ID: 20250612_155000
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
    <title>Basic E-Commerce Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>La Guarida E-Commerce</h1>
        <nav>
            <ul>
                <li><a href="#products">Products</a></li>
                <li><a href="#cart">Shopping Cart (<span id="cart-count">0</span>)</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="products">
            <h2>Product Listings</h2>
            <div id="product-list" class="product-list"></div>
        </section>

        <section id="cart">
            <h2>Your Shopping Cart</h2>
            <div id="cart-items" class="cart-items"></div>
            <div id="total-price">Total: $0.00</div>
            <button id="checkout">Checkout</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 La Guarida. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #282c34;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

nav ul {
    list-style-type: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 20px;
}

.product-item {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    width: 200px;
    margin: 10px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.cart-items {
    padding: 20px;
}
```

```javascript
// script.js

// Sample product data
const products = [
    { id: 1, name: "Product 1", price: 10.00 },
    { id: 2, name: "Product 2", price: 15.00 },
    { id: 3, name: "Product 3", price: 20.00 },
];

// Initialize cart
let cart = [];

// Function to render products
function renderProducts() {
    const productList = document.getElementById('product-list');
    products.forEach(product => {
        const productItem = document.createElement('div');
        productItem.className = 'product-item';
        productItem.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price.toFixed(2)}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productItem);
    });
}

// Function to add product to cart
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        const cartItem = cart.find(item => item.id === product.id);
        if (cartItem) {
            cartItem.quantity += 1; // Increase quantity if already in cart
        } else {
            cart.push({ ...product, quantity: 1 });
        }
        updateCart();
    } else {
        console.error("Product not found");
    }
}

// Function to update cart display
function updateCart() {
    const cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = ''; // Clear current cart display
    let total = 0;

    cart.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.textContent = `${item.name} - Quantity: ${item.quantity} - Total: $${(item.price * item.quantity).toFixed(2)}`;
        cartItemsContainer.appendChild(cartItem);
        total += item.price * item.quantity;
    });

    document.getElementById('cart-count').textContent = cart.length;
    document.getElementById('total-price').textContent = `Total: $${total.toFixed(2)}`;
}

// Function to handle checkout
document.getElementById('checkout').onclick = function() {
    if (cart.length === 0) {
        alert("Your cart is empty!");
    } else {
        alert("Proceeding to checkout...");
        // Implement checkout logic here
    }
}

// Initial rendering of products
renderProducts();
```
