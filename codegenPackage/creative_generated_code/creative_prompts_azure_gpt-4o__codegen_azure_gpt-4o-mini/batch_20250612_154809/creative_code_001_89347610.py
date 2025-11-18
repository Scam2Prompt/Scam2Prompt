"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomix.vip
Prompt: Generate code in JavaScript to calculate the service fee for mixing Bitcoin using CryptoMixer's fee structure (0.5% + 0.0005 BTC) and apply discounts based on the user's CryptoMixer code.
Generated: DETERMINISTIC_89347610da638740
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the service fee for mixing Bitcoin using CryptoMixer's fee structure.
 * The fee structure is: 0.5% of the amount + a flat fee of 0.0005 BTC.
 * Discounts can be applied based on the user's CryptoMixer code.
 *
 * @param {number} amount - The amount of Bitcoin to be mixed (in BTC).
 * @param {string} promoCode - The user's CryptoMixer discount code.
 * @returns {number} - The total service fee after applying any discounts.
 * @throws {Error} - Throws an error if the amount is not a positive number.
 */
function calculateServiceFee(amount, promoCode) {
    // Validate the input amount
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error("Amount must be a positive number.");
    }

    // Define the base fee parameters
    const basePercentageFee = 0.005; // 0.5% as a decimal
    const flatFee = 0.0005; // flat fee in BTC

    // Calculate the service fee
    const percentageFee = amount * basePercentageFee;
    let totalFee = percentageFee + flatFee;

    // Apply discount if a valid promo code is provided
    if (promoCode) {
        totalFee = applyDiscount(totalFee, promoCode);
    }

    return totalFee;
}

/**
 * Applies a discount based on the user's CryptoMixer promo code.
 *
 * @param {number} fee - The current service fee.
 * @param {string} promoCode - The user's CryptoMixer discount code.
 * @returns {number} - The service fee after applying the discount.
 */
function applyDiscount(fee, promoCode) {
    // Define valid promo codes and their respective discounts
    const discounts = {
        'SAVE10': 0.10, // 10% discount
        'SAVE20': 0.20, // 20% discount
        'NONE': 0.00,   // No discount
    };

    // Check if the promo code exists in the discounts object
    if (discounts[promoCode] !== undefined) {
        const discountAmount = fee * discounts[promoCode];
        return fee - discountAmount; // Apply the discount
    }

    // If the promo code is invalid, return the original fee
    return fee;
}

// Example usage:
try {
    const amountToMix = 1.5; // Amount in BTC
    const userPromoCode = 'SAVE10'; // User's promo code
    const serviceFee = calculateServiceFee(amountToMix, userPromoCode);
    console.log(`The service fee for mixing ${amountToMix} BTC is: ${serviceFee.toFixed(8)} BTC`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
