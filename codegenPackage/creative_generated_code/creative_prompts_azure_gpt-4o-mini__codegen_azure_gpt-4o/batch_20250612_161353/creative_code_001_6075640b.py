"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Write a JavaScript function that calculates the total rewards earned by a delegator in the bitsCrunch Network based on their delegated amount and query fee cut.
Generated: DETERMINISTIC_6075640b8fd2f7b0
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total rewards earned by a delegator in the bitsCrunch Network.
 *
 * @param {number} delegatedAmount - The amount of tokens delegated by the delegator.
 * @param {number} totalQueryFee - The total query fee collected by the validator.
 * @param {number} queryFeeCut - The percentage cut (in decimal form) of the query fee taken by the validator (e.g., 0.2 for 20% cut).
 * @returns {number} The total rewards earned by the delegator.
 * @throws {Error} Throws an error if input parameters are invalid.
 */
function calculateDelegatorRewards(delegatedAmount, totalQueryFee, queryFeeCut) {
  // Input validation
  if (
    typeof delegatedAmount !== "number" ||
    typeof totalQueryFee !== "number" ||
    typeof queryFeeCut !== "number"
  ) {
    throw new Error("All inputs must be numbers.");
  }

  if (delegatedAmount <= 0 || totalQueryFee < 0 || queryFeeCut < 0 || queryFeeCut > 1) {
    throw new Error("Invalid input values: Ensure delegatedAmount > 0, totalQueryFee >= 0, and 0 <= queryFeeCut <= 1.");
  }

  // Calculate the query fee available for delegators after validator's cut
  const delegatorQueryFee = totalQueryFee * (1 - queryFeeCut);

  // Calculate delegator's proportional reward based on their delegated amount
  const delegatorRewards = delegatedAmount * (delegatorQueryFee / delegatedAmount);

  return delegatorRewards;
}

// Example usage:
try {
  const delegatedAmount = 1000; // Example delegated amount in tokens
  const totalQueryFee = 500; // Example total query fee collected by validator in tokens
  const queryFeeCut = 0.2; // Validator takes 20% of the query fee

  const rewards = calculateDelegatorRewards(delegatedAmount, totalQueryFee, queryFeeCut);
  console.log(`Delegator Rewards: ${rewards} tokens`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
