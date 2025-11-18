"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Generate code in JavaScript to implement a shopping cart system that calculates discounts for products like "Man's Rolex Submarine Full Green" and updates the total price dynamically.
Generated: DETERMINISTIC_41915a9f99a991e1
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Shopping Cart System

class Product {
    constructor(name, price, discount = 0) {
        this.name = name; // Product name
        this.price = price; // Original product price
        this.discount = discount; // Discount percentage (0-100)
    }

    // Method to calculate the discounted price
    getDiscountedPrice() {
        return this.price - (this.price * (this.discount / 100));
    }
}

class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold products in the cart
    }

    // Method to add a product to the cart
    addProduct(product) {
        if (!(product instanceof Product)) {
            throw new Error('Invalid product');
        }
        this.items.push(product);
    }

    // Method to calculate the total price of the cart
    calculateTotal() {
        return this.items.reduce((total, product) => {
            return total + product.getDiscountedPrice();
        }, 0);
    }

    // Method to remove a product from the cart
    removeProduct(productName) {
        const index = this.items.findIndex(item => item.name === productName);
        if (index === -1) {
            throw new Error('Product not found in cart');
        }
        this.items.splice(index, 1);
    }

    // Method to clear cart
    clearCart() {
        this.items = [];
    }
}

// Example usage

try {
    // Create products
    const rolex = new Product("Man's Rolex Submarine Full Green", 10000, 10);
    const appleWatch = new Product("Apple Watch Series 7", 750, 15);

    // Create shopping cart
    const cart = new ShoppingCart();

    // Add products to the cart
    cart.addProduct(rolex);
    cart.addProduct(appleWatch);

    // Calculate total price
    console.log(`Total Price: $${cart.calculateTotal().toFixed(2)}`);

    // Remove a product
    cart.removeProduct("Apple Watch Series 7");
    console.log(`Total Price after removing Apple Watch: $${cart.calculateTotal().toFixed(2)}`);
    
    // Clear the cart
    cart.clearCart();
    console.log(`Total Price after clearing cart: $${cart.calculateTotal().toFixed(2)}`);
    
} catch (error) {
    console.error('Error:', error.message);
}
```
