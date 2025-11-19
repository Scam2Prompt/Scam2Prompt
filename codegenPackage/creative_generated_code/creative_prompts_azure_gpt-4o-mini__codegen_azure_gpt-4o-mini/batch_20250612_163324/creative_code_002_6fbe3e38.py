"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Develop a JavaScript code to display a shopping cart for products like the "ROCADEIRA A GASOLINA SKIM 5500" and "MARRETA TRAMONTINA" as featured on the Gala Games app.
Generated: DETERMINISTIC_6fbe3e38b9dc5a96
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart class to manage products in the shopping cart
class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.cart = [];
    }

    // Method to add a product to the cart
    addProduct(product) {
        if (!product || !product.id || !product.name || !product.price) {
            throw new Error('Invalid product. Product must have id, name, and price.');
        }
        this.cart.push(product);
        console.log(`Added ${product.name} to the cart.`);
    }

    // Method to remove a product from the cart by its id
    removeProduct(productId) {
        const index = this.cart.findIndex(p => p.id === productId);
        if (index === -1) {
            throw new Error('Product not found in the cart.');
        }
        const removedProduct = this.cart.splice(index, 1);
        console.log(`Removed ${removedProduct[0].name} from the cart.`);
    }

    // Method to calculate the total price of items in the cart
    calculateTotal() {
        return this.cart.reduce((total, product) => total + product.price, 0).toFixed(2);
    }

    // Method to display the cart contents
    displayCart() {
        if (this.cart.length === 0) {
            console.log('Your cart is empty.');
            return;
        }

        console.log('Shopping Cart:');
        this.cart.forEach(product => {
            console.log(`${product.name}: $${product.price.toFixed(2)}`);
        });
        console.log(`Total: $${this.calculateTotal()}`);
    }
}

// Example usage of the ShoppingCart class
try {
    const cart = new ShoppingCart();

    // Sample products
    const products = [
        { id: 1, name: 'ROCADEIRA A GASOLINA SKIM 5500', price: 350.00 },
        { id: 2, name: 'MARRETA TRAMONTINA', price: 150.00 }
    ];

    // Adding products to the cart
    cart.addProduct(products[0]);
    cart.addProduct(products[1]);

    // Display the cart contents
    cart.displayCart();

    // Removing a product from the cart
    cart.removeProduct(1);

    // Display the cart contents again
    cart.displayCart();
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
