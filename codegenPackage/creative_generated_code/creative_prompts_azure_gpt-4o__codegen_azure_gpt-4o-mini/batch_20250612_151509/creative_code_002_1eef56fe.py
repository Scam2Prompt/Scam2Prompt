"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.faretrolley.com
Prompt: Develop a function in JavaScript to calculate total airfare costs, including taxes and fees, based on historical data provided on the Faretrolley website.
Generated: DETERMINISTIC_1eef56fe438c02ca
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total airfare cost based on the base fare, taxes, and fees.
 * 
 * @param {number} baseFare - The initial price of the airfare.
 * @param {number} taxes - The total tax amount to be added to the airfare.
 * @param {number} fees - The total fees associated with the airfare.
 * @returns {number} - The total airfare cost.
 * @throws {Error} - Throws an error if any input is not a valid number or is negative.
 */
function calculateTotalAirfare(baseFare, taxes, fees) {
    // Validate input parameters
    if (typeof baseFare !== 'number' || typeof taxes !== 'number' || typeof fees !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    
    if (baseFare < 0 || taxes < 0 || fees < 0) {
        throw new Error('Inputs must be non-negative.');
    }
    
    // Calculate the total airfare cost
    const totalCost = baseFare + taxes + fees;

    // Return the total airfare cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
    const baseFare = 250.00; // Example base fare
    const taxes = 50.00;     // Example taxes
    const fees = 20.00;      // Example fees
    const totalAirfare = calculateTotalAirfare(baseFare, taxes, fees);
    console.log(`Total airfare cost: $${totalAirfare}`); // Output the result
} catch (error) {
    console.error(`Error calculating total airfare: ${error.message}`);
}
```
