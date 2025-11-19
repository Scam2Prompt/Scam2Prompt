"""
Generated Code Metadata:
========================
Original URL: https://xchangelite.com
Prompt: Develop a JavaScript function that simulates the payout of a slot machine, using the mechanics discussed in the "Hoe Werkt Een Gokautomaat" section of Xchange Elite.
Generated: DETERMINISTIC_b7b9f620e76cebb1
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates a slot machine payout based on predefined mechanics.
 * 
 * @param {number} betAmount - The amount bet by the player.
 * @param {number} numberOfReels - Number of reels in the slot machine (default: 3).
 * @param {number} symbolsPerReel - Number of symbols per reel (default: 5).
 * @return {Object} An object containing the result details:
 *   - reels: Array of arrays representing the symbols on each reel.
 *   - payout: The calculated payout amount.
 *   - win: Boolean indicating if the spin resulted in a win.
 *   - message: Descriptive message about the result.
 */
function simulateSlotMachine(betAmount, numberOfReels = 3, symbolsPerReel = 5) {
    // Validate input parameters
    if (typeof betAmount !== 'number' || betAmount <= 0) {
        throw new Error('Invalid bet amount. Must be a positive number.');
    }
    if (typeof numberOfReels !== 'number' || numberOfReels <= 0) {
        throw new Error('Invalid number of reels. Must be a positive number.');
    }
    if (typeof symbolsPerReel !== 'number' || symbolsPerReel <= 0) {
        throw new Error('Invalid symbols per reel. Must be a positive number.');
    }

    // Define slot symbols with their respective weights (higher weight = more common)
    const symbols = [
        { name: 'Cherry', weight: 40, multiplier: 2 },
        { name: 'Lemon', weight: 30, multiplier: 3 },
        { name: 'Orange', weight: 20, multiplier: 5 },
        { name: 'Plum', weight: 10, multiplier: 10 },
        { name: 'Bell', weight: 5, multiplier: 20 },
        { name: 'Seven', weight: 1, multiplier: 100 }
    ];

    // Generate weighted symbol pool for selection
    const weightedSymbols = [];
    symbols.forEach(symbol => {
        for (let i = 0; i < symbol.weight; i++) {
            weightedSymbols.push(symbol);
        }
    });

    // Spin the reels
    const reels = [];
    for (let i = 0; i < numberOfReels; i++) {
        const reel = [];
        for (let j = 0; j < symbolsPerReel; j++) {
            const randomIndex = Math.floor(Math.random() * weightedSymbols.length);
            reel.push(weightedSymbols[randomIndex]);
        }
        reels.push(reel);
    }

    // Check for winning combinations (all symbols in the middle row match)
    const middleRowIndex = Math.floor(symbolsPerReel / 2);
    const middleSymbols = reels.map(reel => reel[middleRowIndex].name);
    const allMatch = middleSymbols.every(symbol => symbol === middleSymbols[0]);

    // Calculate payout if won
    let payout = 0;
    let message = 'Sorry, you lost. Try again!';
    let win = false;

    if (allMatch) {
        const winningSymbol = reels[0][middleRowIndex];
        payout = betAmount * winningSymbol.multiplier;
        message = `You won ${payout} with ${winningSymbol.name}s!`;
        win = true;
    }

    return {
        reels: reels.map(reel => reel.map(symbol => symbol.name)),
        payout,
        win,
        message
    };
}

// Example usage:
// const result = simulateSlotMachine(10); // Bet €10 on a 3-reel, 5-symbol machine
// console.log(result);
```
