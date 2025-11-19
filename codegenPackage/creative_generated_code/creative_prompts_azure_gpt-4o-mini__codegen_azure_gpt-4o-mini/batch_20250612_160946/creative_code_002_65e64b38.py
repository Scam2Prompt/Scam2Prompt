"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bevm-airdrop.vercel.app
Prompt: Generate a JavaScript function that calculates the monthly unlock percentage of GEB tokens over the first 12 months and the subsequent 48 months.
Generated: DETERMINISTIC_65e64b3889699b1b
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the monthly unlock percentage of GEB tokens over 
 * the first 12 months and the subsequent 48 months.
 * 
 * @param {number} totalSupply - The total supply of GEB tokens.
 * @returns {object} An object containing the unlock percentages for the first 12 months and the next 48 months.
 * @throws {Error} Throws an error if totalSupply is not a positive number.
 */
function calculateUnlockPercentage(totalSupply) {
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('totalSupply must be a positive number.');
    }

    // Constants for unlock percentages
    const firstYearUnlockRate = 0.1; // 10% for the first year
    const secondYearUnlockRate = 0.025; // 2.5% per month for the next 48 months

    // Calculate the monthly unlock for the first 12 months
    const firstYearMonthlyUnlock = (totalSupply * firstYearUnlockRate) / 12;
    
    // Calculate the monthly unlock for the next 48 months
    const secondYearMonthlyUnlock = (totalSupply * (secondYearUnlockRate * 12)) / 48;

    return {
        firstYearMonthlyUnlock: firstYearMonthlyUnlock,
        secondYearMonthlyUnlock: secondYearMonthlyUnlock
    };
}

// Example usage:
try {
    const totalSupply = 1000000; // Example total supply of GEB tokens
    const unlockPercentages = calculateUnlockPercentage(totalSupply);
    console.log('Monthly Unlock Percentages: ', unlockPercentages);
} catch (error) {
    console.error('Error calculating unlock percentages:', error.message);
}
```
