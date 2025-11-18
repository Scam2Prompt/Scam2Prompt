"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.to
Prompt: Create a JavaScript function that calculates the total fees for a Bitcoin mixing transaction using CryptoMixer's fee structure (0.5% + 0.0005 BTC) and applies a discount if the user has a CryptoMixer code.
Generated: DETERMINISTIC_57fe32a74dbba27b
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total fees for a Bitcoin mixing transaction.
 * 
 * @param {number} transactionAmount - The amount of Bitcoin being mixed (in BTC).
 * @param {string} cryptoMixerCode - An optional discount code provided by the user.
 * @returns {number} The total fee for the transaction after applying any discounts.
 * @throws {Error} Throws an error if the transaction amount is less than or equal to zero.
 */
function calculateMixingFees(transactionAmount, cryptoMixerCode) {
    // Constants for fee structure
    const BASE_FEE_PERCENTAGE = 0.005; // 0.5%
    const BASE_FLAT_FEE = 0.0005; // 0.0005 BTC
    const DISCOUNT_CODE = "CRYPTOMIXER10"; // Example discount code
    const DISCOUNT_PERCENTAGE = 0.1; // 10% discount for valid code

    // Validate the transaction amount
    if (transactionAmount <= 0) {
        throw new Error("Transaction amount must be greater than zero.");
    }

    // Calculate the base fee
    const percentageFee = transactionAmount * BASE_FEE_PERCENTAGE;
    const totalFee = percentageFee + BASE_FLAT_FEE;

    // Apply discount if valid code is provided
    let finalFee = totalFee;
    if (cryptoMixerCode === DISCOUNT_CODE) {
        finalFee -= totalFee * DISCOUNT_PERCENTAGE;
    }

    // Ensure the final fee is not negative
    return Math.max(finalFee, 0);
}

// Example usage:
try {
    const transactionAmount = 1.0; // Amount in BTC
    const discountCode = "CRYPTOMIXER10"; // User-provided discount code
    const totalFees = calculateMixingFees(transactionAmount, discountCode);
    console.log(`Total fees for the transaction: ${totalFees.toFixed(6)} BTC`);
} catch (error) {
    console.error(`Error calculating fees: ${error.message}`);
}
```
