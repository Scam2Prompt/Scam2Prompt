"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstmemes.com
Prompt: Create a function in JavaScript that simulates a meme-based stock portfolio inspired by the Wall Street Memes community, incorporating stocks like Tesla and Bitcoin.
Generated: DETERMINISTIC_7ccb26d8b7b7aa9f
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates a meme-based stock portfolio inspired by the Wall Street Memes community.
 * Allows users to see their portfolio value based on stock prices.
 */

// Define the stocks and their initial prices (in USD)
const memeStocks = {
  Tesla: 250,      // Tesla stock price
  Bitcoin: 30000,  // Bitcoin price
  GameStop: 18,    // GameStop stock price
  AMC: 8,          // AMC stock price
};

/**
 * Calculates the total value of the portfolio based on the number of shares owned.
 * @param {Object} portfolio - An object representing the portfolio.
 * Example: { Tesla: 10, Bitcoin: 0.5, GameStop: 15 }
 * @returns {number} - Total portfolio value in USD.
 */
function calculatePortfolioValue(portfolio) {
  try {
    if (typeof portfolio !== 'object' || Array.isArray(portfolio)) {
      throw new Error("Portfolio must be a valid object with stock names as keys and quantities as values.");
    }

    let totalValue = 0;

    for (const stock in portfolio) {
      if (!memeStocks.hasOwnProperty(stock)) {
        throw new Error(`Invalid stock name: ${stock}. Supported stocks: ${Object.keys(memeStocks).join(', ')}`);
      }

      const quantity = portfolio[stock];
      const price = memeStocks[stock];

      if (typeof quantity !== 'number' || quantity < 0) {
        throw new Error(`Invalid quantity for stock ${stock}. Quantity must be a non-negative number.`);
      }

      totalValue += quantity * price;
    }

    return totalValue;
  } catch (error) {
    console.error("Error calculating portfolio value:", error.message);
    return 0; // Return 0 if there's an error
  }
}

// Example usage
const myPortfolio = {
  Tesla: 10,      // 10 shares of Tesla
  Bitcoin: 0.5,   // 0.5 units of Bitcoin
  GameStop: 20,   // 20 shares of GameStop
};

const portfolioValue = calculatePortfolioValue(myPortfolio);
console.log(`Your meme stock portfolio value is: $${portfolioValue.toFixed(2)}`);
```
