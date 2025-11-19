"""
Generated Code Metadata:
========================
Original URL: https://base-org.pages.dev
Prompt: Design a next-gen product on Base that utilizes Smart Wallet for instant wallet creation with passkeys, and describe its potential use cases.
Generated: DETERMINISTIC_840d75aaa9ff937c
Batch ID: 20250622_204650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.base.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('ethers');
const { Base } = require('@base-protocol/sdk');

// Define a class for the next-gen product
class NextGenProduct {
  /**
   * Initialize the product with a provider and a passkey
   * @param {ethers.providers.Provider} provider - The provider to use
   * @param {string} passkey - The passkey for the Smart Wallet
   */
  constructor(provider, passkey) {
    this.provider = provider;
    this.passkey = passkey;
    this.smartWallet = null;
  }

  /**
   * Create a new Smart Wallet instance
   * @async
   * @returns {Promise<void>}
   */
  async createSmartWallet() {
    try {
      // Initialize the Base protocol
      const base = new Base(this.provider);

      // Create a new Smart Wallet instance
      this.smartWallet = await base.createSmartWallet({
        passkey: this.passkey,
      });

      console.log('Smart Wallet created:', this.smartWallet.address);
    } catch (error) {
      console.error('Error creating Smart Wallet:', error);
      throw error;
    }
  }

  /**
   * Get the balance of the Smart Wallet
   * @async
   * @returns {Promise<string>} The balance of the Smart Wallet
   */
  async getBalance() {
    try {
      if (!this.smartWallet) {
        throw new Error('Smart Wallet not created');
      }

      // Get the balance of the Smart Wallet
      const balance = await this.smartWallet.getBalance();

      return balance.toString();
    } catch (error) {
      console.error('Error getting balance:', error);
      throw error;
    }
  }

  /**
   * Send a transaction from the Smart Wallet
   * @async
   * @param {string} to - The address to send to
   * @param {string} amount - The amount to send
   * @returns {Promise<string>} The transaction hash
   */
  async sendTransaction(to, amount) {
    try {
      if (!this.smartWallet) {
        throw new Error('Smart Wallet not created');
      }

      // Send a transaction from the Smart Wallet
      const tx = await this.smartWallet.sendTransaction({
        to,
        value: ethers.utils.parseEther(amount),
      });

      return tx.hash;
    } catch (error) {
      console.error('Error sending transaction:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  // Create a new provider
  const provider = new ethers.providers.JsonRpcProvider('https://mainnet.base.org');

  // Create a new instance of the next-gen product
  const product = new NextGenProduct(provider, 'my-passkey');

  // Create a new Smart Wallet instance
  await product.createSmartWallet();

  // Get the balance of the Smart Wallet
  const balance = await product.getBalance();
  console.log('Balance:', balance);

  // Send a transaction from the Smart Wallet
  const txHash = await product.sendTransaction('0x...', '1.0');
  console.log('Transaction hash:', txHash);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
