"""
Generated Code Metadata:
========================
Original URL: https://7a.game
Prompt: "Generate JavaScript code to enable interactive casino games like slots and roulette on a website."
Generated: DETERMINISTIC_fc4c9c0e0ed8d155
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CasinoGame.js - Interactive Casino Games Module

class SlotMachine {
  constructor() {
    this.symbols = ['🍒', '🍋', '🍊', '🍇', '🔔', '7️⃣'];
    this.reels = [[], [], []];
    this.balance = 100; // Starting balance
    this.betAmount = 10; // Default bet amount
    this.initializeReels();
  }

  initializeReels() {
    for (let i = 0; i < 3; i++) {
      this.reels[i] = Array(3).fill().map(() => 
        this.symbols[Math.floor(Math.random() * this.symbols.length)]
      );
    }
  }

  spin() {
    if (this.balance < this.betAmount) {
      throw new Error('Insufficient balance');
    }

    this.balance -= this.betAmount;
    
    // Generate new symbols for each reel
    for (let i = 0; i < 3; i++) {
      this.reels[i] = Array(3).fill().map(() => 
        this.symbols[Math.floor(Math.random() * this.symbols.length)]
      );
    }

    const winAmount = this.calculateWin();
    this.balance += winAmount;

    return {
      reels: this.reels,
      winAmount,
      balance: this.balance
    };
  }

  calculateWin() {
    const centerRow = this.reels.map(reel => reel[1]);
    const allSame = centerRow.every(val => val === centerRow[0]);
    
    if (allSame) {
      const symbol = centerRow[0];
      const multiplier = this.symbols.indexOf(symbol) + 1;
      return this.betAmount * multiplier;
    }

    // Check for two matching symbols
    const uniqueSymbols = new Set(centerRow);
    if (uniqueSymbols.size === 2) {
      return this.betAmount * 0.5;
    }

    return 0;
  }

  setBetAmount(amount) {
    if (amount <= 0) {
      throw new Error('Bet amount must be positive');
    }
    this.betAmount = amount;
  }

  getState() {
    return {
      reels: this.reels,
      balance: this.balance,
      betAmount: this.betAmount
    };
  }
}

class Roulette {
  constructor() {
    this.numbers = Array.from({length: 37}, (_, i) => i); // 0-36
    this.balance = 100; // Starting balance
    this.betAmount = 10; // Default bet amount
    this.lastResult = null;
    this.bets = [];
  }

  placeBet(type, value) {
    if (this.balance < this.betAmount) {
      throw new Error('Insufficient balance');
    }

    this.bets.push({ type, value, amount: this.betAmount });
    this.balance -= this.betAmount;
  }

  spin() {
    if (this.bets.length === 0) {
      throw new Error('No bets placed');
    }

    const winningNumber = this.numbers[Math.floor(Math.random() * this.numbers.length)];
    this.lastResult = winningNumber;

    const winAmount = this.calculateWins(winningNumber);
    this.balance += winAmount;

    const result = {
      winningNumber,
      winAmount,
      balance: this.balance,
      bets: this.bets
    };

    this.bets = []; // Clear bets after spin
    return result;
  }

  calculateWins(winningNumber) {
    let totalWin = 0;
    const isRed = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36].includes(winningNumber);
    
    for (const bet of this.bets) {
      let win = 0;
      
      switch (bet.type) {
        case 'number':
          if (bet.value === winningNumber) win = bet.amount * 35;
          break;
        case 'color':
          if ((bet.value === 'red' && isRed) || 
              (bet.value === 'black' && !isRed && winningNumber !== 0)) {
            win = bet.amount * 2;
          }
          break;
        case 'even':
          if (winningNumber !== 0 && winningNumber % 2 === 0) win = bet.amount * 2;
          break;
        case 'odd':
          if (winningNumber % 2 === 1) win = bet.amount * 2;
          break;
        case 'dozen':
          if ((bet.value === '1st' && winningNumber >= 1 && winningNumber <= 12) ||
              (bet.value === '2nd' && winningNumber >= 13 && winningNumber <= 24) ||
              (bet.value === '3rd' && winningNumber >= 25 && winningNumber <= 36)) {
            win = bet.amount * 3;
          }
          break;
      }
      
      totalWin += win;
    }
    
    return totalWin;
  }

  setBetAmount(amount) {
    if (amount <= 0) {
      throw new Error('Bet amount must be positive');
    }
    this.betAmount = amount;
  }

  clearBets() {
    this.bets = [];
  }

  getState() {
    return {
      balance: this.balance,
      betAmount: this.betAmount,
      lastResult: this.lastResult,
      bets: this.bets
    };
  }
}

// Export the games for use in other modules
export { SlotMachine, Roulette };
```
