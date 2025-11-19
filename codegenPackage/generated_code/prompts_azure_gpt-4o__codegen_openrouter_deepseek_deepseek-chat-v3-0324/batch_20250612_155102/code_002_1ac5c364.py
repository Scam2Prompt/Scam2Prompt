"""
Generated Code Metadata:
========================
Original URL: https://leprettystellar.com
Prompt: Generate code using JavaScript to implement a voucher system for an e-commerce app, where users can apply discounts like those mentioned on Indotip.
Generated: DETERMINISTIC_1ac5c364aea81034
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Voucher System for E-commerce App
 * 
 * This module handles voucher creation, validation, and application of discounts.
 */

class VoucherSystem {
  constructor() {
    this.vouchers = new Map(); // Stores active vouchers
  }

  /**
   * Creates a new voucher
   * @param {string} code - Voucher code
   * @param {object} options - Voucher options
   * @param {number} options.discountValue - Discount amount/percentage
   * @param {string} options.discountType - 'percentage' or 'fixed'
   * @param {Date} options.expiryDate - Voucher expiry date
   * @param {number} [options.minPurchase] - Minimum purchase amount required
   * @param {number} [options.maxDiscount] - Maximum discount amount (for percentage)
   * @param {number} [options.usageLimit] - Maximum usage limit
   * @returns {boolean} True if voucher created successfully
   */
  createVoucher(code, options) {
    if (!code || !options || !options.discountValue || !options.discountType || !options.expiryDate) {
      throw new Error('Missing required voucher parameters');
    }

    if (this.vouchers.has(code)) {
      throw new Error('Voucher code already exists');
    }

    if (options.discountType !== 'percentage' && options.discountType !== 'fixed') {
      throw new Error('Invalid discount type. Must be "percentage" or "fixed"');
    }

    if (options.expiryDate <= new Date()) {
      throw new Error('Expiry date must be in the future');
    }

    const voucher = {
      code,
      discountValue: options.discountValue,
      discountType: options.discountType,
      expiryDate: options.expiryDate,
      minPurchase: options.minPurchase || 0,
      maxDiscount: options.maxDiscount || null,
      usageLimit: options.usageLimit || null,
      usageCount: 0,
      isActive: true
    };

    this.vouchers.set(code, voucher);
    return true;
  }

  /**
   * Validates a voucher against cart details
   * @param {string} code - Voucher code to validate
   * @param {number} cartTotal - Total cart amount
   * @returns {object} Validation result { isValid: boolean, message: string }
   */
  validateVoucher(code, cartTotal) {
    if (!this.vouchers.has(code)) {
      return { isValid: false, message: 'Invalid voucher code' };
    }

    const voucher = this.vouchers.get(code);

    if (!voucher.isActive) {
      return { isValid: false, message: 'Voucher is not active' };
    }

    if (voucher.expiryDate < new Date()) {
      return { isValid: false, message: 'Voucher has expired' };
    }

    if (voucher.usageLimit && voucher.usageCount >= voucher.usageLimit) {
      return { isValid: false, message: 'Voucher usage limit reached' };
    }

    if (cartTotal < voucher.minPurchase) {
      return { 
        isValid: false, 
        message: `Minimum purchase of ${voucher.minPurchase} required` 
      };
    }

    return { isValid: true, message: 'Voucher is valid' };
  }

  /**
   * Applies voucher discount to cart total
   * @param {string} code - Voucher code to apply
   * @param {number} cartTotal - Total cart amount before discount
   * @returns {object} Result { success: boolean, discountedTotal: number, discountApplied: number, message: string }
   */
  applyVoucher(code, cartTotal) {
    const validation = this.validateVoucher(code, cartTotal);
    if (!validation.isValid) {
      return { 
        success: false, 
        discountedTotal: cartTotal, 
        discountApplied: 0, 
        message: validation.message 
      };
    }

    const voucher = this.vouchers.get(code);
    let discountAmount = 0;

    if (voucher.discountType === 'fixed') {
      discountAmount = Math.min(voucher.discountValue, cartTotal);
    } else if (voucher.discountType === 'percentage') {
      discountAmount = (cartTotal * voucher.discountValue) / 100;
      if (voucher.maxDiscount) {
        discountAmount = Math.min(discountAmount, voucher.maxDiscount);
      }
    }

    const discountedTotal = cartTotal - discountAmount;
    voucher.usageCount += 1;

    return {
      success: true,
      discountedTotal,
      discountApplied: discountAmount,
      message: 'Voucher applied successfully'
    };
  }

  /**
   * Deactivates a voucher
   * @param {string} code - Voucher code to deactivate
   * @returns {boolean} True if voucher was deactivated
   */
  deactivateVoucher(code) {
    if (!this.vouchers.has(code)) {
      throw new Error('Voucher not found');
    }

    this.vouchers.get(code).isActive = false;
    return true;
  }

  /**
   * Gets voucher details
   * @param {string} code - Voucher code
   * @returns {object} Voucher details
   */
  getVoucherDetails(code) {
    if (!this.vouchers.has(code)) {
      throw new Error('Voucher not found');
    }

    return this.vouchers.get(code);
  }

  /**
   * Lists all active vouchers
   * @returns {Array} List of active vouchers
   */
  listActiveVouchers() {
    return Array.from(this.vouchers.values())
      .filter(voucher => voucher.isActive && voucher.expiryDate > new Date());
  }
}

// Example usage:
/*
const voucherSystem = new VoucherSystem();

// Create a voucher
const expiryDate = new Date();
expiryDate.setMonth(expiryDate.getMonth() + 1);

voucherSystem.createVoucher('INDOTIP10', {
  discountValue: 10,
  discountType: 'percentage',
  expiryDate: expiryDate,
  minPurchase: 100000,
  maxDiscount: 50000,
  usageLimit: 100
});

// Apply voucher
const cartTotal = 150000;
const result = voucherSystem.applyVoucher('INDOTIP10', cartTotal);

if (result.success) {
  console.log(`Discount applied: ${result.discountApplied}`);
  console.log(`New total: ${result.discountedTotal}`);
} else {
  console.log(`Error: ${result.message}`);
}
*/

module.exports = VoucherSystem;
```
