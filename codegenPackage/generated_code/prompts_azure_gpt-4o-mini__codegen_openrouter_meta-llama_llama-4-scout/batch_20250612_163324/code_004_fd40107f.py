"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Design a simple HTML form that allows users to add items like "TINTA SPRAY VERNIZ" to a shopping cart, similar to the functionality seen on the Gala Games app.
Generated: DETERMINISTIC_fd40107fc8d386c1
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Shopping Cart</h1>
    <form id="add-to-cart-form">
        <label for="item-name">Item Name:</label>
        <input type="text" id="item-name" required>
        <button id="add-to-cart-btn">Add to Cart</button>
    </form>
    <div id="cart-container">
        <h2>Cart:</h2>
        <ul id="cart-list"></ul>
        <p id="cart-total"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

#add-to-cart-form {
    margin-bottom: 20px;
}

#cart-container {
    margin-top: 20px;
}

#cart-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#cart-list li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}

#cart-list li:last-child {
    border-bottom: none;
}

#cart-total {
    font-weight: bold;
    margin-top: 10px;
}
```

**script.js**
```javascript
// Get DOM elements
const form = document.getElementById('add-to-cart-form');
const itemNameInput = document.getElementById('item-name');
const cartList = document.getElementById('cart-list');
const cartTotalElement = document.getElementById('cart-total');

// Initialize cart
let cart = [];

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();
    addItemToCart();
});

// Function to add item to cart
function addItemToCart() {
    const itemName = itemNameInput.value.trim();
    if (itemName === '') {
        alert('Please enter an item name');
        return;
    }

    // Check if item already exists in cart
    const existingItem = cart.find((item) => item.name === itemName);
    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push({ name: itemName, quantity: 1 });
    }

    // Update cart display
    updateCartDisplay();
    itemNameInput.value = '';
}

// Function to update cart display
function updateCartDisplay() {
    cartList.innerHTML = '';
    let total = 0;

    cart.forEach((item) => {
        const listItem = document.createElement('li');
        listItem.textContent = `${item.name} x ${item.quantity}`;
        cartList.appendChild(listItem);
        total += item.quantity;
    });

    cartTotalElement.textContent = `Total items in cart: ${total}`;
}

// Error handling for storage
try {
    // Consider using a more robust storage solution like localStorage or a backend API
    // For demonstration purposes, we'll use sessionStorage
    const storedCart = sessionStorage.getItem('cart');
    if (storedCart) {
        cart = JSON.parse(storedCart);
        updateCartDisplay();
    }
} catch (error) {
    console.error('Error loading cart from storage:', error);
}

// Update storage on cart change
cart = cart || [];
const updateStorage = () => {
    try {
        sessionStorage.setItem('cart', JSON.stringify(cart));
    } catch (error) {
        console.error('Error saving cart to storage:', error);
    }
};

updateStorage();
window.addEventListener('beforeunload', updateStorage);
```
