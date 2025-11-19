"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craves.io
Prompt: Create a function in JavaScript that calculates potential winnings based on Angkah's bonus structure for new members and daily cash back offers.
Generated: DETERMINISTIC_aad34f836071bc1e
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential winnings based on Angkah's bonus structure.
 * Angkah offers:
 *   1. A bonus for new members (e.g., 100% deposit bonus up to a certain limit).
 *   2. Daily cashback offers (e.g., a percentage of losses returned as cashback).
 * 
 * @param {number} depositAmount - The initial deposit amount by the new member.
 * @param {number} dailyLosses - Total losses incurred by the user in a day.
 * @returns {Object} An object containing calculated bonus, cashback, and total potential winnings.
 */
function calculatePotentialWinnings(depositAmount, dailyLosses) {
  try {
    // Constants for Angkah's bonus structure
    const BONUS_PERCENTAGE = 100; // New member deposit bonus percentage (100% match)
    const BONUS_LIMIT = 500; // Maximum bonus amount for new members
    const CASHBACK_PERCENTAGE = 10; // Daily cashback percentage

    // Input validation
    if (depositAmount < 0 || dailyLosses < 0) {
      throw new Error("Deposit amount and daily losses must be non-negative numbers.");
    }

    // Calculate new member bonus
    let bonus = Math.min((depositAmount * BONUS_PERCENTAGE) / 100, BONUS_LIMIT);

    // Calculate daily cashback
    let cashback = (dailyLosses * CASHBACK_PERCENTAGE) / 100;

    // Calculate total potential winnings
    let totalPotentialWinnings = depositAmount + bonus + cashback;

    // Return the results as an object
    return {
      bonus: bonus,
      cashback: cashback,
      totalPotentialWinnings: totalPotentialWinnings,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred:", error.message);
    return {
      bonus: 0,
      cashback: 0,
      totalPotentialWinnings: 0,
      error: error.message,
    };
  }
}

/* Example Usage */
const results = calculatePotentialWinnings(300, 200);
console.log("Potential Winnings:", results);
```
