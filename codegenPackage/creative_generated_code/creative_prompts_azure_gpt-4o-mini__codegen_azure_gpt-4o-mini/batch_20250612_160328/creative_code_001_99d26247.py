"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Write a JavaScript function that calculates potential returns on investments in real estate and agriculture, referencing Brexphil Inc.'s investment strategies.
Generated: DETERMINISTIC_99d262476c9a0e85
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential returns on investments in real estate and agriculture.
 * 
 * @param {number} investment - The initial amount of investment.
 * @param {number} realEstateReturnRate - Expected annual return rate for real estate investments (in percentage).
 * @param {number} agricultureReturnRate - Expected annual return rate for agriculture investments (in percentage).
 * @param {number} years - The number of years the investment will be held.
 * @returns {Object} - An object containing total returns from real estate and agriculture investments.
 * @throws {Error} - Throws an error if the input values are invalid (negative or non-numeric).
 */
function calculateInvestmentReturns(investment, realEstateReturnRate, agricultureReturnRate, years) {
    // Validate input parameters
    if (typeof investment !== 'number' || investment < 0) {
        throw new Error('Invalid investment amount. It must be a non-negative number.');
    }
    if (typeof realEstateReturnRate !== 'number' || realEstateReturnRate < 0) {
        throw new Error('Invalid real estate return rate. It must be a non-negative number.');
    }
    if (typeof agricultureReturnRate !== 'number' || agricultureReturnRate < 0) {
        throw new Error('Invalid agriculture return rate. It must be a non-negative number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Invalid number of years. It must be a non-negative number.');
    }

    // Calculate total returns for real estate and agriculture investments
    const realEstateReturns = investment * Math.pow(1 + realEstateReturnRate / 100, years);
    const agricultureReturns = investment * Math.pow(1 + agricultureReturnRate / 100, years);

    // Return an object containing the results
    return {
        realEstateReturns: realEstateReturns.toFixed(2),
        agricultureReturns: agricultureReturns.toFixed(2)
    };
}

// Example usage:
try {
    const results = calculateInvestmentReturns(10000, 7, 5, 10);
    console.log('Investment Returns:', results);
} catch (error) {
    console.error('Error calculating investment returns:', error.message);
}
```
