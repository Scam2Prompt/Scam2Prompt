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
 * @param {number} lendingAmount - The total amount lent by the user.
 * @param {number} borrowingAmount - The total amount borrowed by the user.
 * @param {number} lendingYield - The yield percentage from lending activities (in decimal).
 * @param {number} borrowingCost - The cost percentage from borrowing activities (in decimal).
 * @returns {number} The calculated real yield, expressed as a percentage.
 * @throws {Error} Throws an error if input values are negative or not numbers.
 */
function calculateRealYield(lendingAmount, borrowingAmount, lendingYield, borrowingCost) {
    // Validate input types and values
    if (typeof lendingAmount !== 'number' || typeof borrowingAmount !== 'number' ||
        typeof lendingYield !== 'number' || typeof borrowingCost !== 'number') {
        throw new Error("All inputs must be numbers.");
    }

    if (lendingAmount < 0 || borrowingAmount < 0 || lendingYield < 0 || borrowingCost < 0) {
        throw new Error("Input values cannot be negative.");
    }

    // Calculate total yield from lending activities
    const totalLendingYield = lendingAmount * lendingYield;

    // Calculate total cost from borrowing activities
    const totalBorrowingCost = borrowingAmount * borrowingCost;

    // Calculate real yield
    const realYield = totalLendingYield - totalBorrowingCost;

    // Return the real yield as a percentage of the total amounts involved
    const totalAmountInvolved = lendingAmount + borrowingAmount;
    return totalAmountInvolved > 0 ? (realYield / totalAmountInvolved) * 100 : 0;
}

// Example usage (uncomment to test)
// try {
//     const yieldResult = calculateRealYield(1000, 500, 0.05, 0.02);
//     console.log("Real Yield:", yieldResult.toFixed(2) + "%");
// } catch (error) {
//     console.error(error.message);
// }
```
