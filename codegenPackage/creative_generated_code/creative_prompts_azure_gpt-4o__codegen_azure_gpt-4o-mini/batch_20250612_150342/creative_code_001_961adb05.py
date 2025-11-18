"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-wallet-demo.vercel.app
Prompt: Create a JavaScript function to track costs for tokens, NFTs, DeFi, and gas fees, inspired by the features outlined on the MetaMask Wallet Demo site.
Generated: DETERMINISTIC_961adb05d2ba984f
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * TokenCostTracker is a class that helps in tracking costs for tokens, NFTs, DeFi investments, and gas fees.
 * It provides methods to add costs, get total costs, and generate a summary report.
 */
class TokenCostTracker {
    constructor() {
        this.costs = {
            tokens: 0,
            nfts: 0,
            defi: 0,
            gasFees: 0,
        };
    }

    /**
     * Adds a cost to the specified category.
     * @param {string} category - The category to which the cost belongs ('tokens', 'nfts', 'defi', 'gasFees').
     * @param {number} amount - The amount to add to the category.
     * @throws {Error} Throws an error if the category is invalid or amount is negative.
     */
    addCost(category, amount) {
        if (!(category in this.costs)) {
            throw new Error(`Invalid category: ${category}. Valid categories are: tokens, nfts, defi, gasFees.`);
        }
        if (amount < 0) {
            throw new Error(`Amount cannot be negative: ${amount}`);
        }
        this.costs[category] += amount;
    }

    /**
     * Returns the total cost across all categories.
     * @returns {number} The total cost.
     */
    getTotalCost() {
        return Object.values(this.costs).reduce((total, cost) => total + cost, 0);
    }

    /**
     * Generates a summary report of costs per category.
     * @returns {object} An object containing the costs per category and the total cost.
     */
    generateReport() {
        const totalCost = this.getTotalCost();
        return {
            ...this.costs,
            totalCost,
        };
    }
}

// Usage example
try {
    const tracker = new TokenCostTracker();
    tracker.addCost('tokens', 100);
    tracker.addCost('nfts', 200);
    tracker.addCost('defi', 50);
    tracker.addCost('gasFees', 5);
    
    const report = tracker.generateReport();
    console.log(report);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
