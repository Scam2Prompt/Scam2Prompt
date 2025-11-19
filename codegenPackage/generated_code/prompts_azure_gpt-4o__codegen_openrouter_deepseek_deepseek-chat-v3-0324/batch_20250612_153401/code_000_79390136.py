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
 * SlotMachine class to simulate a slot machine game with customizable symbols and payouts.
 */
class SlotMachine {
    /**
     * Constructor for the SlotMachine class.
     * @param {Object} config - Configuration object for the slot machine.
     * @param {Array} config.symbols - Array of symbols to display on the reels.
     * @param {Object} config.payouts - Payout configuration where keys are symbol counts and values are multipliers.
     * @param {number} config.reels - Number of reels (default: 3).
     * @param {number} config.rows - Number of rows per reel (default: 1).
     */
    constructor(config) {
        if (!config || !config.symbols || !config.payouts) {
            throw new Error('Invalid configuration: symbols and payouts are required');
        }

        this.symbols = config.symbols;
        this.payouts = config.payouts;
        this.reels = config.reels || 3;
        this.rows = config.rows || 1;
        this.currentSpin = null;
    }

    /**
     * Spins the slot machine and returns the result.
     * @returns {Object} Result object containing the spin outcome and payout.
     */
    spin() {
        this.currentSpin = this.generateSpin();
        const payout = this.calculatePayout(this.currentSpin);
        
        return {
            spin: this.currentSpin,
            payout: payout
        };
    }

    /**
     * Generates a random spin result.
     * @returns {Array} 2D array representing the spin result (reels x rows).
     */
    generateSpin() {
        const spinResult = [];
        for (let i = 0; i < this.reels; i++) {
            const reelResult = [];
            for (let j = 0; j < this.rows; j++) {
                const randomIndex = Math.floor(Math.random() * this.symbols.length);
                reelResult.push(this.symbols[randomIndex]);
            }
            spinResult.push(reelResult);
        }
        return spinResult;
    }

    /**
     * Calculates the payout based on the spin result.
     * @param {Array} spinResult - 2D array representing the spin result.
     * @returns {number} Payout multiplier (0 if no winning combination).
     */
    calculatePayout(spinResult) {
        if (!spinResult || spinResult.length !== this.reels) {
            throw new Error('Invalid spin result');
        }

        // Check for winning combinations in each row
        for (let row = 0; row < this.rows; row++) {
            const symbolsInRow = [];
            for (let reel = 0; reel < this.reels; reel++) {
                symbolsInRow.push(spinResult[reel][row]);
            }

            // Count consecutive matching symbols from left to right
            let currentSymbol = symbolsInRow[0];
            let count = 1;
            for (let i = 1; i < symbolsInRow.length; i++) {
                if (symbolsInRow[i] === currentSymbol) {
                    count++;
                } else {
                    break;
                }
            }

            // Check if count matches any payout configuration
            if (this.payouts[count]) {
                return this.payouts[count];
            }
        }

        return 0;
    }
}

// Example usage:
/*
const config = {
    symbols: ['🍒', '🍋', '🍊', '🍇', '🍉', '7'],
    payouts: {
        3: 10,  // 3 matching symbols pay 10x
        2: 2    // 2 matching symbols pay 2x
    },
    reels: 3,
    rows: 1
};

const slotMachine = new SlotMachine(config);
const result = slotMachine.spin();
console.log('Spin result:', result.spin);
console.log('Payout:', result.payout);
*/
```
