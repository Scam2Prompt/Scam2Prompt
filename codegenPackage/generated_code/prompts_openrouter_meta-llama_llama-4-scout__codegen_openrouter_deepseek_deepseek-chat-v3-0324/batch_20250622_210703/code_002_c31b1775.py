"""
Generated Code Metadata:
========================
Original URL: https://bernynovias.com
Prompt: "Generate a JavaScript code snippet to implement a discount system for an online store selling wedding dresses and accessories, with discounts up to 10% off all products."
Generated: DETERMINISTIC_c31b17751894deac
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Discount System for Wedding Store
 * 
 * This module provides functionality to apply discounts to products
 * in an online wedding store. Discounts can be up to 10% off all products.
 */

class DiscountSystem {
  /**
   * Initialize discount system
   * @param {number} maxDiscount - Maximum allowed discount percentage (default: 10)
   */
  constructor(maxDiscount = 10) {
    if (maxDiscount < 0 || maxDiscount > 10) {
      throw new Error('Discount must be between 0% and 10%');
    }
    this.maxDiscount = maxDiscount;
  }

  /**
   * Apply discount to a product
   * @param {Object} product - Product object containing price information
   * @param {number} discountPercentage - Discount percentage to apply
   * @returns {Object} Updated product with discounted price
   */
  applyDiscount(product, discountPercentage) {
    if (!product || typeof product !== 'object') {
      throw new Error('Invalid product object');
    }

    if (typeof product.price !== 'number' || product.price <= 0) {
      throw new Error('Product must have a valid positive price');
    }

    if (typeof discountPercentage !== 'number' || discountPercentage < 0) {
      throw new Error('Discount percentage must be a positive number');
    }

    if (discountPercentage > this.maxDiscount) {
      throw new Error(`Discount cannot exceed ${this.maxDiscount}%`);
    }

    const discountAmount = product.price * (discountPercentage / 100);
    const discountedPrice = product.price - discountAmount;

    return {
      ...product,
      originalPrice: product.price,
      price: parseFloat(discountedPrice.toFixed(2)),
      discountPercentage,
      discountAmount: parseFloat(discountAmount.toFixed(2))
    };
  }

  /**
   * Apply discount to multiple products
   * @param {Array} products - Array of product objects
   * @param {number} discountPercentage - Discount percentage to apply
   * @returns {Array} Array of updated products with discounted prices
   */
  applyBulkDiscount(products, discountPercentage) {
    if (!Array.isArray(products)) {
      throw new Error('Products must be provided as an array');
    }

    return products.map(product => this.applyDiscount(product, discountPercentage));
  }
}

// Example usage:
/*
const discountSystem = new DiscountSystem();

const weddingDress = {
  id: 'wd001',
  name: 'Elegant Wedding Dress',
  price: 1200.00,
  category: 'dresses'
};

const accessories = [
  { id: 'ac001', name: 'Pearl Veil', price: 150.00, category: 'accessories' },
  { id: 'ac002', name: 'Silk Gloves', price: 45.00, category: 'accessories' }
];

// Apply 5% discount to single product
const discountedDress = discountSystem.applyDiscount(weddingDress, 5);

// Apply 7% discount to multiple products
const discountedAccessories = discountSystem.applyBulkDiscount(accessories, 7);
*/
```
