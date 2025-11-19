"""
Generated Code Metadata:
========================
Original URL: https://wap.xushuishiwu.cn
Prompt: Generate code to interact with the MetaMask wallet API for importing wallet tokens and executing secure transactions, as outlined in the "MetaMask导入钱包代币全面指南" section.
Generated: DETERMINISTIC_fcfe27071e81c87a
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const ethers = require('ethers');

// MetaMask Wallet Interaction Class
class MetaMaskWallet {
  /**
   * Initialize the MetaMask wallet interaction
   */
  constructor() {
    this.provider = null;
    this.signer = null;
    this.walletAddress = null;
  }

  /**
   * Check if MetaMask is installed
   * @returns {boolean} True if MetaMask is installed
   */
  isMetaMaskInstalled() {
    return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
  }

  /**
   * Connect to MetaMask wallet
   * @returns {Promise<string>} Connected wallet address
   * @throws {Error} If MetaMask is not installed or connection fails
   */
  async connectWallet() {
    if (!this.isMetaMaskInstalled()) {
      throw new Error('MetaMask is not installed');
    }

    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      this.walletAddress = accounts[0];
      
      // Initialize ethers provider and signer
      this.provider = new ethers.providers.Web3Provider(window.ethereum);
      this.signer = this.provider.getSigner();
      
      return this.walletAddress;
    } catch (error) {
      throw new Error(`Failed to connect wallet: ${error.message}`);
    }
  }

  /**
   * Get the current wallet address
   * @returns {string} Wallet address
   * @throws {Error} If wallet is not connected
   */
  getWalletAddress() {
    if (!this.walletAddress) {
      throw new Error('Wallet is not connected');
    }
    return this.walletAddress;
  }

  /**
   * Import token to wallet
   * @param {string} tokenAddress - ERC20 token contract address
   * @param {string} tokenSymbol - Token symbol
   * @param {number} tokenDecimals - Token decimals
   * @returns {Promise<boolean>} True if token was successfully added
   * @throws {Error} If wallet is not connected or token import fails
   */
  async importToken(tokenAddress, tokenSymbol, tokenDecimals) {
    if (!this.walletAddress) {
      throw new Error('Wallet is not connected');
    }

    try {
      const wasAdded = await window.ethereum.request({
        method: 'wallet_watchAsset',
        params: {
          type: 'ERC20',
          options: {
            address: tokenAddress,
            symbol: tokenSymbol,
            decimals: tokenDecimals,
          },
        },
      });

      return wasAdded;
    } catch (error) {
      throw new Error(`Failed to import token: ${error.message}`);
    }
  }

  /**
   * Send a transaction
   * @param {string} to - Recipient address
   * @param {string} value - Amount to send in wei
   * @param {Object} [options] - Additional transaction options
   * @returns {Promise<ethers.providers.TransactionResponse>} Transaction response
   * @throws {Error} If wallet is not connected or transaction fails
   */
  async sendTransaction(to, value, options = {}) {
    if (!this.signer) {
      throw new Error('Wallet is not connected');
    }

    try {
      const tx = await this.signer.sendTransaction({
        to,
        value,
        ...options
      });
      return tx;
    } catch (error) {
      throw new Error(`Transaction failed: ${error.message}`);
    }
  }

  /**
   * Get token balance
   * @param {string} tokenAddress - ERC20 token contract address
   * @returns {Promise<string>} Token balance
   * @throws {Error} If wallet is not connected or balance check fails
   */
  async getTokenBalance(tokenAddress) {
    if (!this.walletAddress) {
      throw new Error('Wallet is not connected');
    }

    try {
      const tokenContract = new ethers.Contract(
        tokenAddress,
        ['function balanceOf(address) view returns (uint256)'],
        this.provider
      );
      const balance = await tokenContract.balanceOf(this.walletAddress);
      return ethers.utils.formatUnits(balance, 18); // Assuming standard 18 decimals
    } catch (error) {
      throw new Error(`Failed to get token balance: ${error.message}`);
    }
  }

  /**
   * Listen for account changes
   * @param {function} callback - Callback function when account changes
   */
  onAccountChanged(callback) {
    if (!this.isMetaMaskInstalled()) return;

    window.ethereum.on('accountsChanged', (accounts) => {
      if (accounts.length === 0) {
        this.walletAddress = null;
        this.signer = null;
      } else {
        this.walletAddress = accounts[0];
        this.signer = this.provider.getSigner();
      }
      callback(accounts);
    });
  }

  /**
   * Listen for chain changes
   * @param {function} callback - Callback function when chain changes
   */
  onChainChanged(callback) {
    if (!this.isMetaMaskInstalled()) return;

    window.ethereum.on('chainChanged', (chainId) => {
      // Reinitialize provider when chain changes
      this.provider = new ethers.providers.Web3Provider(window.ethereum);
      this.signer = this.provider.getSigner();
      callback(chainId);
    });
  }
}

// Example usage:
// const wallet = new MetaMaskWallet();
// await wallet.connectWallet();
// await wallet.importToken('0x...', 'TOKEN', 18);
// const tx = await wallet.sendTransaction('0x...', ethers.utils.parseEther('1.0'));
```
