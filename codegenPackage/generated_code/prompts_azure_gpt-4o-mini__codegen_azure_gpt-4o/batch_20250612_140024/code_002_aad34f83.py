"""
Generated Code Metadata:
========================
Original URL: https://craves.io
Prompt: Create a function in JavaScript that calculates potential winnings based on Angkah's bonus structure for new members and daily cash back offers.
Generated: DETERMINISTIC_aad34f836071bc1e
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate potential winnings based on Angkah's bonus structure.
 * 
 * @param {number} depositAmount - The amount deposited by the user.
 * @param {number} dailyCashBackRate - The daily cashback rate (percentage).
 * @param {number} days - The number of days the cashback is applied.
 * @returns {number} - The total potential winnings.
 * 
 * Assumptions:
 * - New members receive a fixed bonus of 20% on their initial deposit.
 * - Daily cashback is calculated as a percentage of the deposit amount.
 * - Cashback accumulates over the specified number of days.
 */
function calculatePotentialWinnings(depositAmount, dailyCashBackRate, days) {
  // Input validation
  if (typeof depositAmount !== 'number' || depositAmount <= 0) {
    throw new Error("Invalid deposit amount. It must be a positive number.");
  }
  if (typeof dailyCashBackRate !== 'number' || dailyCashBackRate < 0 || dailyCashBackRate > 100) {
    throw new Error("Invalid daily cashback rate. It must be a percentage between 0 and 100.");
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error("Invalid number of days. It must be a positive integer.");
  }

  // Calculate the new member bonus (20% of the deposit amount)
  const newMemberBonus = depositAmount * 0.2;

  // Calculate the daily cashback amount
  const dailyCashBack = (depositAmount * dailyCashBackRate) / 100;

  // Calculate the total cashback over the specified number of days
  const totalCashBack = dailyCashBack * days;

  // Calculate the total potential winnings
  const totalWinnings = depositAmount + newMemberBonus + totalCashBack;

  return totalWinnings;
}

// Example usage:
try {
  const depositAmount = 1000; // User's deposit amount
  const dailyCashBackRate = 5; // Daily cashback rate in percentage
  const days = 7; // Number of days cashback is applied

  const potentialWinnings = calculatePotentialWinnings(depositAmount, dailyCashBackRate, days);
  console.log(`Total potential winnings: $${potentialWinnings.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
