"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Generate a code snippet in JavaScript for a simple calculator that determines the cost of moving sleds to different pull centers in Australia, considering factors mentioned on jobbo.com.au."
Generated: DETERMINISTIC_475e9fed9b906dae
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Sled Moving Costs
 * Calculates the cost of moving sleds to different pull centers in Australia.
 * Factors are based on jobbo.com.au (e.g., distance, weight, and base rate).
 */

// Constants for cost calculation
const BASE_RATE = 50; // Base rate in AUD
const COST_PER_KM = 2; // Cost per kilometer in AUD
const COST_PER_KG = 0.5; // Cost per kilogram in AUD

/**
 * Function to calculate the moving cost
 * @param {number} distance - Distance to the pull center in kilometers
 * @param {number} weight - Weight of the sled in kilograms
 * @returns {number} - Total cost in AUD
 */
function calculateMovingCost(distance, weight) {
  try {
    // Validate inputs
    if (distance < 0 || weight < 0) {
      throw new Error("Distance and weight must be non-negative numbers.");
    }

    // Calculate cost
    const distanceCost = distance * COST_PER_KM;
    const weightCost = weight * COST_PER_KG;
    const totalCost = BASE_RATE + distanceCost + weightCost;

    return totalCost;
  } catch (error) {
    console.error("Error calculating moving cost:", error.message);
    return null; // Return null in case of an error
  }
}

/**
 * Example usage of the calculator
 */
function main() {
  // Example inputs
  const distanceToPullCenter = 120; // in kilometers
  const sledWeight = 300; // in kilograms

  // Calculate cost
  const movingCost = calculateMovingCost(distanceToPullCenter, sledWeight);

  if (movingCost !== null) {
    console.log(`The total cost to move the sled is: $${movingCost.toFixed(2)} AUD`);
  } else {
    console.log("Failed to calculate the moving cost due to an error.");
  }
}

// Run the example
main();
```
