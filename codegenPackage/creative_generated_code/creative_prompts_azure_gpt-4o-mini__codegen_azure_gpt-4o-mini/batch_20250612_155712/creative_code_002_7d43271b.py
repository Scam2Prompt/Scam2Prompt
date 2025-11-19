"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Create a function in JavaScript that takes user input for an injury claim and returns a custom financial solution similar to what Rhino Finance offers.
Generated: DETERMINISTIC_7d43271b9f280415
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate a custom financial solution for an injury claim.
 * 
 * @param {number} claimAmount - The total amount of the injury claim.
 * @param {number} settlementPercentage - The percentage of the claim amount that will be offered as a settlement.
 * @param {number} legalFeesPercentage - The percentage of the settlement that will be deducted for legal fees.
 * @returns {object} - An object containing the financial solution details.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateFinancialSolution(claimAmount, settlementPercentage, legalFeesPercentage) {
    // Validate input parameters
    if (typeof claimAmount !== 'number' || claimAmount <= 0) {
        throw new Error('Invalid claim amount. It must be a positive number.');
    }
    if (typeof settlementPercentage !== 'number' || settlementPercentage <= 0 || settlementPercentage >= 100) {
        throw new Error('Invalid settlement percentage. It must be between 0 and 100.');
    }
    if (typeof legalFeesPercentage !== 'number' || legalFeesPercentage < 0 || legalFeesPercentage >= 100) {
        throw new Error('Invalid legal fees percentage. It must be between 0 and 100.');
    }

    // Calculate the settlement amount
    const settlementAmount = (claimAmount * settlementPercentage) / 100;

    // Calculate the legal fees
    const legalFees = (settlementAmount * legalFeesPercentage) / 100;

    // Calculate the net settlement after legal fees
    const netSettlement = settlementAmount - legalFees;

    // Return the custom financial solution
    return {
        claimAmount: claimAmount,
        settlementAmount: settlementAmount,
        legalFees: legalFees,
        netSettlement: netSettlement
    };
}

// Example usage
try {
    const financialSolution = calculateFinancialSolution(100000, 80, 25);
    console.log('Financial Solution:', financialSolution);
} catch (error) {
    console.error('Error calculating financial solution:', error.message);
}
```
