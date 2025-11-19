"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Provide a code example for implementing the Moxie Bonding Curves in a decentralized application on Farcaster.
Generated: DETERMINISTIC_e8d7625e1748df3e
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// MoxieBondingCurve.js

/**
 * Moxie Bonding Curve implementation for Farcaster decentralized application.
 */

class MoxieBondingCurve {
  /**
   * Constructor for MoxieBondingCurve.
   * @param {object} params - Curve parameters.
   * @param {number} params.initialSupply - Initial token supply.
   * @param {number} params.initialPrice - Initial token price.
   * @param {number} params.curveSlope - Slope of the bonding curve.
   */
  constructor(params) {
    this.initialSupply = params.initialSupply;
    this.initialPrice = params.initialPrice;
    this.curveSlope = params.curveSlope;
    this.currentSupply = params.initialSupply;
    this.currentPrice = params.initialPrice;
  }

  /**
   * Calculate the new price based on the bonding curve.
   * @param {number} amount - Amount of tokens to buy or sell.
   * @param {string} direction - Direction of the transaction (buy or sell).
   * @returns {number} New price after the transaction.
   */
  calculatePrice(amount, direction) {
    try {
      if (direction !== 'buy' && direction !== 'sell') {
        throw new Error('Invalid direction. Must be "buy" or "sell".');
      }

      let newSupply;
      if (direction === 'buy') {
        newSupply = this.currentSupply + amount;
      } else {
        if (amount > this.currentSupply) {
          throw new Error('Insufficient tokens for sale.');
        }
        newSupply = this.currentSupply - amount;
      }

      // Bonding curve formula: P = P0 * e^(slope * (S - S0))
      const newPrice = this.initialPrice * Math.exp(this.curveSlope * (newSupply - this.initialSupply));
      return newPrice;
    } catch (error) {
      console.error('Error calculating price:', error);
      throw error;
    }
  }

  /**
   * Execute a buy or sell transaction on the bonding curve.
   * @param {number} amount - Amount of tokens to buy or sell.
   * @param {string} direction - Direction of the transaction (buy or sell).
   * @returns {object} Transaction result with new price and supply.
   */
  executeTransaction(amount, direction) {
    try {
      const newPrice = this.calculatePrice(amount, direction);
      if (direction === 'buy') {
        this.currentSupply += amount;
      } else {
        this.currentSupply -= amount;
      }
      this.currentPrice = newPrice;
      return { newPrice, newSupply: this.currentSupply };
    } catch (error) {
      console.error('Error executing transaction:', error);
      throw error;
    }
  }
}

// Example usage:
const curveParams = {
  initialSupply: 1000,
  initialPrice: 1.0,
  curveSlope: 0.001,
};

const moxieCurve = new MoxieBondingCurve(curveParams);

const buyAmount = 100;
const buyResult = moxieCurve.executeTransaction(buyAmount, 'buy');
console.log(`Buy ${buyAmount} tokens:`, buyResult);

const sellAmount = 50;
const sellResult = moxieCurve.executeTransaction(sellAmount, 'sell');
console.log(`Sell ${sellAmount} tokens:`, sellResult);
```
