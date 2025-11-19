"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.com
Prompt: Generate an example of integrating multiple features from Reown's toolkit to maximize efficiency in an onchain payment application.
Generated: DETERMINISTIC_94e92230181254b5
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules from Reown's toolkit
import { 
  Address, 
  Amount, 
  AssetId, 
  BlockHeight, 
  MerkleRoot, 
  OutPoint, 
  Transaction, 
  TxBuilder, 
  Wallet 
} from '@reown/toolkit';

// Define a class for the onchain payment application
class OnchainPaymentApp {
  /**
   * Initialize the onchain payment application
   * @param {Wallet} wallet - The wallet instance for the application
   */
  constructor(wallet) {
    this.wallet = wallet;
  }

  /**
   * Create a new transaction for payment
   * @param {Address} recipientAddress - The recipient's address
   * @param {Amount} amount - The amount to be sent
   * @param {AssetId} assetId - The asset ID for the transaction
   * @returns {Transaction} The created transaction
   */
  async createTransaction(recipientAddress, amount, assetId) {
    try {
      // Get the current block height
      const blockHeight = await this.wallet.getBlockHeight();

      // Create a new transaction builder
      const txBuilder = new TxBuilder();

      // Add the recipient output to the transaction
      txBuilder.addOutput(recipientAddress, amount);

      // Add a change output for the remaining balance
      const changeAddress = await this.wallet.getChangeAddress();
      txBuilder.addChangeOutput(changeAddress);

      // Set the transaction's lock height
      txBuilder.setLockHeight(blockHeight + 10);

      // Build the transaction
      const transaction = txBuilder.build();

      // Sign the transaction
      await this.wallet.signTransaction(transaction);

      return transaction;
    } catch (error) {
      throw new Error(`Failed to create transaction: ${error.message}`);
    }
  }

  /**
   * Broadcast the transaction to the network
   * @param {Transaction} transaction - The transaction to be broadcast
   * @returns {string} The transaction ID
   */
  async broadcastTransaction(transaction) {
    try {
      // Broadcast the transaction to the network
      const txid = await this.wallet.broadcastTransaction(transaction);

      return txid;
    } catch (error) {
      throw new Error(`Failed to broadcast transaction: ${error.message}`);
    }
  }

  /**
   * Get the transaction history for the wallet
   * @returns {Array} The transaction history
   */
  async getTransactionHistory() {
    try {
      // Get the transaction history from the wallet
      const history = await this.wallet.getTransactionHistory();

      return history;
    } catch (error) {
      throw new Error(`Failed to get transaction history: ${error.message}`);
    }
  }
}

// Example usage
async function main() {
  // Create a new wallet instance
  const wallet = new Wallet({
    network: 'testnet',
    mnemonic: 'your_mnemonic_phrase',
  });

  // Create a new onchain payment application instance
  const app = new OnchainPaymentApp(wallet);

  // Create a new transaction
  const recipientAddress = new Address('testnet', ' recipient_address');
  const amount = new Amount(1000);
  const assetId = new AssetId(' asset_id');
  const transaction = await app.createTransaction(recipientAddress, amount, assetId);

  // Broadcast the transaction
  const txid = await app.broadcastTransaction(transaction);
  console.log(`Transaction ID: ${txid}`);

  // Get the transaction history
  const history = await app.getTransactionHistory();
  console.log(`Transaction History: ${JSON.stringify(history)}`);
}

main().catch((error) => {
  console.error(error);
});
```
