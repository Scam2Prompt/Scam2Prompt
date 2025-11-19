"""
Generated Code Metadata:
========================
Original URL: https://cdfi.pages.dev
Prompt: Write code to integrate a wallet connection feature using Web3.js for a DeFi dashboard similar to the one described on the CeDeFiAi platform.
Generated: DETERMINISTIC_1f042ba6fb35f101
Batch ID: 20250612_153400
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

  // Initialize Web3 and event listeners
  async init() {
    try {
      this.provider = await detectEthereumProvider();

      if (this.provider) {
        this.web3 = new Web3(this.provider);
        this._setupEventListeners();
        return true;
      } else {
        console.error('Please install MetaMask or another Web3 provider');
        return false;
      }
    } catch (error) {
      console.error('Error initializing Web3:', error);
      return false;
    }
  }

  // Set up event listeners for account and chain changes
  _setupEventListeners() {
    if (!this.provider) return;

    this.provider.on('accountsChanged', (accounts) => {
      this.accounts = accounts;
      this._handleConnectionChange();
    });

    this.provider.on('chainChanged', (chainId) => {
      this.chainId = chainId;
      this._handleConnectionChange();
    });

    this.provider.on('disconnect', (error) => {
      console.error('Provider disconnected:', error);
      this._resetState();
    });
  }

  // Handle connection state changes
  _handleConnectionChange() {
    this.isConnected = this.accounts.length > 0;
    if (this.isConnected) {
      console.log('Wallet connected:', this.accounts[0]);
      // Dispatch custom event or callback for UI updates
      document.dispatchEvent(new CustomEvent('walletConnected', {
        detail: {
          account: this.accounts[0],
          chainId: this.chainId
        }
      }));
    } else {
      console.log('Wallet disconnected');
      document.dispatchEvent(new CustomEvent('walletDisconnected'));
    }
  }

  // Reset connection state
  _resetState() {
    this.accounts = [];
    this.chainId = null;
    this.isConnected = false;
    this._handleConnectionChange();
  }

  // Connect wallet
  async connectWallet() {
    try {
      if (!this.provider) {
        throw new Error('No Web3 provider detected');
      }

      const accounts = await this.provider.request({
        method: 'eth_requestAccounts'
      });

      const chainId = await this.provider.request({
        method: 'eth_chainId'
      });

      this.accounts = accounts;
      this.chainId = chainId;
      this.isConnected = accounts.length > 0;
      this._handleConnectionChange();

      return {
        success: true,
        account: accounts[0],
        chainId: chainId
      };
    } catch (error) {
      console.error('Error connecting wallet:', error);
      return {
        success: false,
        error: error.message
      };
    }
  }

  // Disconnect wallet
  async disconnectWallet() {
    try {
      if (this.provider && this.provider.close) {
        await this.provider.close();
      }
      this._resetState();
      return { success: true };
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
      return {
        success: false,
        error: error.message
      };
    }
  }

  // Get current account
  getAccount() {
    return this.accounts.length > 0 ? this.accounts[0] : null;
  }

  // Get current chain ID
  getChainId() {
    return this.chainId;
  }

  // Check if wallet is connected
  isWalletConnected() {
    return this.isConnected;
  }

  // Switch network
  async switchNetwork(chainId) {
    try {
      await this.provider.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: chainId }],
      });
      return { success: true };
    } catch (error) {
      console.error('Error switching network:', error);
      return {
        success: false,
        error: error.message
      };
    }
  }
}

// Export singleton instance
const walletConnector = new WalletConnector();
export default walletConnector;
```
