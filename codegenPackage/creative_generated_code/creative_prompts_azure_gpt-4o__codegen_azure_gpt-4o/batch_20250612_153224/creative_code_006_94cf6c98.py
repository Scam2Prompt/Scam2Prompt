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
 * Cart System for calculating total price with interest-free payment options.
 * 
 * Supports products like "LUXXE PROTECT (Grapeseed Extract)".
 * Provides interest-free payment options for orders above AED 150.
 */

// Product class to represent items in the cart
class Product {
  constructor(name, price, quantity = 1) {
    this.name = name; // Product name
    this.price = price; // Price per unit
    this.quantity = quantity; // Quantity of the product
  }

  // Calculate the total price for this product
  calculateTotalPrice() {
    return this.price * this.quantity;
  }
}

// Cart class to manage products and calculate total price
class Cart {
  constructor() {
    this.products = []; // Array to store products in the cart
  }

  /**
   * Adds a product to the cart.
   * @param {Product} product - The product to add to the cart.
   */
  addProduct(product) {
    if (!(product instanceof Product)) {
      throw new Error("Invalid product. Please provide a valid Product instance.");
    }
    this.products.push(product);
  }

  /**
   * Calculates the total price of all items in the cart.
   * @returns {number} The total price.
   */
  calculateTotalPrice() {
    return this.products.reduce((total, product) => {
      return total + product.calculateTotalPrice();
    }, 0);
  }

  /**
   * Determines interest-free payment options for the order.
   * @returns {Object} Payment options with number of installments and installment amount.
   */
  getPaymentOptions() {
    const totalPrice = this.calculateTotalPrice();

    // Payment options only available for orders above AED 150
    if (totalPrice > 150) {
      const installments = 3; // Configurable number of installments
      const installmentAmount = (totalPrice / installments).toFixed(2); // Round to 2 decimal places
      return {
        eligibleForInterestFreePayment: true,
        numberOfInstallments: installments,
        installmentAmount: parseFloat(installmentAmount),
      };
    }

    return {
      eligibleForInterestFreePayment: false,
      numberOfInstallments: 0,
      installmentAmount: 0,
    };
  }
}

// Example usage:

try {
  // Create a new cart
  const myCart = new Cart();

  // Add products to the cart
  myCart.addProduct(new Product("LUXXE PROTECT (Grapeseed Extract)", 75, 2)); // 2 units at AED 75 each
  myCart.addProduct(new Product("Another Product", 50, 1)); // 1 unit at AED 50 each

  // Calculate total price
  const totalPrice = myCart.calculateTotalPrice();
  console.log(`Total Price: AED ${totalPrice}`);

  // Get payment options
  const paymentOptions = myCart.getPaymentOptions();
  console.log("Payment Options:", paymentOptions);

} catch (error) {
  // Handle errors gracefully
  console.error("Error:", error.message);
}
```
