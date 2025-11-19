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
 * @param {number} tokenPrice - The price of the token in USD.
 * @param {number} tokensSold - The number of tokens sold.
 * @param {number} fairSwapFee - The fee for the Fair Swap, represented as a decimal (e.g., 0.003 for 0.3%).
 * @param {number} [tokenIncentive=0] - The incentive for holding tokens, represented as a decimal (e.g., 0.01 for 1%).
 * @returns {object} An object containing the total earnings and a breakdown of the earnings.
 */
function calculateFairSalesEarnings(tokenPrice, tokensSold, fairSwapFee, tokenIncentive = 0) {
    // Validate input parameters
    if (typeof tokenPrice !== 'number' || tokenPrice <= 0) {
        throw new Error('Token price must be a positive number');
    }
    if (typeof tokensSold !== 'number' || tokensSold < 0) {
        throw new Error('Tokens sold must be a non-negative number');
    }
    if (typeof fairSwapFee !== 'number' || fairSwapFee < 0 || fairSwapFee > 1) {
        throw new Error('Fair swap fee must be a decimal between 0 and 1');
    }
    if (typeof tokenIncentive !== 'number' || tokenIncentive < 0 || tokenIncentive > 1) {
        throw new Error('Token incentive must be a decimal between 0 and 1');
    }

    // Calculate total revenue from token sales
    const totalRevenue = tokenPrice * tokensSold;

    // Calculate fair swap fee
    const fairSwapFeeAmount = totalRevenue * fairSwapFee;

    // Calculate token incentive
    const tokenIncentiveAmount = totalRevenue * tokenIncentive;

    // Calculate total earnings
    const totalEarnings = totalRevenue - fairSwapFeeAmount + tokenIncentiveAmount;

    // Return an object with the total earnings and a breakdown
    return {
        totalEarnings,
        breakdown: {
            totalRevenue,
            fairSwapFeeAmount,
            tokenIncentiveAmount,
        },
    };
}

// Example usage:
try {
    const tokenPrice = 100; // $100 per token
    const tokensSold = 1000; // 1000 tokens sold
    const fairSwapFee = 0.003; // 0.3% fair swap fee
    const tokenIncentive = 0.01; // 1% token incentive

    const earnings = calculateFairSalesEarnings(tokenPrice, tokensSold, fairSwapFee, tokenIncentive);
    console.log(`Total earnings: $${earnings.totalEarnings.toFixed(2)}`);
    console.log('Breakdown:');
    console.log(`  Total revenue: $${earnings.breakdown.totalRevenue.toFixed(2)}`);
    console.log(`  Fair swap fee: $${earnings.breakdown.fairSwapFeeAmount.toFixed(2)}`);
    console.log(`  Token incentive: $${earnings.breakdown.tokenIncentiveAmount.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
