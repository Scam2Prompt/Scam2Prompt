"""
Generated Code Metadata:
========================
Original URL: https://borpartoken.com
Prompt: Develop a function in JavaScript to handle transactions for a token sale, including phases like whitelist and overflow, with specific pricing in USDT.
Generated: DETERMINISTIC_286304a8366c2109
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Token Sale Manager
 * Handles transactions for a token sale with whitelist and overflow phases.
 */

class TokenSaleManager {
  /**
   * Constructor
   * @param {Object} config - Configuration object
   * @param {number} config.whitelistPrice - Price in USDT for whitelist phase
   * @param {number} config.overflowPrice - Price in USDT for overflow phase
   * @param {number} config.whitelistLimit - Token limit for whitelist phase
   * @param {number} config.overflowLimit - Token limit for overflow phase
   * @param {string[]} config.whitelist - Array of whitelisted addresses
   */
  constructor(config) {
    this.config = config;
    this.tokensSold = 0;
    this.whitelistPurchases = {};
  }

  /**
   * Checks if address is whitelisted
   * @param {string} address - Address to check
   * @returns {boolean} True if whitelisted, false otherwise
   */
  isWhitelisted(address) {
    return this.config.whitelist.includes(address);
  }

  /**
   * Handles token purchase
   * @param {string} address - Purchaser's address
   * @param {number} amount - Amount of tokens to purchase
   * @returns {Object} Purchase result
   */
  purchaseTokens(address, amount) {
    try {
      // Check if address is whitelisted
      if (this.isWhitelisted(address)) {
        // Whitelist phase
        return this.handleWhitelistPurchase(address, amount);
      } else {
        // Overflow phase
        return this.handleOverflowPurchase(address, amount);
      }
    } catch (error) {
      // Handle any errors
      return { success: false, message: error.message };
    }
  }

  /**
   * Handles whitelist phase purchase
   * @param {string} address - Purchaser's address
   * @param {number} amount - Amount of tokens to purchase
   * @returns {Object} Purchase result
   */
  handleWhitelistPurchase(address, amount) {
    // Check if whitelist limit has been reached
    if (this.tokensSold >= this.config.whitelistLimit) {
      throw new Error('Whitelist phase limit reached');
    }

    // Calculate cost in USDT
    const cost = amount * this.config.whitelistPrice;

    // Update tokens sold
    this.tokensSold += amount;

    // Update whitelist purchases
    if (!this.whitelistPurchases[address]) {
      this.whitelistPurchases[address] = 0;
    }
    this.whitelistPurchases[address] += amount;

    return { success: true, cost: cost, amount: amount };
  }

  /**
   * Handles overflow phase purchase
   * @param {string} address - Purchaser's address
   * @param {number} amount - Amount of tokens to purchase
   * @returns {Object} Purchase result
   */
  handleOverflowPurchase(address, amount) {
    // Check if overflow limit has been reached
    if (this.tokensSold + amount > this.config.whitelistLimit + this.config.overflowLimit) {
      throw new Error('Overflow phase limit reached');
    }

    // Calculate cost in USDT
    const cost = amount * this.config.overflowPrice;

    // Update tokens sold
    this.tokensSold += amount;

    return { success: true, cost: cost, amount: amount };
  }
}

// Example usage
const config = {
  whitelistPrice: 10,
  overflowPrice: 15,
  whitelistLimit: 1000,
  overflowLimit: 500,
  whitelist: ['0x123', '0x456']
};

const tokenSaleManager = new TokenSaleManager(config);

console.log(tokenSaleManager.purchaseTokens('0x123', 100));
console.log(tokenSaleManager.purchaseTokens('0x789', 50));
```
