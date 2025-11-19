"""
Generated Code Metadata:
========================
Original URL: https://draco.finance
Prompt: Create a code example for integrating a wallet connection feature into a DeFi platform similar to Draco Finance.
Generated: DETERMINISTIC_a925f45e563c44f2
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnection.js
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';
import WalletConnectProvider from '@walletconnect/web3-provider';

// Configuration for Web3Modal
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: process.env.REACT_APP_INFURA_ID, // Replace with your Infura ID
    },
  },
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // optional
  providerOptions, // required
});

// Wallet connection manager
class WalletConnection {
  constructor() {
    this.provider = null;
    this.signer = null;
    this.account = null;
    this.chainId = null;
  }

  // Connect wallet
  async connectWallet() {
    try {
      const instance = await web3Modal.connect();
      this.provider = new ethers.providers.Web3Provider(instance);
      this.signer = this.provider.getSigner();
      this.account = await this.signer.getAddress();
      this.chainId = await this.signer.getChainId();

      // Subscribe to accounts change
      instance.on('accountsChanged', (accounts) => {
        if (accounts.length === 0) {
          this.disconnectWallet();
        } else {
          this.account = accounts[0];
        }
      });

      // Subscribe to chainId change
      instance.on('chainChanged', (chainId) => {
        this.chainId = parseInt(chainId, 16);
      });

      return {
        success: true,
        account: this.account,
        chainId: this.chainId,
      };
    } catch (error) {
      console.error('Wallet connection error:', error);
      return {
        success: false,
        error: error.message,
      };
    }
  }

  // Disconnect wallet
  async disconnectWallet() {
    try {
      if (web3Modal.cachedProvider) {
        web3Modal.clearCachedProvider();
      }
      this.provider = null;
      this.signer = null;
      this.account = null;
      this.chainId = null;
      return { success: true };
    } catch (error) {
      console.error('Wallet disconnection error:', error);
      return {
        success: false,
        error: error.message,
      };
    }
  }

  // Get current wallet state
  getWalletState() {
    return {
      isConnected: !!this.account,
      account: this.account,
      chainId: this.chainId,
    };
  }

  // Get signer
  getSigner() {
    if (!this.signer) {
      throw new Error('Wallet not connected');
    }
    return this.signer;
  }

  // Get provider
  getProvider() {
    if (!this.provider) {
      throw new Error('Wallet not connected');
    }
    return this.provider;
  }
}

export default WalletConnection;
```
