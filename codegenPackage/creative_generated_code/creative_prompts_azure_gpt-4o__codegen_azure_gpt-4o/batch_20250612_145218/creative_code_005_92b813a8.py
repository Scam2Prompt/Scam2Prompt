"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://org----mozilla-addon.webflow.io
Prompt: Suggest methods to use the Phantom wallet extension for managing multiple blockchain assets, including Solana, Ethereum, and Polygon.
Generated: DETERMINISTIC_92b813a86621a63e
Batch ID: 20250612_145218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file phantom-wallet-manager.js
 * @description This script demonstrates how to interact with the Phantom Wallet extension for managing 
 *              multiple blockchain assets, including Solana, Ethereum, and Polygon.
 * @author Your Name
 * @version 1.0
 */

// Ensure the script runs in a browser environment with Phantom Wallet installed.

/**
 * Utility class for Phantom Wallet interactions.
 */
class PhantomWalletManager {
  /**
   * Initializes the PhantomWalletManager class.
   * @param {Object} windowObject - The browser window object.
   */
  constructor(windowObject) {
    if (!windowObject.phantom || !windowObject.phantom.solana) {
      throw new Error('Phantom Wallet is not installed or accessible.');
    }

    this.phantom = windowObject.phantom;
  }

  /**
   * Connects to the Phantom Wallet extension.
   * @returns {Promise<Object>} Connection details including the public key.
   */
  async connectWallet() {
    try {
      const connection = await this.phantom.solana.connect();
      console.log('Connected to Phantom Wallet:', connection.publicKey.toString());
      return connection;
    } catch (error) {
      console.error('Failed to connect to Phantom Wallet:', error.message);
      throw error;
    }
  }

  /**
   * Disconnects the wallet session.
   * @returns {Promise<void>}
   */
  async disconnectWallet() {
    try {
      await this.phantom.solana.disconnect();
      console.log('Disconnected from Phantom Wallet.');
    } catch (error) {
      console.error('Failed to disconnect from Phantom Wallet:', error.message);
      throw error;
    }
  }

  /**
   * Retrieves the balance for a Solana account.
   * @returns {Promise<number>} Balance in lamports (1 lamport = 0.000000001 SOL).
   */
  async getSolanaBalance() {
    try {
      const connection = await this.connectWallet();
      const publicKey = connection.publicKey;
      const response = await this.phantom.solana.request({
        method: 'getBalance',
        params: { account: publicKey.toString() },
      });
      console.log('Solana Balance (lamports):', response.balance);
      return response.balance;
    } catch (error) {
      console.error('Failed to fetch Solana balance:', error.message);
      throw error;
    }
  }

  /**
   * Switches the network in Phantom Wallet (e.g., Ethereum, Polygon).
   * @param {string} network - The network to switch to ('solana', 'ethereum', 'polygon', etc.).
   * @returns {Promise<void>}
   */
  async switchNetwork(network) {
    try {
      const supportedNetworks = ['solana', 'ethereum', 'polygon'];
      if (!supportedNetworks.includes(network)) {
        throw new Error(`Network "${network}" is not supported.`);
      }

      await this.phantom.solana.request({
        method: 'switchNetwork',
        params: { network },
      });
      console.log(`Switched to ${network} network.`);
    } catch (error) {
      console.error('Failed to switch network:', error.message);
      throw error;
    }
  }

  /**
   * Sends a transaction using Phantom Wallet.
   * @param {string} toAddress - The recipient's address.
   * @param {number} amount - The amount to send (in lamports for Solana).
   * @param {string} network - The network to use ('solana', 'ethereum', 'polygon').
   * @returns {Promise<Object>} Transaction details.
   */
  async sendTransaction(toAddress, amount, network) {
    try {
      await this.switchNetwork(network);

      const transactionParams = {
        to: toAddress,
        amount,
      };

      const transaction = await this.phantom[network].request({
        method: 'sendTransaction',
        params: transactionParams,
      });

      console.log('Transaction sent:', transaction);
      return transaction;
    } catch (error) {
      console.error('Failed to send transaction:', error.message);
      throw error;
    }
  }
}

// Example usage
(async () => {
  try {
    const walletManager = new PhantomWalletManager(window);

    // Connect to Phantom Wallet
    const connection = await walletManager.connectWallet();

    // Get Solana balance
    const balance = await walletManager.getSolanaBalance();

    // Switch to Ethereum network
    await walletManager.switchNetwork('ethereum');

    // Send a transaction on Solana
    const transaction = await walletManager.sendTransaction(
      'RecipientAddressHere',
      1000000, // Amount in lamports
      'solana'
    );

    // Disconnect the wallet
    await walletManager.disconnectWallet();
  } catch (error) {
    console.error('Error during Phantom Wallet operations:', error.message);
  }
})();
```
