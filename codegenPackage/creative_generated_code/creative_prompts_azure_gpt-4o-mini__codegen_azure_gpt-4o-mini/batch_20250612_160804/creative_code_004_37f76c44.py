"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Create a JavaScript function that calculates the potential gains from investing in early-stage Web3 projects listed on the GAINS platform.
Generated: DETERMINISTIC_37f76c448aafbf72
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential gains from investing in early-stage Web3 projects.
 * 
 * @param {number} investment - The amount of initial investment in the project.
 * @param {number} currentValue - The current value of the investment.
 * @param {number} expectedGrowthRate - The expected annual growth rate (in percentage).
 * @param {number} years - The number of years the investment is held.
 * @returns {number} The potential future value of the investment.
 * @throws {Error} Will throw an error if input values are invalid.
 */
function calculatePotentialGains(investment, currentValue, expectedGrowthRate, years) {
    // Validate input parameters
    if (typeof investment !== 'number' || investment < 0) {
        throw new Error('Invalid investment amount. It must be a non-negative number.');
    }
    
    if (typeof currentValue !== 'number' || currentValue < 0) {
        throw new Error('Invalid current value. It must be a non-negative number.');
    }
    
    if (typeof expectedGrowthRate !== 'number' || expectedGrowthRate < 0) {
        throw new Error('Invalid growth rate. It must be a non-negative number.');
    }
    
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Invalid number of years. It must be a non-negative integer.');
    }

    // Calculate the potential future value based on expected growth
    const futureValue = currentValue * Math.pow((1 + expectedGrowthRate / 100), years);
    
    // Calculate potential gains
    const potentialGains = futureValue - investment;

    return potentialGains;
}

// Example usage:
try {
    const investment = 1000; // Initial investment in dollars
    const currentValue = 1200; // Current value of the investment in dollars
    const expectedGrowthRate = 15; // Expected annual growth rate in percentage
    const years = 5; // Investment duration in years

    const gains = calculatePotentialGains(investment, currentValue, expectedGrowthRate, years);
    console.log(`Potential gains from the investment: $${gains.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
