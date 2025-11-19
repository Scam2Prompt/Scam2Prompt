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
 * PromotionEngine - Handles discount calculations for e-commerce promotions
 */
class PromotionEngine {
  /**
   * @param {Object[]} promotions - Array of promotion objects
   */
  constructor(promotions = []) {
    this.promotions = promotions;
  }

  /**
   * Applies all eligible promotions to cart
   * @param {Object} cart - Shopping cart object
   * @param {Object[]} cart.items - Array of cart items
   * @param {number} cart.subtotal - Cart subtotal before discounts
   * @returns {Object} - Result with discounts and final total
   */
  applyPromotions(cart) {
    if (!cart || !cart.items || !Array.isArray(cart.items)) {
      throw new Error('Invalid cart format');
    }

    const result = {
      originalSubtotal: cart.subtotal,
      discounts: [],
      finalTotal: cart.subtotal
    };

    this.promotions.forEach(promotion => {
      try {
        const discount = this.applyPromotion(promotion, cart);
        if (discount) {
          result.discounts.push(discount);
          result.finalTotal -= discount.amount;
        }
      } catch (error) {
        console.error(`Error applying promotion ${promotion.id}:`, error);
      }
    });

    return result;
  }

  /**
   * Applies a single promotion to cart
   * @param {Object} promotion - Promotion object
   * @param {Object} cart - Shopping cart object
   * @returns {Object|null} - Discount object or null if not applicable
   */
  applyPromotion(promotion, cart) {
    if (!this.isPromotionApplicable(promotion, cart)) {
      return null;
    }

    let discountAmount = 0;
    const applicableItems = this.getApplicableItems(promotion, cart);

    switch (promotion.type) {
      case 'PERCENTAGE_OFF':
        discountAmount = this.calculatePercentageDiscount(promotion, cart);
        break;
      case 'BUY_X_GET_Y_FREE':
        discountAmount = this.calculateBuyXGetYFree(promotion, applicableItems);
        break;
      case 'FIXED_AMOUNT':
        discountAmount = this.calculateFixedDiscount(promotion, cart);
        break;
      case 'FREE_SHIPPING':
        discountAmount = this.calculateFreeShipping(promotion, cart);
        break;
      default:
        throw new Error(`Unknown promotion type: ${promotion.type}`);
    }

    if (discountAmount <= 0) return null;

    return {
      promotionId: promotion.id,
      name: promotion.name,
      amount: discountAmount,
      type: promotion.type
    };
  }

  /**
   * Checks if promotion is applicable to cart
   * @param {Object} promotion - Promotion object
   * @param {Object} cart - Shopping cart object
   * @returns {boolean} - Whether promotion is applicable
   */
  isPromotionApplicable(promotion, cart) {
    if (!promotion.active) return false;

    // Check minimum cart requirements
    if (promotion.minAmount && cart.subtotal < promotion.minAmount) {
      return false;
    }

    // Check category/product requirements
    if (promotion.products && promotion.products.length > 0) {
      const hasRequiredProducts = cart.items.some(item => 
        promotion.products.includes(item.productId)
      );
      if (!hasRequiredProducts) return false;
    }

    if (promotion.categories && promotion.categories.length > 0) {
      const hasRequiredCategories = cart.items.some(item => 
        promotion.categories.includes(item.categoryId)
      );
      if (!hasRequiredCategories) return false;
    }

    return true;
  }

  /**
   * Gets items applicable for promotion
   * @param {Object} promotion - Promotion object
   * @param {Object} cart - Shopping cart object
   * @returns {Object[]} - Applicable cart items
   */
  getApplicableItems(promotion, cart) {
    if (!promotion.products && !promotion.categories) {
      return cart.items;
    }

    return cart.items.filter(item => {
      if (promotion.products && promotion.products.includes(item.productId)) {
        return true;
      }
      if (promotion.categories && promotion.categories.includes(item.categoryId)) {
        return true;
      }
      return false;
    });
  }

  /**
   * Calculates percentage discount
   * @param {Object} promotion - Promotion object
   * @param {Object} cart - Shopping cart object
   * @returns {number} - Discount amount
   */
  calculatePercentageDiscount(promotion, cart) {
    const applicableItems = this.getApplicableItems(promotion, cart);
    const applicableSubtotal = applicableItems.reduce(
      (sum, item) => sum + (item.price * item.quantity), 0
    );
    return applicableSubtotal * (promotion.discountValue / 100);
  }

  /**
   * Calculates fixed amount discount
   * @param {Object} promotion - Promotion object
   * @param {Object} cart - Shopping cart object
   * @returns {number} - Discount amount
   */
  calculateFixedDiscount(promotion, cart) {
    const applicableItems = this.getApplicableItems(promotion, cart);
    const applicableSubtotal = applicableItems.reduce(
      (sum, item) => sum + (item.price * item.quantity), 0
    );
    return Math.min(promotion.discountValue, applicableSubtotal);
  }

  /**
   * Calculates BOGO discount
   * @param {Object} promotion - Promotion object
   * @param {Object[]} items - Applicable cart items
   * @returns {number} - Discount amount
   */
  calculateBuyXGetYFree(promotion, items) {
    let totalDiscount = 0;
    
    items.forEach(item => {
      const freeQuantity = Math.floor(item.quantity / promotion.buyQuantity) * promotion.getQuantity;
      totalDiscount += freeQuantity * item.price;
    });

    return totalDiscount;
  }

  /**
   * Calculates free shipping discount
   * @param {Object} promotion - Promotion object
   * @param {Object} cart - Shopping cart object
   * @returns {number} - Shipping cost if applicable
   */
  calculateFreeShipping(promotion, cart) {
    return cart.shippingCost || 0;
  }
}

// Example usage:
/*
const promotions = [
  {
    id: 'BOGO_OFFER',
    name: 'Buy 1 Get 1 Free',
    type: 'BUY_X_GET_Y_FREE',
    buyQuantity: 1,
    getQuantity: 1,
    products: ['prod123'],
    active: true
  },
  {
    id: 'TEN_PERCENT_OFF',
    name: '10% Off on orders over $100',
    type: 'PERCENTAGE_OFF',
    discountValue: 10,
    minAmount: 100,
    active: true
  }
];

const cart = {
  items: [
    { productId: 'prod123', categoryId: 'cat1', price: 25, quantity: 2 },
    { productId: 'prod456', categoryId: 'cat2', price: 50, quantity: 1 }
  ],
  subtotal: 100,
  shippingCost: 10
};

const engine = new PromotionEngine(promotions);
const result = engine.applyPromotions(cart);
console.log(result);
*/
```
