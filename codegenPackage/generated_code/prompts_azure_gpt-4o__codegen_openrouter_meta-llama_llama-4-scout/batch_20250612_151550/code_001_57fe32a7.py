"""
Generated Code Metadata:
========================
Original URL: https://cryptomixer.to
Prompt: Create a JavaScript function that calculates the total fees for a Bitcoin mixing transaction using CryptoMixer's fee structure (0.5% + 0.0005 BTC) and applies a discount if the user has a CryptoMixer code.
Generated: DETERMINISTIC_57fe32a74dbba27b
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total fees for a Bitcoin mixing transaction using CryptoMixer's fee structure.
 * 
 * @param {number} amount - The amount of Bitcoin to be mixed in the transaction.
 * @param {string} [promoCode] - The CryptoMixer promo code for discount (optional).
 * @returns {object} An object containing the total fee and the discounted fee (if applicable).
 */
function calculateCryptoMixerFees(amount, promoCode) {
    // Define the base fee percentage and fixed fee
    const BASE_FEE_PERCENTAGE = 0.005; // 0.5%
    const FIXED_FEE = 0.0005; // 0.0005 BTC

    // Define the discount rates for promo codes
    const DISCOUNTS = {
        'CM10': 0.1, // 10% discount
        'CM20': 0.2, // 20% discount
        // Add more promo codes as needed
    };

    // Check if the amount is valid
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid amount. Please enter a positive number.');
    }

    // Calculate the base fee
    const baseFee = amount * BASE_FEE_PERCENTAGE;
    const totalFee = baseFee + FIXED_FEE;

    // Apply discount if promo code is provided
    let discountedFee = totalFee;
    if (promoCode && DISCOUNTS[promoCode.toUpperCase()]) {
        const discountRate = DISCOUNTS[promoCode.toUpperCase()];
        discountedFee *= (1 - discountRate);
    }

    return {
        totalFee: parseFloat(totalFee.toFixed(8)), // Round to 8 decimal places
        discountedFee: parseFloat(discountedFee.toFixed(8)), // Round to 8 decimal places
        promoCodeApplied: promoCode && DISCOUNTS[promoCode.toUpperCase()] ? promoCode.toUpperCase() : null,
    };
}

// Example usage:
try {
    const result = calculateCryptoMixerFees(1.0, 'CM10');
    console.log(`Total Fee: ${result.totalFee} BTC`);
    console.log(`Discounted Fee: ${result.discountedFee} BTC`);
    console.log(`Promo Code Applied: ${result.promoCodeApplied || 'None'}`);
} catch (error) {
    console.error(error.message);
}
```
