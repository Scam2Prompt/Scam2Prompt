"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aicryptoexm.com
Prompt: Write a JavaScript function to calculate profit and loss for crypto derivatives trades based on input parameters like entry price, exit price, and leverage.
Generated: DETERMINISTIC_21925b5d9442fcb0
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate profit or loss for crypto derivatives trades.
 *
 * @param {number} entryPrice - The price at which the position was opened.
 * @param {number} exitPrice - The price at which the position was closed.
 * @param {number} leverage - The leverage applied to the trade (e.g., 10 for 10x leverage).
 * @param {boolean} isLong - Indicates whether the position is long (true) or short (false).
 * @param {number} positionSize - The size of the position in USD.
 *
 * @returns {object} - An object containing profitLoss (number) and direction (string).
 *                     'profit' if positive, 'loss' if negative, 'break-even' if zero.
 */
function calculateCryptoProfitLoss(entryPrice, exitPrice, leverage, isLong, positionSize) {
  // Input validation
  if (
    typeof entryPrice !== 'number' ||
    typeof exitPrice !== 'number' ||
    typeof leverage !== 'number' ||
    typeof positionSize !== 'number' ||
    typeof isLong !== 'boolean'
  ) {
    throw new Error('Invalid input types. Please ensure all parameters are of the correct type.');
  }

  if (entryPrice <= 0 || exitPrice <= 0 || leverage <= 0 || positionSize <= 0) {
    throw new Error('Parameters must be positive numbers greater than zero.');
  }

  // Calculate the percentage change in price
  const percentageChange = ((exitPrice - entryPrice) / entryPrice) * 100;

  // Adjust percentage change based on position type (long or short)
  const adjustedChange = isLong ? percentageChange : -percentageChange;

  // Calculate profit/loss with leverage applied
  const profitLoss = (adjustedChange / 100) * leverage * positionSize;

  // Determine the direction of the trade outcome
  let direction = 'break-even';
  if (profitLoss > 0) {
    direction = 'profit';
  } else if (profitLoss < 0) {
    direction = 'loss';
  }

  // Return the result as an object
  return {
    profitLoss: parseFloat(profitLoss.toFixed(2)), // Rounded to 2 decimal places
    direction: direction,
  };
}

// Example usage:
// const result = calculateCryptoProfitLoss(1000, 1200, 10, true, 500);
// console.log(result); // { profitLoss: 1000.00, direction: 'profit' }
```
