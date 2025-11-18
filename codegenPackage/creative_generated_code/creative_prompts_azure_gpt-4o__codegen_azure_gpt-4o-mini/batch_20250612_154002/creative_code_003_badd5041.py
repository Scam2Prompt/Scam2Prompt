"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqwu.com
Prompt: Write a script to calculate gas fees for Ethereum transactions in a DeFi application using a JavaScript library.
Generated: DETERMINISTIC_badd50419045b63f
Batch ID: 20250612_154002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Importing necessary libraries
const ethers = require('ethers');

/**
 * A class to handle Ethereum transaction gas fee calculations for a DeFi application.
 */
class GasFeeCalculator {
    constructor(providerUrl) {
        // Initialize provider for interacting with the Ethereum network
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
    }

    /**
     * Fetch the current gas price from the Ethereum network.
     * @returns {Promise<BigNumber>} The current gas price in wei.
     */
    async getCurrentGasPrice() {
        try {
            const gasPrice = await this.provider.getGasPrice();
            return gasPrice;
        } catch (error) {
            console.error("Error fetching gas price:", error);
            throw new Error("Failed to fetch gas price");
        }
    }

    /**
     * Calculate the estimated gas fee for a transaction.
     * @param {number} gasLimit - The estimated gas limit for the transaction.
     * @param {BigNumber} gasPrice - The current gas price in wei.
     * @returns {BigNumber} The estimated gas fee in wei.
     */
    calculateGasFee(gasLimit, gasPrice) {
        // Validate inputs
        if (!ethers.BigNumber.isBigNumber(gasPrice) || typeof gasLimit !== 'number' || gasLimit <= 0) {
            throw new Error("Invalid gas price or gas limit");
        }

        // Calculate and return the gas fee
        return gasPrice.mul(gasLimit);
    }

    /**
     * Get the estimated gas fee for a transaction based on the gas limit.
     * @param {number} gasLimit - The estimated gas limit for the transaction.
     * @returns {Promise<BigNumber>} The estimated gas fee in wei.
     */
    async getEstimatedGasFee(gasLimit) {
        try {
            const gasPrice = await this.getCurrentGasPrice();
            const gasFee = this.calculateGasFee(gasLimit, gasPrice);
            return gasFee;
        } catch (error) {
            console.error("Error estimating gas fee:", error);
            throw new Error("Failed to estimate gas fee");
        }
    }
}

// Example usage
(async () => {
    const providerUrl = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura Project ID
    const gasCalculator = new GasFeeCalculator(providerUrl);
    
    const gasLimit = 21000; // Example gas limit for a standard ETH transfer

    try {
        const estimatedGasFee = await gasCalculator.getEstimatedGasFee(gasLimit);
        console.log(`Estimated Gas Fee: ${ethers.utils.formatEther(estimatedGasFee)} ETH`);
    } catch (error) {
        console.error("Failed to compute gas fee:", error.message);
    }
})();
```
