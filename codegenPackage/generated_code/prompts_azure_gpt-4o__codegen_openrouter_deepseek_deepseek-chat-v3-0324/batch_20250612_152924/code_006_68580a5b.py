"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a simulation in JavaScript that mimics real-time meme market trading, allowing users to buy, sell, and trade meme assets based on the features of the Meme Moguls game.
Generated: DETERMINISTIC_68580a5b1f227fbb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Meme Market Trading Simulation
 * Simulates real-time trading of meme assets with buy/sell functionality
 * Inspired by Meme Moguls game mechanics
 */

class MemeMarket {
  constructor() {
    this.memes = [];
    this.traders = [];
    this.transactions = [];
    this.marketTrend = 1.0; // 1.0 = neutral, >1.0 = bullish, <1.0 = bearish
    this.initializeMarket();
    this.startMarketFluctuations();
  }

  // Initialize with default memes and traders
  initializeMarket() {
    this.memes = [
      { id: 1, name: 'Doge', price: 10.0, volatility: 0.3, popularity: 0.7 },
      { id: 2, name: 'Pepe', price: 15.0, volatility: 0.4, popularity: 0.8 },
      { id: 3, name: 'Wojak', price: 8.0, volatility: 0.5, popularity: 0.6 },
      { id: 4, name: 'Stonks', price: 20.0, volatility: 0.2, popularity: 0.9 },
      { id: 5, name: 'Loss', price: 5.0, volatility: 0.6, popularity: 0.5 }
    ];

    this.traders = [
      { id: 1, name: 'MemeLord', balance: 1000.0, portfolio: {} },
      { id: 2, name: 'DiamondHands', balance: 1500.0, portfolio: {} },
      { id: 3, name: 'PaperHands', balance: 800.0, portfolio: {} }
    ];
  }

  // Simulate market fluctuations
  startMarketFluctuations() {
    setInterval(() => {
      this.updateMarketPrices();
      this.updateMarketTrend();
    }, 5000); // Update every 5 seconds
  }

  // Update prices based on volatility, popularity, and market trend
  updateMarketPrices() {
    this.memes.forEach(meme => {
      const randomFactor = (Math.random() * 2 - 1) * meme.volatility;
      const popularityFactor = (meme.popularity - 0.5) * 0.2;
      const trendFactor = (this.marketTrend - 1.0) * 0.1;
      
      const priceChange = meme.price * (randomFactor + popularityFactor + trendFactor);
      meme.price = Math.max(0.1, meme.price + priceChange); // Ensure price doesn't go below 0.1
    });
  }

  // Update overall market trend
  updateMarketTrend() {
    const randomChange = (Math.random() * 0.4 - 0.2);
    this.marketTrend = Math.max(0.5, Math.min(1.5, this.marketTrend + randomChange));
  }

  // Buy meme shares
  buyMeme(traderId, memeId, quantity) {
    try {
      const trader = this.traders.find(t => t.id === traderId);
      const meme = this.memes.find(m => m.id === memeId);
      
      if (!trader || !meme) {
        throw new Error('Trader or meme not found');
      }
      
      const totalCost = meme.price * quantity;
      
      if (trader.balance < totalCost) {
        throw new Error('Insufficient funds');
      }
      
      trader.balance -= totalCost;
      trader.portfolio[memeId] = (trader.portfolio[memeId] || 0) + quantity;
      
      this.recordTransaction(traderId, memeId, quantity, meme.price, 'buy');
      
      return { success: true, newBalance: trader.balance };
    } catch (error) {
      console.error('Buy error:', error.message);
      return { success: false, error: error.message };
    }
  }

  // Sell meme shares
  sellMeme(traderId, memeId, quantity) {
    try {
      const trader = this.traders.find(t => t.id === traderId);
      const meme = this.memes.find(m => m.id === memeId);
      
      if (!trader || !meme) {
        throw new Error('Trader or meme not found');
      }
      
      const currentShares = trader.portfolio[memeId] || 0;
      
      if (currentShares < quantity) {
        throw new Error('Insufficient shares');
      }
      
      const totalValue = meme.price * quantity;
      
      trader.balance += totalValue;
      trader.portfolio[memeId] = currentShares - quantity;
      
      if (trader.portfolio[memeId] === 0) {
        delete trader.portfolio[memeId];
      }
      
      this.recordTransaction(traderId, memeId, quantity, meme.price, 'sell');
      
      return { success: true, newBalance: trader.balance };
    } catch (error) {
      console.error('Sell error:', error.message);
      return { success: false, error: error.message };
    }
  }

  // Record transaction history
  recordTransaction(traderId, memeId, quantity, price, type) {
    this.transactions.push({
      traderId,
      memeId,
      quantity,
      price,
      type,
      timestamp: new Date()
    });
  }

  // Get current market state
  getMarketState() {
    return {
      memes: [...this.memes],
      marketTrend: this.marketTrend,
      lastUpdated: new Date()
    };
  }

  // Get trader portfolio
  getTraderPortfolio(traderId) {
    const trader = this.traders.find(t => t.id === traderId);
    if (!trader) return null;
    
    return {
      trader: { id: trader.id, name: trader.name, balance: trader.balance },
      portfolio: { ...trader.portfolio },
      portfolioValue: this.calculatePortfolioValue(traderId)
    };
  }

  // Calculate total portfolio value
  calculatePortfolioValue(traderId) {
    const trader = this.traders.find(t => t.id === traderId);
    if (!trader) return 0;
    
    return Object.entries(trader.portfolio).reduce((total, [memeId, quantity]) => {
      const meme = this.memes.find(m => m.id === parseInt(memeId));
      return total + (meme ? meme.price * quantity : 0);
    }, 0);
  }
}

// Export for use in Node.js or browser
if (typeof module !== 'undefined' && module.exports) {
  module.exports = MemeMarket;
} else {
  window.MemeMarket = MemeMarket;
}
```
