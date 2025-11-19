"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbsjkqfku.com
Prompt: Explain how to create a custom transaction using DeFi Saver's Recipe Creator that combines multiple DeFi actions in one transaction.
Generated: DETERMINISTIC_a45ad769041c80da
Batch ID: 20250612_162744
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.defisaver.com/recipes/${recipeId}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your.ethereum.node": {
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
// Import necessary libraries
const ethers = require('ethers');
const axios = require('axios');

// Define a class for custom transaction creation
class DeFiTransaction {
    constructor(providerUrl, privateKey) {
        // Initialize provider and wallet
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
    }

    /**
     * Create a custom transaction using DeFi Saver's Recipe Creator
     * @param {string} recipeId - The ID of the recipe to execute
     * @param {number} gasLimit - The gas limit for the transaction
     * @param {number} gasPrice - The gas price for the transaction in Gwei
     * @returns {Promise<string>} - The transaction hash
     */
    async createTransaction(recipeId, gasLimit, gasPrice) {
        try {
            // Fetch the recipe details from DeFi Saver
            const recipe = await this.fetchRecipe(recipeId);
            // Build the transaction payload
            const txData = this.buildTxData(recipe);
            // Create the transaction object
            const tx = {
                to: recipe.contractAddress,
                value: ethers.utils.parseEther(recipe.value.toString()),
                gasLimit: gasLimit,
                gasPrice: ethers.utils.parseUnits(gasPrice.toString(), 'gwei'),
                data: txData,
            };
            // Send the transaction
            const txResponse = await this.wallet.sendTransaction(tx);
            console.log(`Transaction sent: ${txResponse.hash}`);
            // Wait for the transaction to be confirmed
            await txResponse.wait();
            console.log(`Transaction confirmed in block: ${txResponse.blockNumber}`);
            return txResponse.hash;
        } catch (error) {
            console.error('Error creating transaction:', error);
            throw new Error('Transaction creation failed');
        }
    }

    /**
     * Fetch the recipe details from DeFi Saver API
     * @param {string} recipeId - The ID of the recipe to fetch
     * @returns {Promise<Object>} - The recipe details
     */
    async fetchRecipe(recipeId) {
        try {
            const response = await axios.get(`https://api.defisaver.com/recipes/${recipeId}`);
            if (!response.data) {
                throw new Error('Recipe not found');
            }
            return response.data;
        } catch (error) {
            console.error('Error fetching recipe:', error);
            throw new Error('Fetching recipe failed');
        }
    }

    /**
     * Build the transaction data from the recipe
     * @param {Object} recipe - The recipe details
     * @returns {string} - The transaction data in hex format
     */
    buildTxData(recipe) {
        // Assuming the recipe includes a method and parameters for the contract call
        const methodSignature = recipe.methodSignature;
        const parameters = recipe.parameters;
        return ethers.utils.defaultAbiCoder.encode([methodSignature], parameters);
    }
}

// Example usage
(async () => {
    const providerUrl = 'https://your.ethereum.node'; // Replace with your Ethereum node URL
    const privateKey = 'your-private-key'; // Replace with your wallet's private key
    const recipeId = 'your-recipe-id'; // Replace with the recipe ID
    const gasLimit = 300000; // Set the gas limit
    const gasPrice = 100; // Set the gas price in Gwei

    const deFiTx = new DeFiTransaction(providerUrl, privateKey);
    try {
        const txHash = await deFiTx.createTransaction(recipeId, gasLimit, gasPrice);
        console.log(`Transaction hash: ${txHash}`);
    } catch (error) {
        console.error('Transaction execution failed:', error);
    }
})();
```
