"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cakco.com
Prompt: Create a JavaScript function to implement a discount feature for bags on an online store, inspired by the sales promotions mentioned on Cakco.com.
Generated: DETERMINISTIC_9499b98ea8a9ac6c
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Applies a discount to the price of bags based on a promotional rate.
 * 
 * @param {number} originalPrice - The original price of the bag.
 * @param {number} discountRate - The discount rate to apply (as a percentage).
 * @returns {number} - The final price after applying the discount.
 * @throws {Error} - Throws an error if originalPrice or discountRate are invalid.
 */
function applyBagDiscount(originalPrice, discountRate) {
    // Validate input
    if (typeof originalPrice !== 'number' || originalPrice < 0) {
        throw new Error('Invalid original price. It must be a non-negative number.');
    }
    if (typeof discountRate !== 'number' || discountRate < 0 || discountRate > 100) {
        throw new Error('Invalid discount rate. It must be a number between 0 and 100.');
    }

    // Calculate the discount amount
    const discountAmount = (originalPrice * discountRate) / 100;

    // Calculate the final price after discount
    const finalPrice = originalPrice - discountAmount;

    // Ensure final price does not drop below zero
    return Math.max(finalPrice, 0);
}

// Example usage:
try {
    const originalPrice = 100; // Original price of the bag
    const discountRate = 20;   // Discount rate (20%)
    const discountedPrice = applyBagDiscount(originalPrice, discountRate);
    console.log(`The discounted price is: $${discountedPrice.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
