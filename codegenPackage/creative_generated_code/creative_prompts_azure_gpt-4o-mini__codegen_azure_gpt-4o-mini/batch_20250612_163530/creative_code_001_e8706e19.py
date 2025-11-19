"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magahat-3gz.pages.dev
Prompt: Write a JavaScript function that calculates the total fees for minting a token in the MAGA•THE•DONALD•TRUMP collection based on the provided fee structure and mint count.
Generated: DETERMINISTIC_e8706e19495367e4
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total fees for minting a token in the MAGA•THE•DONALD•TRUMP collection.
 * 
 * @param {number} mintCount - The number of tokens to mint. Must be a positive integer.
 * @param {number} baseFee - The base fee for minting a single token. Must be a positive number.
 * @param {number} additionalFee - The additional fee for each token beyond the first. Must be a non-negative number.
 * @returns {number} The total fees for minting the specified number of tokens.
 * @throws {Error} Throws an error if mintCount is not a positive integer, or if baseFee or additionalFee are negative.
 */
function calculateMintingFees(mintCount, baseFee, additionalFee) {
    // Validate inputs
    if (!Number.isInteger(mintCount) || mintCount <= 0) {
        throw new Error("mintCount must be a positive integer.");
    }
    if (typeof baseFee !== 'number' || baseFee < 0) {
        throw new Error("baseFee must be a non-negative number.");
    }
    if (typeof additionalFee !== 'number' || additionalFee < 0) {
        throw new Error("additionalFee must be a non-negative number.");
    }

    // Calculate total fees
    let totalFees = baseFee; // Start with the base fee
    if (mintCount > 1) {
        totalFees += (mintCount - 1) * additionalFee; // Add additional fees for extra tokens
    }

    return totalFees; // Return the total fees
}

// Example usage:
try {
    const mintCount = 5;
    const baseFee = 10.00; // Base fee in currency
    const additionalFee = 2.00; // Additional fee per token

    const totalFees = calculateMintingFees(mintCount, baseFee, additionalFee);
    console.log(`Total fees for minting ${mintCount} tokens: $${totalFees.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
