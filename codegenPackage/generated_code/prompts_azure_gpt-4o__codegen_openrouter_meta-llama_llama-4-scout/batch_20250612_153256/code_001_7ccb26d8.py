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
 * Represents a stock in the portfolio.
 */
class Stock {
  /**
   * Creates a new Stock instance.
   * @param {string} symbol - The stock symbol (e.g., TSLA, BTC).
   * @param {string} name - The stock name (e.g., Tesla, Bitcoin).
   * @param {number} price - The current stock price.
   */
  constructor(symbol, name, price) {
    this.symbol = symbol;
    this.name = name;
    this.price = price;
  }

  /**
   * Updates the stock price.
   * @param {number} newPrice - The new stock price.
   */
  updatePrice(newPrice) {
    if (newPrice < 0) {
      throw new Error(`Invalid price: ${newPrice}. Price cannot be negative.`);
    }
    this.price = newPrice;
  }
}

/**
 * Represents a portfolio of stocks.
 */
class Portfolio {
  /**
   * Creates a new Portfolio instance.
   */
  constructor() {
    this.stocks = {};
  }

  /**
   * Adds a stock to the portfolio.
   * @param {Stock} stock - The stock to add.
   * @param {number} quantity - The quantity of the stock to add.
   */
  addStock(stock, quantity) {
    if (quantity <= 0) {
      throw new Error(`Invalid quantity: ${quantity}. Quantity must be greater than 0.`);
    }
    this.stocks[stock.symbol] = { stock, quantity };
  }

  /**
   * Removes a stock from the portfolio.
   * @param {string} symbol - The symbol of the stock to remove.
   */
  removeStock(symbol) {
    if (!this.stocks[symbol]) {
      throw new Error(`Stock not found: ${symbol}`);
    }
    delete this.stocks[symbol];
  }

  /**
   * Updates the price of a stock in the portfolio.
   * @param {string} symbol - The symbol of the stock to update.
   * @param {number} newPrice - The new price of the stock.
   */
  updateStockPrice(symbol, newPrice) {
    if (!this.stocks[symbol]) {
      throw new Error(`Stock not found: ${symbol}`);
    }
    this.stocks[symbol].stock.updatePrice(newPrice);
  }

  /**
   * Calculates the total value of the portfolio.
   * @returns {number} The total value of the portfolio.
   */
  calculateTotalValue() {
    let totalValue = 0;
    for (const stock of Object.values(this.stocks)) {
      totalValue += stock.stock.price * stock.quantity;
    }
    return totalValue;
  }
}

// Example usage:
function main() {
  try {
    const portfolio = new Portfolio();

    const tesla = new Stock('TSLA', 'Tesla', 1000);
    const bitcoin = new Stock('BTC', 'Bitcoin', 50000);

    portfolio.addStock(tesla, 10);
    portfolio.addStock(bitcoin, 0.1);

    console.log(`Initial portfolio value: $${portfolio.calculateTotalValue().toFixed(2)}`);

    portfolio.updateStockPrice('TSLA', 1200);
    portfolio.updateStockPrice('BTC', 60000);

    console.log(`Updated portfolio value: $${portfolio.calculateTotalValue().toFixed(2)}`);

    portfolio.removeStock('TSLA');

    console.log(`Portfolio value after removing TSLA: $${portfolio.calculateTotalValue().toFixed(2)}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
