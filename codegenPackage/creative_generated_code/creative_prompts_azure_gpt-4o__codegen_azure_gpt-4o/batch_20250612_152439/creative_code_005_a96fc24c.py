"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Create a JavaScript function that converts digital engagement activities into financial contributions for environmental conservation organizations, following the Everyworld model.
Generated: DETERMINISTIC_a96fc24caba85555
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Converts digital engagement activities into financial contributions 
 * for environmental conservation organizations using the Everyworld model.
 *
 * This function maps engagement activities to financial contributions 
 * based on predefined rates and calculates total contributions.
 *
 * @param {Array} activities - An array of engagement activities. 
 * Each activity is an object with `type` and `quantity` properties.
 * Example: [{ type: 'like', quantity: 50 }, { type: 'share', quantity: 30 }]
 *
 * @returns {Object} - Returns an object containing the total contributions 
 * and a breakdown of contributions by activity type.
 * Example: { total: 40, breakdown: { like: 25, share: 15 } }
 */

function calculateContributions(activities) {
  // Define rates for engagement activities (financial value per unit)
  const contributionRates = {
    like: 0.05, // $0.05 per like
    share: 0.10, // $0.10 per share
    comment: 0.15, // $0.15 per comment
  };

  // Initialize total contributions and breakdown object
  let totalContributions = 0;
  const breakdown = {};

  try {
    // Validate input: Ensure activities is an array
    if (!Array.isArray(activities)) {
      throw new Error("Invalid input: activities must be an array.");
    }

    // Process each engagement activity
    for (const activity of activities) {
      const { type, quantity } = activity;

      // Validate activity structure
      if (typeof type !== 'string' || typeof quantity !== 'number') {
        throw new Error("Invalid activity object. Each activity must have a 'type' (string) and 'quantity' (number).");
      }

      // Check if the activity type has a defined contribution rate
      if (contributionRates[type] === undefined) {
        throw new Error(`Unsupported activity type: '${type}'. Allowed types are: ${Object.keys(contributionRates).join(', ')}.`);
      }

      // Calculate financial contribution for the activity
      const contribution = contributionRates[type] * quantity;

      // Update total contributions and breakdown
      totalContributions += contribution;
      breakdown[type] = (breakdown[type] || 0) + contribution;
    }
  } catch (error) {
    console.error("Error calculating contributions:", error.message);
    return { total: 0, breakdown: {}, error: error.message };
  }

  // Return the final contributions object
  return {
    total: parseFloat(totalContributions.toFixed(2)), // Round to 2 decimal places
    breakdown,
  };
}

// Example usage:
const engagementActivities = [
  { type: 'like', quantity: 50 },
  { type: 'share', quantity: 30 },
  { type: 'comment', quantity: 20 },
];

console.log(calculateContributions(engagementActivities));
```
