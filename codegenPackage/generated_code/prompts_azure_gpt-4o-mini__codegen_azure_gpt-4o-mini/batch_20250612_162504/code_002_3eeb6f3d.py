"""
Generated Code Metadata:
========================
Original URL: https://dogepreneur-in.pages.dev
Prompt: Create a JavaScript function that calculates potential returns from holding DogePreneur tokens based on rental income and property appreciation.
Generated: DETERMINISTIC_3eeb6f3d4e6f15b1
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential returns from holding DogePreneur tokens based on rental income and property appreciation.
 * 
 * @param {number} initialInvestment - The initial investment amount in DogePreneur tokens.
 * @param {number} rentalIncome - The annual rental income generated from the property.
 * @param {number} propertyAppreciationRate - The annual property appreciation rate (as a percentage).
 * @param {number} years - The number of years to hold the investment.
 * @returns {object} - An object containing total returns and breakdown of rental income and appreciation.
 * @throws {Error} - Throws an error if any input is invalid (negative values, non-numeric).
 */
function calculateDogePreneurReturns(initialInvestment, rentalIncome, propertyAppreciationRate, years) {
    // Validate inputs
    if (typeof initialInvestment !== 'number' || initialInvestment < 0) {
        throw new Error('Initial investment must be a non-negative number.');
    }
    if (typeof rentalIncome !== 'number' || rentalIncome < 0) {
        throw new Error('Rental income must be a non-negative number.');
    }
    if (typeof propertyAppreciationRate !== 'number' || propertyAppreciationRate < 0) {
        throw new Error('Property appreciation rate must be a non-negative number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }

    // Calculate total rental income over the specified years
    const totalRentalIncome = rentalIncome * years;

    // Calculate total property appreciation over the specified years
    const totalAppreciation = initialInvestment * (Math.pow(1 + (propertyAppreciationRate / 100), years) - 1);

    // Calculate total returns
    const totalReturns = initialInvestment + totalRentalIncome + totalAppreciation;

    // Return the results as an object
    return {
        totalReturns: totalReturns,
        totalRentalIncome: totalRentalIncome,
        totalAppreciation: totalAppreciation
    };
}

// Example usage (uncomment to test):
// try {
//     const results = calculateDogePreneurReturns(1000, 200, 5, 10);
//     console.log(results);
// } catch (error) {
//     console.error(error.message);
// }
```
