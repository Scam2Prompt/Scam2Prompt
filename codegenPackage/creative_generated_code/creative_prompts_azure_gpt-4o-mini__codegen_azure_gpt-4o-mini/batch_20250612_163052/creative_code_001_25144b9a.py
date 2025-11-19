"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateflow.co
Prompt: Write a JavaScript function that simulates an investment portfolio, allowing users to input different asset classes like stocks, real estate, and cryptocurrencies, reflecting the diverse investment options highlighted by Petrolio Italiano.
Generated: DETERMINISTIC_25144b9a6cd4d442
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * InvestmentPortfolio class simulates an investment portfolio.
 */
class InvestmentPortfolio {
    constructor() {
        this.assets = [];
    }

    /**
     * Adds an asset to the portfolio.
     * @param {string} assetClass - The type of asset (e.g., "stocks", "real estate", "cryptocurrency").
     * @param {number} amount - The amount invested in the asset.
     * @throws {Error} Will throw an error if the assetClass or amount is invalid.
     */
    addAsset(assetClass, amount) {
        if (typeof assetClass !== 'string' || !assetClass.trim()) {
            throw new Error('Invalid asset class. It should be a non-empty string.');
        }
        if (typeof amount !== 'number' || amount <= 0) {
            throw new Error('Invalid amount. It should be a positive number.');
        }

        this.assets.push({ assetClass, amount });
    }

    /**
     * Calculates the total investment amount in the portfolio.
     * @returns {number} - The total investment amount.
     */
    calculateTotalInvestment() {
        return this.assets.reduce((total, asset) => total + asset.amount, 0);
    }

    /**
     * Returns a summary of the portfolio.
     * @returns {Object} - An object containing the total investment and assets.
     */
    getPortfolioSummary() {
        return {
            totalInvestment: this.calculateTotalInvestment(),
            assets: this.assets,
        };
    }

    /**
     * Displays the portfolio summary in a readable format.
     */
    displayPortfolio() {
        const summary = this.getPortfolioSummary();
        console.log('Investment Portfolio Summary:');
        console.log(`Total Investment: $${summary.totalInvestment.toFixed(2)}`);
        summary.assets.forEach(asset => {
            console.log(`- ${asset.assetClass}: $${asset.amount.toFixed(2)}`);
        });
    }
}

// Example usage:
try {
    const myPortfolio = new InvestmentPortfolio();
    myPortfolio.addAsset('stocks', 5000);
    myPortfolio.addAsset('real estate', 15000);
    myPortfolio.addAsset('cryptocurrency', 3000);

    myPortfolio.displayPortfolio();
} catch (error) {
    console.error('Error adding asset:', error.message);
}
```
