"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqed.com
Prompt: Write a function to calculate yield from an Ethereum-based DeFi staking protocol using JavaScript.
Generated: DETERMINISTIC_7803bbab08fab0a3
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the yield from an Ethereum-based DeFi staking protocol.
 * 
 * @param {number} principal - The amount of Ethereum staked (in ETH).
 * @param {number} annualRate - The annual percentage yield (APY) provided by the protocol (in percent).
 * @param {number} daysStaked - The number of days the Ethereum has been staked.
 * @returns {number} - The yield earned (in ETH).
 * 
 * @throws {Error} If input parameters are invalid (e.g., negative or non-numeric values).
 */
function calculateStakingYield(principal, annualRate, daysStaked) {
    // Input validation
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error("Invalid principal amount. Must be a positive number.");
    }
    if (typeof annualRate !== 'number' || annualRate < 0) {
        throw new Error("Invalid annual rate. Must be a non-negative number.");
    }
    if (typeof daysStaked !== 'number' || daysStaked < 0) {
        throw new Error("Invalid staking duration. Must be a non-negative number.");
    }

    // Constants
    const DAYS_IN_YEAR = 365;

    // Calculate yield
    const dailyRate = annualRate / 100 / DAYS_IN_YEAR; // Convert APY to daily rate
    const yield = principal * dailyRate * daysStaked;

    return yield;
}

// Example Usage:
try {
    const principal = 10; // 10 ETH
    const annualRate = 5; // 5% APY
    const daysStaked = 30; // Staked for 30 days

    const yield = calculateStakingYield(principal, annualRate, daysStaked);
    console.log(`Yield earned: ${yield} ETH`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
