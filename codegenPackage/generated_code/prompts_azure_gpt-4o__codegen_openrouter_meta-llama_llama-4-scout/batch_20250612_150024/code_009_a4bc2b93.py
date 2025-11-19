"""
Generated Code Metadata:
========================
Original URL: https://zkbridge.pages.dev
Prompt: Provide an example of using zkBridge to enable cross-chain data availability between Ethereum rollups like Arbitrum and Optimism.
Generated: DETERMINISTIC_a4bc2b9321a94973
Batch ID: 20250612_150024
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.optimism.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://arb-mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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

// Define constants for zkBridge configuration
const ZKBridgeAddress = '0x...'; // Replace with zkBridge contract address
const ZKBridgeAbi = [...]; // Replace with zkBridge contract ABI
const EthereumRpcUrl = 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID';
const ArbitrumRpcUrl = 'https://arb-mainnet.infura.io/v3/YOUR_PROJECT_ID';
const OptimismRpcUrl = 'https://mainnet.optimism.io';

// Define a class for zkBridge client
class ZkBridgeClient {
  /**
   * Initialize the zkBridge client with Ethereum providers
   * @param {string} ethereumRpcUrl - Ethereum RPC URL
   * @param {string} arbitrumRpcUrl - Arbitrum RPC URL
   * @param {string} optimismRpcUrl - Optimism RPC URL
   */
  constructor(ethereumRpcUrl, arbitrumRpcUrl, optimismRpcUrl) {
    this.ethereumProvider = new ethers.providers.JsonRpcProvider(ethereumRpcUrl);
    this.arbitrumProvider = new ethers.providers.JsonRpcProvider(arbitrumRpcUrl);
    this.optimismProvider = new ethers.providers.JsonRpcProvider(optimismRpcUrl);
    this.zkBridgeContract = new ethers.Contract(ZKBridgeAddress, ZKBridgeAbi, this.ethereumProvider);
  }

  /**
   * Send a message from Ethereum to Arbitrum using zkBridge
   * @param {string} message - Message to be sent
   */
  async sendMessageToArbitrum(message) {
    try {
      // Get the latest nonce from the zkBridge contract
      const nonce = await this.zkBridgeContract.getNonce();

      // Create a new message with the given message and nonce
      const encodedMessage = ethers.utils.arrayify(message);
      const tx = await this.zkBridgeContract.sendMessageToArbitrum(encodedMessage, nonce);

      // Wait for the transaction to be mined
      await tx.wait();

      console.log(`Message sent to Arbitrum: ${message}`);
    } catch (error) {
      console.error('Error sending message to Arbitrum:', error);
    }
  }

  /**
   * Send a message from Ethereum to Optimism using zkBridge
   * @param {string} message - Message to be sent
   */
  async sendMessageToOptimism(message) {
    try {
      // Get the latest nonce from the zkBridge contract
      const nonce = await this.zkBridgeContract.getNonce();

      // Create a new message with the given message and nonce
      const encodedMessage = ethers.utils.arrayify(message);
      const tx = await this.zkBridgeContract.sendMessageToOptimism(encodedMessage, nonce);

      // Wait for the transaction to be mined
      await tx.wait();

      console.log(`Message sent to Optimism: ${message}`);
    } catch (error) {
      console.error('Error sending message to Optimism:', error);
    }
  }

  /**
   * Verify a message on Arbitrum using zkBridge
   * @param {string} message - Message to be verified
   */
  async verifyMessageOnArbitrum(message) {
    try {
      // Get the proof from the zkBridge contract
      const proof = await this.zkBridgeContract.getProof(message);

      // Verify the proof on Arbitrum
      const arbitrumVerifier = new ethers.Contract('0x...', [...], this.arbitrumProvider);
      const isValid = await arbitrumVerifier.verifyProof(proof);

      if (isValid) {
        console.log(`Message verified on Arbitrum: ${message}`);
      } else {
        console.error(`Invalid proof for message on Arbitrum: ${message}`);
      }
    } catch (error) {
      console.error('Error verifying message on Arbitrum:', error);
    }
  }

  /**
   * Verify a message on Optimism using zkBridge
   * @param {string} message - Message to be verified
   */
  async verifyMessageOnOptimism(message) {
    try {
      // Get the proof from the zkBridge contract
      const proof = await this.zkBridgeContract.getProof(message);

      // Verify the proof on Optimism
      const optimismVerifier = new ethers.Contract('0x...', [...], this.optimismProvider);
      const isValid = await optimismVerifier.verifyProof(proof);

      if (isValid) {
        console.log(`Message verified on Optimism: ${message}`);
      } else {
        console.error(`Invalid proof for message on Optimism: ${message}`);
      }
    } catch (error) {
      console.error('Error verifying message on Optimism:', error);
    }
  }
}

// Example usage
async function main() {
  const zkBridgeClient = new ZkBridgeClient(EthereumRpcUrl, ArbitrumRpcUrl, OptimismRpcUrl);

  // Send a message from Ethereum to Arbitrum
  await zkBridgeClient.sendMessageToArbitrum('Hello, Arbitrum!');

  // Send a message from Ethereum to Optimism
  await zkBridgeClient.sendMessageToOptimism('Hello, Optimism!');

  // Verify a message on Arbitrum
  await zkBridgeClient.verifyMessageOnArbitrum('Hello, Arbitrum!');

  // Verify a message on Optimism
  await zkBridgeClient.verifyMessageOnOptimism('Hello, Optimism!');
}

main().catch((error) => {
  console.error('Error:', error);
});
```
