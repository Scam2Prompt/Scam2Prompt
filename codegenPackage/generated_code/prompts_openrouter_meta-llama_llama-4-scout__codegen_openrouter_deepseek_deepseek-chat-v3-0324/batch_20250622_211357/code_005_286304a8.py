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
 * TokenSaleHandler - Handles token sale transactions including whitelist and overflow phases.
 */
class TokenSaleHandler {
  /**
   * @param {Object} config - Configuration object for the token sale
   * @param {number} config.whitelistPrice - Price per token in USDT during whitelist phase
   * @param {number} config.publicPrice - Price per token in USDT during public sale
   * @param {number} config.maxWhitelistPurchase - Maximum tokens allowed per whitelisted address
   * @param {number} config.maxPublicPurchase - Maximum tokens allowed per public address
   * @param {Set} whitelist - Set of whitelisted addresses
   */
  constructor(config, whitelist = new Set()) {
    if (!config || typeof config !== 'object') {
      throw new Error('Configuration must be provided');
    }

    this.whitelistPrice = config.whitelistPrice;
    this.publicPrice = config.publicPrice;
    this.maxWhitelistPurchase = config.maxWhitelistPurchase;
    this.maxPublicPurchase = config.maxPublicPurchase;
    this.whitelist = whitelist;
    this.salePhase = 'inactive'; // 'inactive', 'whitelist', 'public', 'overflow'
    this.totalSold = 0;
    this.purchases = new Map(); // address => { totalTokens, totalPaid }
  }

  /**
   * Sets the current sale phase
   * @param {string} phase - The sale phase to set
   */
  setSalePhase(phase) {
    const validPhases = ['inactive', 'whitelist', 'public', 'overflow'];
    if (!validPhases.includes(phase)) {
      throw new Error(`Invalid sale phase. Must be one of: ${validPhases.join(', ')}`);
    }
    this.salePhase = phase;
  }

  /**
   * Adds addresses to the whitelist
   * @param {Array<string>} addresses - Array of addresses to add
   */
  addToWhitelist(addresses) {
    if (!Array.isArray(addresses)) {
      throw new Error('Addresses must be provided as an array');
    }
    addresses.forEach(address => this.whitelist.add(address));
  }

  /**
   * Processes a token purchase
   * @param {string} buyerAddress - The buyer's address
   * @param {number} usdtAmount - Amount of USDT sent for purchase
   * @returns {Object} - Result of the purchase { success, tokensPurchased, change, message }
   */
  purchaseTokens(buyerAddress, usdtAmount) {
    try {
      if (this.salePhase === 'inactive') {
        return { success: false, tokensPurchased: 0, change: usdtAmount, message: 'Sale is not active' };
      }

      if (typeof usdtAmount !== 'number' || usdtAmount <= 0) {
        return { success: false, tokensPurchased: 0, change: usdtAmount, message: 'Invalid USDT amount' };
      }

      const isWhitelisted = this.whitelist.has(buyerAddress);
      let pricePerToken, maxPurchase;

      if (this.salePhase === 'whitelist') {
        if (!isWhitelisted) {
          return { success: false, tokensPurchased: 0, change: usdtAmount, message: 'Address not whitelisted' };
        }
        pricePerToken = this.whitelistPrice;
        maxPurchase = this.maxWhitelistPurchase;
      } else {
        pricePerToken = this.publicPrice;
        maxPurchase = this.maxPublicPurchase;
      }

      const existingPurchase = this.purchases.get(buyerAddress) || { totalTokens: 0, totalPaid: 0 };
      const maxAdditionalTokens = maxPurchase - existingPurchase.totalTokens;

      if (maxAdditionalTokens <= 0) {
        return { success: false, tokensPurchased: 0, change: usdtAmount, message: 'Purchase limit reached' };
      }

      const potentialTokens = Math.floor(usdtAmount / pricePerToken);
      const tokensToPurchase = Math.min(potentialTokens, maxAdditionalTokens);
      const totalCost = tokensToPurchase * pricePerToken;
      const change = usdtAmount - totalCost;

      if (tokensToPurchase <= 0) {
        return { success: false, tokensPurchased: 0, change: usdtAmount, message: 'Insufficient funds for at least one token' };
      }

      this.purchases.set(buyerAddress, {
        totalTokens: existingPurchase.totalTokens + tokensToPurchase,
        totalPaid: existingPurchase.totalPaid + totalCost
      });

      this.totalSold += tokensToPurchase;

      return {
        success: true,
        tokensPurchased: tokensToPurchase,
        change,
        message: 'Purchase successful'
      };
    } catch (error) {
      console.error('Error processing purchase:', error);
      return { success: false, tokensPurchased: 0, change: usdtAmount, message: 'Transaction failed' };
    }
  }

  /**
   * Handles overflow distribution
   * @param {number} totalTokens - Total tokens available for overflow
   * @param {Array<string>} participants - Array of participant addresses
   * @returns {Object} - Result of overflow distribution { success, allocations, message }
   */
  handleOverflow(totalTokens, participants) {
    try {
      if (this.salePhase !== 'overflow') {
        return { success: false, allocations: null, message: 'Not in overflow phase' };
      }

      if (!Array.isArray(participants) || participants.length === 0) {
        return { success: false, allocations: null, message: 'Invalid participants list' };
      }

      if (typeof totalTokens !== 'number' || totalTokens <= 0) {
        return { success: false, allocations: null, message: 'Invalid token amount' };
      }

      const totalContributions = participants.reduce((sum, addr) => {
        const purchase = this.purchases.get(addr);
        return sum + (purchase ? purchase.totalPaid : 0);
      }, 0);

      if (totalContributions <= 0) {
        return { success: false, allocations: null, message: 'No contributions found' };
      }

      const allocations = {};
      participants.forEach(addr => {
        const purchase = this.purchases.get(addr);
        if (purchase) {
          const share = purchase.totalPaid / totalContributions;
          allocations[addr] = Math.floor(share * totalTokens);
        }
      });

      return {
        success: true,
        allocations,
        message: 'Overflow distribution completed'
      };
    } catch (error) {
      console.error('Error handling overflow:', error);
      return { success: false, allocations: null, message: 'Overflow distribution failed' };
    }
  }
}

module.exports = TokenSaleHandler;
```
