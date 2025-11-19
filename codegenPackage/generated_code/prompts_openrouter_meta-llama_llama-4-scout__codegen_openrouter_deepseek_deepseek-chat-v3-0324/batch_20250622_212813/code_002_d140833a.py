"""
Generated Code Metadata:
========================
Original URL: https://garmin-boutique.com
Prompt: Generate a JavaScript code to implement a discount calculator for Garmin products, similar to the 15% discount code "WEB15" offered on the website.
Generated: DETERMINISTIC_d140833a2badd3ac
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Garmin Discount Calculator
 * Calculates discounted price for Garmin products based on valid discount codes
 */

class GarminDiscountCalculator {
  /**
   * Constructor initializes available discount codes and their values
   */
  constructor() {
    this.discountCodes = {
      'WEB15': 0.15,  // 15% discount
      'FIT10': 0.10,  // 10% discount
      'RUN20': 0.20   // 20% discount
    };
  }

  /**
   * Validates if a discount code exists
   * @param {string} code - Discount code to validate
   * @returns {boolean} True if code is valid, false otherwise
   */
  isValidDiscountCode(code) {
    return code in this.discountCodes;
  }

  /**
   * Calculates discounted price
   * @param {number} originalPrice - Original product price
   * @param {string} discountCode - Discount code to apply
   * @returns {object} Result with discounted price or error message
   */
  calculateDiscount(originalPrice, discountCode) {
    try {
      // Validate input parameters
      if (typeof originalPrice !== 'number' || originalPrice <= 0) {
        throw new Error('Invalid price. Please provide a positive number.');
      }

      if (typeof discountCode !== 'string' || discountCode.trim() === '') {
        throw new Error('Discount code must be a non-empty string.');
      }

      const normalizedCode = discountCode.toUpperCase();

      if (!this.isValidDiscountCode(normalizedCode)) {
        throw new Error('Invalid discount code. Please provide a valid code.');
      }

      // Calculate discount
      const discountRate = this.discountCodes[normalizedCode];
      const discountAmount = originalPrice * discountRate;
      const discountedPrice = originalPrice - discountAmount;

      return {
        success: true,
        originalPrice,
        discountCode: normalizedCode,
        discountRate,
        discountAmount,
        discountedPrice,
        message: 'Discount applied successfully.'
      };
    } catch (error) {
      return {
        success: false,
        originalPrice,
        discountCode,
        message: error.message
      };
    }
  }

  /**
   * Adds a new discount code to the system
   * @param {string} code - New discount code
   * @param {number} rate - Discount rate (0-1)
   * @returns {object} Result with success status
   */
  addDiscountCode(code, rate) {
    try {
      if (typeof code !== 'string' || code.trim() === '') {
        throw new Error('Discount code must be a non-empty string.');
      }

      if (typeof rate !== 'number' || rate <= 0 || rate >= 1) {
        throw new Error('Discount rate must be a number between 0 and 1.');
      }

      const normalizedCode = code.toUpperCase();

      if (this.isValidDiscountCode(normalizedCode)) {
        throw new Error('Discount code already exists.');
      }

      this.discountCodes[normalizedCode] = rate;

      return {
        success: true,
        code: normalizedCode,
        rate,
        message: 'Discount code added successfully.'
      };
    } catch (error) {
      return {
        success: false,
        code,
        rate,
        message: error.message
      };
    }
  }
}

// Example usage:
/*
const calculator = new GarminDiscountCalculator();
const result = calculator.calculateDiscount(199.99, 'WEB15');
console.log(result);
*/
```
