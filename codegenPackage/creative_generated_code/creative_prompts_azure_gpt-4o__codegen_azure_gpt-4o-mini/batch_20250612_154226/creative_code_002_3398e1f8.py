"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Create a function in JavaScript to dynamically update the "Wall Memes" shopping cart when a user adds or removes products, ensuring compatibility with PrestaShop-based platforms.
Generated: DETERMINISTIC_3398e1f8e543913d
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart class to manage products in the "Wall Memes" shopping cart.
 */
class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.cart = [];
    }
    
    /**
     * Adds a product to the shopping cart.
     * @param {Object} product - The product object to add.
     * @throws Will throw an error if the product is invalid.
     */
    addProduct(product) {
        // Validate product before adding
        if (!this.isValidProduct(product)) {
            throw new Error("Invalid product");
        }
        
        // Check if product already exists in the cart
        const existingProductIndex = this.cart.findIndex(item => item.id === product.id);
        if (existingProductIndex >= 0) {
            // Update quantity if product exists
            this.cart[existingProductIndex].quantity += product.quantity;
        } else {
            // Add new product to the cart
            this.cart.push({ ...product, quantity: product.quantity });
        }

        // Update the cart display
        this.updateCartDisplay();
    }
    
    /**
     * Removes a product from the shopping cart.
     * @param {number} productId - The ID of the product to remove.
     * @throws Will throw an error if the product ID is invalid.
     */
    removeProduct(productId) {
        // Validate product ID
        if (typeof productId !== 'number') {
            throw new Error("Invalid product ID");
        }

        // Filter out the product to be removed
        this.cart = this.cart.filter(item => item.id !== productId);

        // Update the cart display
        this.updateCartDisplay();
    }
    
    /**
     * Validates the product object.
     * @param {Object} product - The product object to validate.
     * @returns {boolean} - True if valid, false otherwise.
     */
    isValidProduct(product) {
        return product && product.id && product.quantity && product.quantity > 0;
    }

    /**
     * Updates the shopping cart display on the webpage.
     * (Placeholder function for integrating with PrestaShop)
     */
    updateCartDisplay() {
        // Here, you would update the cart UI in your PrestaShop theme,
        // e.g., updating the cart icon, total items, etc.
        console.log("Cart updated:", this.cart);
        // Implement specific DOM manipulation for PrestaShop as needed
    }
}

// Example usage
const cart = new ShoppingCart();

try {
    cart.addProduct({ id: 1, name: "Funny Meme", quantity: 2 });
    cart.addProduct({ id: 2, name: "Silly Meme", quantity: 1 });
    cart.removeProduct(1);
} catch (error) {
    console.error(error.message);
}
```
