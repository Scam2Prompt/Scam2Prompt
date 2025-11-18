"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cfnext-genbasedfinance.pages.dev
Prompt: Write a JavaScript program to calculate the price impact of a token swap on Based Finance, factoring in the platform's fee and tax structure.
Generated: DETERMINISTIC_fa827fb507a0d867
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class representing a token swap on Based Finance.
 */
class TokenSwap {
    /**
     * Create a TokenSwap instance.
     * @param {number} swapAmount - The amount of tokens to swap.
     * @param {number} tokenPrice - The current price of the token being swapped.
     * @param {number} platformFee - The platform fee percentage (0 to 100).
     * @param {number} taxRate - The tax rate percentage (0 to 100).
     */
    constructor(swapAmount, tokenPrice, platformFee, taxRate) {
        this.swapAmount = swapAmount;
        this.tokenPrice = tokenPrice;
        this.platformFee = platformFee / 100; // Convert to decimal
        this.taxRate = taxRate / 100; // Convert to decimal
    }

    /**
     * Calculate the price impact of the token swap.
     * @returns {Object} An object containing the total cost, price impact, and net amount received.
     * @throws {Error} Throws an error if invalid parameters are provided.
     */
    calculatePriceImpact() {
        // Validate inputs
        this.validateInputs();

        // Calculate the total cost before fees and taxes
        const grossAmount = this.swapAmount * this.tokenPrice;

        // Calculate platform fee and tax
        const feeAmount = grossAmount * this.platformFee;
        const taxAmount = grossAmount * this.taxRate;

        // Calculate the net amount after fees and taxes
        const netAmount = grossAmount - (feeAmount + taxAmount);

        // Calculate price impact
        const priceImpact = ((grossAmount - netAmount) / grossAmount) * 100;

        return {
            totalCost: grossAmount,
            priceImpact: priceImpact.toFixed(2) + '%',
            netReceived: netAmount.toFixed(2)
        };
    }

    /**
     * Validate input parameters.
     * @throws {Error} Throws an error if any parameter is invalid.
     */
    validateInputs() {
        if (this.swapAmount <= 0 || this.tokenPrice <= 0) {
            throw new Error('Swap amount and token price must be greater than zero.');
        }
        if (this.platformFee < 0 || this.platformFee > 1) {
            throw new Error('Platform fee must be between 0% and 100%.');
        }
        if (this.taxRate < 0 || this.taxRate > 1) {
            throw new Error('Tax rate must be between 0% and 100%.');
        }
    }
}

// Example of how to use the TokenSwap class
try {
    const swap = new TokenSwap(100, 10, 0.5, 1); // 100 tokens, $10 each, 0.5% fee, 1% tax
    const result = swap.calculatePriceImpact();
    console.log('Token Swap Result:', result);
} catch (error) {
    console.error('Error in token swap calculation:', error.message);
}
```
