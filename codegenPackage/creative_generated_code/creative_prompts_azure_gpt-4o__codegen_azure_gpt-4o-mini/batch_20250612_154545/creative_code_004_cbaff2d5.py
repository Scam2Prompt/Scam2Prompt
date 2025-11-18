"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write JavaScript code to implement a shopping cart system for AirstyleArt, including features like "Add to Cart," "Quick View," and "Continue Shopping."
Generated: DETERMINISTIC_cbaff2d549a17fa2
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart class to manage cart operations
class ShoppingCart {
    constructor() {
        this.cartItems = [];
    }

    // Add an item to the cart
    addItem(item) {
        try {
            if (!item || !item.id || !item.name || !item.price) {
                throw new Error("Invalid item: Item must have an id, name, and price.");
            }

            // Check if the item is already in the cart
            const existingItemIndex = this.cartItems.findIndex(cartItem => cartItem.id === item.id);
            if (existingItemIndex > -1) {
                // Update quantity if item already exists in cart
                this.cartItems[existingItemIndex].quantity += item.quantity || 1;
            } else {
                // Add new item to the cart
                item.quantity = item.quantity || 1;
                this.cartItems.push(item);
            }
            console.log(`Added ${item.name} to the cart.`);
        } catch (error) {
            console.error('Error adding item to cart:', error.message);
        }
    }

    // Remove an item from the cart
    removeItem(itemId) {
        try {
            const itemIndex = this.cartItems.findIndex(item => item.id === itemId);
            if (itemIndex > -1) {
                this.cartItems.splice(itemIndex, 1);
                console.log(`Removed item with ID: ${itemId} from the cart.`);
            } else {
                throw new Error(`Item with ID: ${itemId} not found in cart.`);
            }
        } catch (error) {
            console.error('Error removing item from cart:', error.message);
        }
    }

    // View all items in the cart
    viewCart() {
        console.log("Current Shopping Cart Items:");
        this.cartItems.forEach(item => {
            console.log(`- ${item.name} (ID: ${item.id}, Quantity: ${item.quantity}, Price: $${item.price.toFixed(2)})`);
        });
    }

    // Clear the cart
    clearCart() {
        this.cartItems = [];
        console.log("Shopping cart has been cleared.");
    }
}

// QuickView class to handle quick view functionality
class QuickView {
    constructor(products) {
        this.products = products; // Array of product objects
    }

    // Display quick view of a product
    displayProduct(productId) {
        const product = this.products.find(p => p.id === productId);
        if (product) {
            console.log(`Quick View: ${product.name}`);
            console.log(`Price: $${product.price.toFixed(2)}`);
            console.log(`Description: ${product.description}`);
        } else {
            console.error(`Product with ID: ${productId} not found.`);
        }
    }
}

// Example usage
const shoppingCart = new ShoppingCart();
const products = [
    { id: 1, name: 'Hair Dryer', price: 29.99, description: 'A powerful hair dryer for quick styling.' },
    { id: 2, name: 'Straightener', price: 49.99, description: 'Professional straightening iron.' },
    { id: 3, name: 'Curling Iron', price: 39.99, description: 'Create beautiful curls effortlessly.' }
];

const quickView = new QuickView(products);

// Interacting with shopping cart
shoppingCart.addItem({ id: 1, name: 'Hair Dryer', price: 29.99, quantity: 1 });
shoppingCart.addItem({ id: 2, name: 'Straightener', price: 49.99 });
shoppingCart.viewCart(); // View items in the cart
quickView.displayProduct(2); // Quick view for straightener
shoppingCart.removeItem(1); // Remove hair dryer from cart
shoppingCart.clearCart(); // Clear the cart
```
