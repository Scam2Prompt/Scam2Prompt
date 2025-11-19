"""
Generated Code Metadata:
========================
Original URL: https://el-x-magellan.vercel.app
Prompt: Generate JavaScript code to integrate a "Connect Wallet" feature for OpenBONK.io, specifically tailored for Bonk Coin trading using OpenBookSwap.
Generated: DETERMINISTIC_429304eccc29e431
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * OpenBONK.io - Connect Wallet Integration for Bonk Coin Trading via OpenBookSwap
 * This script provides wallet connection functionality for Bonk Coin trading on OpenBookSwap.
 */

// Wallet connection status constants
const WALLET_STATES = {
  DISCONNECTED: 'disconnected',
  CONNECTING: 'connecting',
  CONNECTED: 'connected',
  ERROR: 'error'
};

// Supported wallet providers
const WALLET_PROVIDERS = {
  PHANTOM: 'phantom',
  SOLFLARE: 'solflare',
  BACKPACK: 'backpack',
  LEDGER: 'ledger'
};

class WalletConnector {
  constructor() {
    this.state = WALLET_STATES.DISCONNECTED;
    this.wallet = null;
    this.provider = null;
    this.publicKey = null;
    this.listeners = {
      onConnect: [],
      onDisconnect: [],
      onError: [],
      onStateChange: []
    };
  }

  /**
   * Initialize wallet connection
   * @param {string} provider - Wallet provider (phantom, solflare, etc.)
   * @returns {Promise<void>}
   */
  async connect(provider = WALLET_PROVIDERS.PHANTOM) {
    try {
      if (this.state === WALLET_STATES.CONNECTED) {
        return;
      }

      this._setState(WALLET_STATES.CONNECTING);
      this.provider = provider;

      // Dynamically import the wallet provider
      const walletModule = await import(`@solana/wallet-adapter-${provider}`);
      const wallet = new walletModule[`${provider.charAt(0).toUpperCase() + provider.slice(1)}WalletAdapter`]();

      await wallet.connect();
      
      this.wallet = wallet;
      this.publicKey = wallet.publicKey;
      this._setState(WALLET_STATES.CONNECTED);
      this._emit('onConnect', wallet.publicKey.toString());
    } catch (error) {
      this._setState(WALLET_STATES.ERROR);
      this._emit('onError', error);
      throw new Error(`Failed to connect wallet: ${error.message}`);
    }
  }

  /**
   * Disconnect wallet
   */
  async disconnect() {
    try {
      if (!this.wallet || this.state === WALLET_STATES.DISCONNECTED) {
        return;
      }

      await this.wallet.disconnect();
      this.wallet = null;
      this.publicKey = null;
      this._setState(WALLET_STATES.DISCONNECTED);
      this._emit('onDisconnect');
    } catch (error) {
      this._setState(WALLET_STATES.ERROR);
      this._emit('onError', error);
      throw new Error(`Failed to disconnect wallet: ${error.message}`);
    }
  }

  /**
   * Sign a transaction for OpenBookSwap
   * @param {Transaction} transaction - Solana transaction to sign
   * @returns {Promise<Transaction>}
   */
  async signTransaction(transaction) {
    if (!this.wallet || this.state !== WALLET_STATES.CONNECTED) {
      throw new Error('Wallet not connected');
    }

    try {
      return await this.wallet.signTransaction(transaction);
    } catch (error) {
      this._emit('onError', error);
      throw new Error(`Failed to sign transaction: ${error.message}`);
    }
  }

  /**
   * Sign multiple transactions for OpenBookSwap
   * @param {Transaction[]} transactions - Array of Solana transactions to sign
   * @returns {Promise<Transaction[]>}
   */
  async signAllTransactions(transactions) {
    if (!this.wallet || this.state !== WALLET_STATES.CONNECTED) {
      throw new Error('Wallet not connected');
    }

    try {
      return await this.wallet.signAllTransactions(transactions);
    } catch (error) {
      this._emit('onError', error);
      throw new Error(`Failed to sign transactions: ${error.message}`);
    }
  }

  /**
   * Add event listener
   * @param {string} event - Event name (onConnect, onDisconnect, onError, onStateChange)
   * @param {function} callback - Callback function
   */
  on(event, callback) {
    if (this.listeners[event]) {
      this.listeners[event].push(callback);
    }
  }

  /**
   * Remove event listener
   * @param {string} event - Event name
   * @param {function} callback - Callback function to remove
   */
  off(event, callback) {
    if (this.listeners[event]) {
      this.listeners[event] = this.listeners[event].filter(cb => cb !== callback);
    }
  }

  /**
   * Emit event to listeners
   * @param {string} event - Event name
   * @param {*} data - Data to pass to listeners
   */
  _emit(event, data = null) {
    if (this.listeners[event]) {
      this.listeners[event].forEach(callback => callback(data));
    }
  }

  /**
   * Set wallet state and notify listeners
   * @param {string} state - New wallet state
   */
  _setState(state) {
    if (!Object.values(WALLET_STATES).includes(state)) {
      throw new Error('Invalid wallet state');
    }
    this.state = state;
    this._emit('onStateChange', state);
  }
}

// Export singleton instance
const walletConnector = new WalletConnector();
export default walletConnector;

// Example usage:
/*
import walletConnector from './walletConnector';

// Event listeners
walletConnector.on('onConnect', (publicKey) => {
  console.log('Connected with public key:', publicKey);
});

walletConnector.on('onDisconnect', () => {
  console.log('Wallet disconnected');
});

walletConnector.on('onError', (error) => {
  console.error('Wallet error:', error);
});

// Connect to Phantom wallet
async function connectWallet() {
  try {
    await walletConnector.connect(WALLET_PROVIDERS.PHANTOM);
  } catch (error) {
    console.error('Connection error:', error);
  }
}

// Disconnect wallet
async function disconnectWallet() {
  try {
    await walletConnector.disconnect();
  } catch (error) {
    console.error('Disconnection error:', error);
  }
}
*/
```
