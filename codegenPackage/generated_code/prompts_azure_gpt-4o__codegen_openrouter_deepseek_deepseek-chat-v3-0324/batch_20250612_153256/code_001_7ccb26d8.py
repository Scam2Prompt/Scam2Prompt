"""
Generated Code Metadata:
========================
Original URL: https://wallstmemes.com
Prompt: Create a function in JavaScript that simulates a meme-based stock portfolio inspired by the Wall Street Memes community, incorporating stocks like Tesla and Bitcoin.
Generated: DETERMINISTIC_7ccb26d8b7b7aa9f
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MemeStockPortfolio - A simulated portfolio inspired by Wall Street Memes community.
 * Includes popular meme stocks like Tesla and Bitcoin.
 */
class MemeStockPortfolio {
    /**
     * Constructor initializes the portfolio with default meme stocks.
     */
    constructor() {
        this.portfolio = {
            'TSLA': { shares: 0, avgPrice: 0, currentPrice: 250.00 }, // Tesla
            'BTC': { shares: 0, avgPrice: 0, currentPrice: 42000.00 }, // Bitcoin
            'GME': { shares: 0, avgPrice: 0, currentPrice: 20.00 },   // GameStop
            'AMC': { shares: 0, avgPrice: 0, currentPrice: 5.00 },    // AMC
            'DOGE': { shares: 0, avgPrice: 0, currentPrice: 0.10 }    // Dogecoin
        };
        this.cashBalance = 10000.00; // Starting cash balance
        this.transactionHistory = [];
    }

    /**
     * Buy shares of a stock.
     * @param {string} ticker - Stock ticker symbol
     * @param {number} shares - Number of shares to buy
     * @param {number} price - Price per share (optional, uses current price if not provided)
     * @returns {object} Transaction result or error
     */
    buyStock(ticker, shares, price = null) {
        try {
            if (!this.portfolio[ticker]) {
                throw new Error(`Stock ${ticker} not found in portfolio`);
            }

            if (shares <= 0) {
                throw new Error('Shares must be positive');
            }

            const currentPrice = price || this.portfolio[ticker].currentPrice;
            const totalCost = shares * currentPrice;

            if (totalCost > this.cashBalance) {
                throw new Error('Insufficient funds');
            }

            // Update portfolio
            const currentShares = this.portfolio[ticker].shares;
            const currentAvg = this.portfolio[ticker].avgPrice;
            
            this.portfolio[ticker].shares += shares;
            this.portfolio[ticker].avgPrice = 
                ((currentShares * currentAvg) + (shares * currentPrice)) / 
                (currentShares + shares);
            
            // Update cash balance
            this.cashBalance -= totalCost;

            // Record transaction
            const transaction = {
                type: 'BUY',
                ticker,
                shares,
                price: currentPrice,
                total: totalCost,
                timestamp: new Date().toISOString()
            };
            this.transactionHistory.push(transaction);

            return {
                success: true,
                message: `Bought ${shares} shares of ${ticker} at $${currentPrice.toFixed(2)}`,
                transaction
            };
        } catch (error) {
            return {
                success: false,
                message: error.message
            };
        }
    }

    /**
     * Sell shares of a stock.
     * @param {string} ticker - Stock ticker symbol
     * @param {number} shares - Number of shares to sell
     * @param {number} price - Price per share (optional, uses current price if not provided)
     * @returns {object} Transaction result or error
     */
    sellStock(ticker, shares, price = null) {
        try {
            if (!this.portfolio[ticker]) {
                throw new Error(`Stock ${ticker} not found in portfolio`);
            }

            if (shares <= 0) {
                throw new Error('Shares must be positive');
            }

            if (shares > this.portfolio[ticker].shares) {
                throw new Error('Insufficient shares to sell');
            }

            const currentPrice = price || this.portfolio[ticker].currentPrice;
            const totalValue = shares * currentPrice;

            // Update portfolio
            this.portfolio[ticker].shares -= shares;
            
            // Update cash balance
            this.cashBalance += totalValue;

            // Record transaction
            const transaction = {
                type: 'SELL',
                ticker,
                shares,
                price: currentPrice,
                total: totalValue,
                timestamp: new Date().toISOString()
            };
            this.transactionHistory.push(transaction);

            return {
                success: true,
                message: `Sold ${shares} shares of ${ticker} at $${currentPrice.toFixed(2)}`,
                transaction
            };
        } catch (error) {
            return {
                success: false,
                message: error.message
            };
        }
    }

    /**
     * Update current prices for all stocks in portfolio.
     * @param {object} priceUpdates - Object with ticker:price pairs
     */
    updatePrices(priceUpdates) {
        for (const [ticker, price] of Object.entries(priceUpdates)) {
            if (this.portfolio[ticker]) {
                this.portfolio[ticker].currentPrice = price;
            }
        }
    }

    /**
     * Get current portfolio value.
     * @returns {object} Portfolio summary with total value and breakdown
     */
    getPortfolioValue() {
        let totalValue = this.cashBalance;
        const breakdown = {};

        for (const [ticker, data] of Object.entries(this.portfolio)) {
            const value = data.shares * data.currentPrice;
            breakdown[ticker] = {
                shares: data.shares,
                avgPrice: data.avgPrice,
                currentPrice: data.currentPrice,
                value: value,
                profit: data.shares * (data.currentPrice - data.avgPrice)
            };
            totalValue += value;
        }

        return {
            totalValue,
            cashBalance: this.cashBalance,
            investments: breakdown,
            lastUpdated: new Date().toISOString()
        };
    }

    /**
     * Get transaction history.
     * @returns {array} Array of all transactions
     */
    getTransactionHistory() {
        return this.transactionHistory;
    }
}

// Example usage:
// const portfolio = new MemeStockPortfolio();
// portfolio.buyStock('TSLA', 10);
// portfolio.sellStock('TSLA', 5);
// portfolio.updatePrices({ 'TSLA': 260.00, 'BTC': 45000.00 });
// console.log(portfolio.getPortfolioValue());
```
