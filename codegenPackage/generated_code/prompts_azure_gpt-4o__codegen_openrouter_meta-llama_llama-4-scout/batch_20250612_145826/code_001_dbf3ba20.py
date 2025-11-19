"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Generate code to create a presale widget for a cryptocurrency like $FROP, allowing users to connect their wallets, select payment methods across multiple blockchains, and purchase tokens.
Generated: DETERMINISTIC_dbf3ba20f37146c1
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import axios from 'axios';

// Define constants
const SUPPORTED_BLOCKCHAINS = ['ethereum', 'binance-smart-chain', 'polygon'];
const SUPPORTED_PAYMENT_METHODS = ['metamask', 'walletconnect', 'coinbase-wallet'];

// Define the PresaleWidget class
class PresaleWidget {
  /**
   * Initialize the presale widget
   * @param {string} contractAddress - The address of the presale contract
   * @param {string} tokenAddress - The address of the token being sold
   */
  constructor(contractAddress, tokenAddress) {
    this.contractAddress = contractAddress;
    this.tokenAddress = tokenAddress;
    this.web3 = new Web3(window.ethereum);
    this.provider = new ethers.providers.Web3Provider(window.ethereum);
    this.signer = this.provider.getSigner();
  }

  /**
   * Connect the user's wallet
   * @returns {Promise<string>} The user's wallet address
   */
  async connectWallet() {
    try {
      // Check if the user's wallet is connected
      if (!window.ethereum) {
        throw new Error('No wallet detected');
      }

      // Request access to the user's wallet
      await window.ethereum.request({ method: 'eth_accounts' });

      // Get the user's wallet address
      const accounts = await this.web3.eth.getAccounts();
      return accounts[0];
    } catch (error) {
      console.error('Error connecting wallet:', error);
      throw error;
    }
  }

  /**
   * Get the supported payment methods
   * @returns {string[]} The supported payment methods
   */
  getSupportedPaymentMethods() {
    return SUPPORTED_PAYMENT_METHODS;
  }

  /**
   * Get the supported blockchains
   * @returns {string[]} The supported blockchains
   */
  getSupportedBlockchains() {
    return SUPPORTED_BLOCKCHAINS;
  }

  /**
   * Purchase tokens
   * @param {string} paymentMethod - The payment method to use
   * @param {string} blockchain - The blockchain to use
   * @param {number} amount - The amount of tokens to purchase
   * @returns {Promise<string>} The transaction hash
   */
  async purchaseTokens(paymentMethod, blockchain, amount) {
    try {
      // Validate the payment method and blockchain
      if (!SUPPORTED_PAYMENT_METHODS.includes(paymentMethod)) {
        throw new Error(`Unsupported payment method: ${paymentMethod}`);
      }

      if (!SUPPORTED_BLOCKCHAINS.includes(blockchain)) {
        throw new Error(`Unsupported blockchain: ${blockchain}`);
      }

      // Get the user's wallet address
      const walletAddress = await this.connectWallet();

      // Get the presale contract
      const contract = new ethers.Contract(this.contractAddress, [
        {
          inputs: [
            { internalType: 'address', name: 'wallet', type: 'address' },
            { internalType: 'uint256', name: 'amount', type: 'uint256' },
          ],
          name: 'purchaseTokens',
          outputs: [],
          stateMutability: 'payable',
          type: 'function',
        },
      ], this.signer);

      // Purchase tokens
      const transaction = await contract.purchaseTokens(walletAddress, amount, {
        value: ethers.utils.parseEther(amount.toString()),
      });

      // Wait for the transaction to confirm
      await transaction.wait();

      return transaction.hash;
    } catch (error) {
      console.error('Error purchasing tokens:', error);
      throw error;
    }
  }
}

// Example usage
const presaleWidget = new PresaleWidget('0x...', '0x...');

// Connect the user's wallet
presaleWidget.connectWallet().then((walletAddress) => {
  console.log('Wallet connected:', walletAddress);
}).catch((error) => {
  console.error('Error connecting wallet:', error);
});

// Get the supported payment methods
console.log('Supported payment methods:', presaleWidget.getSupportedPaymentMethods());

// Get the supported blockchains
console.log('Supported blockchains:', presaleWidget.getSupportedBlockchains());

// Purchase tokens
presaleWidget.purchaseTokens('metamask', 'ethereum', 10).then((transactionHash) => {
  console.log('Tokens purchased:', transactionHash);
}).catch((error) => {
  console.error('Error purchasing tokens:', error);
});
```
