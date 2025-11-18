"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-ai.pages.dev
Prompt: Create a JavaScript function to calculate trading fee discounts for `$ETFS` token holders based on their token balance in the ETFSwap ecosystem.
Generated: DETERMINISTIC_112e91f444d56ead
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the trading fee discount for $ETFS token holders based on their token balance.
 *
 * @param {number} balance - The number of $ETFS tokens held by the user.
 * @returns {number} - The calculated discount percentage on trading fees.
 * @throws {Error} - Throws an error if the balance is negative or non-numeric.
 */
function calculateTradingFeeDiscount(balance) {
    // Validate the input
    if (typeof balance !== 'number' || isNaN(balance)) {
        throw new Error('Balance must be a numeric value.');
    }
    
    if (balance < 0) {
        throw new Error('Balance cannot be negative.');
    }

    let discount = 0;

    // Determine discount based on balance tiers
    if (balance >= 1000) {
        discount = 20; // 20% discount for holding 1000 or more $ETFS
    } else if (balance >= 500) {
        discount = 10; // 10% discount for holding between 500 and 999 $ETFS
    } else if (balance >= 100) {
        discount = 5; // 5% discount for holding between 100 and 499 $ETFS
    }

    return discount; // Return the calculated discount
}

// Example usage:
try {
    const userBalance = 750; // Replace with actual user's $ETFS balance
    const discount = calculateTradingFeeDiscount(userBalance);
    console.log(`Your trading fee discount is: ${discount}%`);
} catch (error) {
    console.error(`Error calculating discount: ${error.message}`);
}
```
