"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://radical-wear.cz
Prompt: Write a function in JavaScript that updates the shopping cart total dynamically when products are added, inspired by the Radical Wear checkout process.
Generated: DETERMINISTIC_92ebaf0d456df245
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart class to manage cart items and calculate the total price.
 */
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold cart items
    }

    /**
     * Adds a product to the shopping cart.
     * @param {Object} product - The product to add, contains id, name, price, and quantity.
     * @throws Will throw an error if the product is invalid.
     */
    addProduct(product) {
        if (!product || !product.id || !product.name || !product.price || !product.quantity) {
            throw new Error('Invalid product details');
        }
        
        const existingProduct = this.items.find(item => item.id === product.id);
        
        if (existingProduct) {
            // If product already exists, update its quantity
            existingProduct.quantity += product.quantity;
        } else {
            // Add new product to the cart
            this.items.push({ ...product });
        }
        
        this.updateCartTotal(); // Update the cart total after adding the product
    }

    /**
     * Calculates the total price of items in the shopping cart.
     * @returns {number} Total price of items in the cart.
     */
    calculateTotal() {
        return this.items.reduce((total, item) => {
            return total + (item.price * item.quantity);
        }, 0);
    }

    /**
     * Updates the cart total and displays it to the user.
     */
    updateCartTotal() {
        const total = this.calculateTotal();
        console.log(`Cart Total: $${total.toFixed(2)}`); // Display total in console
        
        // You can also update a UI element here, e.g., document.getElementById('cart-total').innerText = `$${total.toFixed(2)}`;
    }

    /**
     * Clears the shopping cart.
     */
    clearCart() {
        this.items = [];
        this.updateCartTotal(); // Update total after clearing the cart
    }
}

// Example usage:
const cart = new ShoppingCart();

try {
    cart.addProduct({ id: 1, name: 'T-Shirt', price: 19.99, quantity: 2 });
    cart.addProduct({ id: 2, name: 'Jeans', price: 39.99, quantity: 1 });
    cart.addProduct({ id: 1, name: 'T-Shirt', price: 19.99, quantity: 1 }); // Update quantity for T-Shirt
} catch (error) {
    console.error(error.message); // Handle errors gracefully
}
```
