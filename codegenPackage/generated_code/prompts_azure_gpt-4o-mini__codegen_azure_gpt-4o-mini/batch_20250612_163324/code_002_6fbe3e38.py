"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Develop a JavaScript code to display a shopping cart for products like the "ROCADEIRA A GASOLINA SKIM 5500" and "MARRETA TRAMONTINA" as featured on the Gala Games app.
Generated: DETERMINISTIC_6fbe3e38b9dc5a96
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ShoppingCart class to manage the shopping cart functionality
class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.cart = [];
    }

    // Method to add a product to the cart
    addProduct(product) {
        if (!product || !product.id || !product.name || !product.price) {
            throw new Error("Invalid product. Product must have id, name, and price.");
        }
        this.cart.push(product);
        console.log(`${product.name} has been added to the cart.`);
    }

    // Method to remove a product from the cart by id
    removeProduct(productId) {
        const initialLength = this.cart.length;
        this.cart = this.cart.filter(product => product.id !== productId);
        if (this.cart.length < initialLength) {
            console.log(`Product with id ${productId} has been removed from the cart.`);
        } else {
            console.warn(`Product with id ${productId} not found in the cart.`);
        }
    }

    // Method to calculate the total price of the cart
    calculateTotal() {
        return this.cart.reduce((total, product) => total + product.price, 0).toFixed(2);
    }

    // Method to display the cart contents
    displayCart() {
        if (this.cart.length === 0) {
            console.log("Your cart is empty.");
            return;
        }
        console.log("Shopping Cart Contents:");
        this.cart.forEach(product => {
            console.log(`- ${product.name}: $${product.price.toFixed(2)}`);
        });
        console.log(`Total: $${this.calculateTotal()}`);
    }
}

// Example products
const product1 = { id: 1, name: "ROCADEIRA A GASOLINA SKIM 5500", price: 299.99 };
const product2 = { id: 2, name: "MARRETA TRAMONTINA", price: 49.99 };

// Create a new shopping cart instance
const myCart = new ShoppingCart();

try {
    // Add products to the cart
    myCart.addProduct(product1);
    myCart.addProduct(product2);

    // Display the cart
    myCart.displayCart();

    // Remove a product from the cart
    myCart.removeProduct(1);

    // Display the cart again
    myCart.displayCart();
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
