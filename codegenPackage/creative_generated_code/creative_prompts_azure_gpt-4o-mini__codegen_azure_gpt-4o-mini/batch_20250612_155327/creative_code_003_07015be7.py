"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panicinpolkadots.com
Prompt: Develop a JavaScript function that dynamically displays a shopping cart for handmade items like rugs and quilts, similar to the shopping experience on Panic in Polkadots.
Generated: DETERMINISTIC_07015be7f034f2b9
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart class to manage the items in the shopping cart
class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.items = [];
    }

    // Add an item to the cart
    addItem(item) {
        // Check if item is valid
        if (!item || !item.id || !item.name || !item.price) {
            throw new Error('Invalid item. Item must have id, name, and price.');
        }
        this.items.push(item);
        this.displayCart();
    }

    // Remove an item from the cart by id
    removeItem(itemId) {
        const index = this.items.findIndex(item => item.id === itemId);
        // Check if item exists in the cart
        if (index === -1) {
            console.warn(`Item with id ${itemId} not found in the cart.`);
            return;
        }
        this.items.splice(index, 1);
        this.displayCart();
    }

    // Calculate the total price of items in the cart
    calculateTotal() {
        return this.items.reduce((total, item) => total + item.price, 0).toFixed(2);
    }

    // Display the cart items and total price
    displayCart() {
        const cartContainer = document.getElementById('cartContainer');
        cartContainer.innerHTML = ''; // Clear previous items

        // Check if there are items in the cart
        if (this.items.length === 0) {
            cartContainer.innerHTML = '<p>Your cart is empty.</p>';
            return;
        }

        // Create a list of cart items
        const itemList = document.createElement('ul');
        this.items.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.onclick = () => this.removeItem(item.id); // Remove item on click
            listItem.appendChild(removeButton);
            itemList.appendChild(listItem);
        });

        // Add item list and total to the cart container
        const total = document.createElement('p');
        total.textContent = `Total: $${this.calculateTotal()}`;
        cartContainer.appendChild(itemList);
        cartContainer.appendChild(total);
    }
}

// Example usage
const cart = new ShoppingCart();

// Example function to simulate adding items to the cart
function addToCartExample() {
    try {
        const item1 = { id: 'rug1', name: 'Handmade Rug', price: 150.00 };
        const item2 = { id: 'quilt1', name: 'Quilt', price: 120.00 };
        
        cart.addItem(item1);
        cart.addItem(item2);
    } catch (error) {
        console.error(error.message);
    }
}

// Initialize the cart display on window load
window.onload = () => {
    addToCartExample();
};
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart</title>
    <style>
        /* Basic styling for the cart */
        #cartContainer {
            border: 1px solid #ddd;
            padding: 10px;
            width: 300px;
        }
        button {
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    <div id="cartContainer"></div>
    <script src="shoppingCart.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
