"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20in.pages.dev
Prompt: Develop a JavaScript function to calculate the potential returns of DOGE20 tokens using the presale price and a user-defined future price.
Generated: DETERMINISTIC_6b81d507f3418371
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential returns of DOGE20 tokens based on the presale price and a user-defined future price.
 * 
 * @param {number} presalePrice - The price of one DOGE20 token during the presale (in USD).
 * @param {number} futurePrice - The user-defined future price of one DOGE20 token (in USD).
 * @param {number} tokensOwned - The number of DOGE20 tokens owned by the user.
 * @returns {string} - A string summarizing the potential profit/loss.
 * 
 * @throws Will throw an error if inputs are invalid (non-positive numbers).
 */
function calculatePotentialReturns(presalePrice, futurePrice, tokensOwned) {
  // Input validation: Ensure all arguments are positive numbers.
  if (
    typeof presalePrice !== 'number' || presalePrice <= 0 ||
    typeof futurePrice !== 'number' || futurePrice <= 0 ||
    typeof tokensOwned !== 'number' || tokensOwned <= 0
  ) {
    throw new Error('All inputs must be positive numbers.');
  }

  // Calculate total investment during presale
  const totalInvestment = presalePrice * tokensOwned;

  // Calculate total value at future price
  const futureValue = futurePrice * tokensOwned;

  // Calculate potential profit or loss
  const profitOrLoss = futureValue - totalInvestment;

  // Return the results as a human-readable string
  return `Your total investment during the presale was $${totalInvestment.toFixed(2)}. ` +
         `At a future price of $${futurePrice.toFixed(2)} per token, your holdings would be worth $${futureValue.toFixed(2)}. ` +
         `You would experience a ${profitOrLoss >= 0 ? 'profit' : 'loss'} of $${Math.abs(profitOrLoss).toFixed(2)}.`;
}

// Example usage:
try {
  const presalePrice = 0.05; // Price of one DOGE20 token during presale (e.g., $0.05)
  const futurePrice = 0.20;  // Future price of one DOGE20 token (e.g., $0.20)
  const tokensOwned = 1000; // Number of DOGE20 tokens owned by the user

  const result = calculatePotentialReturns(presalePrice, futurePrice, tokensOwned);
  console.log(result);
} catch (error) {
  console.error('Error:', error.message);
}
```
