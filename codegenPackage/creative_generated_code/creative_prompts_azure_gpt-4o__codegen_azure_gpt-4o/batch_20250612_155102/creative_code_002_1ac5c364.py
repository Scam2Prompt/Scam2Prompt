"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Generate code using JavaScript to implement a voucher system for an e-commerce app, where users can apply discounts like those mentioned on Indotip.
Generated: DETERMINISTIC_1ac5c364aea81034
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Voucher System for an E-commerce App
// This code implements a basic voucher system where users can apply discount vouchers during checkout.

// Utility function to validate voucher code format
function isValidVoucherCode(voucherCode) {
  const regex = /^[A-Z0-9]{5,10}$/; // Voucher code must be 5-10 alphanumeric characters
  return regex.test(voucherCode);
}

// Function to calculate discounted price
function applyVoucher(voucherCode, originalPrice) {
  // Mock database of vouchers
  const voucherDatabase = {
    'INDOTIP10': { type: 'percentage', value: 10 }, // 10% discount
    'INDOTIP50': { type: 'fixed', value: 50 }, // $50 discount
    'FREESHIP': { type: 'freeShipping', value: 0 } // Free shipping
  };

  // Validate voucher code
  if (!isValidVoucherCode(voucherCode)) {
    throw new Error('Invalid voucher code format.');
  }

  const voucher = voucherDatabase[voucherCode];

  // Check if voucher exists
  if (!voucher) {
    throw new Error('Voucher code not found.');
  }

  let discountedPrice = originalPrice;

  // Apply discount based on voucher type
  switch (voucher.type) {
    case 'percentage':
      discountedPrice = originalPrice - (originalPrice * voucher.value) / 100;
      break;

    case 'fixed':
      discountedPrice = originalPrice - voucher.value;
      if (discountedPrice < 0) discountedPrice = 0; // Ensure price doesn't go negative
      break;

    case 'freeShipping':
      console.log('Free shipping applied! Discount is not on the product price.');
      break;

    default:
      throw new Error('Unknown voucher type.');
  }

  return discountedPrice;
}

// Example usage
try {
  const originalPrice = 200; // Original price of the cart
  const voucherCode = 'INDOTIP10'; // User-provided voucher code

  const finalPrice = applyVoucher(voucherCode, originalPrice);
  console.log(`Original Price: $${originalPrice}`);
  console.log(`Final Price after applying voucher "${voucherCode}": $${finalPrice}`);
} catch (error) {
  console.error(error.message); // Log error message
}

// Note: In a production system, ensure this code integrates with your backend securely,
// validates voucher code ownership, and prevents abuse.
```
