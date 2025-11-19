"""
Generated Code Metadata:
========================
Original URL: https://fastlink.pages.dev
Prompt: Generate a JavaScript code for a simple slot game interface, inspired by Panen889's game portfolio, including popular games like Big Bass Bonanza and Rujak Bonanza.
Generated: DETERMINISTIC_32222dcb789feeb5
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Slot Game Interface
 * Inspired by Panen889's game portfolio
 */

class SlotGame {
  constructor(options) {
    this.options = {
      reels: 3,
      rows: 3,
      symbols: ['🍒', '🍋', '🍊', '🍇', '🔔', '7️⃣', '💎'],
      payouts: {
        '🍒': [0, 2, 5, 10],
        '🍋': [0, 2, 5, 10],
        '🍊': [0, 3, 7, 15],
        '🍇': [0, 3, 7, 15],
        '🔔': [0, 5, 10, 20],
        '7️⃣': [0, 7, 15, 30],
        '💎': [0, 10, 25, 50]
      },
      betAmount: 1,
      credits: 100,
      ...options
    };

    this.reels = [];
    this.winLines = [];
    this.init();
  }

  init() {
    // Initialize reels with random symbols
    for (let i = 0; i < this.options.reels; i++) {
      this.reels[i] = [];
      for (let j = 0; j < this.options.rows; j++) {
        this.reels[i][j] = this.getRandomSymbol();
      }
    }
  }

  getRandomSymbol() {
    return this.options.symbols[
      Math.floor(Math.random() * this.options.symbols.length)
    ];
  }

  spin() {
    if (this.options.credits < this.options.betAmount) {
      throw new Error('Insufficient credits');
    }

    // Deduct bet amount
    this.options.credits -= this.options.betAmount;

    // Generate new reels
    for (let i = 0; i < this.options.reels; i++) {
      for (let j = 0; j < this.options.rows; j++) {
        this.reels[i][j] = this.getRandomSymbol();
      }
    }

    // Check for wins
    this.checkWins();

    return {
      reels: this.reels,
      winLines: this.winLines,
      credits: this.options.credits
    };
  }

  checkWins() {
    this.winLines = [];
    
    // Check horizontal lines (simplified for demo)
    for (let row = 0; row < this.options.rows; row++) {
      const firstSymbol = this.reels[0][row];
      let count = 1;
      
      for (let reel = 1; reel < this.options.reels; reel++) {
        if (this.reels[reel][row] === firstSymbol) {
          count++;
        } else {
          break;
        }
      }
      
      if (count >= 2) {
        const payout = this.options.payouts[firstSymbol][count - 1];
        if (payout > 0) {
          this.winLines.push({
            symbols: Array(count).fill(firstSymbol),
            payout: payout * this.options.betAmount,
            line: `Row ${row + 1}`
          });
          this.options.credits += payout * this.options.betAmount;
        }
      }
    }
  }

  setBetAmount(amount) {
    if (amount <= 0) {
      throw new Error('Bet amount must be positive');
    }
    this.options.betAmount = amount;
  }

  addCredits(amount) {
    if (amount <= 0) {
      throw new Error('Credit amount must be positive');
    }
    this.options.credits += amount;
  }
}

// UI Implementation
class SlotGameUI {
  constructor(containerId, gameOptions) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container with ID ${containerId} not found`);
    }

    this.game = new SlotGame(gameOptions);
    this.initUI();
    this.bindEvents();
  }

  initUI() {
    this.container.innerHTML = `
      <div class="slot-container">
        <div class="slot-reels"></div>
        <div class="slot-controls">
          <div class="credit-display">Credits: ${this.game.options.credits}</div>
          <div class="bet-controls">
            <button class="bet-down">-</button>
            <span class="bet-amount">${this.game.options.betAmount}</span>
            <button class="bet-up">+</button>
          </div>
          <button class="spin-button">SPIN</button>
          <div class="win-display"></div>
        </div>
      </div>
    `;

    this.renderReels();
  }

  renderReels() {
    const reelsContainer = this.container.querySelector('.slot-reels');
    reelsContainer.innerHTML = '';

    for (let row = 0; row < this.game.options.rows; row++) {
      const rowElement = document.createElement('div');
      rowElement.className = 'reel-row';

      for (let reel = 0; reel < this.game.options.reels; reel++) {
        const symbolElement = document.createElement('div');
        symbolElement.className = 'reel-symbol';
        symbolElement.textContent = this.game.reels[reel][row];
        rowElement.appendChild(symbolElement);
      }

      reelsContainer.appendChild(rowElement);
    }
  }

  bindEvents() {
    this.container.querySelector('.spin-button').addEventListener('click', () => {
      try {
        const result = this.game.spin();
        this.renderReels();
        this.updateUI(result);
      } catch (error) {
        alert(error.message);
      }
    });

    this.container.querySelector('.bet-up').addEventListener('click', () => {
      this.game.setBetAmount(this.game.options.betAmount + 1);
      this.updateBetDisplay();
    });

    this.container.querySelector('.bet-down').addEventListener('click', () => {
      if (this.game.options.betAmount > 1) {
        this.game.setBetAmount(this.game.options.betAmount - 1);
        this.updateBetDisplay();
      }
    });
  }

  updateUI(result) {
    this.container.querySelector('.credit-display').textContent = 
      `Credits: ${result.credits}`;

    const winDisplay = this.container.querySelector('.win-display');
    winDisplay.innerHTML = '';

    if (result.winLines.length > 0) {
      result.winLines.forEach(win => {
        const winElement = document.createElement('div');
        winElement.className = 'win-line';
        winElement.innerHTML = `
          <span class="win-symbols">${win.symbols.join(' ')}</span>
          <span class="win-amount">+${win.payout}</span>
          <span class="win-line">${win.line}</span>
        `;
        winDisplay.appendChild(winElement);
      });
    }
  }

  updateBetDisplay() {
    this.container.querySelector('.bet-amount').textContent = 
      this.game.options.betAmount;
  }
}

// CSS Styles (would typically be in a separate file)
const style = document.createElement('style');
style.textContent = `
  .slot-container {
    font-family: Arial, sans-serif;
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background: #1a1a2e;
    border-radius: 10px;
    color: white;
  }
  
  .slot-reels {
    background: #16213e;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
  }
  
  .reel-row {
    display: flex;
    justify-content: space-around;
    margin: 10px 0;
  }
  
  .reel-symbol {
    font-size: 2rem;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #0f3460;
    border-radius: 5px;
  }
  
  .slot-controls {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  .credit-display, .bet-amount {
    font-size: 1.2rem;
    font-weight: bold;
  }
  
  .bet-controls {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
  }
  
  .bet-controls button {
    background: #e94560;
    color: white;
    border: none;
    border-radius: 5px;
    width: 30px;
    height: 30px;
    font-size: 1.2rem;
    cursor: pointer;
  }
  
  .spin-button {
    background: #e94560;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
