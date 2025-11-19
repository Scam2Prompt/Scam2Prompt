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
 * Applies a discount if the user has a valid CryptoMixer discount code.
 * 
 * @param {number} amount - The amount of Bitcoin to be mixed (in BTC)
 * @param {string|null} discountCode - Optional discount code (null if none)
 * @returns {Object} An object containing the base fee, discount amount, and total fee
 * @throws {Error} If the amount is not a positive number
 */
function calculateMixingFees(amount, discountCode = null) {
    // Validate input
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Amount must be a positive number');
    }

    const BASE_FEE_PERCENTAGE = 0.005; // 0.5%
    const BASE_FIXED_FEE = 0.0005; // 0.0005 BTC
    const DISCOUNT_PERCENTAGE = 0.25; // 25% discount if code is valid

    // Calculate base fee
    const percentageFee = amount * BASE_FEE_PERCENTAGE;
    const baseFee = percentageFee + BASE_FIXED_FEE;

    // Check for discount code and apply if valid
    let discount = 0;
    let hasDiscount = false;
    
    if (discountCode && typeof discountCode === 'string' && discountCode.trim() !== '') {
        hasDiscount = true;
        discount = baseFee * DISCOUNT_PERCENTAGE;
    }

    const totalFee = baseFee - discount;

    return {
        baseFee: parseFloat(baseFee.toFixed(8)),
        discount: parseFloat(discount.toFixed(8)),
        totalFee: parseFloat(totalFee.toFixed(8)),
        hasDiscount
    };
}
```
