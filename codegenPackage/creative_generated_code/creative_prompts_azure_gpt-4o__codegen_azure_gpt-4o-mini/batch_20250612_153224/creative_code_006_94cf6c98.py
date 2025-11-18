"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Create a JavaScript function to implement a cart system for products like "LUXXE PROTECT (Grapeseed Extract)" that calculates the total price, including interest-free payment options for orders above AED 150.
Generated: DETERMINISTIC_94cf6c984dd6ee4e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cart class to manage products and calculate the total price.
 */
class Cart {
    constructor() {
        this.items = [];
        this.totalPrice = 0;
    }

    /**
     * Adds a product to the cart.
     * @param {Object} product - The product to add
     * @param {string} product.name - The name of the product
     * @param {number} product.price - The price of the product
     * @param {number} product.quantity - The quantity of the product
     */
    addProduct(product) {
        try {
            if (!product.name || product.price < 0 || product.quantity < 1) {
                throw new Error("Invalid product details");
            }

            this.items.push(product);
            this.calculateTotal();
        } catch (error) {
            console.error("Error adding product:", error.message);
        }
    }

    /**
     * Calculates the total price of all products in the cart.
     */
    calculateTotal() {
        this.totalPrice = this.items.reduce((total, item) => {
            return total + (item.price * item.quantity);
        }, 0);
    }

    /**
     * Retrieves the total price with a payment option message if applicable.
     * @returns {Object} - An object containing total price and payment option message
     */
    getTotalPrice() {
        let paymentOptions = '';

        if (this.totalPrice > 150) {
            paymentOptions = "Interest-free payment options are available.";
        }

        return {
            totalPrice: this.totalPrice.toFixed(2), // Formatted to two decimal places
            paymentOptions: paymentOptions
        };
    }

    /**
     * Clears the cart.
     */
    clearCart() {
        this.items = [];
        this.totalPrice = 0;
    }
}

// Example Usage:
const cart = new Cart();
cart.addProduct({ name: "LUXXE PROTECT (Grapeseed Extract)", price: 75, quantity: 2 });
cart.addProduct({ name: "Product 2", price: 50, quantity: 1 });

const totalInfo = cart.getTotalPrice();
console.log(`Total Price: AED ${totalInfo.totalPrice}`);
if (totalInfo.paymentOptions) {
    console.log(totalInfo.paymentOptions);
}

// Clear the cart after use (if needed)
cart.clearCart();
```
