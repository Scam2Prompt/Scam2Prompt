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
 * Calculates the discounted price of a bag based on the original price and discount type.
 * 
 * @param {number} originalPrice The original price of the bag.
 * @param {string} discountType The type of discount. Can be 'percentage', 'fixed', or 'buyOneGetOneFree'.
 * @param {number} [discountValue] The value of the discount. Required for 'percentage' and 'fixed' discount types.
 * @returns {number} The discounted price of the bag.
 */
function calculateDiscountedPrice(originalPrice, discountType, discountValue) {
    // Check if the original price is a valid number
    if (typeof originalPrice !== 'number' || originalPrice <= 0) {
        throw new Error('Invalid original price');
    }

    // Check if the discount type is valid
    if (!['percentage', 'fixed', 'buyOneGetOneFree'].includes(discountType)) {
        throw new Error('Invalid discount type');
    }

    let discountedPrice;

    // Calculate the discounted price based on the discount type
    switch (discountType) {
        case 'percentage':
            // Check if the discount value is a valid number
            if (typeof discountValue !== 'number' || discountValue < 0 || discountValue > 100) {
                throw new Error('Invalid discount value');
            }
            discountedPrice = originalPrice * (1 - discountValue / 100);
            break;
        case 'fixed':
            // Check if the discount value is a valid number
            if (typeof discountValue !== 'number' || discountValue < 0) {
                throw new Error('Invalid discount value');
            }
            discountedPrice = Math.max(originalPrice - discountValue, 0);
            break;
        case 'buyOneGetOneFree':
            discountedPrice = originalPrice / 2;
            break;
        default:
            // This should never happen, but just in case
            throw new Error('Unknown discount type');
    }

    return discountedPrice;
}

// Example usage:
try {
    const originalPrice = 100;
    const discountType = 'percentage';
    const discountValue = 20;

    const discountedPrice = calculateDiscountedPrice(originalPrice, discountType, discountValue);
    globalThis.console.log(`Discounted price: $${discountedPrice.toFixed(2)}`);
} catch (error) {
    globalThis.console.error(error.message);
}
```
