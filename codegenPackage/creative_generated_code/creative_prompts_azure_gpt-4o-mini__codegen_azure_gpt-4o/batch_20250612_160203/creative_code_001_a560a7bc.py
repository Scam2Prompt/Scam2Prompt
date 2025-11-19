"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://awards-lidofinance.com
Prompt: Write a JavaScript function that calculates the potential cash back rewards for a user based on their spending habits with Discover credit cards.
Generated: DETERMINISTIC_a560a7bcb475427e
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential cash back rewards for a user based on their spending habits.
 * Discover credit cards offer different reward categories, such as:
 * - 5% cash back on quarterly rotating categories (up to $1,500 spent per quarter).
 * - 1% cash back on all other purchases (no cap).
 *
 * @param {Object} spending - An object representing the user's spending across categories.
 * Example:
 * {
 *   "groceries": 500,
 *   "restaurants": 700,
 *   "gas": 400,
 *   "other": 600
 * }
 * @param {Array} rotatingCategories - Array of strings for current quarter's 5% reward categories.
 * Example: ["groceries", "gas"]
 * 
 * @returns {number} - Total cash back rewards earned.
 */
function calculateCashBack(spending, rotatingCategories) {
  // Validate input parameters
  if (typeof spending !== 'object' || !Array.isArray(rotatingCategories)) {
    throw new Error('Invalid input: spending must be an object and rotatingCategories must be an array.');
  }

  // Constants
  const FIVE_PERCENT_RATE = 0.05;
  const ONE_PERCENT_RATE = 0.01;
  const QUARTERLY_SPENDING_CAP = 1500;

  let totalCashBack = 0;

  // Iterate through spending categories
  for (const category in spending) {
    if (spending.hasOwnProperty(category)) {
      const amountSpent = spending[category];

      // Validate spending values
      if (typeof amountSpent !== 'number' || amountSpent < 0) {
        throw new Error(`Invalid spending amount for category "${category}". Must be a positive number.`);
      }

      // Check if the category qualifies for 5% cash back
      if (rotatingCategories.includes(category)) {
        const eligibleAmount = Math.min(amountSpent, QUARTERLY_SPENDING_CAP);
        const fivePercentCashBack = eligibleAmount * FIVE_PERCENT_RATE;
        totalCashBack += fivePercentCashBack;

        // Add 1% cash back for any amount spent beyond the cap
        if (amountSpent > QUARTERLY_SPENDING_CAP) {
          const excessAmount = amountSpent - QUARTERLY_SPENDING_CAP;
          totalCashBack += excessAmount * ONE_PERCENT_RATE;
        }
      } else {
        // All other categories earn 1% cash back
        totalCashBack += amountSpent * ONE_PERCENT_RATE;
      }
    }
  }

  return totalCashBack;
}

// Example Usage
try {
  const userSpending = {
    groceries: 500,
    restaurants: 700,
    gas: 400,
    other: 600
  };
  const currentQuarterCategories = ['groceries', 'gas'];

  const rewards = calculateCashBack(userSpending, currentQuarterCategories);
  console.log(`Total Cash Back Rewards: $${rewards.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
