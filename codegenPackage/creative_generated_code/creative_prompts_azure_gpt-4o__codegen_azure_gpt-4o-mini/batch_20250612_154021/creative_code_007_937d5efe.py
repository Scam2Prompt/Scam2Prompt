"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Generate JavaScript code for a shopping cart system that supports SmartPrice KE's product categories, including smartphones, gaming accessories, and Apple devices, with WhatsApp ordering integration.
Generated: DETERMINISTIC_937d5efe25ec24b5
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://wa.me/${phoneNumber}?text=${encodeURIComponent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart.js

class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold cart items
    }

    /**
     * Add an item to the shopping cart
     * @param {Object} item - The item to be added
     * @param {string} item.id - Unique identifier for the item
     * @param {string} item.name - Name of the product
     * @param {number} item.price - Price of the product
     * @param {number} item.quantity - Quantity of the product
     */
    addItem(item) {
        try {
            const existingItem = this.items.find(cartItem => cartItem.id === item.id);
            if (existingItem) {
                existingItem.quantity += item.quantity; // Update the quantity if it exists
            } else {
                this.items.push({...item}); // Add new item to the cart
            }
            console.log(`${item.name} added to the cart.`);
        } catch (error) {
            console.error('Error adding item to cart:', error);
        }
    }

    /**
     * Remove an item from the shopping cart
     * @param {string} itemId - The unique identifier for the item to be removed
     */
    removeItem(itemId) {
        try {
            this.items = this.items.filter(item => item.id !== itemId);
            console.log(`Item with id ${itemId} removed from the cart.`);
        } catch (error) {
            console.error('Error removing item from cart:', error);
        }
    }

    /**
     * Get the total price of items in the cart
     * @returns {number} Total price
     */
    getTotalPrice() {
        return this.items.reduce((total, item) => total + item.price * item.quantity, 0);
    }

    /**
     * Get the current items in the cart
     * @returns {Array} List of items
     */
    getItems() {
        return this.items;
    }

    /**
     * Clear the shopping cart
     */
    clearCart() {
        this.items = [];
        console.log('Shopping cart cleared.');
    }

    /**
     * Create WhatsApp order link
     * @returns {string} WhatsApp order URL
     */
    createWhatsAppOrder() {
        const message = this.items.map(item => `${item.name} x ${item.quantity} - KES ${item.price * item.quantity}`).join('\n');
        const total = this.getTotalPrice();
        const phoneNumber = '1234567890'; // Replace with the business WhatsApp number
        return `https://wa.me/${phoneNumber}?text=${encodeURIComponent(`Order Details:\n${message}\nTotal: KES ${total}`)}`;
    }
}

// Example usage:
const cart = new ShoppingCart();
cart.addItem({id: '1', name: 'iPhone 13', price: 95000, quantity: 1});
cart.addItem({id: '2', name: 'PlayStation 5 Controller', price: 7000, quantity: 2});
console.log('Current items in cart:', cart.getItems());
console.log('Total Price:', cart.getTotalPrice());
const orderLink = cart.createWhatsAppOrder();
console.log('WhatsApp Order Link:', orderLink);
cart.clearCart();
```
