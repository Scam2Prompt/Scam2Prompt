"""
Generated Code Metadata:
========================
Original URL: https://cakco.com
Prompt: Create a JavaScript function to implement a discount feature for bags on an online store, inspired by the sales promotions mentioned on Cakco.com.
Generated: DETERMINISTIC_9499b98ea8a9ac6c
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the discounted price for bags based on the promotion rules.
 * @param {number} originalPrice - The original price of the bag.
 * @param {number} quantity - The quantity of bags being purchased.
 * @param {string} discountCode - The discount code applied (optional).
 * @returns {Object} An object containing the discounted price and discount details.
 * @throws {Error} If invalid parameters are provided.
 */
function calculateBagDiscount(originalPrice, quantity, discountCode = '') {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || originalPrice <= 0) {
        throw new Error('Original price must be a positive number');
    }
    if (typeof quantity !== 'number' || quantity <= 0 || !Number.isInteger(quantity)) {
        throw new Error('Quantity must be a positive integer');
    }
    if (typeof discountCode !== 'string') {
        throw new Error('Discount code must be a string');
    }

    // Initialize discount variables
    let discountPercentage = 0;
    let discountName = '';
    let discountApplied = false;

    // Apply quantity-based discounts
    if (quantity >= 3) {
        discountPercentage = 15; // 15% off for 3+ items
        discountName = 'Bulk Purchase Discount';
        discountApplied = true;
    } else if (quantity >= 2) {
        discountPercentage = 10; // 10% off for 2 items
        discountName = 'Pair Purchase Discount';
        discountApplied = true;
    }

    // Apply promo code discounts (stackable with quantity discounts)
    const promoCodeDiscounts = {
        'BAGLOVE': 10,
        'SUMMERBAGS': 15,
        'FREESHIP': 0 // Special case for free shipping
    };

    if (discountCode && promoCodeDiscounts.hasOwnProperty(discountCode)) {
        discountPercentage += promoCodeDiscounts[discountCode];
        discountName = discountName 
            ? `${discountName} + ${discountCode} Promo` 
            : `${discountCode} Promo`;
        discountApplied = true;
    }

    // Calculate final price
    const discountAmount = originalPrice * (discountPercentage / 100);
    const discountedPrice = originalPrice - discountAmount;

    return {
        originalPrice: originalPrice,
        quantity: quantity,
        discountPercentage: discountPercentage,
        discountAmount: discountAmount,
        discountedPrice: discountedPrice,
        discountName: discountName,
        discountApplied: discountApplied,
        discountCode: discountCode
    };
}

/**
 * Formats the discount information for display.
 * @param {Object} discountInfo - The discount information object from calculateBagDiscount.
 * @returns {string} Formatted discount message.
 */
function formatDiscountMessage(discountInfo) {
    if (!discountInfo.discountApplied) {
        return 'No discounts applied.';
    }

    let message = `Discount Applied: ${discountInfo.discountName} (${discountInfo.discountPercentage}% off)`;
    message += `\nOriginal Price: $${discountInfo.originalPrice.toFixed(2)}`;
    message += `\nDiscount Amount: $${discountInfo.discountAmount.toFixed(2)}`;
    message += `\nFinal Price: $${discountInfo.discountedPrice.toFixed(2)}`;

    return message;
}

// Example usage:
try {
    const discountInfo = calculateBagDiscount(100, 2, 'BAGLOVE');
    console.log(formatDiscountMessage(discountInfo));
} catch (error) {
    console.error('Error calculating discount:', error.message);
}
```
