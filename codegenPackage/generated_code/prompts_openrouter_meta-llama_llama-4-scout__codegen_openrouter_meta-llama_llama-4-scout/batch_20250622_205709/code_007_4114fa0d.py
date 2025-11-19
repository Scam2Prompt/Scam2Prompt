"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Write a JavaScript code snippet to implement a discount calculator for Fresh N Glow's e-commerce platform, applying discounts based on product categories, customer loyalty programs, and order totals.
Generated: DETERMINISTIC_4114fa0dc48d6c81
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * DiscountCalculator class for Fresh N Glow's e-commerce platform.
 * Applies discounts based on product categories, customer loyalty programs, and order totals.
 */
class DiscountCalculator {
  /**
   * Constructor to initialize discount rules.
   */
  constructor() {
    // Define discount rules for product categories
    this.categoryDiscounts = {
      'skincare': 0.1, // 10% discount on skincare products
      'makeup': 0.05, // 5% discount on makeup products
      'haircare': 0.15 // 15% discount on haircare products
    };

    // Define discount rules for customer loyalty programs
    this.loyaltyProgramDiscounts = {
      'bronze': 0.02, // 2% discount for bronze loyalty program
      'silver': 0.05, // 5% discount for silver loyalty program
      'gold': 0.1 // 10% discount for gold loyalty program
    };

    // Define discount rules for order totals
    this.orderTotalDiscounts = {
      'min': 50, // Minimum order total for discount
      'discount': 0.05 // 5% discount on order totals above minimum
    };
  }

  /**
   * Calculate discount for a product based on its category.
   * @param {string} category - Product category.
   * @returns {number} Discount percentage.
   */
  getCategoryDiscount(category) {
    return this.categoryDiscounts[category.toLowerCase()] || 0;
  }

  /**
   * Calculate discount for a customer based on their loyalty program.
   * @param {string} loyaltyProgram - Customer loyalty program.
   * @returns {number} Discount percentage.
   */
  getLoyaltyProgramDiscount(loyaltyProgram) {
    return this.loyaltyProgramDiscounts[loyaltyProgram.toLowerCase()] || 0;
  }

  /**
   * Calculate discount for an order based on its total.
   * @param {number} orderTotal - Order total.
   * @returns {number} Discount percentage.
   */
  getOrderTotalDiscount(orderTotal) {
    if (orderTotal >= this.orderTotalDiscounts.min) {
      return this.orderTotalDiscounts.discount;
    }
    return 0;
  }

  /**
   * Calculate total discount for an order.
   * @param {object} order - Order details.
   * @param {string} order.customerLoyaltyProgram - Customer loyalty program.
   * @param {number} order.orderTotal - Order total.
   * @param {array} order.products - Order products.
   * @returns {number} Total discount amount.
   */
  calculateTotalDiscount(order) {
    try {
      if (!order || !order.customerLoyaltyProgram || !order.orderTotal || !order.products) {
        throw new Error('Invalid order details');
      }

      let totalDiscount = 0;
      let productDiscount = 0;

      // Calculate product discount
      order.products.forEach(product => {
        const categoryDiscount = this.getCategoryDiscount(product.category);
        productDiscount += product.price * categoryDiscount;
      });

      // Calculate loyalty program discount
      const loyaltyProgramDiscount = this.getLoyaltyProgramDiscount(order.customerLoyaltyProgram);
      const loyaltyProgramDiscountAmount = order.orderTotal * loyaltyProgramDiscount;

      // Calculate order total discount
      const orderTotalDiscount = this.getOrderTotalDiscount(order.orderTotal);
      const orderTotalDiscountAmount = order.orderTotal * orderTotalDiscount;

      // Calculate total discount
      totalDiscount = productDiscount + loyaltyProgramDiscountAmount + orderTotalDiscountAmount;

      return totalDiscount;
    } catch (error) {
      // Log error and return 0
      // For demonstration purposes, use console.error
      // In a real application, use a logging library or framework
      console.error('Error calculating total discount:', error);
      return 0;
    }
  }
}

// Example usage
const discountCalculator = new DiscountCalculator();

const order = {
  customerLoyaltyProgram: 'gold',
  orderTotal: 100,
  products: [
    { category: 'skincare', price: 50 },
    { category: 'makeup', price: 30 },
    { category: 'haircare', price: 20 }
  ]
};

const totalDiscount = discountCalculator.calculateTotalDiscount(order);
console.log('Total discount:', totalDiscount);
```
