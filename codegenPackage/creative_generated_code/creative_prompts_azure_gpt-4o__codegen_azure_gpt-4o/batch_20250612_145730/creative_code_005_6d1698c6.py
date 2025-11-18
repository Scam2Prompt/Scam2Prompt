"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Create a function in JavaScript to dynamically update a shopping cart when users add PEKANA products like "PK 81 NEOCARD" or "PK 45 AKUTUR" to their cart.
Generated: DETERMINISTIC_6d1698c6fb8d59a5
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Shopping Cart Module
 * This module provides functionality to dynamically update a shopping cart
 * when users add PEKANA products.
 */

// Shopping cart object to store items
const shoppingCart = {
  items: [], // List of items in the cart
  totalQuantity: 0, // Total number of items in the cart
  totalPrice: 0, // Total price of all items in the cart

  /**
   * Adds a product to the shopping cart.
   * @param {string} productName - Name of the PEKANA product to add.
   * @param {number} quantity - Quantity of the product to add.
   * @param {number} price - Price of the product (per unit).
   */
  addProduct(productName, quantity, price) {
    try {
      // Validate input parameters
      if (typeof productName !== "string" || productName.trim() === "") {
        throw new Error("Invalid product name.");
      }
      if (typeof quantity !== "number" || quantity <= 0) {
        throw new Error("Quantity must be a positive number.");
      }
      if (typeof price !== "number" || price <= 0) {
        throw new Error("Price must be a positive number.");
      }

      // Check if product already exists in the cart
      const existingProductIndex = this.items.findIndex(
        (item) => item.productName === productName
      );

      if (existingProductIndex !== -1) {
        // Update quantity and total price for existing product
        this.items[existingProductIndex].quantity += quantity;
        this.items[existingProductIndex].totalPrice += quantity * price;
      } else {
        // Add new product to the cart
        this.items.push({
          productName: productName,
          quantity: quantity,
          unitPrice: price,
          totalPrice: quantity * price,
        });
      }

      // Update cart totals
      this.totalQuantity += quantity;
      this.totalPrice += quantity * price;

      console.log(`Product "${productName}" added to the cart.`);
      console.log("Cart updated successfully.");
    } catch (error) {
      // Log error to console
      console.error("Error adding product to cart:", error.message);
    }
  },

  /**
   * Displays the current state of the shopping cart.
   */
  displayCart() {
    console.log("Shopping Cart:");
    console.table(this.items);
    console.log(`Total Quantity: ${this.totalQuantity}`);
    console.log(`Total Price: $${this.totalPrice.toFixed(2)}`);
  },
};

// Example usage
shoppingCart.addProduct("PK 81 NEOCARD", 2, 19.99); // Add 2 PK 81 NEOCARD to the cart
shoppingCart.addProduct("PK 45 AKUTUR", 1, 14.99); // Add 1 PK 45 AKUTUR to the cart
shoppingCart.addProduct("PK 81 NEOCARD", 1, 19.99); // Add 1 more PK 81 NEOCARD to the cart

shoppingCart.displayCart(); // Display the current state of the shopping cart
```
