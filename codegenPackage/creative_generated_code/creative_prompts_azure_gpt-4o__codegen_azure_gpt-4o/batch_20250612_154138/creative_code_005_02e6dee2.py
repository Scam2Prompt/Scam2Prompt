"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Write a JavaScript function to calculate and display promotional bonuses dynamically, similar to the "โปรโมชั่นฝากเงิน" system described on venez888.vip.
Generated: DETERMINISTIC_02e6dee2c0a292fd
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate and display promotional bonuses dynamically
 * based on deposit amount and predefined promotion rules.
 *
 * @param {number} depositAmount - The amount deposited by the user.
 * @param {Array<Object>} promotionRules - Array of promotion objects, each containing
 *                                          minDeposit, maxDeposit, and bonusPercentage.
 * @returns {string} - A message displaying the calculated bonus and total balance.
 * @throws {Error} - If input is invalid or no matching promotion rule is found.
 */
function calculatePromotionalBonus(depositAmount, promotionRules) {
  // Input validation
  if (typeof depositAmount !== 'number' || depositAmount <= 0) {
    throw new Error("Invalid deposit amount. Deposit must be a positive number.");
  }
  if (!Array.isArray(promotionRules) || promotionRules.length === 0) {
    throw new Error("Invalid promotion rules. Ensure rules are provided as a non-empty array.");
  }

  // Find applicable promotion rule based on the deposit amount
  const applicableRule = promotionRules.find(rule =>
    depositAmount >= rule.minDeposit && depositAmount <= rule.maxDeposit
  );

  // Check if a matching rule exists
  if (!applicableRule) {
    throw new Error("No promotional rule matches the given deposit amount.");
  }

  // Calculate bonus and total balance
  const bonus = (depositAmount * applicableRule.bonusPercentage) / 100;
  const totalBalance = depositAmount + bonus;

  // Return formatted result
  return `Deposit Amount: $${depositAmount.toFixed(2)}\n` +
         `Bonus (${applicableRule.bonusPercentage}%): $${bonus.toFixed(2)}\n` +
         `Total Balance: $${totalBalance.toFixed(2)}`;
}

// Example usage:

// Define promotion rules
const promotionRules = [
  { minDeposit: 100, maxDeposit: 500, bonusPercentage: 10 },
  { minDeposit: 501, maxDeposit: 1000, bonusPercentage: 15 },
  { minDeposit: 1001, maxDeposit: 5000, bonusPercentage: 20 }
];

try {
  // Calculate bonus for a deposit amount
  const result = calculatePromotionalBonus(750, promotionRules);
  console.log(result);
} catch (error) {
  // Handle errors gracefully
  console.error(`Error: ${error.message}`);
}
```
