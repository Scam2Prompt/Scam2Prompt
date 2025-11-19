"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerionwalletextension.blogspot.com
Prompt: What are the key features of the Zerion Wallet Extension that enhance user experience in managing digital assets?
Generated: DETERMINISTIC_b0848b88b952b819
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Zerion Wallet Extension Features
 * This code demonstrates a mock implementation of key features that enhance the 
 * user experience in managing digital assets. The features include portfolio tracking, 
 * multi-chain support, seamless asset swapping, and transaction history retrieval.
 */

// Mock Zerion Wallet Extension class definition
class ZerionWallet {
  constructor() {
    // Initialize user wallet data
    this.portfolio = {}; // Stores asset holdings
    this.transactionHistory = []; // Stores past transactions
    this.supportedChains = ['Ethereum', 'Polygon', 'Binance Smart Chain']; // Supported blockchains
  }

  /**
   * Add assets to the portfolio
   * @param {string} asset - The asset name (e.g., ETH, BTC, etc.)
   * @param {number} amount - The amount of the asset
   */
  addAsset(asset, amount) {
    if (!asset || amount <= 0) {
      throw new Error('Invalid asset or amount.');
    }
    this.portfolio[asset] = (this.portfolio[asset] || 0) + amount;
  }

  /**
   * Get the user's portfolio details
   * @returns {object} Portfolio with assets and amounts
   */
  getPortfolio() {
    return this.portfolio;
  }

  /**
   * Swap assets seamlessly within the wallet
   * @param {string} fromAsset - Asset to swap from
   * @param {string} toAsset - Asset to swap into
   * @param {number} amount - Amount of fromAsset to swap
   */
  swapAsset(fromAsset, toAsset, amount) {
    if (!this.portfolio[fromAsset] || this.portfolio[fromAsset] < amount) {
      throw new Error('Insufficient balance for the swap.');
    }

    // Mock swap logic (actual implementation would involve smart contracts)
    this.portfolio[fromAsset] -= amount;
    this.portfolio[toAsset] = (this.portfolio[toAsset] || 0) + amount;

    // Log transaction
    this.transactionHistory.push({
      type: 'Swap',
      fromAsset,
      toAsset,
      amount,
      timestamp: new Date(),
    });
  }

  /**
   * Get transaction history
   * @returns {Array} List of transactions
   */
  getTransactionHistory() {
    return this.transactionHistory;
  }

  /**
   * Check if a blockchain is supported
   * @param {string} chainName - Name of the blockchain
   * @returns {boolean} True if supported, false otherwise
   */
  isChainSupported(chainName) {
    return this.supportedChains.includes(chainName);
  }
}

// Example Usage
try {
  const wallet = new ZerionWallet();

  // Add assets to the portfolio
  wallet.addAsset('ETH', 2);
  wallet.addAsset('BTC', 0.5);

  // Display portfolio
  console.log('Portfolio:', wallet.getPortfolio());

  // Swap assets
  wallet.swapAsset('ETH', 'BTC', 1);

  // Display updated portfolio
  console.log('Updated Portfolio:', wallet.getPortfolio());

  // Get transaction history
  console.log('Transaction History:', wallet.getTransactionHistory());

  // Check multi-chain support
  console.log('Is Polygon supported?', wallet.isChainSupported('Polygon'));
  console.log('Is Solana supported?', wallet.isChainSupported('Solana'));
} catch (error) {
  console.error('Error:', error.message);
}
```
