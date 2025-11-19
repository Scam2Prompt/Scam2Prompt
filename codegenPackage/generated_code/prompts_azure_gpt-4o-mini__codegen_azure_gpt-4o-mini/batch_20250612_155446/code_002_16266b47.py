"""
Generated Code Metadata:
========================
Original URL: https://energiakert.com
Prompt: Create a JavaScript function that enhances user experience on a shopping website by implementing a real-time cart update feature, inspired by EnergiaKert's shopping experience.
Generated: DETERMINISTIC_16266b47e120d1f8
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ShoppingCart class to manage cart operations
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold cart items
        this.cartElement = document.getElementById('cart'); // Cart display element
        this.updateCartDisplay(); // Initial cart display update
    }

    // Method to add an item to the cart
    addItem(item) {
        // Check if item already exists in the cart
        const existingItem = this.items.find(cartItem => cartItem.id === item.id);
        if (existingItem) {
            existingItem.quantity += item.quantity; // Update quantity if exists
        } else {
            this.items.push(item); // Add new item to cart
        }
        this.updateCartDisplay(); // Update cart display
    }

    // Method to remove an item from the cart
    removeItem(itemId) {
        this.items = this.items.filter(item => item.id !== itemId); // Filter out the item
        this.updateCartDisplay(); // Update cart display
    }

    // Method to update the cart display
    updateCartDisplay() {
        // Clear current cart display
        this.cartElement.innerHTML = '';

        // Check if cart is empty
        if (this.items.length === 0) {
            this.cartElement.innerHTML = '<p>Your cart is empty.</p>';
            return;
        }

        // Create and append cart items to the display
        this.items.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'cart-item';
            itemElement.innerHTML = `
                <span>${item.name} (x${item.quantity})</span>
                <button onclick="cart.removeItem(${item.id})">Remove</button>
            `;
            this.cartElement.appendChild(itemElement);
        });

        // Update total items count
        this.updateTotalCount();
    }

    // Method to update total items count
    updateTotalCount() {
        const totalCount = this.items.reduce((total, item) => total + item.quantity, 0);
        document.getElementById('total-count').innerText = `Total Items: ${totalCount}`;
    }
}

// Initialize the shopping cart
const cart = new ShoppingCart();

// Function to handle adding items to the cart
function addToCart(itemId, itemName, itemQuantity) {
    // Validate input
    if (itemQuantity <= 0) {
        console.error('Quantity must be greater than zero.');
        return;
    }

    // Create item object
    const item = {
        id: itemId,
        name: itemName,
        quantity: itemQuantity
    };

    // Add item to cart
    cart.addItem(item);
}

// Example usage: Adding items to the cart
document.getElementById('add-item-button').addEventListener('click', () => {
    const itemId = parseInt(document.getElementById('item-id').value);
    const itemName = document.getElementById('item-name').value;
    const itemQuantity = parseInt(document.getElementById('item-quantity').value);
    
    addToCart(itemId, itemName, itemQuantity);
});
```

```html
<!-- HTML structure for the shopping cart -->
<div id="cart"></div>
<div id="total-count">Total Items: 0</div>

<!-- Input fields for adding items -->
<input type="number" id="item-id" placeholder="Item ID" required>
<input type="text" id="item-name" placeholder="Item Name" required>
<input type="number" id="item-quantity" placeholder="Quantity" required>
<button id="add-item-button">Add to Cart</button>
```
