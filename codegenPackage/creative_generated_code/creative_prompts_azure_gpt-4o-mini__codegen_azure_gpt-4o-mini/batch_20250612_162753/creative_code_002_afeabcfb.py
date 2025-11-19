"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Create a JavaScript function that dynamically updates a shopping cart with items such as "Cámara de Seguridad WiFi Inteligente" and "ageLOC® LumiSpa®" based on user selections, similar to the functionality on Mass Compras.
Generated: DETERMINISTIC_afeabcfbfff9d5ce
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart class to manage the items in the shopping cart.
 */
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold the cart items
    }

    /**
     * Adds an item to the shopping cart.
     * @param {Object} item - The item to add, should have id, name, and price properties.
     */
    addItem(item) {
        if (!item.id || !item.name || !item.price) {
            console.error("Invalid item. Must have id, name, and price.");
            return;
        }
        this.items.push(item);
        this.updateCartDisplay();
    }

    /**
     * Removes an item from the shopping cart by id.
     * @param {string} itemId - The id of the item to remove.
     */
    removeItem(itemId) {
        const initialLength = this.items.length;
        this.items = this.items.filter(item => item.id !== itemId);
        if (this.items.length === initialLength) {
            console.warn(`Item with id ${itemId} not found in the cart.`);
        }
        this.updateCartDisplay();
    }

    /**
     * Updates the display of the shopping cart.
     * This function should be called after any modification to the cart.
     */
    updateCartDisplay() {
        const cartContainer = document.getElementById('cart');
        cartContainer.innerHTML = ''; // Clear the current cart display

        if (this.items.length === 0) {
            cartContainer.innerHTML = '<p>Your cart is empty.</p>';
            return;
        }

        // Create a list of items in the cart
        const itemList = document.createElement('ul');
        this.items.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
            itemList.appendChild(listItem);
        });

        cartContainer.appendChild(itemList);
    }

    /**
     * Clears all items from the shopping cart.
     */
    clearCart() {
        this.items = []; // Reset the items array
        this.updateCartDisplay();
    }
}

// Example usage
const cart = new ShoppingCart();

// Sample item objects
const cameraItem = { id: '1', name: 'Cámara de Seguridad WiFi Inteligente', price: 99.99 };
const lumiSpaItem = { id: '2', name: 'ageLOC® LumiSpa®', price: 219.00 };

// Adding items to the cart
cart.addItem(cameraItem);
cart.addItem(lumiSpaItem);

// Removing an item from the cart
// cart.removeItem('1'); // Uncomment to test removing an item

// Clear the cart
// cart.clearCart(); // Uncomment to test clearing the cart
```
This code defines a `ShoppingCart` class that facilitates adding and removing items while dynamically updating the cart display on a webpage. The implementation includes error handling for invalid item inputs and removal attempts for non-existent items.
