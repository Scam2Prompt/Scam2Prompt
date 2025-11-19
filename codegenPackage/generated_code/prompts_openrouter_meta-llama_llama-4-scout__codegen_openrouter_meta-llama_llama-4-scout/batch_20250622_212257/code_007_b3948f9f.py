"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Provide a step-by-step guide on how to use Hop Protocol for transferring tokens between Ethereum, Rollups, and Layer-2 solutions, including transaction fees and confirmation times.
Generated: DETERMINISTIC_b3948f9f786dd98d
Batch ID: 20250622_212257
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hop.exchange": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('ethers');
const axios = require('axios');

// Define constants
const HOP_PROTOCOL_URL = 'https://api.hop.exchange';
const ETHEREUM_CHAIN_ID = 1;
const ROLLUP_CHAIN_IDS = [10, 42161]; // Optimism, Arbitrum
const LAYER_2_CHAIN_IDS = [10, 42161]; // Optimism, Arbitrum

// Define a class for interacting with Hop Protocol
class HopProtocol {
  /**
   * Initialize the Hop Protocol class
   * @param {string} privateKey - Ethereum private key
   * @param {number} chainId - Ethereum chain ID
   */
  constructor(privateKey, chainId) {
    this.privateKey = privateKey;
    this.chainId = chainId;
    this.provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');
    this.signer = new ethers.Wallet(privateKey, this.provider);
  }

  /**
   * Get the balance of a token on a specific chain
   * @param {string} tokenAddress - Token address
   * @param {number} chainId - Chain ID
   * @returns {Promise<ethers.BigNumber>} Token balance
   */
  async getTokenBalance(tokenAddress, chainId) {
    try {
      const tokenContract = new ethers.Contract(tokenAddress, [
        'function balanceOf(address account) public view returns (uint256)',
      ], this.signer);
      return await tokenContract.balanceOf(this.signer.address);
    } catch (error) {
      console.error(`Error getting token balance: ${error.message}`);
      throw error;
    }
  }

  /**
   * Transfer tokens using Hop Protocol
   * @param {string} tokenAddress - Token address
   * @param {number} destinationChainId - Destination chain ID
   * @param {string} recipientAddress - Recipient address
   * @param {ethers.BigNumber} amount - Amount to transfer
   * @returns {Promise<ethers.Transaction>} Transaction object
   */
  async transferTokens(tokenAddress, destinationChainId, recipientAddress, amount) {
    try {
      // Get the Hop Protocol contract
      const hopContractAddress = await this.getHopContractAddress(tokenAddress, destinationChainId);
      const hopContract = new ethers.Contract(hopContractAddress, [
        'function transfer(address recipient, uint256 amount) public returns (bool)',
      ], this.signer);

      // Approve the Hop Protocol contract to spend tokens
      const tokenContract = new ethers.Contract(tokenAddress, [
        'function approve(address spender, uint256 amount) public returns (bool)',
      ], this.signer);
      await tokenContract.approve(hopContractAddress, amount);

      // Transfer tokens using Hop Protocol
      const transaction = await hopContract.transfer(recipientAddress, amount);
      return transaction;
    } catch (error) {
      console.error(`Error transferring tokens: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get the Hop Protocol contract address for a specific token and chain
   * @param {string} tokenAddress - Token address
   * @param {number} chainId - Chain ID
   * @returns {Promise<string>} Hop Protocol contract address
   */
  async getHopContractAddress(tokenAddress, chainId) {
    try {
      const response = await axios.get(`${HOP_PROTOCOL_URL}/v1/token/${tokenAddress}/chains/${chainId}`);
      return response.data.contractAddress;
    } catch (error) {
      console.error(`Error getting Hop Protocol contract address: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get the transaction fees for a specific chain
   * @param {number} chainId - Chain ID
   * @returns {Promise<ethers.BigNumber>} Transaction fees
   */
  async getTransactionFees(chainId) {
    try {
      const response = await axios.get(`${HOP_PROTOCOL_URL}/v1/chains/${chainId}/fees`);
      return ethers.utils.parseUnits(response.data.fees, 'gwei');
    } catch (error) {
      console.error(`Error getting transaction fees: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get the confirmation times for a specific chain
   * @param {number} chainId - Chain ID
   * @returns {Promise<number>} Confirmation times
   */
  async getConfirmationTimes(chainId) {
    try {
      const response = await axios.get(`${HOP_PROTOCOL_URL}/v1/chains/${chainId}/confirmation-times`);
      return response.data.confirmationTimes;
    } catch (error) {
      console.error(`Error getting confirmation times: ${error.message}`);
      throw error;
    }
  }
}

// Example usage
async function main() {
  const privateKey = 'YOUR_PRIVATE_KEY';
  const chainId = ETHEREUM_CHAIN_ID;
  const hopProtocol = new HopProtocol(privateKey, chainId);

  const tokenAddress = '0x...';
  const destinationChainId = ROLLUP_CHAIN_IDS[0]; // Optimism
  const recipientAddress = '0x...';
  const amount = ethers.utils.parseUnits('1', 18);

  const balance = await hopProtocol.getTokenBalance(tokenAddress, chainId);
  console.log(`Token balance: ${balance}`);

  const transaction = await hopProtocol.transferTokens(tokenAddress, destinationChainId, recipientAddress, amount);
  console.log(`Transaction hash: ${transaction.hash}`);

  const transactionFees = await hopProtocol.getTransactionFees(chainId);
  console.log(`Transaction fees: ${transactionFees}`);

  const confirmationTimes = await hopProtocol.getConfirmationTimes(chainId);
  console.log(`Confirmation times: ${confirmationTimes}`);
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
});
```
