"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hometymex.co.za
Prompt: Create a JavaScript function that calculates the potential cashback amount from HomeTyme based on different home loan values.
Generated: DETERMINISTIC_d18a1e4beaf6d224
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential cashback amount based on home loan value.
 * 
 * HomeTyme cashback tiers:
 * - Loan value less than $100,000: 0.5% cashback
 * - Loan value between $100,000 and $300,000: 1% cashback
 * - Loan value greater than $300,000: 1.5% cashback
 * 
 * @param {number} loanValue - The value of the home loan.
 * @returns {number|null} The potential cashback amount, or null if input is invalid.
 */
function calculateCashback(loanValue) {
  // Validate input: loanValue must be a positive number
  if (typeof loanValue !== 'number' || loanValue <= 0) {
    console.error("Invalid loan value. Must be a positive number.");
    return null;
  }

  let cashbackPercentage = 0;

  // Determine cashback percentage based on loan tiers
  if (loanValue < 100000) {
    cashbackPercentage = 0.005; // 0.5%
  } else if (loanValue >= 100000 && loanValue <= 300000) {
    cashbackPercentage = 0.01; // 1%
  } else if (loanValue > 300000) {
    cashbackPercentage = 0.015; // 1.5%
  }

  // Calculate cashback amount
  const cashbackAmount = loanValue * cashbackPercentage;

  // Ensure the result is rounded to 2 decimal places for currency formatting
  return Math.round(cashbackAmount * 100) / 100;
}

// Example usage:
const loanValue = 250000; // Replace with desired loan value
const cashback = calculateCashback(loanValue);

if (cashback !== null) {
  console.log(`For a loan value of $${loanValue}, the potential cashback is $${cashback}.`);
}
```
