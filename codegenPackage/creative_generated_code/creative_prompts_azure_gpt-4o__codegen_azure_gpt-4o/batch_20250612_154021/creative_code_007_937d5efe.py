"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Generate JavaScript code for a shopping cart system that supports SmartPrice KE's product categories, including smartphones, gaming accessories, and Apple devices, with WhatsApp ordering integration.
Generated: DETERMINISTIC_937d5efe25ec24b5
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Shopping Cart System for SmartPrice KE
 * Supports product categories: smartphones, gaming accessories, Apple devices
 * Includes WhatsApp ordering integration
 */

// Product categories
const categories = {
  SMARTPHONES: "Smartphones",
  GAMING_ACCESSORIES: "Gaming Accessories",
  APPLE_DEVICES: "Apple Devices",
};

// Sample product catalog
const productCatalog = [
  { id: 1, name: "iPhone 14", category: categories.APPLE_DEVICES, price: 1200 },
  { id: 2, name: "Samsung Galaxy S23", category: categories.SMARTPHONES, price: 1000 },
  { id: 3, name: "PS5 DualSense Controller", category: categories.GAMING_ACCESSORIES, price: 75 },
  { id: 4, name: "AirPods Pro", category: categories.APPLE_DEVICES, price: 250 },
];

// Shopping cart
class ShoppingCart {
  constructor() {
    this.items = [];
  }

  /**
   * Add product to the cart
   * @param {Object} product - Product object from product catalog
   * @param {number} quantity - Quantity of product to add
   */
  addItem(product, quantity) {
    if (!product || quantity <= 0) {
      console.error("Invalid product or quantity.");
      return;
    }
    const existingItem = this.items.find((item) => item.product.id === product.id);
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.items.push({ product, quantity });
    }
    console.log(`${product.name} added to cart. Quantity: ${quantity}`);
  }

  /**
   * Remove product from the cart
   * @param {number} productId - ID of the product to remove
   */
  removeItem(productId) {
    this.items = this.items.filter((item) => item.product.id !== productId);
    console.log(`Product ID ${productId} removed from cart.`);
  }

  /**
   * Calculate the total price of items in the cart
   * @returns {number} Total price
   */
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.product.price * item.quantity, 0);
  }

  /**
   * Generate WhatsApp order message
   * @returns {string} WhatsApp message
   */
  generateWhatsAppMessage() {
    if (this.items.length === 0) {
      return "Your shopping cart is empty.";
    }
    let message = "Hello SmartPrice KE, I'd like to order the following products:\n\n";
    this.items.forEach((item) => {
      message += `${item.quantity}x ${item.product.name} - $${item.product.price * item.quantity}\n`;
    });
    message += `\nTotal: $${this.calculateTotal()}\nThank you!`;
    return message;
  }
}

// Example usage
const cart = new ShoppingCart();
cart.addItem(productCatalog[0], 1); // Add iPhone 14 to cart
cart.addItem(productCatalog[2], 2); // Add 2 PS5 DualSense Controllers to cart
console.log(`Total Price: $${cart.calculateTotal()}`);
console.log("WhatsApp Order:", cart.generateWhatsAppMessage());

// WhatsApp integration (Simulation)
/**
 * Send order via WhatsApp (replace with actual API call in production)
 * @param {string} message - WhatsApp message content
 */
function sendOrderViaWhatsApp(message) {
  const whatsappNumber = "+254700000000"; // Replace with SmartPrice KE's WhatsApp number
  console.log(`Sending order to WhatsApp: ${whatsappNumber}`);
  console.log(`Message:\n${message}`);
}

sendOrderViaWhatsApp(cart.generateWhatsAppMessage());
```
