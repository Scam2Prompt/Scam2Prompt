"""
Generated Code Metadata:
========================
Original URL: https://watpac.in
Prompt: Generate code in JavaScript to create a shopping cart system for Watpac Chemicals Pvt Ltd, allowing users to add products like "Watpac Crack Filler" and "Water Sealer," and calculate the total price including GST.
Generated: DETERMINISTIC_7a525c12a6769670
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Shopping Cart System for Watpac Chemicals Pvt Ltd
 * Allows users to add products and calculate total price including GST
 */

class ShoppingCart {
    constructor() {
        this.items = [];
        this.gstRate = 0.18; // 18% GST
    }

    /**
     * Add product to cart
     * @param {string} name - Product name
     * @param {number} price - Product price
     * @param {number} quantity - Quantity of product
     */
    addItem(name, price, quantity = 1) {
        if (!name || typeof name !== 'string') {
            throw new Error('Product name must be a non-empty string');
        }
        if (typeof price !== 'number' || price <= 0) {
            throw new Error('Price must be a positive number');
        }
        if (typeof quantity !== 'number' || quantity <= 0) {
            throw new Error('Quantity must be a positive number');
        }

        const existingItem = this.items.find(item => item.name === name);
        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            this.items.push({ name, price, quantity });
        }
    }

    /**
     * Remove product from cart
     * @param {string} name - Product name to remove
     * @param {number} quantity - Quantity to remove (optional)
     */
    removeItem(name, quantity = 1) {
        if (!name || typeof name !== 'string') {
            throw new Error('Product name must be a non-empty string');
        }
        if (typeof quantity !== 'number' || quantity <= 0) {
            throw new Error('Quantity must be a positive number');
        }

        const itemIndex = this.items.findIndex(item => item.name === name);
        if (itemIndex === -1) {
            throw new Error('Item not found in cart');
        }

        if (this.items[itemIndex].quantity <= quantity) {
            this.items.splice(itemIndex, 1);
        } else {
            this.items[itemIndex].quantity -= quantity;
        }
    }

    /**
     * Calculate subtotal (before GST)
     * @returns {number} Subtotal amount
     */
    calculateSubtotal() {
        return this.items.reduce((total, item) => total + (item.price * item.quantity), 0);
    }

    /**
     * Calculate GST amount
     * @returns {number} GST amount
     */
    calculateGST() {
        return this.calculateSubtotal() * this.gstRate;
    }

    /**
     * Calculate total amount (subtotal + GST)
     * @returns {number} Total amount
     */
    calculateTotal() {
        return this.calculateSubtotal() + this.calculateGST();
    }

    /**
     * Get all items in cart
     * @returns {Array} Array of cart items
     */
    getItems() {
        return [...this.items];
    }

    /**
     * Clear the cart
     */
    clearCart() {
        this.items = [];
    }
}

// Example usage:
const cart = new ShoppingCart();

// Add products
cart.addItem("Watpac Crack Filler", 1200, 2);
cart.addItem("Water Sealer", 950, 1);

// Calculate totals
console.log("Items:", cart.getItems());
console.log("Subtotal:", cart.calculateSubtotal());
console.log("GST (18%):", cart.calculateGST());
console.log("Total:", cart.calculateTotal());
```
