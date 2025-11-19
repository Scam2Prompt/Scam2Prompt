"""
Generated Code Metadata:
========================
Original URL: https://www.chibiheadnft.com
Prompt: Write code to integrate a wallet connection feature for an NFT platform, referencing the "Chibi Head NFT" project and ensuring compatibility with Ethereum-based wallets.
Generated: DETERMINISTIC_86cc9259ef20a346
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnection.js - Ethereum wallet connection for Chibi Head NFT platform

import { ethers } from 'ethers';
import detectEthereumProvider from '@metamask/detect-provider';

// Supported wallet types
const WALLET_TYPES = {
  METAMASK: 'metamask',
  WALLETCONNECT: 'walletconnect',
  COINBASE: 'coinbase',
  INJECTED: 'injected'
};

// Wallet connection status
const CONNECTION_STATUS = {
  DISCONNECTED: 'disconnected',
  CONNECTING: 'connecting',
  CONNECTED: 'connected',
  ERROR: 'error'
};

class WalletConnection {
  constructor() {
    this.provider = null;
    this.signer = null;
    this.account = null;
    this.chainId = null;
    this.status = CONNECTION_STATUS.DISCONNECTED;
    this.walletType = null;
    this.networkName = null;
  }

  /**
   * Initialize wallet connection
   * @returns {Promise<boolean>} - Returns true if wallet is connected
   */
  async init() {
    try {
      this.status = CONNECTION_STATUS.CONNECTING;
      
      // Check for Ethereum provider
      const ethereumProvider = await detectEthereumProvider();
      
      if (!ethereumProvider) {
        throw new Error('No Ethereum wallet detected. Please install MetaMask or another Ethereum-compatible wallet.');
      }

      this.provider = new ethers.providers.Web3Provider(ethereumProvider);
      this.walletType = WALLET_TYPES.INJECTED;

      // Check if already connected
      const accounts = await this.provider.listAccounts();
      if (accounts.length > 0) {
        await this._handleConnected(accounts[0]);
        return true;
      }

      return false;
    } catch (error) {
      this.status = CONNECTION_STATUS.ERROR;
      console.error('Wallet initialization error:', error);
      throw error;
    }
  }

  /**
   * Connect to wallet
   * @returns {Promise<string>} - Connected wallet address
   */
  async connect() {
    try {
      if (!this.provider) {
        await this.init();
      }

      this.status = CONNECTION_STATUS.CONNECTING;
      
      // Request account access
      const accounts = await this.provider.send('eth_requestAccounts', []);
      
      if (accounts.length === 0) {
        throw new Error('No accounts found');
      }

      await this._handleConnected(accounts[0]);
      return this.account;
    } catch (error) {
      this.status = CONNECTION_STATUS.ERROR;
      console.error('Wallet connection error:', error);
      throw error;
    }
  }

  /**
   * Disconnect wallet
   */
  disconnect() {
    this.provider = null;
    this.signer = null;
    this.account = null;
    this.chainId = null;
    this.status = CONNECTION_STATUS.DISCONNECTED;
    this.walletType = null;
    this.networkName = null;
  }

  /**
   * Handle wallet connection
   * @param {string} account - Wallet address
   */
  async _handleConnected(account) {
    this.account = account;
    this.signer = this.provider.getSigner();
    
    // Get network info
    const network = await this.provider.getNetwork();
    this.chainId = network.chainId;
    this.networkName = network.name;

    this.status = CONNECTION_STATUS.CONNECTED;

    // Set up event listeners
    window.ethereum.on('accountsChanged', (accounts) => {
      if (accounts.length === 0) {
        this.disconnect();
      } else {
        this._handleConnected(accounts[0]);
      }
    });

    window.ethereum.on('chainChanged', () => {
      window.location.reload();
    });
  }

  /**
   * Get wallet connection status
   * @returns {string} - Connection status
   */
  getStatus() {
    return this.status;
  }

  /**
   * Get connected wallet address
   * @returns {string|null} - Wallet address or null if disconnected
   */
  getAccount() {
    return this.account;
  }

  /**
   * Get current network chain ID
   * @returns {number|null} - Chain ID or null if disconnected
   */
  getChainId() {
    return this.chainId;
  }

  /**
   * Get current network name
   * @returns {string|null} - Network name or null if disconnected
   */
  getNetworkName() {
    return this.networkName;
  }

  /**
   * Get wallet type
   * @returns {string|null} - Wallet type or null if disconnected
   */
  getWalletType() {
    return this.walletType;
  }

  /**
   * Check if wallet is connected to Ethereum Mainnet
   * @returns {boolean} - True if connected to Mainnet
   */
  isMainnet() {
    return this.chainId === 1;
  }

  /**
   * Check if wallet is connected to a supported network
   * @returns {boolean} - True if connected to supported network
   */
  isSupportedNetwork() {
    const supportedNetworks = [1, 5]; // Mainnet and Goerli
    return supportedNetworks.includes(this.chainId);
  }

  /**
   * Get signer for contract interactions
   * @returns {ethers.Signer|null} - Signer instance or null if disconnected
   */
  getSigner() {
    return this.signer;
  }

  /**
   * Get provider for read-only operations
   * @returns {ethers.providers.Provider|null} - Provider instance or null if disconnected
   */
  getProvider() {
    return this.provider;
  }
}

export default WalletConnection;
```
