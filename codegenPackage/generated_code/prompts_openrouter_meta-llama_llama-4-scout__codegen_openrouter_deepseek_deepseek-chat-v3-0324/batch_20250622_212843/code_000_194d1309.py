"""
Generated Code Metadata:
========================
Original URL: https://ethbvt.com
Prompt: Write a JavaScript function to enable and handle pledge functionality for an Ethereum-based project.
Generated: DETERMINISTIC_194d1309a7893293
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * @file PledgeHandler.js
 * @description Handles pledge functionality for an Ethereum-based project.
 * @version 1.0.0
 * @license MIT
 */

const ethers = require('ethers');
const { abi } = require('./PledgeContractABI.json');

class PledgeHandler {
  /**
   * Initialize the PledgeHandler with provider and contract details
   * @param {Object} config - Configuration object
   * @param {string} config.contractAddress - The deployed contract address
   * @param {ethers.providers.Provider} config.provider - Ethers provider instance
   * @param {string} [config.chainId] - Chain ID for network validation
   */
  constructor(config) {
    if (!config.contractAddress || !config.provider) {
      throw new Error('Missing required configuration parameters');
    }

    this.contractAddress = config.contractAddress;
    this.provider = config.provider;
    this.chainId = config.chainId;
    this.contract = new ethers.Contract(
      this.contractAddress,
      abi,
      this.provider
    );
  }

  /**
   * Connect a signer to the contract for write operations
   * @param {ethers.Signer} signer - Ethers signer instance
   */
  connectSigner(signer) {
    if (!signer) {
      throw new Error('Signer is required');
    }
    this.contract = this.contract.connect(signer);
  }

  /**
   * Make a pledge to the project
   * @param {string} amount - Amount to pledge in ETH
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async makePledge(amount) {
    if (!amount || isNaN(amount)) {
      throw new Error('Invalid pledge amount');
    }

    try {
      const tx = await this.contract.pledge({
        value: ethers.utils.parseEther(amount.toString())
      });
      return await tx.wait();
    } catch (error) {
      console.error('Pledge failed:', error);
      throw new Error(`Pledge transaction failed: ${error.message}`);
    }
  }

  /**
   * Get total pledged amount in ETH
   * @returns {Promise<string>} Total pledged amount
   */
  async getTotalPledged() {
    try {
      const total = await this.contract.totalPledged();
      return ethers.utils.formatEther(total);
    } catch (error) {
      console.error('Failed to get total pledged:', error);
      throw new Error(`Failed to fetch total pledged: ${error.message}`);
    }
  }

  /**
   * Get user's pledge amount in ETH
   * @param {string} address - User's Ethereum address
   * @returns {Promise<string>} User's pledged amount
   */
  async getUserPledge(address) {
    if (!ethers.utils.isAddress(address)) {
      throw new Error('Invalid Ethereum address');
    }

    try {
      const pledge = await this.contract.userPledges(address);
      return ethers.utils.formatEther(pledge);
    } catch (error) {
      console.error('Failed to get user pledge:', error);
      throw new Error(`Failed to fetch user pledge: ${error.message}`);
    }
  }

  /**
   * Withdraw pledge (only callable by contract owner)
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async withdrawPledge() {
    try {
      const tx = await this.contract.withdraw();
      return await tx.wait();
    } catch (error) {
      console.error('Withdrawal failed:', error);
      throw new Error(`Withdrawal transaction failed: ${error.message}`);
    }
  }

  /**
   * Listen for pledge events
   * @param {Function} callback - Callback function to handle events
   * @returns {void}
   */
  onPledgeEvent(callback) {
    if (typeof callback !== 'function') {
      throw new Error('Callback must be a function');
    }

    this.contract.on('Pledged', (user, amount, event) => {
      callback({
        user,
        amount: ethers.utils.formatEther(amount),
        event
      });
    });
  }

  /**
   * Remove all event listeners
   */
  removeAllListeners() {
    this.contract.removeAllListeners();
  }
}

module.exports = PledgeHandler;
```
