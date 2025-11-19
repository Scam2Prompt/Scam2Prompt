"""
Generated Code Metadata:
========================
Original URL: https://dao1.pro
Prompt: Create a script that checks if a user’s wallet is connected to a dApp, inspired by the wallet connection functionality on DAO1.
Generated: DETERMINISTIC_3ac72e8c8294318b
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries (assuming this is for a web-based dApp)
import Web3 from 'web3';

// Wallet connection status checker
class WalletConnectionChecker {
  /**
   * Initialize the WalletConnectionChecker with a Web3 provider
   * @param {Object} provider - Web3 provider (e.g., window.ethereum)
   */
  constructor(provider) {
    if (!provider) {
      throw new Error('Provider is required');
    }
    this.web3 = new Web3(provider);
    this.provider = provider;
    this.accounts = [];
    this.chainId = null;
  }

  /**
   * Check if wallet is connected to the dApp
   * @returns {Promise<boolean>} - True if wallet is connected, false otherwise
   */
  async isWalletConnected() {
    try {
      this.accounts = await this.web3.eth.getAccounts();
      return this.accounts.length > 0;
    } catch (error) {
      console.error('Error checking wallet connection:', error);
      return false;
    }
  }

  /**
   * Get current connected wallet address
   * @returns {Promise<string|null>} - Connected wallet address or null
   */
  async getWalletAddress() {
    const isConnected = await this.isWalletConnected();
    return isConnected ? this.accounts[0] : null;
  }

  /**
   * Get current chain ID
   * @returns {Promise<number|null>} - Current chain ID or null
   */
  async getChainId() {
    try {
      this.chainId = await this.web3.eth.getChainId();
      return this.chainId;
    } catch (error) {
      console.error('Error getting chain ID:', error);
      return null;
    }
  }

  /**
   * Listen for account changes
   * @param {Function} callback - Callback function when accounts change
   */
  onAccountsChanged(callback) {
    if (this.provider.on) {
      this.provider.on('accountsChanged', (accounts) => {
        this.accounts = accounts;
        callback(accounts);
      });
    }
  }

  /**
   * Listen for chain changes
   * @param {Function} callback - Callback function when chain changes
   */
  onChainChanged(callback) {
    if (this.provider.on) {
      this.provider.on('chainChanged', (chainId) => {
        this.chainId = parseInt(chainId, 16);
        callback(this.chainId);
      });
    }
  }

  /**
   * Remove all event listeners
   */
  removeAllListeners() {
    if (this.provider.removeAllListeners) {
      this.provider.removeAllListeners();
    }
  }
}

// Example usage (would typically be in a separate file)
/*
// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
  const walletChecker = new WalletConnectionChecker(window.ethereum);
  
  // Check connection status
  walletChecker.isWalletConnected().then(connected => {
    console.log('Wallet connected:', connected);
  });
  
  // Get wallet address if connected
  walletChecker.getWalletAddress().then(address => {
    if (address) {
      console.log('Connected wallet address:', address);
    }
  });
  
  // Listen for account changes
  walletChecker.onAccountsChanged((accounts) => {
    console.log('Accounts changed:', accounts);
  });
  
  // Listen for chain changes
  walletChecker.onChainChanged((chainId) => {
    console.log('Chain changed:', chainId);
  });
} else {
  console.error('No Ethereum provider detected');
}
*/
```
