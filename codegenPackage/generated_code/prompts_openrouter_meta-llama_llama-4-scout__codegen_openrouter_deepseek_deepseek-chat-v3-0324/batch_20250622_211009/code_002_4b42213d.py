"""
Generated Code Metadata:
========================
Original URL: https://jellydrop.web.app
Prompt: Generate JavaScript code for a simple Jelly Drop trading simulator.
Generated: DETERMINISTIC_4b42213d91ffdc17
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Jelly Drop Trading Simulator
 * Simulates buying and selling jelly drops with price fluctuations.
 */

class JellyDropSimulator {
    /**
     * Initialize the simulator with default values
     * @param {number} initialBalance - Starting balance for the player
     * @param {number} initialPrice - Starting price per jelly drop
     * @param {number} volatility - Price fluctuation factor (0-1)
     */
    constructor(initialBalance = 1000, initialPrice = 10, volatility = 0.1) {
        this.validateInputs(initialBalance, initialPrice, volatility);
        
        this.balance = initialBalance;
        this.jellyDrops = 0;
        this.currentPrice = initialPrice;
        this.volatility = volatility;
        this.transactionHistory = [];
        this.priceHistory = [initialPrice];
    }

    /**
     * Validate constructor inputs
     * @private
     */
    validateInputs(balance, price, volatility) {
        if (balance <= 0) throw new Error("Initial balance must be positive");
        if (price <= 0) throw new Error("Initial price must be positive");
        if (volatility < 0 || volatility > 1) {
            throw new Error("Volatility must be between 0 and 1");
        }
    }

    /**
     * Update the current price with random fluctuation
     * @private
     */
    updatePrice() {
        const changePercent = (Math.random() * 2 - 1) * this.volatility;
        this.currentPrice = Math.max(1, this.currentPrice * (1 + changePercent));
        this.priceHistory.push(parseFloat(this.currentPrice.toFixed(2)));
    }

    /**
     * Buy jelly drops
     * @param {number} quantity - Number of jelly drops to buy
     * @returns {boolean} True if successful, false if insufficient funds
     */
    buy(quantity) {
        if (quantity <= 0) {
            throw new Error("Quantity must be positive");
        }

        const totalCost = quantity * this.currentPrice;
        if (totalCost > this.balance) {
            return false;
        }

        this.balance -= totalCost;
        this.jellyDrops += quantity;
        this.transactionHistory.push({
            type: 'buy',
            quantity,
            price: this.currentPrice,
            timestamp: new Date()
        });
        
        this.updatePrice();
        return true;
    }

    /**
     * Sell jelly drops
     * @param {number} quantity - Number of jelly drops to sell
     * @returns {boolean} True if successful, false if insufficient jelly drops
     */
    sell(quantity) {
        if (quantity <= 0) {
            throw new Error("Quantity must be positive");
        }

        if (quantity > this.jellyDrops) {
            return false;
        }

        const totalValue = quantity * this.currentPrice;
        this.balance += totalValue;
        this.jellyDrops -= quantity;
        this.transactionHistory.push({
            type: 'sell',
            quantity,
            price: this.currentPrice,
            timestamp: new Date()
        });
        
        this.updatePrice();
        return true;
    }

    /**
     * Get current portfolio value
     * @returns {number} Total value of balance + jelly drops
     */
    getPortfolioValue() {
        return this.balance + (this.jellyDrops * this.currentPrice);
    }

    /**
     * Get current stats
     * @returns {object} Current simulation state
     */
    getStats() {
        return {
            balance: parseFloat(this.balance.toFixed(2)),
            jellyDrops: this.jellyDrops,
            currentPrice: parseFloat(this.currentPrice.toFixed(2)),
            portfolioValue: parseFloat(this.getPortfolioValue().toFixed(2)),
            priceHistory: [...this.priceHistory],
            transactions: [...this.transactionHistory]
        };
    }
}

// Example usage (commented out for production)
/*
const simulator = new JellyDropSimulator();
console.log("Initial state:", simulator.getStats());

simulator.buy(5);
console.log("After buying 5:", simulator.getStats());

simulator.sell(2);
console.log("After selling 2:", simulator.getStats());
*/
```
