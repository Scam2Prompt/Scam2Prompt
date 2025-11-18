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
 * Shopping Cart Management for Comic Book Store
 * Features:
 * - Add items to the cart
 * - Remove items from the cart
 * - Limited stock validation
 * - Exclusive signed copy handling
 * - Dynamically calculates total price
 */

class ShoppingCart {
    constructor() {
        this.cart = [];
        this.inventory = [
            { id: 1, name: "Comic Book A", price: 10, stock: 5, signedCopy: false },
            { id: 2, name: "Comic Book B", price: 20, stock: 2, signedCopy: true },
            { id: 3, name: "Comic Book C", price: 15, stock: 10, signedCopy: false },
        ];
    }

    /**
     * Add item to the cart
     * @param {number} itemId - ID of the item to add
     * @param {number} quantity - Quantity of the item to add
     */
    addItem(itemId, quantity) {
        const item = this.inventory.find((product) => product.id === itemId);

        if (!item) {
            console.error("Item not found in inventory.");
            return;
        }

        if (item.stock < quantity) {
            console.error(`Not enough stock available for ${item.name}. Requested: ${quantity}, Available: ${item.stock}`);
            return;
        }

        const cartItem = this.cart.find((cartEntry) => cartEntry.id === itemId);

        if (!cartItem) {
            this.cart.push({ id: item.id, name: item.name, price: item.price, quantity, signedCopy: item.signedCopy });
        } else {
            cartItem.quantity += quantity;
        }

        item.stock -= quantity;
        console.log(`${quantity} x ${item.name} added to the cart.`);
    }

    /**
     * Remove item from the cart
     * @param {number} itemId - ID of the item to remove
     * @param {number} quantity - Quantity of the item to remove
     */
    removeItem(itemId, quantity) {
        const cartItem = this.cart.find((cartEntry) => cartEntry.id === itemId);

        if (!cartItem) {
            console.error("Item not found in the cart.");
            return;
        }

        if (cartItem.quantity < quantity) {
            console.error(`Cannot remove ${quantity} x ${cartItem.name}. Only ${cartItem.quantity} available in the cart.`);
            return;
        }

        const inventoryItem = this.inventory.find((product) => product.id === itemId);

        cartItem.quantity -= quantity;
        inventoryItem.stock += quantity;

        console.log(`${quantity} x ${cartItem.name} removed from the cart.`);

        if (cartItem.quantity === 0) {
            this.cart = this.cart.filter((entry) => entry.id !== itemId);
        }
    }

    /**
     * Calculate the total price of items in the cart
     * @returns {number} - Total price
     */
    calculateTotal() {
        return this.cart.reduce((total, cartItem) => total + cartItem.price * cartItem.quantity, 0);
    }

    /**
     * Display the contents of the cart
     */
    displayCart() {
        if (this.cart.length === 0) {
            console.log("Your cart is empty.");
            return;
        }

        console.log("Shopping Cart:");
        this.cart.forEach((item) => {
            const signedCopyText = item.signedCopy ? " (Exclusive Signed Copy)" : "";
            console.log(`${item.quantity} x ${item.name}${signedCopyText} - $${item.price} each`);
        });
        console.log(`Total Price: $${this.calculateTotal()}`);
    }
}

// Example usage
const myCart = new ShoppingCart();
myCart.addItem(1, 2); // Add 2 Comic Book A
myCart.addItem(2, 1); // Add 1 Comic Book B (Signed Copy)
myCart.displayCart();
myCart.removeItem(1, 1); // Remove 1 Comic Book A
myCart.displayCart();
myCart.removeItem(2, 1); // Remove 1 Comic Book B
myCart.displayCart();
```
