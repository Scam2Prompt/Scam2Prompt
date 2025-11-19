"""
Generated Code Metadata:
========================
Original URL: https://ethphbi.com
Prompt: Write code to handle Ethereum gas fee calculations for a pledge system using JavaScript and Web3.js.
Generated: DETERMINISTIC_cc9e08b329762387
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const Web3 = require('web3');

/**
 * Ethereum Gas Fee Calculator for Pledge System
 */
class GasFeeCalculator {
    /**
     * Initialize the GasFeeCalculator with a Web3 provider
     * @param {string} providerUrl - Ethereum node URL (e.g., Infura, Alchemy)
     */
    constructor(providerUrl) {
        if (!providerUrl) {
            throw new Error('Provider URL is required');
        }
        this.web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));
    }

    /**
     * Get current gas price in wei
     * @returns {Promise<string>} Current gas price in wei
     */
    async getCurrentGasPrice() {
        try {
            const gasPrice = await this.web3.eth.getGasPrice();
            return gasPrice;
        } catch (error) {
            throw new Error(`Failed to fetch gas price: ${error.message}`);
        }
    }

    /**
     * Estimate gas for a transaction
     * @param {Object} txParams - Transaction parameters
     * @param {string} txParams.from - Sender address
     * @param {string} txParams.to - Recipient address (contract address for pledges)
     * @param {string} txParams.data - Transaction data (ABI-encoded)
     * @returns {Promise<number>} Estimated gas limit
     */
    async estimateGas(txParams) {
        if (!txParams || !txParams.from || !txParams.to || !txParams.data) {
            throw new Error('Invalid transaction parameters');
        }

        try {
            const gasLimit = await this.web3.eth.estimateGas(txParams);
            return gasLimit;
        } catch (error) {
            throw new Error(`Failed to estimate gas: ${error.message}`);
        }
    }

    /**
     * Calculate total transaction cost in ETH
     * @param {string} gasPrice - Gas price in wei
     * @param {number} gasLimit - Gas limit
     * @returns {string} Total cost in ETH
     */
    calculateTransactionCost(gasPrice, gasLimit) {
        if (!gasPrice || !gasLimit) {
            throw new Error('Gas price and gas limit are required');
        }

        try {
            const costWei = this.web3.utils.toBN(gasPrice).mul(this.web3.utils.toBN(gasLimit));
            return this.web3.utils.fromWei(costWei, 'ether');
        } catch (error) {
            throw new Error(`Failed to calculate transaction cost: ${error.message}`);
        }
    }

    /**
     * Get recommended gas parameters for a pledge transaction
     * @param {Object} txParams - Transaction parameters
     * @returns {Promise<Object>} Gas parameters { gasPrice, gasLimit, costETH }
     */
    async getRecommendedGasParameters(txParams) {
        try {
            const [gasPrice, gasLimit] = await Promise.all([
                this.getCurrentGasPrice(),
                this.estimateGas(txParams)
            ]);

            const costETH = this.calculateTransactionCost(gasPrice, gasLimit);

            return {
                gasPrice,
                gasLimit,
                costETH
            };
        } catch (error) {
            throw new Error(`Failed to get gas parameters: ${error.message}`);
        }
    }
}

module.exports = GasFeeCalculator;
```
