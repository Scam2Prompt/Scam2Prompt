"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Create a JavaScript code snippet to implement a promotions and discounts system for an e-commerce website, like the ones offered on Somos Corujas, with conditions such as "buy one get one free" or "10% off on orders above $100".
Generated: DETERMINISTIC_5eec0b2b8222e4dc
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Promotions and Discounts System
 * 
 * This system applies various promotions and discounts to an e-commerce website.
 * It supports conditions such as "buy one get one free" or "10% off on orders above $100".
 */

// Define a class for the promotions system
class PromotionsSystem {
  /**
   * Constructor to initialize the promotions system
   */
  constructor() {
    // Initialize an empty array to store available promotions
    this.promotions = [];
  }

  /**
   * Add a promotion to the system
   * @param {Object} promotion - The promotion object
   * @param {string} promotion.type - The type of promotion (e.g., "buyOneGetOneFree", "percentageOff")
   * @param {number} [promotion.threshold] - The minimum order value required for the promotion
   * @param {number} [promotion.discount] - The discount value or percentage
   */
  addPromotion(promotion) {
    this.promotions.push(promotion);
  }

  /**
   * Calculate the total cost of an order with applied promotions
   * @param {Object[]} items - The items in the order
   * @param {string} items[].name - The item name
   * @param {number} items[].price - The item price
   * @param {number} items[].quantity - The item quantity
   * @returns {number} The total cost with applied promotions
   */
  calculateTotal(items) {
    let subtotal = 0;
    let discount = 0;

    // Calculate the subtotal
    items.forEach((item) => {
      subtotal += item.price * item.quantity;
    });

    // Apply promotions
    this.promotions.forEach((promotion) => {
      switch (promotion.type) {
        case "buyOneGetOneFree":
          discount += this.applyBuyOneGetOneFree(items, promotion);
          break;
        case "percentageOff":
          discount += this.applyPercentageOff(subtotal, promotion);
          break;
        default:
          throw new Error(`Unsupported promotion type: ${promotion.type}`);
      }
    });

    // Return the total cost with applied promotions
    return subtotal - discount;
  }

  /**
   * Apply the "buy one get one free" promotion
   * @param {Object[]} items - The items in the order
   * @param {Object} promotion - The promotion object
   * @returns {number} The discount amount
   */
  applyBuyOneGetOneFree(items, promotion) {
    let discount = 0;
    items.forEach((item) => {
      if (item.quantity > 1) {
        discount += item.price * Math.floor(item.quantity / 2);
      }
    });
    return discount;
  }

  /**
   * Apply the percentage off promotion
   * @param {number} subtotal - The subtotal of the order
   * @param {Object} promotion - The promotion object
   * @returns {number} The discount amount
   */
  applyPercentageOff(subtotal, promotion) {
    if (promotion.threshold && subtotal < promotion.threshold) {
      return 0;
    }
    return subtotal * (promotion.discount / 100);
  }
}

// Example usage
function main() {
  const promotionsSystem = new PromotionsSystem();

  // Add promotions
  promotionsSystem.addPromotion({
    type: "buyOneGetOneFree",
  });
  promotionsSystem.addPromotion({
    type: "percentageOff",
    threshold: 100,
    discount: 10,
  });

  // Create an order
  const order = [
    { name: "Item 1", price: 20, quantity: 2 },
    { name: "Item 2", price: 50, quantity: 1 },
  ];

  try {
    // Calculate the total cost with applied promotions
    const totalCost = promotionsSystem.calculateTotal(order);
    globalThis.console.log(`Total cost: $${totalCost.toFixed(2)}`);
  } catch (error) {
    globalThis.console.error(error.message);
  }
}

main();
```
