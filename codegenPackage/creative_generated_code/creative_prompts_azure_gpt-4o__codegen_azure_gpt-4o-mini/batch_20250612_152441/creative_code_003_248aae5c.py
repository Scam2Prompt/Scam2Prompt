"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-mvp.pages.dev
Prompt: Write a function in JavaScript to calculate the collateral ratio (C-ratio) for a user on the SYNTHR platform, given their debt balance and collateral balance. Use the platform's requirement of a minimum 150% C-ratio.
Generated: DETERMINISTIC_248aae5c17624bc2
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the collateral ratio (C-ratio) for a user on the SYNTHR platform.
 *
 * The C-ratio is calculated as:
 * C-ratio = (Collateral Balance / Debt Balance) * 100
 *
 * The platform requires a minimum C-ratio of 150% for users.
 *
 * @param {number} collateralBalance - The amount of collateral the user has.
 * @param {number} debtBalance - The amount of debt the user has.
 * @returns {object} - An object containing the C-ratio and whether it meets the minimum requirement.
 * @throws {Error} - Throws an error if collateralBalance or debtBalance are negative or if debtBalance is zero.
 */
function calculateCollateralRatio(collateralBalance, debtBalance) {
    // Validate input parameters
    if (collateralBalance < 0) {
        throw new Error("Collateral balance cannot be negative.");
    }
    if (debtBalance < 0) {
        throw new Error("Debt balance cannot be negative.");
    }
    if (debtBalance === 0) {
        throw new Error("Debt balance cannot be zero.");
    }

    // Calculate the collateral ratio
    const collateralRatio = (collateralBalance / debtBalance) * 100;

    // Check if the collateral ratio meets the minimum requirement
    const meetsMinimumRequirement = collateralRatio >= 150;

    return {
        collateralRatio: collateralRatio,
        meetsMinimumRequirement: meetsMinimumRequirement
    };
}

// Example usage (for testing purposes)
// const result = calculateCollateralRatio(2000, 1000);
// console.log(result); // { collateralRatio: 200, meetsMinimumRequirement: true }

```
