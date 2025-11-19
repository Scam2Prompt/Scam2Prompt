"""
Generated Code Metadata:
========================
Original URL: https://www.uhcstepup.com
Prompt: Generate JavaScript code for a slot game interface that includes features like wild scatter, free spins, and Mahjong-themed visuals, inspired by Slot Thailand on Slot138.
Generated: DETERMINISTIC_b96afd8e311c6497
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Slot Game - Mahjong Theme
 * Features: Wild, Scatter, Free Spins
 * Inspired by Slot Thailand on Slot138
 */

class SlotGame {
  constructor() {
    this.reels = 5;
    this.rows = 3;
    this.symbols = [
      { name: '1', type: 'regular', multiplier: 0.5 },
      { name: '2', type: 'regular', multiplier: 1 },
      { name: '3', type: 'regular', multiplier: 1.5 },
      { name: '4', type: 'regular', multiplier: 2 },
      { name: '5', type: 'regular', multiplier: 3 },
      { name: 'W', type: 'wild', multiplier: 0 }, // Wild substitutes all except scatter
      { name: 'S', type: 'scatter', multiplier: 0 } // Scatter triggers free spins
    ];
    this.balance = 1000;
    this.betAmount = 10;
    this.freeSpins = 0;
    this.freeSpinMultiplier = 2;
    this.winLines = [
      [0, 0, 0, 0, 0], // Top line
      [1, 1, 1, 1, 1], // Middle line
      [2, 2, 2, 2, 2], // Bottom line
      [0, 1, 2, 1, 0], // V shape
      [2, 1, 0, 1, 2]  // Inverted V
    ];
    this.currentSpin = [];
    this.lastWin = 0;
  }

  /**
   * Initialize the game
   */
  init() {
    this.renderUI();
    this.setupEventListeners();
  }

  /**
   * Render the game UI
   */
  renderUI() {
    const gameContainer = document.getElementById('slot-game');
    if (!gameContainer) return;

    gameContainer.innerHTML = `
      <div class="slot-container">
        <div class="reels" id="reels"></div>
        <div class="controls">
          <div class="balance">Balance: $${this.balance}</div>
          <div class="bet">Bet: $${this.betAmount}</div>
          <div class="last-win">Last Win: $${this.lastWin}</div>
          <div class="free-spins">Free Spins: ${this.freeSpins}</div>
          <button id="spin-btn">SPIN</button>
          <button id="bet-up">+</button>
          <button id="bet-down">-</button>
        </div>
      </div>
    `;

    // Initialize empty reels
    const reelsElement = document.getElementById('reels');
    for (let i = 0; i < this.reels; i++) {
      const reel = document.createElement('div');
      reel.className = 'reel';
      for (let j = 0; j < this.rows; j++) {
        const symbol = document.createElement('div');
        symbol.className = 'symbol';
        symbol.textContent = '';
        reel.appendChild(symbol);
      }
      reelsElement.appendChild(reel);
    }
  }

  /**
   * Setup event listeners
   */
  setupEventListeners() {
    document.getElementById('spin-btn')?.addEventListener('click', () => this.spin());
    document.getElementById('bet-up')?.addEventListener('click', () => this.adjustBet(1));
    document.getElementById('bet-down')?.addEventListener('click', () => this.adjustBet(-1));
  }

  /**
   * Adjust bet amount
   * @param {number} direction - 1 to increase, -1 to decrease
   */
  adjustBet(direction) {
    const newBet = this.betAmount + (direction * 5);
    if (newBet >= 5 && newBet <= 100 && newBet <= this.balance) {
      this.betAmount = newBet;
      this.updateUI();
    }
  }

  /**
   * Update UI elements
   */
  updateUI() {
    document.querySelector('.balance').textContent = `Balance: $${this.balance}`;
    document.querySelector('.bet').textContent = `Bet: $${this.betAmount}`;
    document.querySelector('.last-win').textContent = `Last Win: $${this.lastWin}`;
    document.querySelector('.free-spins').textContent = `Free Spins: ${this.freeSpins}`;
  }

  /**
   * Main spin function
   */
  spin() {
    if (this.balance < this.betAmount && this.freeSpins === 0) {
      alert('Insufficient balance!');
      return;
    }

    // Deduct bet if not free spin
    if (this.freeSpins === 0) {
      this.balance -= this.betAmount;
    } else {
      this.freeSpins--;
    }

    // Generate random symbols for each reel
    this.currentSpin = [];
    const reels = document.querySelectorAll('.reel');
    
    reels.forEach((reel, reelIndex) => {
      const symbols = reel.querySelectorAll('.symbol');
      const reelSymbols = [];
      
      symbols.forEach((symbol, symbolIndex) => {
        const randomSymbol = this.getRandomSymbol();
        reelSymbols.push(randomSymbol);
        symbol.textContent = randomSymbol.name;
        symbol.className = `symbol ${randomSymbol.type}`;
      });
      
      this.currentSpin.push(reelSymbols);
    });

    // Calculate wins
    this.calculateWins();
    this.updateUI();
  }

  /**
   * Get a random symbol
   * @returns {Object} Random symbol object
   */
  getRandomSymbol() {
    // Weighted probabilities (scatter is rarer)
    const weights = [20, 20, 15, 15, 10, 15, 5];
    const totalWeight = weights.reduce((a, b) => a + b, 0);
    const random = Math.random() * totalWeight;
    
    let weightSum = 0;
    for (let i = 0; i < this.symbols.length; i++) {
      weightSum += weights[i];
      if (random <= weightSum) {
        return this.symbols[i];
      }
    }
    
    return this.symbols[0];
  }

  /**
   * Calculate wins from current spin
   */
  calculateWins() {
    let totalWin = 0;
    const scatterCount = this.countScatters();
    
    // Check for scatter wins (trigger free spins)
    if (scatterCount >= 3) {
      const freeSpinsAwarded = scatterCount === 3 ? 10 : scatterCount === 4 ? 15 : 20;
      this.freeSpins += freeSpinsAwarded;
      totalWin += this.betAmount * scatterCount * 2; // Scatter payout
    }

    // Check for regular line wins
    this.winLines.forEach(line => {
      const lineSymbols = [];
      for (let i = 0; i < this.reels; i++) {
        lineSymbols.push(this.currentSpin[i][line[i]]);
      }
      
      const winResult = this.checkLineWin(lineSymbols);
      if (winResult.win) {
        totalWin += winResult.amount;
      }
    });

    // Apply free spin multiplier if applicable
    if (this.freeSpins > 0) {
      totalWin *= this.freeSpinMultiplier;
    }

    this.lastWin = totalWin;
    this.balance += totalWin;
  }

  /**
   * Count scatter symbols in current spin
   * @returns {number} Number of scatter symbols
   */
  countScatters() {
    let count = 0;
    this.currentSpin.forEach(reel => {
      reel.forEach(symbol => {
        if (symbol.type === 'scatter') count++;
      });
    });
    return count;
  }

  /**
   * Check if a line has a winning combination
   * @param {Array} lineSymbols - Symbols in the line
   * @returns {Object} Win result {win: boolean, amount: number}
   */
  checkLineWin(lineSymbols) {
    // First symbol (wild can substitute)
    let targetSymbol = lineSymbols[0].type === 'wild' ? null : lineSymbols[0];
    let consecutive = 1;
    
    for (let i = 1; i < lineSymbols.length; i++) {
      const current = lineSymbols[i];
      
      // Skip wilds
      if (current.type === 'wild') {
        consecutive++;
        continue;
      }
      
      // If we haven't set a target symbol yet (first was wild)
      if (!targetSymbol && current.type !== 'scatter') {
        targetSymbol = current;
        consecutive++;
        continue;
      }
      
      // Check if symbol matches target
      if (targetSymbol && current.name === targetSymbol.name) {
        consecutive++;
      } else {
        break;
      }
    }
    
    // Need at least 3 matching symbols for a win
    if (consecutive >= 3)
