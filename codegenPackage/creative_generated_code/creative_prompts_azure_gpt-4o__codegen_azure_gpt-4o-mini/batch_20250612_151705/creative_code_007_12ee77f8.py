"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unionswap.app
Prompt: Explain how to integrate UnionSwap's asset bridging service into a Web3 wallet application.
Generated: DETERMINISTIC_12ee77f8d1caa487
Batch ID: 20250612_151705
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-provider-url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.unionswap.org": {
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
// web3-wallet.js
// This script integrates UnionSwap's asset bridging service into a Web3 wallet application.

import Web3 from 'web3';
import axios from 'axios';

// Configuration for UnionSwap's API
const UNION_SWAP_API_URL = 'https://api.unionswap.org'; // Replace with the actual API endpoint

/**
 * Initialize Web3 instance
 * @param {string} providerUrl - The URL of the Web3 provider (e.g., Infura, Alchemy)
 * @returns {Web3} - An instance of Web3
 */
function initWeb3(providerUrl) {
    if (!providerUrl) {
        throw new Error('Provider URL is required to initialize Web3.');
    }
    const web3 = new Web3(providerUrl);
    return web3;
}

/**
 * Fetch asset bridge data from UnionSwap API
 * @param {string} fromAsset - The asset to be bridged from
 * @param {string} toAsset - The asset to be bridged to
 * @param {number} amount - The amount to be bridged
 * @returns {Promise<Object>} - The response from the UnionSwap API
 */
async function fetchBridgeData(fromAsset, toAsset, amount) {
    if (!fromAsset || !toAsset || !amount) {
        throw new Error('From asset, to asset, and amount are required.');
    }

    try {
        const response = await axios.get(`${UNION_SWAP_API_URL}/bridge`, {
            params: {
                from: fromAsset,
                to: toAsset,
                amount: amount,
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching bridge data:', error);
        throw new Error('Failed to fetch bridge data from UnionSwap.');
    }
}

/**
 * Execute asset bridging through UnionSwap
 * @param {string} userWalletAddress - The user's wallet address
 * @param {string} fromAsset - The asset to be bridged from
 * @param {string} toAsset - The asset to be bridged to
 * @param {number} amount - The amount to be bridged
 * @param {Web3} web3 - An instance of Web3
 * @returns {Promise<Object>} - Transaction receipt
 */
async function executeAssetBridge(userWalletAddress, fromAsset, toAsset, amount, web3) {
    if (!userWalletAddress || !fromAsset || !toAsset || !amount || !web3) {
        throw new Error('All parameters are required to execute asset bridge.');
    }

    const bridgeData = await fetchBridgeData(fromAsset, toAsset, amount);

    const transactionParameters = {
        to: bridgeData.contractAddress, // Contract address to which the transaction will be sent
        from: userWalletAddress,
        value: web3.utils.toWei(amount.toString(), 'ether'), // Convert amount to Wei
        data: bridgeData.methodData, // Data for the transaction from the bridge response
    };

    try {
        const txHash = await web3.eth.sendTransaction(transactionParameters);
        return txHash; // Return transaction receipt
    } catch (error) {
        console.error('Error executing asset bridge:', error);
        throw new Error('Transaction failed.');
    }
}

// Example usage
(async () => {
    const PROVIDER_URL = 'https://your-provider-url'; // Replace with your provider URL
    const web3 = initWeb3(PROVIDER_URL);

    const userWalletAddress = '0xYourWalletAddress'; // Replace with the user's wallet address
    const fromAsset = 'ETH'; // Asset to bridge from
    const toAsset = 'USDC'; // Asset to bridge to
    const amount = 0.1; // Amount to bridge

    try {
        const txReceipt = await executeAssetBridge(userWalletAddress, fromAsset, toAsset, amount, web3);
        console.log('Transaction successful with receipt:', txReceipt);
    } catch (error) {
        console.error('Error in bridging assets:', error.message);
    }
})();
```
