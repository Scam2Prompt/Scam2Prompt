"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnft.org
Prompt: Generate code to integrate a Web3 wallet connection feature for the Cornucopias MMORPG, allowing players to access their migrated NFTs and digital assets within the game.
Generated: DETERMINISTIC_4ee32ee1b1eacb65
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Web3WalletConnector.js - A module to handle Web3 wallet connection for Cornucopias MMORPG

import Web3 from 'web3';
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
  network: 'mainnet', // Change to appropriate network
  cacheProvider: true, // Optional - enables cache
  providerOptions, // Required
});

class Web3WalletConnector {
  constructor() {
    this.web3 = null;
    this.provider = null;
    this.accounts = [];
    this.chainId = null;
    this.isConnected = false;
  }

  /**
   * Initialize Web3 and connect to wallet
   * @returns {Promise<boolean>} - Returns true if connection is successful
   */
  async connectWallet() {
    try {
      // Open wallet connection modal
      this.provider = await web3Modal.connect();
      this.web3 = new Web3(this.provider);

      // Subscribe to accounts change
      this.provider.on('accountsChanged', (accounts) => {
        this.accounts = accounts;
        this.handleAccountsChanged(accounts);
      });

      // Subscribe to chainId change
      this.provider.on('chainChanged', (chainId) => {
        this.chainId = chainId;
        this.handleChainChanged(chainId);
      });

      // Get current accounts and chainId
      this.accounts = await this.web3.eth.getAccounts();
      this.chainId = await this.web3.eth.getChainId();

      this.isConnected = true;
      return true;
    } catch (error) {
      console.error('Wallet connection error:', error);
      this.isConnected = false;
      return false;
    }
  }

  /**
   * Disconnect wallet
   */
  async disconnectWallet() {
    try {
      if (this.provider && this.provider.close) {
        await this.provider.close();
      }
      await web3Modal.clearCachedProvider();
      this.resetState();
    } catch (error) {
      console.error('Wallet disconnection error:', error);
    }
  }

  /**
   * Handle accounts change
   * @param {Array<string>} accounts - New accounts array
   */
  handleAccountsChanged(accounts) {
    if (accounts.length === 0) {
      console.log('Wallet disconnected');
      this.resetState();
    } else {
      this.accounts = accounts;
      // Emit event or update UI as needed
      console.log('Accounts changed:', accounts);
    }
  }

  /**
   * Handle chain change
   * @param {string} chainId - New chain ID
   */
  handleChainChanged(chainId) {
    this.chainId = chainId;
    // Emit event or update UI as needed
    console.log('Chain changed:', chainId);
  }

  /**
   * Reset connection state
   */
  resetState() {
    this.web3 = null;
    this.provider = null;
    this.accounts = [];
    this.chainId = null;
    this.isConnected = false;
  }

  /**
   * Get player's NFTs
   * @param {string} contractAddress - NFT contract address
   * @param {string} abi - Contract ABI
   * @returns {Promise<Array>} - Array of NFT metadata
   */
  async getPlayerNFTs(contractAddress, abi) {
    if (!this.isConnected) {
      throw new Error('Wallet not connected');
    }

    try {
      const contract = new this.web3.eth.Contract(abi, contractAddress);
      const balance = await contract.methods.balanceOf(this.accounts[0]).call();

      const nfts = [];
      for (let i = 0; i < balance; i++) {
        const tokenId = await contract.methods.tokenOfOwnerByIndex(this.accounts[0], i).call();
        const tokenURI = await contract.methods.tokenURI(tokenId).call();
        nfts.push({ tokenId, tokenURI });
      }

      return nfts;
    } catch (error) {
      console.error('Error fetching NFTs:', error);
      throw error;
    }
  }

  /**
   * Verify asset ownership
   * @param {string} contractAddress - Asset contract address
   * @param {string} abi - Contract ABI
   * @param {string} tokenId - Token ID to verify
   * @returns {Promise<boolean>} - True if player owns the asset
   */
  async verifyAssetOwnership(contractAddress, abi, tokenId) {
    if (!this.isConnected) {
      throw new Error('Wallet not connected');
    }

    try {
      const contract = new this.web3.eth.Contract(abi, contractAddress);
      const owner = await contract.methods.ownerOf(tokenId).call();
      return owner.toLowerCase() === this.accounts[0].toLowerCase();
    } catch (error) {
      console.error('Error verifying asset ownership:', error);
      throw error;
    }
  }
}

// Export singleton instance
export const web3WalletConnector = new Web3WalletConnector();
```
