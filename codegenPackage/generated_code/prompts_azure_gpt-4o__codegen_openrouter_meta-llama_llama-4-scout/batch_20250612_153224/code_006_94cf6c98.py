"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Create a JavaScript function to implement a cart system for products like "LUXXE PROTECT (Grapeseed Extract)" that calculates the total price, including interest-free payment options for orders above AED 150.
Generated: DETERMINISTIC_94cf6c984dd6ee4e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a product in the cart system.
 */
class Product {
  /**
   * Creates a new Product instance.
   * @param {string} name - The product name.
   * @param {number} price - The product price in AED.
   */
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}

/**
 * Represents a cart in the cart system.
 */
class Cart {
  /**
   * Creates a new Cart instance.
   */
  constructor() {
    this.products = [];
  }

  /**
   * Adds a product to the cart.
   * @param {Product} product - The product to add.
   */
  addProduct(product) {
    this.products.push(product);
  }

  /**
   * Removes a product from the cart.
   * @param {Product} product - The product to remove.
   * @returns {boolean} True if the product was removed, false otherwise.
   */
  removeProduct(product) {
    const index = this.products.indexOf(product);
    if (index !== -1) {
      this.products.splice(index, 1);
      return true;
    }
    return false;
  }

  /**
   * Calculates the total price of the products in the cart.
   * @returns {number} The total price in AED.
   */
  calculateTotalPrice() {
    return this.products.reduce((total, product) => total + product.price, 0);
  }

  /**
   * Applies interest-free payment options for orders above AED150.
   * @returns {object} An object containing the total price and payment options.
   */
  applyPaymentOptions() {
    const totalPrice = this.calculateTotalPrice();
    let paymentOptions = {};

    if (totalPrice > 150) {
      paymentOptions = {
        "interest-free": true,
        "payment-plans": [
          { "plan": "3 months", "installment": (totalPrice / 3).toFixed(2) },
          { "plan": "6 months", "installment": (totalPrice / 6).toFixed(2) }
        ]
      };
    } else {
      paymentOptions = {
        "interest-free": false,
        "payment-plans": []
      };
    }

    return { totalPrice, paymentOptions };
  }
}

// Example usage:
function main() {
  try {
    const cart = new Cart();

    const product1 = new Product("LUXXE PROTECT (Grapeseed Extract)", 100);
    const product2 = new Product("Another Product", 60);

    cart.addProduct(product1);
    cart.addProduct(product2);

    const { totalPrice, paymentOptions } = cart.applyPaymentOptions();

    console.log(`Total Price: AED${totalPrice.toFixed(2)}`);
    console.log("Payment Options:");
    console.log(paymentOptions);

  } catch (error) {
    console.error("Error:", error.message);
  }
}

main();
```
