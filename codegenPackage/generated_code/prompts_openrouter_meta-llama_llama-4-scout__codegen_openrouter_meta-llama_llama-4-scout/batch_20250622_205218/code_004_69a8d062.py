"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-fix-scw-signers-offchain-labs.vercel.app
Prompt: Create a code example for using the Arbitrum token bridge with off-chain signers, leveraging the site's specific implementation.
Generated: DETERMINISTIC_69a8d06257ebf34d
Batch ID: 20250622_205218
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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

// Define Arbitrum token bridge contract ABI
const arbitrumTokenBridgeAbi = [
  // Add ABI definitions here
];

// Define off-chain signer class
class OffChainSigner {
  /**
   * Initialize off-chain signer
   * @param {string} privateKey - Private key for signing
   */
  constructor(privateKey) {
    this.privateKey = privateKey;
    this.signer = new ethers.Wallet(privateKey);
  }

  /**
   * Sign a message
   * @param {string} message - Message to sign
   * @returns {Promise<string>} Signed message
   */
  async signMessage(message) {
    return this.signer.signMessage(message);
  }
}

// Define Arbitrum token bridge class
class ArbitrumTokenBridge {
  /**
   * Initialize Arbitrum token bridge
   * @param {string} contractAddress - Contract address of Arbitrum token bridge
   * @param {ethers.Provider} provider - Ethereum provider
   */
  constructor(contractAddress, provider) {
    this.contractAddress = contractAddress;
    this.provider = provider;
    this.contract = new ethers.Contract(contractAddress, arbitrumTokenBridgeAbi, provider);
  }

  /**
   * Get token bridge status
   * @returns {Promise<object>} Token bridge status
   */
  async getTokenBridgeStatus() {
    try {
      return await this.contract.getTokenBridgeStatus();
    } catch (error) {
      console.error('Error getting token bridge status:', error);
      throw error;
    }
  }

  /**
   * Initiate token transfer
   * @param {string} recipient - Recipient address
   * @param {string} tokenAddress - Token address
   * @param {ethers.BigNumber} amount - Amount to transfer
   * @param {OffChainSigner} offChainSigner - Off-chain signer
   * @returns {Promise<string>} Transaction hash
   */
  async initiateTokenTransfer(recipient, tokenAddress, amount, offChainSigner) {
    try {
      const message = `Transfer ${amount} tokens to ${recipient}`;
      const signature = await offChainSigner.signMessage(message);
      return await this.contract.initiateTokenTransfer(recipient, tokenAddress, amount, signature);
    } catch (error) {
      console.error('Error initiating token transfer:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  // Set up Ethereum provider
  const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');

  // Set up off-chain signer
  const privateKey = 'YOUR_PRIVATE_KEY';
  const offChainSigner = new OffChainSigner(privateKey);

  // Set up Arbitrum token bridge
  const contractAddress = '0x...';
  const arbitrumTokenBridge = new ArbitrumTokenBridge(contractAddress, provider);

  // Get token bridge status
  const status = await arbitrumTokenBridge.getTokenBridgeStatus();
  console.log('Token bridge status:', status);

  // Initiate token transfer
  const recipient = '0x...';
  const tokenAddress = '0x...';
  const amount = ethers.utils.parseEther('1.0');
  const txHash = await arbitrumTokenBridge.initiateTokenTransfer(recipient, tokenAddress, amount, offChainSigner);
  console.log('Transaction hash:', txHash);
}

main().catch((error) => {
  console.error('Error:', error);
  process.exit(1);
});
```
