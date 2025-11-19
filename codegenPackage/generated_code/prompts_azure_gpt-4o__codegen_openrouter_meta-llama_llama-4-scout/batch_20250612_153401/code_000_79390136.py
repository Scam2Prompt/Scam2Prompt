"""
Generated Code Metadata:
========================
Original URL: https://7a.game
Prompt: Write JavaScript code to create a basic slot machine simulation with customizable symbols and payout logic.
Generated: DETERMINISTIC_79390136a1cd4ab9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Slot Machine Simulation
 * =======================
 * 
 * A basic slot machine simulation with customizable symbols and payout logic.
 */

// Define the SlotMachine class
class SlotMachine {
  /**
   * Constructor
   * @param {Array<string>} symbols - The symbols to display on the slot machine
   * @param {Object} payouts - The payout logic for each combination of symbols
   */
  constructor(symbols, payouts) {
    if (!Array.isArray(symbols) || symbols.length < 3) {
      throw new Error('At least 3 symbols are required');
    }

    if (typeof payouts !== 'object') {
      throw new Error('Payouts must be an object');
    }

    this.symbols = symbols;
    this.payouts = payouts;
    this.balance = 0;
  }

  /**
   * Spin the slot machine
   * @returns {Array<string>} The result of the spin
   */
  spin() {
    if (this.balance < 1) {
      throw new Error('Insufficient balance');
    }

    this.balance -= 1; // deduct 1 credit for each spin

    const result = [];
    for (let i = 0; i < 3; i++) {
      result.push(this.symbols[Math.floor(Math.random() * this.symbols.length)]);
    }

    return result;
  }

  /**
   * Calculate the payout for a given combination of symbols
   * @param {Array<string>} combination - The combination of symbols
   * @returns {number} The payout amount
   */
  calculatePayout(combination) {
    const key = combination.join(',');
    return this.payouts[key] || 0;
  }

  /**
   * Add credits to the balance
   * @param {number} amount - The amount to add
   */
  addCredits(amount) {
    if (typeof amount !== 'number' || amount <= 0) {
      throw new Error('Invalid amount');
    }

    this.balance += amount;
  }

  /**
   * Get the current balance
   * @returns {number} The current balance
   */
  getBalance() {
    return this.balance;
  }
}

// Example usage
const symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven'];
const payouts = {
  'Cherry,Cherry,Cherry': 10,
  'Lemon,Lemon,Lemon': 20,
  'Orange,Orange,Orange': 30,
  'Plum,Plum,Plum': 40,
  'Bell,Bell,Bell': 50,
  'Bar,Bar,Bar': 100,
  'Seven,Seven,Seven': 1000,
};

const slotMachine = new SlotMachine(symbols, payouts);
slotMachine.addCredits(100);

while (true) {
  console.log(`Balance: ${slotMachine.getBalance()}`);
  const spinResult = slotMachine.spin();
  console.log(`You got: ${spinResult.join(', ')}`);
  const payout = slotMachine.calculatePayout(spinResult);
  console.log(`Payout: ${payout}`);
  slotMachine.addCredits(payout);
  const playAgain = prompt('Play again? (yes/no)');
  if (playAgain.toLowerCase() !== 'yes') {
    break;
  }
}
```
