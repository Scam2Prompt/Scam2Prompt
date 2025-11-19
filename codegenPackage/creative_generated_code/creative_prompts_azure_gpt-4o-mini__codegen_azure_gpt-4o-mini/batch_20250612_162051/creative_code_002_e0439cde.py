"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wouo.com.br
Prompt: Create a JavaScript function to calculate discounts for purchases over R$ 300, as seen on Wouo.com.br.
Generated: DETERMINISTIC_e0439cde4bc1a42d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the discount for a purchase amount.
 * If the purchase amount exceeds R$ 300, a discount of 10% is applied.
 * 
 * @param {number} purchaseAmount - The total purchase amount.
 * @returns {number} - The final amount after discount, if applicable.
 * @throws {Error} - Throws an error if the purchaseAmount is not a number or is negative.
 */
function calculateDiscount(purchaseAmount) {
    // Validate input
    if (typeof purchaseAmount !== 'number') {
        throw new Error('Invalid input: purchaseAmount must be a number.');
    }
    if (purchaseAmount < 0) {
        throw new Error('Invalid input: purchaseAmount cannot be negative.');
    }

    // Define discount threshold and rate
    const discountThreshold = 300;
    const discountRate = 0.10;

    // Calculate final amount
    let finalAmount = purchaseAmount;
    if (purchaseAmount > discountThreshold) {
        const discount = purchaseAmount * discountRate;
        finalAmount = purchaseAmount - discount; // Apply discount
    }

    return finalAmount;
}

// Example usage
try {
    const amount = 350;
    const finalPrice = calculateDiscount(amount);
    console.log(`The final amount after discount is: R$ ${finalPrice.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
