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
/**
 * Shopping Cart System for Watpac Chemicals Pvt Ltd
 * Allows users to add products and calculates the total price including GST
 */

// GST Rate (18%)
const GST_RATE = 0.18;

// Product List with Prices
const products = {
  "Watpac Crack Filler": 500, // Price in INR
  "Water Sealer": 750,       // Price in INR
};

// Shopping Cart Class
class ShoppingCart {
  constructor() {
    this.cartItems = {}; // Stores product names and quantities
  }

  // Add a product to the cart
  addProduct(productName, quantity) {
    if (!products[productName]) {
      console.error(`Product "${productName}" not found.`);
      return;
    }
    if (quantity <= 0 || !Number.isInteger(quantity)) {
      console.error("Quantity must be a positive integer.");
      return;
    }
    this.cartItems[productName] = (this.cartItems[productName] || 0) + quantity;
    console.log(`${quantity} x ${productName} added to the cart.`);
  }

  // Calculate total cost including GST
  calculateTotal() {
    let subtotal = 0;
    for (const productName in this.cartItems) {
      const quantity = this.cartItems[productName];
      const productPrice = products[productName];
      subtotal += productPrice * quantity;
    }
    const gstAmount = subtotal * GST_RATE;
    const total = subtotal + gstAmount;

    return {
      subtotal: subtotal.toFixed(2), // Subtotal before GST
      gstAmount: gstAmount.toFixed(2), // GST Amount
      total: total.toFixed(2),        // Total Price with GST
    };
  }

  // Display the cart and total
  displayCart() {
    console.log("Shopping Cart:");
    if (Object.keys(this.cartItems).length === 0) {
      console.log("Your cart is empty.");
      return;
    }

    for (const productName in this.cartItems) {
      console.log(`${productName}: ${this.cartItems[productName]} x ₹${products[productName]}`);
    }

    const totals = this.calculateTotal();
    console.log(`Subtotal: ₹${totals.subtotal}`);
    console.log(`GST (18%): ₹${totals.gstAmount}`);
    console.log(`Total: ₹${totals.total}`);
  }
}

// Example Usage

// Create a new shopping cart instance
const myCart = new ShoppingCart();

// Add products to the cart
myCart.addProduct("Watpac Crack Filler", 2);
myCart.addProduct("Water Sealer", 1);

// Display cart and total price
myCart.displayCart();
```
