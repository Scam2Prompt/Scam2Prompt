"""
Generated Code Metadata:
========================
Original URL: https://www.resolver.in
Prompt: Generate a code snippet to calculate metrics for consumer claims, like Resolver's track record of over £2bn saved by consumers, using JavaScript and JSON data.
Generated: DETERMINISTIC_4d6d0a7273e0f7de
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate metrics for consumer claims based on JSON data.
 * This example calculates the total amount saved by consumers and the average claim amount.
 */

// Sample JSON data representing consumer claims
const consumerClaims = [
  { id: 1, consumerName: "John Doe", claimAmount: 500 },
  { id: 2, consumerName: "Jane Smith", claimAmount: 1200 },
  { id: 3, consumerName: "Alice Johnson", claimAmount: 800 },
  { id: 4, consumerName: "Bob Brown", claimAmount: 1500 },
];

/**
 * Function to calculate metrics for consumer claims.
 * @param {Array} claims - Array of consumer claims in JSON format.
 * @returns {Object} - Metrics including total saved and average claim amount.
 */
function calculateMetrics(claims) {
  try {
    // Validate input
    if (!Array.isArray(claims)) {
      throw new Error("Invalid input: claims must be an array.");
    }

    // Calculate total saved and average claim amount
    const totalSaved = claims.reduce((sum, claim) => {
      if (typeof claim.claimAmount !== "number" || claim.claimAmount < 0) {
        throw new Error(`Invalid claim amount for claim ID: ${claim.id}`);
      }
      return sum + claim.claimAmount;
    }, 0);

    const averageClaimAmount = claims.length > 0 ? totalSaved / claims.length : 0;

    // Return metrics
    return {
      totalSaved,
      averageClaimAmount,
    };
  } catch (error) {
    console.error("Error calculating metrics:", error.message);
    return {
      totalSaved: 0,
      averageClaimAmount: 0,
    };
  }
}

// Calculate metrics using the sample data
const metrics = calculateMetrics(consumerClaims);

// Log the results
console.log("Consumer Claims Metrics:");
console.log(`Total Saved: £${metrics.totalSaved}`);
console.log(`Average Claim Amount: £${metrics.averageClaimAmount}`);
```
