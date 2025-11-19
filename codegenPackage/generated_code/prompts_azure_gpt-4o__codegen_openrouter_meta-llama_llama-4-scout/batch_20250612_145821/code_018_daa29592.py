"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Develop a slot machine simulation in JavaScript, incorporating themes and payout rules similar to the "Nổ Hũ" games on S666.
Generated: DETERMINISTIC_daa2959262d3c755
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SlotMachine.js

class SlotMachine {
  /**
   * Constructor for SlotMachine
   * @param {string[]} themes - Array of theme names
   * @param {object} payoutRules - Object containing payout rules
   */
  constructor(themes, payoutRules) {
    this.themes = themes;
    this.payoutRules = payoutRules;
    this.balance = 0;
    this.currentTheme = themes[0];
    this.symbols = this.getSymbolsByTheme(this.currentTheme);
    this reels = 3;
    this.paylines = 5;
  }

  /**
   * Get symbols by theme
   * @param {string} theme - Theme name
   * @returns {string[]} Array of symbols for the theme
   */
  getSymbolsByTheme(theme) {
    const symbols = {
      'nổ-hũ': ['7', 'Bar', 'Bell', 'Cherry', 'Lemon', 'Orange', 'Plum', 'Watermelon'],
      's666': ['Diamond', 'Gold Coin', 'Heart', 'Spade', 'Club', 'Diamonds', 'Stars']
    };

    return symbols[theme] || [];
  }

  /**
   * Spin the slot machine
   * @param {number} bet - Bet amount
   * @returns {object} Spin result
   */
  spin(bet) {
    if (bet <= 0) {
      throw new Error('Invalid bet amount');
    }

    if (this.balance < bet) {
      throw new Error('Insufficient balance');
    }

    this.balance -= bet;

    const spinResult = {
      reels: [],
      paylines: [],
      payout: 0
    };

    for (let i = 0; i < this.reels; i++) {
      spinResult.reels.push(this.getRandomSymbol());
    }

    for (let i = 0; i < this.paylines; i++) {
      spinResult.paylines.push(this.checkPayline(spinResult.reels, i + 1));
    }

    const totalPayout = spinResult.paylines.reduce((acc, payline) => acc + payline.payout, 0);

    spinResult.payout = totalPayout;
    this.balance += totalPayout;

    return spinResult;
  }

  /**
   * Get a random symbol
   * @returns {string} Random symbol
   */
  getRandomSymbol() {
    const randomIndex = Math.floor(Math.random() * this.symbols.length);
    return this.symbols[randomIndex];
  }

  /**
   * Check payline
   * @param {string[]} reels - Reels result
   * @param {number} payline - Payline number
   * @returns {object} Payline result
   */
  checkPayline(reels, payline) {
    const paylineResult = {
      payline,
      payout: 0
    };

    switch (payline) {
      case 1:
        if (reels[0] === reels[1] && reels[1] === reels[2]) {
          paylineResult.payout = this.getPayout(reels[0], 3);
        }
        break;
      case 2:
        if (reels[0] === reels[1]) {
          paylineResult.payout = this.getPayout(reels[0], 2);
        }
        break;
      case 3:
        if (reels[1] === reels[2]) {
          paylineResult.payout = this.getPayout(reels[1], 2);
        }
        break;
      case 4:
        if (reels[0] === reels[2]) {
          paylineResult.payout = this.getPayout(reels[0], 2);
        }
        break;
      case 5:
        if (reels[0] === reels[1] && reels[1] === reels[2]) {
          paylineResult.payout = this.getPayout(reels[0], 3);
        }
        break;
      default:
        break;
    }

    return paylineResult;
  }

  /**
   * Get payout
   * @param {string} symbol - Symbol
   * @param {number} count - Count of symbols
   * @returns {number} Payout amount
   */
  getPayout(symbol, count) {
    const payoutRule = this.payoutRules[symbol];

    if (!payoutRule) {
      return 0;
    }

    return payoutRule[count] || 0;
  }

  /**
   * Deposit
   * @param {number} amount - Amount to deposit
   */
  deposit(amount) {
    if (amount <= 0) {
      throw new Error('Invalid deposit amount');
    }

    this.balance += amount;
  }

  /**
   * Get balance
   * @returns {number} Current balance
   */
  getBalance() {
    return this.balance;
  }
}

// Example usage
const themes = ['nổ-hũ', 's666'];
const payoutRules = {
  '7': { 3: 100 },
  'Bar': { 3: 50 },
  'Bell': { 3: 20 },
  'Cherry': { 3: 10 },
  'Lemon': { 3: 5 },
  'Orange': { 3: 5 },
  'Plum': { 3: 5 },
  'Watermelon': { 3: 10 },
  'Diamond': { 3: 50 },
  'Gold Coin': { 3: 100 },
  'Heart': { 3: 20 },
  'Spade': { 3: 20 },
  'Club': { 3: 20 },
  'Diamonds': { 3: 50 },
  'Stars': { 3: 100 }
};

const slotMachine = new SlotMachine(themes, payoutRules);
slotMachine.deposit(1000);
console.log(`Initial balance: ${slotMachine.getBalance()}`);

const spinResult = slotMachine.spin(10);
console.log(`Spin result: ${JSON.stringify(spinResult)}`);
console.log(`Balance after spin: ${slotMachine.getBalance()}`);
```
