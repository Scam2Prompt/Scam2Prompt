"""
Generated Code Metadata:
========================
Original URL: https://123-7bf.pages.dev
Prompt: Generate a code example for implementing a token bridge solution using Web3.js and Ethers.js, ensuring seamless transfers between different blockchain networks.
Generated: DETERMINISTIC_30c87da05597834b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// TokenBridge.js - A cross-chain token bridge implementation using Web3.js and Ethers.js

const Web3 = require('web3');
const { ethers } = require('ethers');
const { abi: bridgeAbi } = require('./BridgeContract.json');
const { abi: tokenAbi } = require('./ERC20Token.json');

class TokenBridge {
  /**
   * Initialize TokenBridge with network configurations
   * @param {Object} config - Configuration object
   * @param {Object} config.sourceNetwork - Source network details
   * @param {Object} config.destinationNetwork - Destination network details
   */
  constructor(config) {
    this.validateConfig(config);
    
    this.sourceNetwork = {
      web3: new Web3(config.sourceNetwork.rpcUrl),
      bridgeAddress: config.sourceNetwork.bridgeAddress,
      tokenAddress: config.sourceNetwork.tokenAddress,
      chainId: config.sourceNetwork.chainId
    };
    
    this.destinationNetwork = {
      provider: new ethers.providers.JsonRpcProvider(config.destinationNetwork.rpcUrl),
      bridgeAddress: config.destinationNetwork.bridgeAddress,
      tokenAddress: config.destinationNetwork.tokenAddress,
      chainId: config.destinationNetwork.chainId
    };
    
    this.sourceBridgeContract = new this.sourceNetwork.web3.eth.Contract(
      bridgeAbi,
      this.sourceNetwork.bridgeAddress
    );
    
    this.sourceTokenContract = new this.sourceNetwork.web3.eth.Contract(
      tokenAbi,
      this.sourceNetwork.tokenAddress
    );
    
    this.destinationBridgeContract = new ethers.Contract(
      this.destinationNetwork.bridgeAddress,
      bridgeAbi,
      this.destinationNetwork.provider
    );
  }

  /**
   * Validate configuration object
   * @param {Object} config - Configuration to validate
   */
  validateConfig(config) {
    if (!config.sourceNetwork || !config.destinationNetwork) {
      throw new Error('Both source and destination networks must be configured');
    }
    
    const requiredFields = ['rpcUrl', 'bridgeAddress', 'tokenAddress', 'chainId'];
    for (const field of requiredFields) {
      if (!config.sourceNetwork[field] || !config.destinationNetwork[field]) {
        throw new Error(`Missing required field: ${field}`);
      }
    }
  }

  /**
   * Approve token transfer to bridge contract
   * @param {string} privateKey - Sender's private key
   * @param {string} amount - Amount to approve (in wei)
   * @returns {Promise<string>} Transaction hash
   */
  async approveTokenTransfer(privateKey, amount) {
    try {
      const account = this.sourceNetwork.web3.eth.accounts.privateKeyToAccount(privateKey);
      this.sourceNetwork.web3.eth.accounts.wallet.add(account);
      
      const tx = this.sourceTokenContract.methods.approve(
        this.sourceNetwork.bridgeAddress,
        amount
      );
      
      const gas = await tx.estimateGas({ from: account.address });
      const gasPrice = await this.sourceNetwork.web3.eth.getGasPrice();
      
      const txData = {
        from: account.address,
        gas,
        gasPrice
      };
      
      const receipt = await tx.send(txData);
      return receipt.transactionHash;
    } catch (error) {
      console.error('Error approving token transfer:', error);
      throw new Error('Failed to approve token transfer');
    }
  }

  /**
   * Lock tokens on source chain to bridge to destination chain
   * @param {string} privateKey - Sender's private key
   * @param {string} amount - Amount to lock (in wei)
   * @param {string} recipient - Recipient address on destination chain
   * @returns {Promise<string>} Transaction hash
   */
  async lockTokens(privateKey, amount, recipient) {
    try {
      const account = this.sourceNetwork.web3.eth.accounts.privateKeyToAccount(privateKey);
      this.sourceNetwork.web3.eth.accounts.wallet.add(account);
      
      const tx = this.sourceBridgeContract.methods.lockTokens(
        this.sourceNetwork.tokenAddress,
        amount,
        this.destinationNetwork.chainId,
        recipient
      );
      
      const gas = await tx.estimateGas({ from: account.address });
      const gasPrice = await this.sourceNetwork.web3.eth.getGasPrice();
      
      const txData = {
        from: account.address,
        gas,
        gasPrice
      };
      
      const receipt = await tx.send(txData);
      return receipt.transactionHash;
    } catch (error) {
      console.error('Error locking tokens:', error);
      throw new Error('Failed to lock tokens');
    }
  }

  /**
   * Claim tokens on destination chain after they've been locked on source chain
   * @param {string} privateKey - Recipient's private key
   * @param {string} txHash - Transaction hash from lockTokens
   * @returns {Promise<string>} Transaction hash
   */
  async claimTokens(privateKey, txHash) {
    try {
      const wallet = new ethers.Wallet(privateKey, this.destinationNetwork.provider);
      const bridgeWithSigner = this.destinationBridgeContract.connect(wallet);
      
      const tx = await bridgeWithSigner.claimTokens(
        txHash,
        this.destinationNetwork.tokenAddress
      );
      
      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error('Error claiming tokens:', error);
      throw new Error('Failed to claim tokens');
    }
  }

  /**
   * Get token balance on source chain
   * @param {string} address - Wallet address
   * @returns {Promise<string>} Token balance (in wei)
   */
  async getSourceBalance(address) {
    try {
      return await this.sourceTokenContract.methods.balanceOf(address).call();
    } catch (error) {
      console.error('Error getting source balance:', error);
      throw new Error('Failed to get source balance');
    }
  }

  /**
   * Get token balance on destination chain
   * @param {string} address - Wallet address
   * @returns {Promise<string>} Token balance (in wei)
   */
  async getDestinationBalance(address) {
    try {
      const tokenContract = new ethers.Contract(
        this.destinationNetwork.tokenAddress,
        tokenAbi,
        this.destinationNetwork.provider
      );
      return await tokenContract.balanceOf(address);
    } catch (error) {
      console.error('Error getting destination balance:', error);
      throw new Error('Failed to get destination balance');
    }
  }
}

module.exports = TokenBridge;
```
