"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freebitcoinmining.website
Prompt: Create a function in JavaScript that calculates the affiliate bonus percentage for a user based on the mining plan details provided by FreeBitcoinMining.
Generated: DETERMINISTIC_9c2a76319492d9f6
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the affiliate bonus percentage based on the mining plan details.
 * 
 * @param {string} plan - The mining plan type (e.g., "basic", "silver", "gold", "platinum").
 * @returns {number} - The affiliate bonus percentage for the given plan.
 * @throws {Error} - Throws an error if the plan type is invalid or missing.
 */
function calculateAffiliateBonus(plan) {
  // Validate the input
  if (!plan || typeof plan !== "string") {
    throw new Error("Invalid plan type provided. Plan must be a non-empty string.");
  }

  // Define bonus percentages for each plan
  const bonusPercentages = {
    basic: 5,    // Basic plan offers a 5% affiliate bonus
    silver: 10,  // Silver plan offers a 10% affiliate bonus
    gold: 15,    // Gold plan offers a 15% affiliate bonus
    platinum: 20 // Platinum plan offers a 20% affiliate bonus
  };

  // Normalize input to lower case for case-insensitive matching
  const normalizedPlan = plan.toLowerCase();

  // Check if the plan exists in the bonusPercentages object
  if (!bonusPercentages.hasOwnProperty(normalizedPlan)) {
    throw new Error(`Invalid plan type: '${plan}'. Valid plans are: basic, silver, gold, platinum.`);
  }

  // Return the bonus percentage for the given plan
  return bonusPercentages[normalizedPlan];
}

// Example usage (uncomment the lines below to test):
// try {
//   console.log(calculateAffiliateBonus("gold")); // Output: 15
//   console.log(calculateAffiliateBonus("silver")); // Output: 10
//   console.log(calculateAffiliateBonus("invalidPlan")); // Throws an error
// } catch (error) {
//   console.error(error.message);
// }
```
