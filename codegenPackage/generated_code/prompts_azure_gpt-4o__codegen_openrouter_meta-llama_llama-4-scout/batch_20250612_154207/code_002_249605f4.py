"""
Generated Code Metadata:
========================
Original URL: https://www.qbt.finance
Prompt: Create a JavaScript function to calculate the "Borrow Limit" for a user on Qubit Finance based on their supplied collateral and the APR rates provided for assets like BTCB and CAKE.
Generated: DETERMINISTIC_249605f48fa6fd93
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the borrow limit for a user on Qubit Finance based on their supplied collateral and APR rates.
 * 
 * @param {Object} collateral - The user's supplied collateral.
 * @param {string} collateral.asset - The asset symbol (e.g., "BTCB", "CAKE").
 * @param {number} collateral.value - The value of the collateral.
 * @param {Object} aprRates - The APR rates for the assets.
 * @param {number} aprRates[asset] - The APR rate for the asset.
 * @returns {number} The borrow limit.
 */
function calculateBorrowLimit(collateral, aprRates) {
    // Define the liquidation threshold (in %) and the borrow limit formula parameters
    const liquidationThreshold = 0.8; // 80%
    const borrowLimitFormula = (collateralValue, aprRate) => collateralValue * liquidationThreshold * (1 - aprRate / 100);

    // Check if collateral and aprRates are valid
    if (!collateral || !aprRates) {
        throw new Error("Invalid input: collateral and aprRates are required.");
    }

    // Check if collateral asset and value are valid
    if (!collateral.asset || !collateral.value) {
        throw new Error("Invalid collateral: asset and value are required.");
    }

    // Check if APR rate for the collateral asset is available
    if (!(collateral.asset in aprRates)) {
        throw new Error(`APR rate for ${collateral.asset} is not available.`);
    }

    // Calculate the borrow limit
    try {
        const aprRate = aprRates[collateral.asset];
        const borrowLimit = borrowLimitFormula(collateral.value, aprRate);
        return borrowLimit;
    } catch (error) {
        throw new Error(`Error calculating borrow limit: ${error.message}`);
    }
}

// Example usage:
const collateral = {
    asset: "BTCB",
    value: 10000,
};

const aprRates = {
    BTCB: 10, // 10% APR
    CAKE: 20, // 20% APR
};

try {
    const borrowLimit = calculateBorrowLimit(collateral, aprRates);
    console.log(`Borrow limit: $${borrowLimit.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
