"""
Generated Code Metadata:
========================
Original URL: https://draco.finance
Prompt: Generate code to detect and handle wallet connection events in a DeFi app, similar to the behavior described on draco.finance.
Generated: DETERMINISTIC_5a77a3dd18a81463
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnectionHandler.js
import { ethers } from 'ethers';
import { detectEthereumProvider } from '@metamask/detect-provider';

class WalletConnectionHandler {
  constructor() {
    this.provider = null;
    this.signer = null;
    this.currentAccount = null;
    this.chainId = null;
    this.eventListeners = {
      accountChanged: [],
      chainChanged: [],
      connected: [],
      disconnected: []
    };
  }

  /**
   * Initialize wallet connection handler
   * @returns {Promise<boolean>} - Returns true if initialization succeeds
   */
  async init() {
    try {
      const ethereumProvider = await detectEthereumProvider();
      
      if (!ethereumProvider) {
        console.error('No Ethereum provider detected');
        return false;
      }

      this.provider = new ethers.providers.Web3Provider(ethereumProvider);
      this._setupEventListeners();
      
      return true;
    } catch (error) {
      console.error('Error initializing wallet connection:', error);
      return false;
    }
  }

  /**
   * Connect to wallet
   * @returns {Promise<string|null>} - Connected account address or null if failed
   */
  async connectWallet() {
    try {
      if (!this.provider) {
        throw new Error('Provider not initialized');
      }

      const accounts = await this.provider.send('eth_requestAccounts', []);
      if (accounts.length === 0) {
        throw new Error('No accounts found');
      }

      this.currentAccount = accounts[0];
      this.signer = this.provider.getSigner();
      this.chainId = await this.provider.send('eth_chainId', []);

      this._emitEvent('connected', {
        account: this.currentAccount,
        chainId: this.chainId
      });

      return this.currentAccount;
    } catch (error) {
      console.error('Error connecting wallet:', error);
      this._emitEvent('disconnected', { error: error.message });
      return null;
    }
  }

  /**
   * Disconnect wallet
   */
  disconnectWallet() {
    this.currentAccount = null;
    this.signer = null;
    this._emitEvent('disconnected');
  }

  /**
   * Add event listener
   * @param {string} eventName - Event name to listen for
   * @param {function} callback - Callback function
   */
  on(eventName, callback) {
    if (this.eventListeners[eventName]) {
      this.eventListeners[eventName].push(callback);
    } else {
      console.warn(`Unknown event: ${eventName}`);
    }
  }

  /**
   * Remove event listener
   * @param {string} eventName - Event name
   * @param {function} callback - Callback function to remove
   */
  off(eventName, callback) {
    if (this.eventListeners[eventName]) {
      this.eventListeners[eventName] = this.eventListeners[eventName].filter(
        cb => cb !== callback
      );
    }
  }

  /**
   * Setup Ethereum provider event listeners
   */
  _setupEventListeners() {
    if (!window.ethereum) return;

    window.ethereum.on('accountsChanged', (accounts) => {
      if (accounts.length === 0) {
        this.disconnectWallet();
      } else {
        this.currentAccount = accounts[0];
        this.signer = this.provider.getSigner();
        this._emitEvent('accountChanged', {
          account: this.currentAccount
        });
      }
    });

    window.ethereum.on('chainChanged', (chainId) => {
      this.chainId = chainId;
      this._emitEvent('chainChanged', {
        chainId: chainId
      });
    });

    window.ethereum.on('disconnect', (error) => {
      this.disconnectWallet();
      this._emitEvent('disconnected', { error: error.message });
    });
  }

  /**
   * Emit event to all registered listeners
   * @param {string} eventName - Event name
   * @param {object} data - Event data
   */
  _emitEvent(eventName, data = {}) {
    if (this.eventListeners[eventName]) {
      this.eventListeners[eventName].forEach(callback => {
        try {
          callback(data);
        } catch (error) {
          console.error(`Error in ${eventName} event handler:`, error);
        }
      });
    }
  }
}

export default WalletConnectionHandler;
```
