"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: Create a JavaScript function that simulates the process of rolling for Doge rewards on Moon5 and displays the results.
Generated: DETERMINISTIC_c141a7bd19f7529d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates rolling for Doge rewards on Moon5.
 * @param {number} rolls - The number of rolls to simulate.
 * @param {number} [minReward=1] - The minimum possible reward (in Doge).
 * @param {number} [maxReward=1000] - The maximum possible reward (in Doge).
 * @param {number} [winChance=0.3] - The probability of winning a reward (0 to 1).
 * @returns {Object} An object containing the results of each roll and summary statistics.
 * @throws {Error} If input parameters are invalid.
 */
function rollForDogeRewards(rolls, minReward = 1, maxReward = 1000, winChance = 0.3) {
    // Validate input parameters
    if (!Number.isInteger(rolls) || rolls <= 0) {
        throw new Error('Number of rolls must be a positive integer');
    }
    if (minReward < 0 || maxReward <= minReward) {
        throw new Error('Invalid reward range: min must be >= 0 and max must be > min');
    }
    if (winChance < 0 || winChance > 1) {
        throw new Error('Win chance must be between 0 and 1');
    }

    const results = [];
    let totalWon = 0;
    let wins = 0;

    for (let i = 0; i < rolls; i++) {
        const isWin = Math.random() <= winChance;
        let reward = 0;

        if (isWin) {
            reward = Math.floor(Math.random() * (maxReward - minReward + 1)) + minReward;
            totalWon += reward;
            wins++;
        }

        results.push({
            roll: i + 1,
            won: isWin,
            reward: isWin ? reward : 0
        });
    }

    return {
        rolls: results,
        summary: {
            totalRolls: rolls,
            totalWon: totalWon,
            winRate: wins / rolls,
            averageWin: wins > 0 ? totalWon / wins : 0,
            minPossibleReward: minReward,
            maxPossibleReward: maxReward,
            winChance: winChance
        }
    };
}

/**
 * Formats and displays the roll results in a human-readable way.
 * @param {Object} results - The results object returned by rollForDogeRewards.
 */
function displayDogeRollResults(results) {
    console.log('=== Doge Rewards Roll Results ===');
    console.log(`Total Rolls: ${results.summary.totalRolls}`);
    console.log(`Total Doge Won: ${results.summary.totalWon}`);
    console.log(`Win Rate: ${(results.summary.winRate * 100).toFixed(1)}%`);
    console.log(`Average Win: ${results.summary.averageWin.toFixed(2)} DOGE`);
    console.log('\nDetailed Results:');
    
    results.rolls.forEach(roll => {
        console.log(`Roll #${roll.roll}: ${roll.won ? `Won ${roll.reward} DOGE` : 'No win'}`);
    });
    
    console.log('=================================');
}

// Example usage:
try {
    const results = rollForDogeRewards(10);
    displayDogeRollResults(results);
} catch (error) {
    console.error('Error:', error.message);
}
```
