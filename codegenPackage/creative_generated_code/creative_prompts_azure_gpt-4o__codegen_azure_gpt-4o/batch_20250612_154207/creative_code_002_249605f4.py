"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qbt.finance
Prompt: Create a JavaScript function to calculate the "Borrow Limit" for a user on Qubit Finance based on their supplied collateral and the APR rates provided for assets like BTCB and CAKE.
Generated: DETERMINISTIC_249605f48fa6fd93
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the borrow limit for a user on Qubit Finance.
 * @param {Object[]} collateral - Array of user-supplied collateral objects.
 *        Each object should contain:
 *        - asset {string}: Name of the asset (e.g., 'BTCB', 'CAKE').
 *        - amount {number}: Amount of the asset supplied.
 * @param {Object} aprRates - Object containing APR rates for each asset.
 *        Key-value pairs should be asset names and their respective APR rates.
 * @returns {number} The calculated borrow limit for the user.
 * @throws {Error} If invalid input is provided or a required asset APR rate is missing.
 */
function calculateBorrowLimit(collateral, aprRates) {
  // Validate input
  if (!Array.isArray(collateral) || typeof aprRates !== 'object') {
    throw new Error('Invalid input: collateral must be an array and aprRates must be an object.');
  }

  let borrowLimit = 0;

  // Iterate through the supplied collateral array
  collateral.forEach((item) => {
    const { asset, amount } = item;

    // Validate individual collateral item
    if (typeof asset !== 'string' || typeof amount !== 'number' || amount < 0) {
      throw new Error(`Invalid collateral item: ${JSON.stringify(item)}`);
    }

    // Get the APR rate for the given asset
    const aprRate = aprRates[asset];
    if (aprRate === undefined) {
      throw new Error(`Missing APR rate for asset: ${asset}`);
    }

    // Validate APR rate
    if (typeof aprRate !== 'number' || aprRate < 0) {
      throw new Error(`Invalid APR rate for asset ${asset}: ${aprRate}`);
    }

    // Calculate borrow limit for this asset and add to the total
    borrowLimit += amount * aprRate;
  });

  return borrowLimit;
}

// Example usage:
// User collateral data
const userCollateral = [
  { asset: 'BTCB', amount: 0.5 }, // 0.5 BTCB
  { asset: 'CAKE', amount: 200 }, // 200 CAKE
];

// APR rates for assets
const aprRates = {
  BTCB: 0.75, // 75% loan-to-value (LTV) rate
  CAKE: 0.6,  // 60% loan-to-value (LTV) rate
};

try {
  const borrowLimit = calculateBorrowLimit(userCollateral, aprRates);
  console.log(`Borrow Limit: ${borrowLimit}`);
} catch (error) {
  console.error(`Error calculating borrow limit: ${error.message}`);
}
```
