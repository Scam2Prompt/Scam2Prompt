"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchlawinc.com
Prompt: Write a script to dynamically update the shopping cart item count and total price for a legal form e-commerce site, similar to the functionality on Launch Law.
Generated: DETERMINISTIC_a5cfb59482519f06
Batch ID: 20250612_153517
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
    <title>Shopping Cart</title>
    <style>
        /* Basic styling for the shopping cart */
        .cart {
            border: 1px solid #ccc;
            padding: 20px;
            width: 300px;
        }
        .item {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
        }
        .total {
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="cart">
    <h2>Shopping Cart</h2>
    <div id="cart-items">
        <!-- Items will be dynamically added here -->
    </div>
    <div class="total" id="cart-total">
        Total: $0.00
    </div>
</div>

<script>
// Cart class to manage items in the shopping cart
class ShoppingCart {
    constructor() {
        this.items = [];
    }

    // Method to add an item to the cart
    addItem(item) {
        const existingItemIndex = this.items.findIndex(i => i.id === item.id);
        if (existingItemIndex !== -1) {
            // Item already exists, update the quantity
            this.items[existingItemIndex].quantity += item.quantity;
        } else {
            // New item, add to the cart
            this.items.push(item);
        }
        this.updateCartView();
    }

    // Method to update the cart view
    updateCartView() {
        const cartItemsContainer = document.getElementById('cart-items');
        const cartTotalElement = document.getElementById('cart-total');
        cartItemsContainer.innerHTML = ''; // Clear existing items
        let totalPrice = 0;

        // Loop through items and display them
        this.items.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'item';
            itemElement.innerHTML = `${item.name} (x${item.quantity}) - $${(item.price * item.quantity).toFixed(2)}`;
            cartItemsContainer.appendChild(itemElement);
            totalPrice += item.price * item.quantity; // Calculate total
        });

        // Update total price display
        cartTotalElement.innerHTML = `Total: $${totalPrice.toFixed(2)}`;
    }
}

// Initialize shopping cart
const cart = new ShoppingCart();

// Example items (In a real application, items would likely be fetched from an API)
const exampleItem1 = { id: 1, name: 'Legal Document A', price: 19.99, quantity: 1 };
const exampleItem2 = { id: 2, name: 'Legal Document B', price: 29.99, quantity: 1 };

// Function to simulate adding items to the cart
function addItemToCart(item) {
    try {
        cart.addItem(item);
    } catch (error) {
        console.error('Error adding item to cart:', error);
    }
}

// Simulate adding items to the cart
addItemToCart(exampleItem1);
addItemToCart(exampleItem2);
addItemToCart(exampleItem1); // Adding the first item again to test quantity update

</script>
</body>
</html>
```
