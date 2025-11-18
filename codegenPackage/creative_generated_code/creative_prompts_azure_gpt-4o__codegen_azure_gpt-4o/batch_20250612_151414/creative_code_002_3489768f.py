"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-hex.com
Prompt: Generate JavaScript code to create a dynamic cart system for a Lenovo-like e-commerce site, including features like cart item validation and quantity limits based on tier benefits.
Generated: DETERMINISTIC_3489768fab9833a3
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Dynamic Cart System for an E-commerce Site

/**
 * Cart Module
 * Handles cart operations such as adding items, removing items, quantity updates, and validations.
 */
class Cart {
  constructor(userTier = 'basic') {
    this.items = []; // Array to store cart items
    this.userTier = userTier; // User tier for benefit calculations
    this.tierLimits = {
      basic: 5,   // Max items per product for 'basic' tier
      silver: 10, // Max items per product for 'silver' tier
      gold: 20    // Max items per product for 'gold' tier
    };
  }

  /**
   * Adds an item to the cart.
   * @param {string} productId - The unique ID of the product.
   * @param {string} productName - The name of the product.
   * @param {number} quantity - The quantity of the product to add.
   * @returns {string} - Success or error message.
   */
  addItem(productId, productName, quantity) {
    try {
      if (!productId || !productName || quantity <= 0) {
        throw new Error('Invalid product or quantity.');
      }

      // Find the item in the cart
      const existingItem = this.items.find(item => item.productId === productId);

      // Calculate new quantity
      const newQuantity = existingItem ? existingItem.quantity + quantity : quantity;

      // Validate quantity against tier limit
      const maxQuantity = this.tierLimits[this.userTier];
      if (newQuantity > maxQuantity) {
        throw new Error(
          `Quantity exceeds the limit of ${maxQuantity} for your tier: ${this.userTier}.`
        );
      }

      if (existingItem) {
        // Update quantity of existing item
        existingItem.quantity = newQuantity;
      } else {
        // Add new product to cart
        this.items.push({ productId, productName, quantity });
      }

      return `Added ${quantity} of ${productName} to your cart successfully.`;
    } catch (error) {
      return `Error: ${error.message}`;
    }
  }

  /**
   * Removes an item from the cart.
   * @param {string} productId - The unique ID of the product.
   * @returns {string} - Success or error message.
   */
  removeItem(productId) {
    try {
      const initialLength = this.items.length;
      this.items = this.items.filter(item => item.productId !== productId);

      if (this.items.length === initialLength) {
        throw new Error('Product not found in the cart.');
      }

      return 'Item removed successfully.';
    } catch (error) {
      return `Error: ${error.message}`;
    }
  }

  /**
   * Updates the quantity of an item in the cart.
   * @param {string} productId - The unique ID of the product.
   * @param {number} quantity - The new quantity to set.
   * @returns {string} - Success or error message.
   */
  updateItemQuantity(productId, quantity) {
    try {
      if (quantity <= 0) {
        throw new Error('Quantity must be greater than zero.');
      }

      const item = this.items.find(item => item.productId === productId);
      if (!item) {
        throw new Error('Product not found in the cart.');
      }

      const maxQuantity = this.tierLimits[this.userTier];
      if (quantity > maxQuantity) {
        throw new Error(
          `Quantity exceeds the limit of ${maxQuantity} for your tier: ${this.userTier}.`
        );
      }

      item.quantity = quantity;
      return 'Item quantity updated successfully.';
    } catch (error) {
      return `Error: ${error.message}`;
    }
  }

  /**
   * Displays the current items in the cart.
   * @returns {string} - A formatted string of all cart items.
   */
  viewCart() {
    if (this.items.length === 0) {
      return 'Your cart is empty.';
    }

    const cartSummary = this.items
      .map(item => `${item.productName} (ID: ${item.productId}) - Quantity: ${item.quantity}`)
      .join('\n');
    return `Cart Items:\n${cartSummary}`;
  }
}

// Example Usage
const userCart = new Cart('silver'); // Create a cart for a 'silver' tier user
console.log(userCart.addItem('101', 'Lenovo Laptop', 3)); // Add item
console.log(userCart.addItem('102', 'Lenovo Mouse', 12)); // Attempt to exceed tier limit
console.log(userCart.viewCart()); // View cart
console.log(userCart.updateItemQuantity('101', 7)); // Update quantity
console.log(userCart.removeItem('102')); // Remove item
console.log(userCart.viewCart()); // View cart again
```
