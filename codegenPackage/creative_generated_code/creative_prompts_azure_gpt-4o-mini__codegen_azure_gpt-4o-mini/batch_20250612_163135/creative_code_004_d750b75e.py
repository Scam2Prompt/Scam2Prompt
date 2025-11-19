"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: Create a JavaScript function that calculates potential earnings from participating in CowSwap's Fair Sales.
Generated: DETERMINISTIC_d750b75e124401aa
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings from participating in CowSwap's Fair Sales.
 * 
 * @param {number} salePrice - The price of the asset being sold.
 * @param {number} saleQuantity - The quantity of the asset being sold.
 * @param {number} transactionFeePercentage - The percentage fee applied to the transaction.
 * @returns {number} - The potential earnings after deducting fees.
 * @throws {Error} - Throws an error if any input parameter is negative.
 */
function calculatePotentialEarnings(salePrice, saleQuantity, transactionFeePercentage) {
    // Input validation
    if (salePrice < 0 || saleQuantity < 0 || transactionFeePercentage < 0) {
        throw new Error("Input parameters must be non-negative.");
    }

    // Calculate total sale amount
    const totalSaleAmount = salePrice * saleQuantity;

    // Calculate transaction fee
    const transactionFee = (transactionFeePercentage / 100) * totalSaleAmount;

    // Calculate potential earnings after deducting fees
    const potentialEarnings = totalSaleAmount - transactionFee;

    return potentialEarnings;
}

// Example usage
try {
    const earnings = calculatePotentialEarnings(100, 5, 2);
    console.log(`Potential Earnings: $${earnings.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating potential earnings: ${error.message}`);
}
```
