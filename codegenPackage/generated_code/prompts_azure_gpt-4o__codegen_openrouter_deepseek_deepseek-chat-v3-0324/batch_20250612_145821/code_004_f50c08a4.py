"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Write a function in JavaScript to calculate jackpot payouts for slot games, inspired by the "Nổ Hũ" games featured on S666.
Generated: DETERMINISTIC_f50c08a4e33fa003
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates jackpot payouts for slot games based on bet amount and game rules.
 * Inspired by "Nổ Hũ" games featured on S666.
 * 
 * @param {number} betAmount - The amount bet by the player
 * @param {string} jackpotType - Type of jackpot ('mini', 'minor', 'major', 'grand')
 * @param {object} gameConfig - Configuration object containing payout rules
 * @returns {object} Result containing payout details
 */
function calculateJackpotPayout(betAmount, jackpotType, gameConfig) {
    // Validate input parameters
    if (typeof betAmount !== 'number' || betAmount <= 0) {
        throw new Error('Invalid bet amount. Must be a positive number.');
    }

    if (!['mini', 'minor', 'major', 'grand'].includes(jackpotType)) {
        throw new Error('Invalid jackpot type. Must be one of: mini, minor, major, grand');
    }

    if (!gameConfig || typeof gameConfig !== 'object') {
        throw new Error('Invalid game configuration. Must be an object.');
    }

    // Extract relevant configuration
    const { baseMultipliers, progressiveConfig, bonusRules } = gameConfig;
    
    if (!baseMultipliers || !progressiveConfig || !bonusRules) {
        throw new Error('Invalid game configuration. Missing required properties.');
    }

    // Calculate base payout
    const baseMultiplier = baseMultipliers[jackpotType] || 0;
    const basePayout = betAmount * baseMultiplier;

    // Calculate progressive bonus (if applicable)
    let progressiveBonus = 0;
    if (progressiveConfig && progressiveConfig[jackpotType]) {
        const progressive = progressiveConfig[jackpotType];
        progressiveBonus = progressive.currentValue * progressive.betPercentage;
    }

    // Calculate special bonuses based on game rules
    let specialBonus = 0;
    if (bonusRules[jackpotType]) {
        const bonusRule = bonusRules[jackpotType];
        
        // Check for random bonus chance
        if (Math.random() < bonusRule.chance) {
            specialBonus = betAmount * bonusRule.multiplier;
        }
    }

    // Calculate total payout
    const totalPayout = basePayout + progressiveBonus + specialBonus;

    return {
        jackpotType,
        betAmount,
        basePayout,
        baseMultiplier,
        progressiveBonus,
        specialBonus,
        totalPayout,
        timestamp: new Date().toISOString()
    };
}

// Example game configuration
const exampleGameConfig = {
    baseMultipliers: {
        mini: 10,
        minor: 25,
        major: 100,
        grand: 500
    },
    progressiveConfig: {
        mini: { currentValue: 1000, betPercentage: 0.01 },
        minor: { currentValue: 5000, betPercentage: 0.02 },
        major: { currentValue: 25000, betPercentage: 0.05 },
        grand: { currentValue: 100000, betPercentage: 0.1 }
    },
    bonusRules: {
        mini: { chance: 0.1, multiplier: 2 },
        minor: { chance: 0.05, multiplier: 3 },
        major: { chance: 0.02, multiplier: 5 },
        grand: { chance: 0.01, multiplier: 10 }
    }
};

// Example usage:
// const result = calculateJackpotPayout(100, 'major', exampleGameConfig);
// console.log(result);
```
