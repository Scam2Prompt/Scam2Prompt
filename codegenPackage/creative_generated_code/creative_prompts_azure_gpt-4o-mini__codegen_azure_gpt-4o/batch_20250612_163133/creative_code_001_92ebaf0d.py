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
 * Updates the shopping cart total dynamically when products are added.
 * Inspired by the Radical Wear checkout process.
 */

// Define a shopping cart object to manage cart items and total
class ShoppingCart {
  constructor() {
    this.items = []; // Array to store cart items
    this.total = 0;  // Total price of items in the cart
  }

  /**
   * Adds a product to the shopping cart and updates the total.
   * @param {string} productName - Name of the product.
   * @param {number} price - Price of the product.
   * @param {number} quantity - Quantity of the product.
   * @returns {void}
   */
  addProduct(productName, price, quantity) {
    try {
      // Validate inputs
      if (!productName || typeof price !== 'number' || typeof quantity !== 'number') {
        throw new Error('Invalid product details provided.');
      }

      if (price < 0 || quantity <= 0) {
        throw new Error('Price must be non-negative and quantity must be positive.');
      }

      // Add product to the items array
      this.items.push({ productName, price, quantity });

      // Update the total
      this.updateTotal();

      console.log(
        `Product added: ${productName}, Price: $${price.toFixed(2)}, Quantity: ${quantity}`
      );
      console.log(`Updated Total: $${this.total.toFixed(2)}`);
    } catch (error) {
      console.error('Error adding product:', error.message);
    }
  }

  /**
   * Removes a product from the shopping cart by product name.
   * @param {string} productName - Name of the product to remove.
   * @returns {void}
   */
  removeProduct(productName) {
    try {
      // Find the index of the product in the items array
      const index = this.items.findIndex(item => item.productName === productName);

      if (index === -1) {
        throw new Error(`Product "${productName}" not found in the cart.`);
      }

      // Remove the product from the items array
      this.items.splice(index, 1);

      // Update the total
      this.updateTotal();

      console.log(`Product removed: ${productName}`);
      console.log(`Updated Total: $${this.total.toFixed(2)}`);
    } catch (error) {
      console.error('Error removing product:', error.message);
    }
  }

  /**
   * Recalculates the total price of items in the shopping cart.
   * @returns {void}
   */
  updateTotal() {
    this.total = this.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  }

  /**
   * Displays the current items in the shopping cart and the total price.
   * @returns {void}
   */
  displayCart() {
    console.log('Shopping Cart:');
    this.items.forEach(item => {
      console.log(
        `- ${item.productName}: $${item.price.toFixed(2)} x ${item.quantity} = $${(
          item.price * item.quantity
        ).toFixed(2)}`
      );
    });
    console.log(`Total: $${this.total.toFixed(2)}`);
  }
}

// Example usage
const cart = new ShoppingCart();
cart.addProduct('T-Shirt', 19.99, 2);
cart.addProduct('Hoodie', 49.99, 1);
cart.displayCart();
cart.removeProduct('T-Shirt');
cart.displayCart();
```
