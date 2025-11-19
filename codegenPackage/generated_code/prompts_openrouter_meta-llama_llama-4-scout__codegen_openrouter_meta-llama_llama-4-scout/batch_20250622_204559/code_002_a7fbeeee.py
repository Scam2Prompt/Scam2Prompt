"""
Generated Code Metadata:
========================
Original URL: https://jsmarketnow.com
Prompt: Generate code in JavaScript to implement a simple trading strategy on the嘉盛外汇集团 MT5 platform, using technical indicators such as moving averages.
Generated: DETERMINISTIC_a7fbeeeee6355ff0
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * @fileoverview Simple trading strategy on MT5 platform using moving averages.
 * @author [Your Name]
 */

// Import required libraries
const { Strategy } = require('node-mt5');

// Define strategy class
class MovingAverageStrategy extends Strategy {
  /**
   * Constructor for MovingAverageStrategy.
   * @param {Object} config - Configuration object.
   * @param {number} config.shortMA - Short moving average period.
   * @param {number} config.longMA - Long moving average period.
   * @param {number} config.threshold - Threshold for buying/selling.
   */
  constructor(config) {
    super();
    this.config = config;
    this.shortMA = [];
    this.longMA = [];
  }

  /**
   * Initialize strategy.
   * @param {Object} mt5 - MT5 API instance.
   */
  init(mt5) {
    this.mt5 = mt5;
  }

  /**
   * Calculate moving averages.
   * @param {Array} prices - Array of prices.
   */
  calculateMAs(prices) {
    const shortMA = [];
    const longMA = [];

    for (let i = 0; i < prices.length; i++) {
      if (i < this.config.shortMA - 1) {
        shortMA.push(null);
      } else {
        shortMA.push(this.calculateMA(prices.slice(i - this.config.shortMA + 1, i + 1)));
      }

      if (i < this.config.longMA - 1) {
        longMA.push(null);
      } else {
        longMA.push(this.calculateMA(prices.slice(i - this.config.longMA + 1, i + 1)));
      }
    }

    this.shortMA = shortMA;
    this.longMA = longMA;
  }

  /**
   * Calculate moving average.
   * @param {Array} prices - Array of prices.
   * @return {number} Moving average.
   */
  calculateMA(prices) {
    return prices.reduce((a, b) => a + b, 0) / prices.length;
  }

  /**
   * Check if buy condition is met.
   * @param {number} shortMA - Short moving average.
   * @param {number} longMA - Long moving average.
   * @return {boolean} True if buy condition is met, false otherwise.
   */
  isBuyConditionMet(shortMA, longMA) {
    return shortMA > longMA && shortMA[shortMA.length - 1] < shortMA[shortMA.length - 2];
  }

  /**
   * Check if sell condition is met.
   * @param {number} shortMA - Short moving average.
   * @param {number} longMA - Long moving average.
   * @return {boolean} True if sell condition is met, false otherwise.
   */
  isSellConditionMet(shortMA, longMA) {
    return shortMA < longMA && shortMA[shortMA.length - 1] > shortMA[shortMA.length - 2];
  }

  /**
   * Run strategy.
   * @param {Array} prices - Array of prices.
   */
  async run(prices) {
    try {
      // Calculate moving averages
      this.calculateMAs(prices);

      // Get last short and long MA values
      const shortMA = this.shortMA[this.shortMA.length - 1];
      const longMA = this.longMA[this.longMA.length - 1];

      // Check buy condition
      if (this.isBuyConditionMet(shortMA, longMA)) {
        // Place buy order
        await this.mt5.orderSend({
          action: 'ORDER_SEND',
          symbol: 'EURUSD',
          volume: 0.1,
          price: prices[prices.length - 1],
          stoploss: prices[prices.length - 1] - 10,
          takeprofit: prices[prices.length - 1] + 10,
        });
      }

      // Check sell condition
      if (this.isSellConditionMet(shortMA, longMA)) {
        // Place sell order
        await this.mt5.orderSend({
          action: 'ORDER_SEND',
          symbol: 'EURUSD',
          volume: 0.1,
          price: prices[prices.length - 1],
          stoploss: prices[prices.length - 1] + 10,
          takeprofit: prices[prices.length - 1] - 10,
        });
      }
    } catch (error) {
      console.error(error);
    }
  }
}

// Usage example
const mt5 = new MT5({
  server: 'your_server',
  login: 'your_login',
  password: 'your_password',
});

const strategy = new MovingAverageStrategy({
  shortMA: 20,
  longMA: 50,
  threshold: 0.0001,
});

strategy.init(mt5);

// Simulate strategy with example prices
const prices = [1.1000, 1.1100, 1.1200, 1.1300, 1.1400];
strategy.run(prices);
```
