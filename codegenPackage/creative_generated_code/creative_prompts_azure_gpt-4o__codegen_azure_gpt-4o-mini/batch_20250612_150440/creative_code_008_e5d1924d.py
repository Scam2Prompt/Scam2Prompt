"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livesupport.tfryx.xyz
Prompt: Write JavaScript code to implement a "Add to Cart" feature that calculates the total price for multiple products, such as "Trek District+ 1 Midstep" and "Castelgarden XDC 180 HD," from https://livesupport.tfryx.xyz.
Generated: DETERMINISTIC_e5d1924d7eb8d623
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a Cart class to manage the shopping cart functionality
class Cart {
    constructor() {
        this.items = []; // Array to hold cart items
    }

    /**
     * Adds a product to the cart.
     * @param {Object} product - The product to add.
     * @param {string} product.name - The name of the product.
     * @param {number} product.price - The price of the product.
     * @param {number} quantity - The quantity of the product to add.
     */
    addItem(product, quantity = 1) {
        if (!product || !product.name || !product.price || quantity <= 0) {
            throw new Error('Invalid product or quantity');
        }

        // Check if the product is already in the cart
        const existingItem = this.items.find(item => item.product.name === product.name);
        if (existingItem) {
            // Update quantity if product is already in cart
            existingItem.quantity += quantity;
        } else {
            // Add new product to the cart
            this.items.push({ product, quantity });
        }
    }

    /**
     * Calculates the total price of all items in the cart.
     * @returns {number} The total price.
     */
    calculateTotal() {
        return this.items.reduce((total, item) => {
            return total + (item.product.price * item.quantity);
        }, 0).toFixed(2); // Return total price rounded to two decimal places
    }

    /**
     * Clears the cart.
     */
    clearCart() {
        this.items = [];
    }

    /**
     * Displays the items in the cart.
     * @returns {Array} The list of items in the cart.
     */
    getItems() {
        return this.items;
    }
}

// Example usage:
try {
    // Create a new cart instance
    const cart = new Cart();

    // Sample products
    const trekBike = { name: 'Trek District+ 1 Midstep', price: 2499.99 };
    const castelgarden = { name: 'Castelgarden XDC 180 HD', price: 1199.99 };

    // Add items to the cart
    cart.addItem(trekBike, 1);
    cart.addItem(castelgarden, 2);

    // Calculate and display total price
    console.log(`Total Price: $${cart.calculateTotal()}`); // Output: Total Price: $4899.97

    // List items in the cart
    console.log('Items in Cart:', cart.getItems());

    // Clear the cart if needed
    // cart.clearCart();

} catch (error) {
    console.error('Error:', error.message);
}
```
