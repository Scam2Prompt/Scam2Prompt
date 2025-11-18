"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap-dev-git-feat-wagmi-8-cowswap.vercel.app
Prompt: Generate a JavaScript script to calculate transaction costs and slippage for trades executed via CoW Swap.
Generated: DETERMINISTIC_4bd64bb3d25e18cc
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * CoW Swap Transaction Cost and Slippage Calculator
 * This script calculates the transaction costs and slippage for trades executed via CoW Swap.
 */

class CoWSwapCalculator {
    /**
     * @param {number} tradeAmount - The amount to be traded.
     * @param {number} marketPrice - The current market price of the asset.
     * @param {number} expectedPrice - The price expected for the trade.
     * @param {number} feePercentage - The transaction fee percentage (e.g., 0.01 for 1%).
     */
    constructor(tradeAmount, marketPrice, expectedPrice, feePercentage) {
        this.tradeAmount = tradeAmount;
        this.marketPrice = marketPrice;
        this.expectedPrice = expectedPrice;
        this.feePercentage = feePercentage;
    }

    /**
     * Calculate the transaction cost based on the trade amount and fee percentage.
     * @returns {number} The transaction cost.
     */
    calculateTransactionCost() {
        try {
            if (this.feePercentage < 0 || this.feePercentage > 1) {
                throw new Error('Fee percentage must be between 0 and 1.');
            }
            const transactionCost = this.tradeAmount * this.feePercentage;
            return transactionCost;
        } catch (error) {
            console.error('Error calculating transaction cost:', error.message);
            return 0;
        }
    }

    /**
     * Calculate the slippage based on the market price and expected price.
     * @returns {number} The slippage percentage.
     */
    calculateSlippage() {
        try {
            if (this.marketPrice <= 0 || this.expectedPrice <= 0) {
                throw new Error('Market price and expected price must be greater than zero.');
            }
            const slippage = ((this.expectedPrice - this.marketPrice) / this.marketPrice) * 100;
            return slippage;
        } catch (error) {
            console.error('Error calculating slippage:', error.message);
            return 0;
        }
    }

    /**
     * Get a summary of the transaction details, including costs and slippage.
     * @returns {Object} An object containing transaction cost and slippage.
     */
    getTransactionSummary() {
        const transactionCost = this.calculateTransactionCost();
        const slippage = this.calculateSlippage();

        return {
            transactionCost: transactionCost.toFixed(2),
            slippage: slippage.toFixed(2) + '%'
        };
    }
}

// Example usage:
const tradeAmount = 1000; // Trade amount in asset's base unit
const marketPrice = 50;    // Current market price
const expectedPrice = 52;  // Expected price for the trade
const feePercentage = 0.01; // 1% transaction fee

const swapCalculator = new CoWSwapCalculator(tradeAmount, marketPrice, expectedPrice, feePercentage);
const summary = swapCalculator.getTransactionSummary();

console.log('Transaction Summary:', summary);
```
