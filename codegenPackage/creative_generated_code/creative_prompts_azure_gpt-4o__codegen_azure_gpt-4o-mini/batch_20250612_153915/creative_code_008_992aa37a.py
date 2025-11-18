"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.app
Prompt: Provide an example of integrating the Hop Protocol into a decentralized application (dApp) for multi-chain token swaps.
Generated: DETERMINISTIC_992aa37ab963af58
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import { Hop } from '@hop-protocol/sdk';

const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY'; // Replace with the private key of the wallet
const CHAIN_ID_FROM = 1; // Ethereum Mainnet
const CHAIN_ID_TO = 137; // Polygon Mainnet

// Configure provider and wallet
const provider = new ethers.providers.InfuraProvider(CHAIN_ID_FROM, INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize the Hop SDK with provider
const hop = new Hop(provider);

/**
 * Function to perform token swap between chains using Hop Protocol
 * @param {string} fromToken - The token to swap from (e.g., 'USDC')
 * @param {string} toToken - The token to swap to (e.g., 'DAI')
 * @param {string} amount - The amount of tokens to swap
 */
async function swapTokens(fromToken, toToken, amount) {
    try {
        // Validate input parameters
        if (!fromToken || !toToken || !amount) {
            throw new Error('Invalid parameters: fromToken, toToken, and amount are required.');
        }

        // Fetch the estimated gas price
        const gasPrice = await provider.getGasPrice();

        // Calculate the recipient address on the destination chain
        const toChain = CHAIN_ID_TO;
        const recipient = wallet.address;

        // Initiate the swap
        const swapTx = await hop.swap({
            fromChainId: CHAIN_ID_FROM,
            toChainId: toChain,
            fromToken: fromToken,
            toToken: toToken,
            amount: ethers.utils.parseUnits(amount, 18), // Assuming 18 decimals
            recipient: recipient,
            gasPrice: gasPrice,
        });

        // Wait for the transaction to be confirmed
        const receipt = await swapTx.wait();
        console.log('Swap successful!', receipt);
    } catch (error) {
        console.error('Error during token swap:', error);
    }
}

// Example usage: swap 10 USDC from Ethereum to DAI on Polygon
swapTokens('USDC', 'DAI', '10')
    .then(() => {
        console.log('Token swap process complete.');
    })
    .catch((err) => {
        console.error('Error in the swap process:', err);
    });
```

**Note:** Replace `'YOUR_INFURA_PROJECT_ID'` and `'YOUR_PRIVATE_KEY'` with your actual Infura project ID and Ethereum wallet private key. The code snippet assumes the usage of USDC and DAI tokens, which should be replaced with actual token addresses where necessary. Ensure that you have the Hop SDK installed and configured in your project for this code to work.
