"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbridge-site.github.io
Prompt: Provide an example of how to integrate cBridge's multi-chain compatibility into a DeFi application for seamless asset transfers across Ethereum, BNB Chain, and Layer 2 networks.
Generated: DETERMINISTIC_effdf90489e9d8db
Batch ID: 20250612_155048
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cbridge.celer.network/api/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// File: cBridgeIntegration.js

// Import required libraries
const axios = require('axios');

// Constants
const CBRIDGE_API_BASE_URL = 'https://cbridge.celer.network/api/v1';
const SUPPORTED_CHAINS = ['Ethereum', 'BNB Chain', 'Arbitrum', 'Optimism']; // Add Layer 2 networks supported by cBridge

/**
 * Fetch available tokens and chains from cBridge API
 * @returns {Promise<Object>} Supported tokens and chains
 */
async function fetchSupportedAssets() {
  try {
    const response = await axios.get(`${CBRIDGE_API_BASE_URL}/supportedTokens`);
    return response.data;
  } catch (error) {
    console.error('Error fetching supported tokens from cBridge:', error.message);
    throw new Error('Failed to fetch supported tokens.');
  }
}

/**
 * Perform cross-chain asset transfer using cBridge
 * @param {Object} transferDetails Details of the transfer
 * @param {string} transferDetails.sourceChain - The chain sending the assets
 * @param {string} transferDetails.targetChain - The chain receiving the assets
 * @param {string} transferDetails.tokenSymbol - The symbol of the token being transferred
 * @param {string} transferDetails.senderAddress - The address sending the assets
 * @param {string} transferDetails.receiverAddress - The address receiving the assets
 * @param {number} transferDetails.amount - The amount of tokens to transfer
 * @returns {Promise<Object>} Transaction result
 */
async function performCrossChainTransfer(transferDetails) {
  try {
    // Validate input
    const { sourceChain, targetChain, tokenSymbol, senderAddress, receiverAddress, amount } = transferDetails;

    if (!SUPPORTED_CHAINS.includes(sourceChain) || !SUPPORTED_CHAINS.includes(targetChain)) {
      throw new Error(`Unsupported chain: ${sourceChain} or ${targetChain}`);
    }

    if (!sourceChain || !targetChain || !tokenSymbol || !senderAddress || !receiverAddress || !amount) {
      throw new Error('Missing required transfer details.');
    }

    // Prepare transfer request payload
    const payload = {
      srcChain: sourceChain,
      destChain: targetChain,
      tokenSymbol: tokenSymbol,
      sender: senderAddress,
      recipient: receiverAddress,
      amount: amount,
    };

    // Send transfer request to cBridge API
    const response = await axios.post(`${CBRIDGE_API_BASE_URL}/transfer`, payload);

    // Return transaction result
    return response.data;
  } catch (error) {
    console.error('Error performing cross-chain transfer:', error.message);
    throw new Error('Failed to perform cross-chain transfer.');
  }
}

/**
 * Example usage of cBridge integration in a DeFi application
 */
async function main() {
  try {
    // Fetch supported assets
    const supportedAssets = await fetchSupportedAssets();
    console.log('Supported Tokens and Chains:', supportedAssets);

    // Define transfer details
    const transferDetails = {
      sourceChain: 'Ethereum',
      targetChain: 'BNB Chain',
      tokenSymbol: 'USDT',
      senderAddress: '0xSenderAddressHere',
      receiverAddress: '0xReceiverAddressHere',
      amount: 100, // Amount to transfer in token's smallest unit
    };

    // Perform asset transfer
    const transactionResult = await performCrossChainTransfer(transferDetails);
    console.log('Transaction Result:', transactionResult);
  } catch (error) {
    console.error('Error in main function:', error.message);
  }
}

// Call main function to demonstrate functionality
main();

```

### Notes:
- Replace `'0xSenderAddressHere'` and `'0xReceiverAddressHere'` with actual wallet addresses.
- You will likely need to integrate wallet signing and authentication (e.g., using web3.js or ethers.js) for production use.
- Make sure to use secure practices for handling sensitive data like private keys.
