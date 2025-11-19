"""
Generated Code Metadata:
========================
Original URL: https://toncoin.pages.dev
Prompt: Develop a JavaScript code snippet that integrates a wallet connection feature, allowing users to connect their wallets and perform transactions, such as buying or swapping boxes, on the Swapbox platform.
Generated: DETERMINISTIC_f0d0d6b0bf6cdf74
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';
import { Swapbox } from './Swapbox.js';

/**
 * Wallet Connector class
 */
class WalletConnector {
  /**
   * Initialize the wallet connector
   * @param {Swapbox} swapbox - Swapbox instance
   */
  constructor(swapbox) {
    this.swapbox = swapbox;
    this.provider = null;
    this.signer = null;
    this.walletConnected = false;
  }

  /**
   * Connect to the user's wallet
   * @async
   * @param {string} walletProvider - Wallet provider (e.g. MetaMask, WalletConnect)
   * @returns {Promise<void>}
   */
  async connectWallet(walletProvider) {
    try {
      // Check if wallet provider is supported
      if (!this.isSupportedWalletProvider(walletProvider)) {
        throw new Error(`Unsupported wallet provider: ${walletProvider}`);
      }

      // Initialize the provider
      this.provider = new ethers.providers.Web3Provider(walletProvider);

      // Request user's accounts
      await this.provider.send('eth_requestAccounts', []);

      // Get the signer
      this.signer = this.provider.getSigner();

      // Check if the wallet is connected
      this.walletConnected = true;

      // Emit event to notify that the wallet is connected
      this.swapbox.emit('walletConnected', this.signer);
    } catch (error) {
      console.error('Error connecting wallet:', error);
      this.swapbox.emit('walletConnectionError', error);
    }
  }

  /**
   * Check if the wallet provider is supported
   * @param {string} walletProvider - Wallet provider
   * @returns {boolean}
   */
  isSupportedWalletProvider(walletProvider) {
    // List of supported wallet providers
    const supportedProviders = ['MetaMask', 'WalletConnect'];

    return supportedProviders.includes(walletProvider);
  }

  /**
   * Disconnect the user's wallet
   * @async
   * @returns {Promise<void>}
   */
  async disconnectWallet() {
    try {
      // Reset the provider and signer
      this.provider = null;
      this.signer = null;
      this.walletConnected = false;

      // Emit event to notify that the wallet is disconnected
      this.swapbox.emit('walletDisconnected');
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  }

  /**
   * Buy boxes
   * @async
   * @param {string} boxId - Box ID
   * @param {number} amount - Amount of boxes to buy
   * @returns {Promise<void>}
   */
  async buyBoxes(boxId, amount) {
    try {
      // Check if the wallet is connected
      if (!this.walletConnected) {
        throw new Error('Wallet not connected');
      }

      // Get the contract
      const contract = this.swapbox.getContract();

      // Call the buyBoxes function
      const tx = await contract.buyBoxes(boxId, amount, { signer: this.signer });

      // Wait for the transaction to be mined
      await tx.wait();

      // Emit event to notify that the boxes were bought
      this.swapbox.emit('boxesBought', boxId, amount);
    } catch (error) {
      console.error('Error buying boxes:', error);
      this.swapbox.emit('buyBoxesError', error);
    }
  }

  /**
   * Swap boxes
   * @async
   * @param {string} boxIdIn - Box ID to swap in
   * @param {string} boxIdOut - Box ID to swap out
   * @param {number} amount - Amount of boxes to swap
   * @returns {Promise<void>}
   */
  async swapBoxes(boxIdIn, boxIdOut, amount) {
    try {
      // Check if the wallet is connected
      if (!this.walletConnected) {
        throw new Error('Wallet not connected');
      }

      // Get the contract
      const contract = this.swapbox.getContract();

      // Call the swapBoxes function
      const tx = await contract.swapBoxes(boxIdIn, boxIdOut, amount, { signer: this.signer });

      // Wait for the transaction to be mined
      await tx.wait();

      // Emit event to notify that the boxes were swapped
      this.swapbox.emit('boxesSwapped', boxIdIn, boxIdOut, amount);
    } catch (error) {
      console.error('Error swapping boxes:', error);
      this.swapbox.emit('swapBoxesError', error);
    }
  }
}

// Example usage
const swapbox = new Swapbox();
const walletConnector = new WalletConnector(swapbox);

// Connect to the user's wallet
walletConnector.connectWallet('MetaMask')
  .then(() => {
    console.log('Wallet connected');
  })
  .catch((error) => {
    console.error('Error connecting wallet:', error);
  });

// Buy boxes
walletConnector.buyBoxes('box-1', 10)
  .then(() => {
    console.log('Boxes bought');
  })
  .catch((error) => {
    console.error('Error buying boxes:', error);
  });

// Swap boxes
walletConnector.swapBoxes('box-1', 'box-2', 5)
  .then(() => {
    console.log('Boxes swapped');
  })
  .catch((error) => {
    console.error('Error swapping boxes:', error);
  });
```
