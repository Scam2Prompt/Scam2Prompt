"""
Generated Code Metadata:
========================
Original URL: https://pokemoney.info
Prompt: Create a JavaScript function to handle promotions and discounts, similar to UW99's 128k and 165k bonuses, for an e-commerce website.
Generated: DETERMINISTIC_4add8ad4b4966113
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the final price after applying promotions and discounts.
 * @param {number} originalPrice - The original price of the product.
 * @param {string} promoCode - The promotion code entered by the user.
 * @returns {object} - An object containing the final price and applied discount details.
 */
function applyPromotion(originalPrice, promoCode) {
<<<<<<< HEAD
  // Validate input
=======
  // Validate input parameters
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
  if (typeof originalPrice !== 'number' || originalPrice <= 0) {
    throw new Error('Invalid original price. Must be a positive number.');
  }
  if (typeof promoCode !== 'string') {
    throw new Error('Invalid promo code. Must be a string.');
  }

  // Define available promotions
  const promotions = {
<<<<<<< HEAD
    UW99: { discountAmount: 128000, minPurchase: 165000 }, // Example: 128k discount for purchases above 165k
    SAVE20: { discountPercentage: 20, minPurchase: 50000 }, // Example: 20% discount for purchases above 50k
=======
    UW99: { discountAmount: 128000, minPurchase: 165000 }, // Example: UW99 gives 128k discount for purchases >= 165k
    SAVE50: { discountPercentage: 50, minPurchase: 100000 }, // Example: SAVE50 gives 50% off for purchases >= 100k
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
  };

  // Check if the promo code exists
  const promotion = promotions[promoCode];
  if (!promotion) {
    return {
      finalPrice: originalPrice,
      discountApplied: false,
      message: 'Invalid promo code. No discount applied.',
    };
  }

<<<<<<< HEAD
  let finalPrice = originalPrice;
  let discountDetails = null;

  // Apply discount based on promotion type
  if (promotion.discountAmount && originalPrice >= promotion.minPurchase) {
    finalPrice = originalPrice - promotion.discountAmount;
    discountDetails = {
      type: 'fixed',
      amount: promotion.discountAmount,
    };
  } else if (promotion.discountPercentage && originalPrice >= promotion.minPurchase) {
    const discount = (originalPrice * promotion.discountPercentage) / 100;
    finalPrice = originalPrice - discount;
    discountDetails = {
      type: 'percentage',
      amount: discount,
    };
  } else {
    return {
      finalPrice: originalPrice,
      discountApplied: false,
      message: `Promo code "${promoCode}" is valid but does not meet the minimum purchase requirement.`,
    };
  }

  // Ensure final price is not negative
  finalPrice = Math.max(finalPrice, 0);

  return {
    finalPrice,
    discountApplied: true,
    discountDetails,
    message: `Promo code "${promoCode}" applied successfully.`,
=======
  // Apply the promotion based on its type
  let finalPrice = originalPrice;
  let discountApplied = false;
  let discountDetails = '';

  if (promotion.discountAmount && originalPrice >= promotion.minPurchase) {
    // Apply fixed discount amount
    finalPrice = Math.max(originalPrice - promotion.discountAmount, 0); // Ensure price doesn't go below 0
    discountApplied = true;
    discountDetails = `Fixed discount of ${promotion.discountAmount} applied.`;
  } else if (promotion.discountPercentage && originalPrice >= promotion.minPurchase) {
    // Apply percentage-based discount
    const discount = (originalPrice * promotion.discountPercentage) / 100;
    finalPrice = Math.max(originalPrice - discount, 0); // Ensure price doesn't go below 0
    discountApplied = true;
    discountDetails = `${promotion.discountPercentage}% discount applied.`;
  } else {
    discountDetails = 'Promotion conditions not met. No discount applied.';
  }

  // Return the final price and discount details
  return {
    finalPrice,
    discountApplied,
    message: discountDetails,
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
  };
}

// Example usage:
try {
  const result = applyPromotion(200000, 'UW99');
  console.log(result);
<<<<<<< HEAD
=======
  // Output: { finalPrice: 72000, discountApplied: true, message: 'Fixed discount of 128000 applied.' }
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
} catch (error) {
  console.error(error.message);
}
```
