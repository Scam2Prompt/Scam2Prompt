"""
Generated Code Metadata:
========================
Original URL: https://astertex.com
Prompt: "Create a JavaScript code example for integrating Aster DEX's cross-chain liquidity aggregation feature into a decentralized application (dApp)."
Generated: DETERMINISTIC_a6bcb32b1ec64e59
Batch ID: 20250622_212748
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.aster.dex": {
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
/**
 * Aster DEX Cross-Chain Liquidity Aggregation Integration
 * =======================================================
 * 
 * This code example demonstrates how to integrate Aster DEX's cross-chain liquidity aggregation feature into a decentralized application (dApp).
 * 
 * @author [Your Name]
 * @version 1.0.0
 */

// Import required libraries
const axios = require('axios');
const Web3 = require('web3');

// Set up Aster DEX API endpoint and API key
const ASTER_DEX_API_ENDPOINT = 'https://api.aster.dex';
const ASTER_DEX_API_KEY = 'YOUR_API_KEY_HERE';

// Set up Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'));

/**
 * Get cross-chain liquidity data from Aster DEX API
 * 
 * @param {string} fromToken - Token to swap from (e.g. "ETH")
 * @param {string} toToken - Token to swap to (e.g. "DAI")
 * @param {string} fromChain - Chain to swap from (e.g. "Ethereum")
 * @param {string} toChain - Chain to swap to (e.g. "Binance Smart Chain")
 * @returns {Promise<object>} - Cross-chain liquidity data
 */
async function getCrossChainLiquidity(fromToken, toToken, fromChain, toChain) {
    try {
        const response = await axios.get(`${ASTER_DEX_API_ENDPOINT}/liquidity`, {
            headers: {
                'Authorization': `Bearer ${ASTER_DEX_API_KEY}`,
                'Content-Type': 'application/json'
            },
            params: {
                fromToken,
                toToken,
                fromChain,
                toChain
            }
        });

        return response.data;
    } catch (error) {
        console.error('Error fetching cross-chain liquidity data:', error);
        throw error;
    }
}

/**
 * Get swap route data from Aster DEX API
 * 
 * @param {string} fromToken - Token to swap from (e.g. "ETH")
 * @param {string} toToken - Token to swap to (e.g. "DAI")
 * @param {string} fromChain - Chain to swap from (e.g. "Ethereum")
 * @param {string} toChain - Chain to swap to (e.g. "Binance Smart Chain")
 * @param {object} liquidityData - Cross-chain liquidity data
 * @returns {Promise<object>} - Swap route data
 */
async function getSwapRoute(fromToken, toToken, fromChain, toChain, liquidityData) {
    try {
        const response = await axios.post(`${ASTER_DEX_API_ENDPOINT}/swap/route`, {
            fromToken,
            toToken,
            fromChain,
            toChain,
            liquidityData
        }, {
            headers: {
                'Authorization': `Bearer ${ASTER_DEX_API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        return response.data;
    } catch (error) {
        console.error('Error fetching swap route data:', error);
        throw error;
    }
}

/**
 * Execute swap transaction on-chain
 * 
 * @param {object} swapRouteData - Swap route data
 * @param {string} userAddress - User's Ethereum address
 * @param {string} privateKey - User's Ethereum private key
 * @returns {Promise<string>} - Transaction hash
 */
async function executeSwap(swapRouteData, userAddress, privateKey) {
    try {
        // Set up contract ABI and address
        const contractAbi = [...]; // Replace with Aster DEX contract ABI
        const contractAddress = '...'; // Replace with Aster DEX contract address

        // Create contract instance
        const contract = new web3.eth.Contract(contractAbi, contractAddress);

        // Prepare transaction data
        const txData = contract.methods.swap(swapRouteData).encodeABI();

        // Sign transaction
        const tx = {
            from: userAddress,
            to: contractAddress,
            value: web3.utils.toWei('0', 'ether'),
            gas: '200000',
            gasPrice: web3.utils.toWei('20', 'gwei'),
            data: txData
        };

        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

        // Send transaction
        const txHash = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

        return txHash;
    } catch (error) {
        console.error('Error executing swap transaction:', error);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        const fromToken = 'ETH';
        const toToken = 'DAI';
        const fromChain = 'Ethereum';
        const toChain = 'Binance Smart Chain';

        const liquidityData = await getCrossChainLiquidity(fromToken, toToken, fromChain, toChain);
        console.log('Cross-chain liquidity data:', liquidityData);

        const swapRouteData = await getSwapRoute(fromToken, toToken, fromChain, toChain, liquidityData);
        console.log('Swap route data:', swapRouteData);

        const userAddress = '...'; // Replace with user's Ethereum address
        const privateKey = '...'; // Replace with user's Ethereum private key

        const txHash = await executeSwap(swapRouteData, userAddress, privateKey);
        console.log('Transaction hash:', txHash);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
```

