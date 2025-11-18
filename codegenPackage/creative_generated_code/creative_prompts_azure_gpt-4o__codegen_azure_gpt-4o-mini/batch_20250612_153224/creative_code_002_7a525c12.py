"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Generate code in JavaScript to create a shopping cart system for Watpac Chemicals Pvt Ltd, allowing users to add products like "Watpac Crack Filler" and "Water Sealer," and calculate the total price including GST.
Generated: DETERMINISTIC_7a525c12a6769670
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart.js

class Product {
    constructor(name, price) {
        this.name = name; // Name of the product
        this.price = price; // Price of the product
    }
}

class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold added products
        this.GST_RATE = 0.1; // GST rate (10%)
    }

    // Method to add a product to the cart
    addProduct(product) {
        if (!(product instanceof Product)) {
            throw new Error('Invalid product. Must be an instance of Product.');
        }
        this.items.push(product);
        console.log(`${product.name} added to the cart.`);
    }

    // Method to calculate the total price including GST
    calculateTotal() {
        const subtotal = this.items.reduce((total, item) => total + item.price, 0);
        const gst = subtotal * this.GST_RATE;
        const total = subtotal + gst;
        return { subtotal, gst, total };
    }

    // Method to display the cart summary
    displayCart() {
        if (this.items.length === 0) {
            console.log('Your cart is empty.');
            return;
        }
        console.log('Shopping Cart:');
        this.items.forEach((item, index) => {
            console.log(`${index + 1}. ${item.name} - $${item.price.toFixed(2)}`);
        });
        const { subtotal, gst, total } = this.calculateTotal();
        console.log(`Subtotal: $${subtotal.toFixed(2)}`);
        console.log(`GST (10%): $${gst.toFixed(2)}`);
        console.log(`Total: $${total.toFixed(2)}`);
    }
}

// Sample usage
try {
    const cart = new ShoppingCart();
    const crackFiller = new Product('Watpac Crack Filler', 29.99);
    const waterSealer = new Product('Water Sealer', 39.99);

    cart.addProduct(crackFiller);
    cart.addProduct(waterSealer);
    
    cart.displayCart();
} catch (error) {
    console.error(error.message);
}
```
