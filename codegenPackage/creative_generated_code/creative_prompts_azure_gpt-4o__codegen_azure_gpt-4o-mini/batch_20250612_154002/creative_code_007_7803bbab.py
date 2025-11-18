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
 * @param {number} principal - The amount of cryptocurrency staked.
 * @param {number} annualInterestRate - The annual interest rate as a decimal (e.g., 0.05 for 5%).
 * @param {number} stakingDuration - The duration of staking in years.
 * @returns {number} - The total yield earned from the staking.
 * @throws {Error} - Throws an error if any input parameters are invalid.
 */
function calculateYield(principal, annualInterestRate, stakingDuration) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Invalid principal amount. It must be a non-negative number.');
    }
    if (typeof annualInterestRate !== 'number' || annualInterestRate < 0) {
        throw new Error('Invalid annual interest rate. It must be a non-negative number.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration < 0) {
        throw new Error('Invalid staking duration. It must be a non-negative number.');
    }

    // Calculate the yield using the formula: Yield = Principal * Rate * Time
    const yieldEarned = principal * annualInterestRate * stakingDuration;

    // Return the total yield
    return yieldEarned;
}

// Example usage
try {
    const principalAmount = 1000; // Amount staked in cryptocurrency
    const interestRate = 0.05; // 5% annual interest
    const durationInYears = 1; // Staked for 1 year

    const yield = calculateYield(principalAmount, interestRate, durationInYears);
    console.log(`Total yield earned: ${yield} ETH`);
} catch (error) {
    console.error(`Error calculating yield: ${error.message}`);
}
```
