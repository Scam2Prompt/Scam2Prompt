"""
Generated Code Metadata:
========================
Original URL: https://ezi-trade.com
Prompt: "Generate a JavaScript function to simulate the investment process on Ezi-Trade, taking into account the weekly returns, investment duration, and capital back guarantee for the Executive plan."
Generated: DETERMINISTIC_7ff63010389f542e
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the investment process on Ezi-Trade for the Executive plan.
 * 
 * @param {number} initialCapital - The initial investment amount.
 * @param {number} durationWeeks - The investment duration in weeks.
 * @param {number} weeklyReturnRate - The weekly return rate (e.g., 0.05 for 5%).
 * @param {boolean} capitalBackGuarantee - Whether the capital back guarantee is enabled.
 * @returns {Object} An object containing the simulation results.
 * @throws {Error} If input validation fails.
 */
function simulateEziTradeInvestment(
  initialCapital,
  durationWeeks,
  weeklyReturnRate,
  capitalBackGuarantee
) {
  // Input validation
  if (
    typeof initialCapital !== 'number' ||
    typeof durationWeeks !== 'number' ||
    typeof weeklyReturnRate !== 'number' ||
    typeof capitalBackGuarantee !== 'boolean'
  ) {
    throw new Error('Invalid input types. All inputs must be numbers except capitalBackGuarantee (boolean).');
  }

  if (initialCapital <= 0 || durationWeeks <= 0 || weeklyReturnRate <= 0) {
    throw new Error('Initial capital, duration, and weekly return rate must be positive numbers.');
  }

  // Calculate weekly returns
  const weeklyReturns = [];
  let currentCapital = initialCapital;
  let totalReturns = 0;

  for (let week = 1; week <= durationWeeks; week++) {
    const weeklyProfit = currentCapital * weeklyReturnRate;
    weeklyReturns.push({
      week,
      capitalAtStart: currentCapital,
      weeklyProfit,
      capitalAtEnd: currentCapital + weeklyProfit,
    });
    totalReturns += weeklyProfit;
    currentCapital += weeklyProfit;
  }

  // Apply capital back guarantee if enabled
  let finalCapital = currentCapital;
  if (capitalBackGuarantee) {
    finalCapital = initialCapital + totalReturns;
  }

  return {
    initialCapital,
    durationWeeks,
    weeklyReturnRate,
    capitalBackGuarantee,
    weeklyReturns,
    totalReturns,
    finalCapital,
  };
}

// Example usage:
// const result = simulateEziTradeInvestment(10000, 12, 0.05, true);
// console.log(result);
```
