"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Develop a shopping cart system in JavaScript that mimics the "Shto ne Shporte" (Add to Cart) feature described on TaniPhone.com.
Generated: DETERMINISTIC_7f80b8cfc9455fcd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Shopping Cart System

class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.cart = [];
    }

    // Adds a product to the cart
    addItem(product) {
        if (!product || !product.id || !product.name || product.price < 0) {
            throw new Error("Invalid product. Please provide a valid product object.");
        }

        // Check if the product is already in the cart
        const existingProductIndex = this.cart.findIndex(item => item.id === product.id);

        if (existingProductIndex !== -1) {
            // Update the quantity of the existing product
            this.cart[existingProductIndex].quantity += 1;
        } else {
            // Add new product to the cart
            this.cart.push({ ...product, quantity: 1 });
        }

        console.log(`${product.name} has been added to the cart.`);
    }

    // Removes a product from the cart
    removeItem(productId) {
        const productIndex = this.cart.findIndex(item => item.id === productId);
        
        if (productIndex === -1) {
            throw new Error("Product not found in the cart.");
        }

        // Remove the product from the cart
        this.cart.splice(productIndex, 1);
        console.log(`Product with ID ${productId} has been removed from the cart.`);
    }

    // Gets the current items in the cart
    getItems() {
        return this.cart;
    }

    // Calculates the total price of items in the cart
    calculateTotal() {
        return this.cart.reduce((total, item) => total + (item.price * item.quantity), 0).toFixed(2);
    }

    // Displays the cart contents in a readable format
    displayCart() {
        if (this.cart.length === 0) {
            console.log("Your shopping cart is empty.");
            return;
        }

        console.log("Shopping Cart Items:");
        this.cart.forEach(item => {
            console.log(`- ${item.name} (ID: ${item.id}) - Price: $${item.price} x ${item.quantity}`);
        });
        console.log(`Total Amount: $${this.calculateTotal()}`);
    }
}

// Example usage:
try {
    const cart = new ShoppingCart();

    // Sample products
    const product1 = { id: 1, name: "iPhone 13", price: 799.99 };
    const product2 = { id: 2, name: "AirPods Pro", price: 249.99 };

    // Adding items to the cart
    cart.addItem(product1);
    cart.addItem(product2);
    cart.addItem(product1); // Adding the same product again

    // Displaying the cart contents
    cart.displayCart();

    // Removing an item from the cart
    cart.removeItem(1); // Remove iPhone 13
    cart.displayCart();

} catch (error) {
    console.error("Error:", error.message);
}
```
