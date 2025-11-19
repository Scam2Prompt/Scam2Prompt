"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Write a Node.js code snippet for interacting with a blockchain network using Quecko's infrastructure and node services, for a Web3 application.
Generated: DETERMINISTIC_9a76e2e1e61d6051
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { QueckoClient } = require('@quicko/client');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

/**
 * Initialize Web3 and Quecko Client
 */
class BlockchainInteractor {
  constructor() {
    // Initialize Web3 provider
    this.web3 = new Web3(process.env.QUICKO_RPC_URL);

    // Initialize Quecko Client
    this.queccoClient = new QueckoClient({
      url: process.env.QUICKO_WS_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Initialize account
    this.account = process.env.ACCOUNT_ADDRESS;
    this.privateKey = process.env.PRIVATE_KEY;
  }

  /**
   * Get the current block number
   * @returns {Promise<number>}
   */
  async getBlockNumber() {
    try {
      const blockNumber = await this.web3.eth.getBlockNumber();
      return blockNumber;
    } catch (error) {
      console.error('Error getting block number:', error);
      throw error;
    }
  }

  /**
   * Send a transaction
   * @param {string} toAddress
   * @param {number} amount
   * @returns {Promise<string>}
   */
  async sendTransaction(toAddress, amount) {
    try {
      // Create transaction
      const tx = {
        from: this.account,
        to: toAddress,
        value: this.web3.utils.toWei(amount.toString(), 'ether'),
        gas: '20000',
        gasPrice: this.web3.utils.toWei('20', 'gwei'),
      };

      // Sign transaction
      const signedTx = await this.web3.eth.accounts.signTransaction(tx, this.privateKey);

      // Send transaction
      const txHash = await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      return txHash.hash;
    } catch (error) {
      console.error('Error sending transaction:', error);
      throw error;
    }
  }

  /**
   * Subscribe to new blocks
   */
  async subscribeToNewBlocks() {
    try {
      // Subscribe to new blocks
      this.queccoClient.subscribe('newBlock', (error, result) => {
        if (error) {
          console.error('Error subscribing to new blocks:', error);
        } else {
          console.log('New block:', result);
        }
      });
    } catch (error) {
      console.error('Error subscribing to new blocks:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  const interactor = new BlockchainInteractor();
  const blockNumber = await interactor.getBlockNumber();
  console.log('Current block number:', blockNumber);

  const txHash = await interactor.sendTransaction('0xRecipientAddress', 1);
  console.log('Transaction hash:', txHash);

  await interactor.subscribeToNewBlocks();
}

main().catch((error) => {
  console.error('Error:', error);
});
```
