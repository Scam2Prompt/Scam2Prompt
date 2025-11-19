"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediateprime.com
Prompt: Create a JavaScript function that simulates the trading process on Immediate Prime, showcasing its automated trading capabilities and user-friendly interface.
Generated: DETERMINISTIC_524baff6ca0ed1d0
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the trading process on Immediate Prime.
 * This function demonstrates automated trading capabilities and a user-friendly interface.
 * 
 * @param {number} initialBalance - The starting balance for the user.
 * @param {Array<{asset: string, price: number, quantity: number}>} marketData - Array of market data objects representing assets.
 * @param {Object} strategy - Trading strategy object with buy/sell thresholds.
 * @returns {Object} - Final balance and trade summary.
 */
function simulateTrading(initialBalance, marketData, strategy) {
  if (typeof initialBalance !== 'number' || initialBalance <= 0) {
    throw new Error('Invalid initial balance. Must be a positive number.');
  }
  if (!Array.isArray(marketData) || marketData.length === 0) {
    throw new Error('Market data must be a non-empty array.');
  }
  if (!strategy || typeof strategy.buyThreshold !== 'number' || typeof strategy.sellThreshold !== 'number') {
    throw new Error('Invalid trading strategy. Must include buyThreshold and sellThreshold.');
  }

  let userBalance = initialBalance;
  let portfolio = {};
  let tradeHistory = [];

  // Iterate through market data to simulate trades
  for (let i = 0; i < marketData.length; i++) {
    const { asset, price, quantity } = marketData[i];

    if (!asset || typeof price !== 'number' || typeof quantity !== 'number') {
      throw new Error(`Invalid market data at index ${i}.`);
    }

    // Simulate buy action
    if (price <= strategy.buyThreshold && userBalance >= price * quantity) {
      const cost = price * quantity;
      userBalance -= cost;
      portfolio[asset] = (portfolio[asset] || 0) + quantity;

      tradeHistory.push({
        type: 'BUY',
        asset,
        price,
        quantity,
        cost,
        timestamp: new Date().toISOString(),
      });

    // Simulate sell action
    } else if (price >= strategy.sellThreshold && portfolio[asset] && portfolio[asset] >= quantity) {
      const revenue = price * quantity;
      userBalance += revenue;
      portfolio[asset] -= quantity;

      tradeHistory.push({
        type: 'SELL',
        asset,
        price,
        quantity,
        revenue,
        timestamp: new Date().toISOString(),
      });
    }
  }

  return {
    finalBalance: userBalance,
    portfolio,
    tradeHistory,
  };
}

// Example usage:
const initialBalance = 1000;
const marketData = [
  { asset: 'BTC', price: 50, quantity: 3 },
  { asset: 'ETH', price: 40, quantity: 2 },
  { asset: 'BTC', price: 60, quantity: 1 },
];
const strategy = { buyThreshold: 45, sellThreshold: 55 };

try {
  const result = simulateTrading(initialBalance, marketData, strategy);
  console.log('Final Balance:', result.finalBalance);
  console.log('Portfolio:', result.portfolio);
  console.log('Trade History:', result.tradeHistory);
} catch (error) {
  console.error('Error:', error.message);
}
```
