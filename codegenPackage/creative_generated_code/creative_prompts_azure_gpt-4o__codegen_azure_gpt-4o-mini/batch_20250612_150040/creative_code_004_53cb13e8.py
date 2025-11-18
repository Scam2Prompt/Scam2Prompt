"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Develop a JavaScript function that dynamically updates a shopping cart for a comic book store, including features like "limited stock" and "exclusive signed copies."
Generated: DETERMINISTIC_53cb13e847cf384b
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart class to manage a shopping cart for a comic book store.
 */
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold items in the cart
    }

    /**
     * Adds an item to the cart.
     * @param {Object} item - The comic book item to add.
     * @param {number} quantity - The quantity of the item to add.
     * @throws Will throw an error if the item is out of stock.
     */
    addItem(item, quantity) {
        if (item.stock < quantity) {
            throw new Error(`Cannot add ${quantity} of ${item.title}. Only ${item.stock} in stock.`);
        }
        
        // Update stock and add to cart
        item.stock -= quantity;
        const cartItem = this.items.find(i => i.id === item.id);
        
        if (cartItem) {
            cartItem.quantity += quantity; // Update quantity if item already in cart
        } else {
            this.items.push({ ...item, quantity }); // Add new item to cart
        }
        
        console.log(`${quantity} of ${item.title} added to the cart.`);
    }

    /**
     * Removes an item from the cart.
     * @param {number} itemId - The ID of the item to remove.
     * @throws Will throw an error if the item is not found in the cart.
     */
    removeItem(itemId) {
        const index = this.items.findIndex(item => item.id === itemId);
        if (index === -1) {
            throw new Error(`Item with ID ${itemId} not found in the cart.`);
        }
        
        const [removedItem] = this.items.splice(index, 1);
        console.log(`${removedItem.title} removed from the cart.`);
    }

    /**
     * Updates the quantity of an item in the cart.
     * @param {number} itemId - The ID of the item to update.
     * @param {number} quantity - The new quantity for the item.
     * @throws Will throw an error if the new quantity exceeds stock or item is not found.
     */
    updateItemQuantity(itemId, quantity) {
        const cartItem = this.items.find(item => item.id === itemId);
        if (!cartItem) {
            throw new Error(`Item with ID ${itemId} not found in the cart.`);
        }
        if (cartItem.stock + cartItem.quantity < quantity) {
            throw new Error(`Cannot update ${cartItem.title} to ${quantity}. Only ${cartItem.stock + cartItem.quantity} available.`);
        }

        cartItem.stock += cartItem.quantity - quantity; // Adjust stock
        cartItem.quantity = quantity; // Update quantity
        console.log(`Quantity of ${cartItem.title} updated to ${quantity}.`);
    }

    /**
     * Gets the total items in the cart.
     * @returns {number} The total item count.
     */
    getTotalItems() {
        return this.items.reduce((total, item) => total + item.quantity, 0);
    }

    /**
     * Gets the cart summary.
     * @returns {Array} The array of items in the cart with their quantities.
     */
    getCartSummary() {
        return this.items.map(item => ({
            title: item.title,
            quantity: item.quantity,
            price: item.price,
            total: item.price * item.quantity
        }));
    }

    /**
     * Clears the cart.
     */
    clearCart() {
        this.items.forEach(item => item.stock += item.quantity); // Restore stock
        this.items = []; // Clear the cart
        console.log(`Cart cleared.`);
    }
}

// Example usage
const comicBookStore = new ShoppingCart();

// Example comic book items
const comic1 = { id: 1, title: 'Comic A', price: 10, stock: 5 };
const comic2 = { id: 2, title: 'Comic B - Signed Edition', price: 15, stock: 2 };

// Add items to cart
try {
    comicBookStore.addItem(comic1, 2);
    comicBookStore.addItem(comic2, 1);
    
    // Update item quantity
    comicBookStore.updateItemQuantity(1, 3);
    
    // Get cart summary
    console.log(comicBookStore.getCartSummary());
    
    // Remove an item
    comicBookStore.removeItem(2);
    
    // Clear cart
    comicBookStore.clearCart();
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
