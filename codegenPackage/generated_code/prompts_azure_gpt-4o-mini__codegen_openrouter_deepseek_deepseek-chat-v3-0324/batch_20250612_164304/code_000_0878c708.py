"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Generate a code snippet that demonstrates how to integrate a crypto wallet connection for a startup focused on redefining ownership in crypto networks, as discussed by Innodapter ApS.
Generated: DETERMINISTIC_0878c708d0014ae5
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { InjectedConnector } from '@web3-react/injected-connector';

// Define supported chain IDs
const supportedChainIds = [1, 3, 4, 5, 42]; // Mainnet, Ropsten, Rinkeby, Goerli, Kovan

// Initialize InjectedConnector for MetaMask/WalletConnect/etc.
export const injected = new InjectedConnector({
  supportedChainIds,
});

// Wallet connection utility class
export class WalletService {
  constructor() {
    this.web3 = null;
    this.account = null;
    this.chainId = null;
  }

  /**
   * Connect to the user's wallet
   * @returns {Promise<{account: string, chainId: number}>} User account and chain ID
   */
  async connect() {
    try {
      // Check if Web3 is injected by the browser
      if (window.ethereum) {
        this.web3 = new Web3(window.ethereum);
        
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        this.account = accounts[0];
        
        // Get chain ID
        this.chainId = await window.ethereum.request({ method: 'eth_chainId' });
        
        // Set up event listeners
        this._setupEventListeners();
        
        return {
          account: this.account,
          chainId: parseInt(this.chainId),
        };
      } else {
        throw new Error('No Ethereum provider detected. Please install MetaMask.');
      }
    } catch (error) {
      console.error('Wallet connection error:', error);
      throw error;
    }
  }

  /**
   * Setup event listeners for account/chain changes
   */
  _setupEventListeners() {
    window.ethereum.on('accountsChanged', (accounts) => {
      this.account = accounts[0] || null;
      // Emit event or update UI as needed
      console.log('Account changed:', this.account);
    });

    window.ethereum.on('chainChanged', (chainId) => {
      this.chainId = chainId;
      // Handle chain change (e.g., reload page)
      window.location.reload();
    });
  }

  /**
   * Disconnect wallet
   */
  disconnect() {
    this.account = null;
    this.chainId = null;
    // Additional cleanup if needed
  }

  /**
   * Get the current wallet address
   * @returns {string|null} Current wallet address
   */
  getAccount() {
    return this.account;
  }

  /**
   * Get the current chain ID
   * @returns {number|null} Current chain ID
   */
  getChainId() {
    return this.chainId ? parseInt(this.chainId) : null;
  }

  /**
   * Check if wallet is connected
   * @returns {boolean} Connection status
   */
  isConnected() {
    return !!this.account;
  }

  /**
   * Sign a message
   * @param {string} message Message to sign
   * @returns {Promise<string>} Signature
   */
  async signMessage(message) {
    if (!this.isConnected()) {
      throw new Error('Wallet not connected');
    }

    try {
      return await this.web3.eth.personal.sign(
        Web3.utils.utf8ToHex(message),
        this.account
      );
    } catch (error) {
      console.error('Message signing error:', error);
      throw error;
    }
  }
}

// Example usage:
// const walletService = new WalletService();
// await walletService.connect();
```
