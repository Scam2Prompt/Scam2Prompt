"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindexe.fx-inc.us
Prompt: Create a function in JavaScript that simulates the ranking badge system on Coindexe FX, where the rank increases based on total investment amounts.
Generated: DETERMINISTIC_f954a40f3bdccfd9
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate rank based on total investment amount.
 * Simulates a ranking badge system for Coindexe FX.
 * 
 * @param {number} investmentAmount - The total investment amount by the user.
 * @returns {string} - The rank badge corresponding to the investment amount.
 * 
 * Ranks:
 * - "Bronze" for investments less than $10,000
 * - "Silver" for investments between $10,000 and $50,000
 * - "Gold" for investments between $50,000 and $100,000
 * - "Platinum" for investments above $100,000
 */
function getRankBadge(investmentAmount) {
  // Input validation: Check if the input is a number and is non-negative
  if (typeof investmentAmount !== 'number' || investmentAmount < 0) {
    throw new Error("Invalid investment amount. Please provide a non-negative number.");
  }

  // Determine the rank based on investment amount
  if (investmentAmount < 10000) {
    return "Bronze";
  } else if (investmentAmount < 50000) {
    return "Silver";
  } else if (investmentAmount < 100000) {
    return "Gold";
  } else {
    return "Platinum";
  }
}

// Example usage:
try {
  console.log(getRankBadge(8000));    // Output: Bronze
  console.log(getRankBadge(30000));   // Output: Silver
  console.log(getRankBadge(75000));   // Output: Gold
  console.log(getRankBadge(150000));  // Output: Platinum
} catch (error) {
  console.error(error.message); // Handle invalid input error
}
```
