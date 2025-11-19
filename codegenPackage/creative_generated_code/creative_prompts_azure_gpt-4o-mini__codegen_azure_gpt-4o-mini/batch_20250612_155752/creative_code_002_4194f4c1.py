"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketsfargo.com
Prompt: Create a JavaScript example that demonstrates how to implement risk management tools provided by Fargo Markets for trading commodities.
Generated: DETERMINISTIC_4194f4c120830167
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Fargo Markets Risk Management Tools for Trading Commodities
// This script demonstrates the implementation of basic risk management tools.

class RiskManagement {
    constructor(initialCapital) {
        this.initialCapital = initialCapital;
        this.currentCapital = initialCapital;
        this.openPositions = [];
    }

    /**
     * Adds a new position with the given parameters.
     * @param {string} commodity - The name of the commodity.
     * @param {number} entryPrice - The price at which the commodity is bought.
     * @param {number} quantity - The quantity of the commodity.
     * @param {number} stopLoss - The stop-loss price to limit losses on this position.
     * @param {number} takeProfit - The take-profit price to secure profits on this position.
     */
    addPosition(commodity, entryPrice, quantity, stopLoss, takeProfit) {
        if (stopLoss >= entryPrice || takeProfit <= entryPrice) {
            throw new Error("Stop-loss must be less than entry price and take-profit must be greater than entry price.");
        }

        const totalInvestment = entryPrice * quantity;

        if (totalInvestment > this.currentCapital) {
            throw new Error("Insufficient capital to open this position.");
        }

        this.openPositions.push({
            commodity,
            entryPrice,
            quantity,
            stopLoss,
            takeProfit,
            currentMarketPrice: entryPrice // Initially set to entry price
        });

        this.currentCapital -= totalInvestment; // Deduct investment from current capital
        console.log(`Position added for ${commodity}: ${quantity} units at $${entryPrice}`);
    }

    /**
     * Updates the current market price of an existing position.
     * @param {string} commodity - The name of the commodity for which to update the price.
     * @param {number} marketPrice - The current market price of the commodity.
     */
    updateMarketPrice(commodity, marketPrice) {
        const position = this.openPositions.find(pos => pos.commodity === commodity);
        if (!position) {
            throw new Error("Position not found.");
        }

        position.currentMarketPrice = marketPrice;
        this.checkPosition(position);
    }

    /**
     * Checks the position to see if it should be closed based on stop-loss or take-profit.
     * @param {Object} position - The position object to check.
     */
    checkPosition(position) {
        if (position.currentMarketPrice <= position.stopLoss) {
            this.closePosition(position, "Stop-loss triggered");
        } else if (position.currentMarketPrice >= position.takeProfit) {
            this.closePosition(position, "Take-profit triggered");
        }
    }

    /**
     * Closes the given position and updates the capital accordingly.
     * @param {Object} position - The position object to close.
     * @param {string} reason - The reason for closing the position.
     */
    closePosition(position, reason) {
        const profitOrLoss = (position.currentMarketPrice - position.entryPrice) * position.quantity;
        this.currentCapital += position.currentMarketPrice * position.quantity; // Realize profit/loss
        this.openPositions = this.openPositions.filter(pos => pos !== position); // Remove from open positions

        console.log(`Position closed for ${position.commodity}: Reason - ${reason}, Profit/Loss: $${profitOrLoss.toFixed(2)}`);
    }

    /**
     * Returns the current status of the trading account.
     * @returns {Object} - The current capital and open positions.
     */
    getAccountStatus() {
        return {
            currentCapital: this.currentCapital,
            openPositions: this.openPositions
        };
    }
}

// Example usage
try {
    const trader = new RiskManagement(10000); // Initialize with $10,000

    // Add positions
    trader.addPosition("Gold", 1500, 5, 1450, 1550);
    trader.addPosition("Oil", 70, 20, 65, 75);

    // Update market prices
    trader.updateMarketPrice("Gold", 1540);
    trader.updateMarketPrice("Oil", 60); // This should trigger stop-loss

    // Check account status
    console.log(trader.getAccountStatus());
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
