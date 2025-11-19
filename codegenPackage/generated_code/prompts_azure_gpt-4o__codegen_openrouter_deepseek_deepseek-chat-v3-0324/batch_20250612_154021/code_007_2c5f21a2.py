"""
Generated Code Metadata:
========================
Original URL: https://yourpalmreading.com
Prompt: Write JavaScript code to implement a dynamic pricing calculator for services, including optional add-ons like 24-hour delivery, as offered on YourPalmReading.com.
Generated: DETERMINISTIC_2c5f21a2bd0f8f06
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamic Pricing Calculator for YourPalmReading.com
 * Calculates total price based on base service and optional add-ons
 */

class PricingCalculator {
  /**
   * Initialize pricing calculator with base prices and add-ons
   * @param {Object} config - Configuration object containing pricing details
   */
  constructor(config) {
    this.basePrices = config.basePrices || {};
    this.addOns = config.addOns || {};
    this.taxRate = config.taxRate || 0;
    this.discountCodes = config.discountCodes || {};
  }

  /**
   * Calculate subtotal for selected services
   * @param {string} service - Selected base service
   * @param {Array} selectedAddOns - Array of selected add-on keys
   * @returns {number} Subtotal amount
   */
  calculateSubtotal(service, selectedAddOns = []) {
    if (!this.basePrices[service]) {
      throw new Error(`Invalid service: ${service}`);
    }

    let subtotal = this.basePrices[service];

    selectedAddOns.forEach(addOn => {
      if (!this.addOns[addOn]) {
        console.warn(`Invalid add-on skipped: ${addOn}`);
        return;
      }
      subtotal += this.addOns[addOn];
    });

    return subtotal;
  }

  /**
   * Apply discount code to subtotal
   * @param {number} subtotal - Current subtotal
   * @param {string} discountCode - Discount code to apply
   * @returns {number} Discounted subtotal
   */
  applyDiscount(subtotal, discountCode) {
    if (!discountCode) return subtotal;

    const discount = this.discountCodes[discountCode];
    if (!discount) {
      console.warn(`Invalid discount code: ${discountCode}`);
      return subtotal;
    }

    return subtotal * (1 - discount);
  }

  /**
   * Calculate tax amount
   * @param {number} subtotal - Current subtotal
   * @returns {number} Tax amount
   */
  calculateTax(subtotal) {
    return subtotal * this.taxRate;
  }

  /**
   * Calculate total price
   * @param {string} service - Selected base service
   * @param {Array} selectedAddOns - Array of selected add-on keys
   * @param {string} discountCode - Optional discount code
   * @returns {Object} Object containing subtotal, tax, and total
   */
  calculateTotal(service, selectedAddOns = [], discountCode = '') {
    try {
      let subtotal = this.calculateSubtotal(service, selectedAddOns);
      subtotal = this.applyDiscount(subtotal, discountCode);
      const tax = this.calculateTax(subtotal);
      const total = subtotal + tax;

      return {
        subtotal: this._formatCurrency(subtotal),
        tax: this._formatCurrency(tax),
        total: this._formatCurrency(total),
        raw: {
          subtotal,
          tax,
          total
        }
      };
    } catch (error) {
      console.error('Error calculating total:', error.message);
      return {
        error: error.message
      };
    }
  }

  /**
   * Format number as currency
   * @param {number} amount - Amount to format
   * @returns {string} Formatted currency string
   * @private
   */
  _formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  }
}

// Example configuration
const pricingConfig = {
  basePrices: {
    'basic': 19.99,
    'premium': 39.99,
    'deluxe': 79.99
  },
  addOns: {
    '24hr_delivery': 9.99,
    'detailed_report': 4.99,
    'video_call': 29.99
  },
  taxRate: 0.08, // 8%
  discountCodes: {
    'WELCOME10': 0.10, // 10% off
    'LOYALTY20': 0.20  // 20% off
  }
};

// Example usage
const calculator = new PricingCalculator(pricingConfig);

// Calculate total for premium service with 24hr delivery and WELCOME10 discount
const orderTotal = calculator.calculateTotal(
  'premium',
  ['24hr_delivery'],
  'WELCOME10'
);

console.log(orderTotal);
```
