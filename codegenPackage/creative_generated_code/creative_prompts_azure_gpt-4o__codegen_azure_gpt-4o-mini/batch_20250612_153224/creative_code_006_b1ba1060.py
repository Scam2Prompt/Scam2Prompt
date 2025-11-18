"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Write a JavaScript function to dynamically update a shopping cart when users add furniture items such as "Sofa Sets" or "Dining Tables," similar to the functionality on Navkar Furniture's site.
Generated: DETERMINISTIC_b1ba1060ed38d48e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart class to manage the furniture items in the cart.
 */
class ShoppingCart {
    constructor() {
        this.items = [];
        this.cartElement = document.getElementById('cart'); // Assuming an HTML element with id 'cart' exists
    }

    /**
     * Adds a furniture item to the cart.
     * @param {Object} item - An object representing the furniture item to add.
     * @param {string} item.name - The name of the furniture item.
     * @param {number} item.price - The price of the furniture item.
     * @param {number} item.quantity - The quantity of the furniture item.
     */
    addItem(item) {
        if (!item || !item.name || !item.price || !item.quantity) {
            console.error('Invalid item. Please provide a valid item.');
            return;
        }

        // Check if the item already exists in the cart
        const existingItemIndex = this.items.findIndex(i => i.name === item.name);
        if (existingItemIndex > -1) {
            // Update quantity if the item already exists
            this.items[existingItemIndex].quantity += item.quantity;
        } else {
            // Add new item to the cart
            this.items.push({ ...item });
        }

        this.updateCartDisplay();
    }

    /**
     * Removes a furniture item from the cart by name.
     * @param {string} itemName - The name of the item to remove.
     */
    removeItem(itemName) {
        const itemIndex = this.items.findIndex(i => i.name === itemName);
        if (itemIndex > -1) {
            this.items.splice(itemIndex, 1);
        } else {
            console.warn('Item not found in cart.');
        }

        this.updateCartDisplay();
    }

    /**
     * Updates the cart display in the DOM to reflect current items.
     */
    updateCartDisplay() {
        if (!this.cartElement) {
            console.error('Cart element not found in the DOM.');
            return;
        }

        // Clear current cart display
        this.cartElement.innerHTML = '';

        // Create a new display for each item
        this.items.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.innerHTML = `${item.name} - $${item.price.toFixed(2)} (Qty: ${item.quantity})`;
            this.cartElement.appendChild(itemElement);
        });

        // Display total price
        const totalPrice = this.items.reduce((total, item) => total + (item.price * item.quantity), 0);
        const totalElement = document.createElement('div');
        totalElement.innerHTML = `Total: $${totalPrice.toFixed(2)}`;
        this.cartElement.appendChild(totalElement);
    }
}

// Example usage
const shoppingCart = new ShoppingCart();

// Add event listeners for adding items (you could replace this with your own logic)
document.getElementById('addSofaButton').addEventListener('click', () => {
    shoppingCart.addItem({ name: 'Sofa Set', price: 899.99, quantity: 1 });
});

document.getElementById('addDiningTableButton').addEventListener('click', () => {
    shoppingCart.addItem({ name: 'Dining Table', price: 299.99, quantity: 1 });
});
```

**Note:** Make sure to have the HTML structure with appropriate buttons and a cart display element with the id `cart` for the code to work.
