"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9ias90dia90sdi9asidasdk.pages.dev
Prompt: Write a JavaScript function to calculate affiliate fees earned from cross-chain swaps executed through THORChain. Include logic for specifying custom fee percentages.
Generated: DETERMINISTIC_8555a92e846b9e4a
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate affiliate fees earned from cross-chain swaps executed through THORChain.
 * 
 * @param {number} swapAmount - The amount of the swap.
 * @param {number} feePercentage - The custom fee percentage to calculate the affiliate fee.
 * @returns {number} The calculated affiliate fee.
 * @throws {Error} Will throw an error if swapAmount or feePercentage is negative.
 */
function calculateAffiliateFee(swapAmount, feePercentage) {
    // Validate inputs
    if (swapAmount < 0) {
        throw new Error("swapAmount must be a non-negative number.");
    }
    if (feePercentage < 0) {
        throw new Error("feePercentage must be a non-negative number.");
    }

    // Calculate the affiliate fee
    const affiliateFee = (swapAmount * feePercentage) / 100;

    return parseFloat(affiliateFee.toFixed(2)); // Return the fee rounded to 2 decimal places
}

// Example usage:
try {
    const swapAmount = 1000; // Amount of swap
    const feePercentage = 2;  // Custom fee percentage
    const fee = calculateAffiliateFee(swapAmount, feePercentage);
    console.log(`Affiliate fee earned: $${fee}`);
} catch (error) {
    console.error(`Error calculating affiliate fee: ${error.message}`);
}
```
