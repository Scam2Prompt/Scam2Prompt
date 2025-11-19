"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: Create a JavaScript function that calculates potential earnings from participating in CowSwap's Fair Sales.
Generated: DETERMINISTIC_d750b75e124401aa
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential earnings from participating in CowSwap's Fair Sales.
 * 
 * @param {number} investmentAmount - The amount invested in the sale (in ETH or other base currency)
 * @param {number} totalSaleAmount - Total amount available in the sale (same currency as investment)
 * @param {number} totalDemand - Total demand/orders in the sale (same currency as investment)
 * @param {number} tokenPrice - Price per token in the base currency
 * @returns {Object} An object containing the allocated tokens and refund amount
 * @throws {Error} If any input is invalid (non-number, negative, etc.)
 */
function calculateCowSwapEarnings(investmentAmount, totalSaleAmount, totalDemand, tokenPrice) {
    // Validate inputs
    if (typeof investmentAmount !== 'number' || 
        typeof totalSaleAmount !== 'number' || 
        typeof totalDemand !== 'number' || 
        typeof tokenPrice !== 'number') {
        throw new Error('All parameters must be numbers');
    }

    if (investmentAmount <= 0 || 
        totalSaleAmount <= 0 || 
        totalDemand <= 0 || 
        tokenPrice <= 0) {
        throw new Error('All parameters must be positive numbers');
    }

    // Calculate allocation ratio (pro-rata if demand exceeds sale amount)
    const allocationRatio = Math.min(totalSaleAmount / totalDemand, 1);
    
    // Calculate allocated amount in base currency
    const allocatedAmount = investmentAmount * allocationRatio;
    
    // Calculate refund amount
    const refundAmount = investmentAmount - allocatedAmount;
    
    // Calculate token allocation
    const allocatedTokens = allocatedAmount / tokenPrice;
    
    return {
        allocatedTokens: allocatedTokens,
        refundAmount: refundAmount,
        allocationRatio: allocationRatio
    };
}

// Example usage:
// try {
//     const result = calculateCowSwapEarnings(10, 1000, 2000, 0.1);
//     console.log('Allocated Tokens:', result.allocatedTokens);
//     console.log('Refund Amount:', result.refundAmount);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
