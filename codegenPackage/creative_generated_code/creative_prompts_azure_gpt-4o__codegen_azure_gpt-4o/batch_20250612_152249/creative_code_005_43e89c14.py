"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidbvuwd5kzejblzv323edzpb2o4gl4xvjm3d2ghg5fxtp4powdsxy.ipfs.dweb.link
Prompt: Develop a function in JavaScript to calculate the real yield for Venus Prime Token users based on their lending and borrowing activities.
Generated: DETERMINISTIC_43e89c14a2788ff8
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateRealYield
 * @description Calculates the real yield for Venus Prime Token users based on their lending and borrowing activities.
 * 
 * @param {number} lendingAPY - Annual Percentage Yield (APY) from lending activities (as a percentage, e.g., 5 for 5%).
 * @param {number} borrowingAPY - Annual Percentage Yield (APY) from borrowing activities (as a percentage, e.g., 3 for 3%).
 * @param {number} borrowedAmount - The total amount borrowed by the user.
 * @param {number} lentAmount - The total amount lent by the user.
 * @returns {number} - The real yield (net annual percentage gain or loss) for the user.
 * 
 * @throws {Error} - Throws an error if input values are invalid (negative, non-numeric, or missing).
 */
function calculateRealYield(lendingAPY, borrowingAPY, borrowedAmount, lentAmount) {
    // Input validation
    if (
        lendingAPY < 0 || borrowingAPY < 0 || borrowedAmount < 0 || lentAmount < 0 ||
        isNaN(lendingAPY) || isNaN(borrowingAPY) || isNaN(borrowedAmount) || isNaN(lentAmount)
    ) {
        throw new Error('Invalid input: All values must be non-negative numbers.');
    }

    // Edge case: If lentAmount is 0, no lending yield can be calculated
    if (lentAmount === 0) {
        return -borrowingAPY; // User incurs borrowing cost only
    }

    // Calculate lending yield (annual gain from lending)
    const lendingYield = (lendingAPY / 100) * lentAmount;

    // Calculate borrowing cost (annual loss from borrowing)
    const borrowingCost = (borrowingAPY / 100) * borrowedAmount;

    // Calculate real yield (net annual percentage gain/loss)
    const realYield = ((lendingYield - borrowingCost) / lentAmount) * 100;

    return realYield;
}

// Example usage:
try {
    const lendingAPY = 5; // 5% lending APY
    const borrowingAPY = 3; // 3% borrowing APY
    const borrowedAmount = 2000; // User borrowed $2000
    const lentAmount = 5000; // User lent $5000

    const realYield = calculateRealYield(lendingAPY, borrowingAPY, borrowedAmount, lentAmount);
    console.log(`Real Yield: ${realYield.toFixed(2)}%`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
