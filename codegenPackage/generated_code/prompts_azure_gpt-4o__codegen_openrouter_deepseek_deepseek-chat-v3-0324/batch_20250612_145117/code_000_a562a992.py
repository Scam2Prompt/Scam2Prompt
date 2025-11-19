"""
Generated Code Metadata:
========================
Original URL: https://ragnarokdao.finance
Prompt: Write code to integrate a cryptocurrency wallet connection feature using Web3.js, similar to the functionality described on the RagnarokDAO website.
Generated: DETERMINISTIC_a562a992f92fd114
Batch ID: 20250612_145117
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
import detectEthereumProvider from '@metamask/detect-provider';

// Wallet connection class
class WalletConnector {
  constructor() {
    this.web3 = null;
    this.provider = null;
    this.accounts = [];
    this.chainId = null;
    this.isConnected = false;
  }

  /**
   * Initialize the wallet connection
   * @returns {Promise<boolean>} - Returns true if initialization is successful
   */
  async init() {
    try {
      // Detect the Ethereum provider (e.g., MetaMask)
      this.provider = await detectEthereumProvider();

      if (this.provider) {
        this.web3 = new Web3(this.provider);
        
        // Check if already connected
        const accounts = await this.web3.eth.getAccounts();
        if (accounts.length > 0) {
          this.accounts = accounts;
          this.isConnected = true;
          this.chainId = await this.web3.eth.getChainId();
        }

        // Set up event listeners
        this.provider.on('accountsChanged', this.handleAccountsChanged.bind(this));
        this.provider.on('chainChanged', this.handleChainChanged.bind(this));
        this.provider.on('disconnect', this.handleDisconnect.bind(this));

        return true;
      } else {
        console.error('Please install MetaMask or another Ethereum wallet!');
        return false;
      }
    } catch (error) {
      console.error('Error initializing wallet connection:', error);
      return false;
    }
  }

  /**
   * Connect to the wallet
   * @returns {Promise<Array<string>>} - Array of connected accounts
   */
  async connect() {
    try {
      if (!this.provider) {
        throw new Error('Wallet provider not initialized');
      }

      // Request account access
      const accounts = await this.provider.request({ method: 'eth_requestAccounts' });
      this.accounts = accounts;
      this.chainId = await this.web3.eth.getChainId();
      this.isConnected = true;
      
      return accounts;
    } catch (error) {
      console.error('Error connecting wallet:', error);
      throw error;
    }
  }

  /**
   * Disconnect the wallet
   */
  disconnect() {
    this.accounts = [];
    this.isConnected = false;
    this.chainId = null;
    // Note: There's no actual "disconnect" method in Ethereum providers
    // This just resets our local state
  }

  /**
   * Handle account changes
   * @param {Array<string>} accounts - New accounts array
   */
  handleAccountsChanged(accounts) {
    if (accounts.length === 0) {
      this.disconnect();
      console.log('Wallet disconnected');
    } else {
      this.accounts = accounts;
      console.log('Accounts changed:', accounts);
    }
    // You might want to emit an event or call a callback here
  }

  /**
   * Handle chain changes
   * @param {string} chainId - New chain ID
   */
  handleChainChanged(chainId) {
    this.chainId = parseInt(chainId, 16);
    console.log('Chain changed:', this.chainId);
    // You might want to emit an event or call a callback here
  }

  /**
   * Handle disconnection
   * @param {object} error - Disconnect error
   */
  handleDisconnect(error) {
    this.disconnect();
    console.error('Wallet disconnected:', error);
    // You might want to emit an event or call a callback here
  }

  /**
   * Get the current account
   * @returns {string|null} - Current account address or null
   */
  getAccount() {
    return this.accounts.length > 0 ? this.accounts[0] : null;
  }

  /**
   * Get the current chain ID
   * @returns {number|null} - Current chain ID or null
   */
  getChainId() {
    return this.chainId;
  }

  /**
   * Check if wallet is connected
   * @returns {boolean} - Connection status
   */
  isWalletConnected() {
    return this.isConnected;
  }

  /**
   * Sign a message
   * @param {string} message - Message to sign
   * @returns {Promise<string>} - Signature
   */
  async signMessage(message) {
    try {
      if (!this.isConnected || !this.accounts.length) {
        throw new Error('Wallet not connected');
      }

      const account = this.getAccount();
      return await this.web3.eth.personal.sign(message, account, '');
    } catch (error) {
      console.error('Error signing message:', error);
      throw error;
    }
  }

  /**
   * Send a transaction
   * @param {object} transaction - Transaction object
   * @returns {Promise<string>} - Transaction hash
   */
  async sendTransaction(transaction) {
    try {
      if (!this.isConnected || !this.accounts.length) {
        throw new Error('Wallet not connected');
      }

      const account = this.getAccount();
      const tx = {
        from: account,
        ...transaction
      };

      return await this.web3.eth.sendTransaction(tx);
    } catch (error) {
      console.error('Error sending transaction:', error);
      throw error;
    }
  }
}

// Example usage:
// const wallet = new WalletConnector();
// await wallet.init();
// const accounts = await wallet.connect();
// console.log('Connected accounts:', accounts);

export default WalletConnector;
```
