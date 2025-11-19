"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chevrox.hpcom.pages.dev
Prompt: Write a JavaScript function that simulates the profit accrual for the Petroleum investment package on Chevrox, detailing the returns for each sector based on different deposit amounts.
Generated: DETERMINISTIC_b070b9eb3c55c8e7
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the profit accrual for the Petroleum investment package on Chevrox.
 * @param {number} depositAmount - The initial investment amount.
 * @returns {Object} - An object containing the returns for each sector.
 * @throws {Error} - Throws an error if the deposit amount is not a positive number.
 */
function simulateProfitAccrual(depositAmount) {
    // Validate the deposit amount
    if (typeof depositAmount !== 'number' || depositAmount <= 0) {
        throw new Error('Deposit amount must be a positive number.');
    }

    // Define sector return rates (in percentage)
    const sectorReturns = {
        upstream: 0.15,   // 15% return for upstream sector
        midstream: 0.10,  // 10% return for midstream sector
        downstream: 0.08, // 8% return for downstream sector
    };

    // Initialize an object to hold the returns for each sector
    const returns = {};

    // Calculate returns for each sector based on the deposit amount
    for (const [sector, rate] of Object.entries(sectorReturns)) {
        returns[sector] = {
            deposit: depositAmount,
            profit: (depositAmount * rate).toFixed(2), // Calculate profit
            totalReturn: (depositAmount + (depositAmount * rate)).toFixed(2), // Total return
        };
    }

    return returns;
}

// Example usage:
try {
    const depositAmount = 10000; // Example deposit amount
    const profitAccrual = simulateProfitAccrual(depositAmount);
    console.log(profitAccrual);
} catch (error) {
    console.error('Error:', error.message);
}
```
