"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Write a JavaScript function to implement the scoring system for Mahjong games as described on Solitaire Network, including tile matching logic.
Generated: DETERMINISTIC_e2a1fc61d859f26d
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Mahjong scoring system implementation based on Solitaire Network rules.
 * Handles tile matching and scoring logic for Mahjong solitaire games.
 */
class MahjongScorer {
    /**
     * Initialize the scorer with game settings.
     * @param {Object} options - Game configuration options
     */
    constructor(options = {}) {
        this.defaultOptions = {
            timeBonus: true,         // Whether to apply time bonus
            baseScore: 1000,         // Base score for each match
            timeBonusMultiplier: 10, // Multiplier for time bonus
            pairBonus: 50,           // Bonus for consecutive pairs
            maxConsecutivePairs: 10, // Max consecutive pairs for bonus
            shufflePenalty: 100      // Penalty for each shuffle
        };

        this.options = { ...this.defaultOptions, ...options };
        this.reset();
    }

    /**
     * Reset the scorer to initial state.
     */
    reset() {
        this.score = 0;
        this.consecutivePairs = 0;
        this.totalPairs = 0;
        this.startTime = Date.now();
        this.shuffleCount = 0;
    }

    /**
     * Calculate and apply score for a matched pair.
     * @param {Object} tile1 - First tile in the pair
     * @param {Object} tile2 - Second tile in the pair
     * @param {boolean} isBonusPair - Whether this is a bonus pair (e.g., season/flower)
     */
    recordPair(tile1, tile2, isBonusPair = false) {
        if (!this.isValidPair(tile1, tile2)) {
            throw new Error('Invalid tile pair');
        }

        let pairScore = this.options.baseScore;

        // Apply bonus for consecutive pairs
        this.consecutivePairs++;
        if (this.consecutivePairs <= this.options.maxConsecutivePairs) {
            pairScore += this.options.pairBonus * this.consecutivePairs;
        }

        // Double score for bonus pairs
        if (isBonusPair) {
            pairScore *= 2;
        }

        this.score += pairScore;
        this.totalPairs++;
    }

    /**
     * Check if two tiles form a valid pair.
     * @param {Object} tile1 - First tile
     * @param {Object} tile2 - Second tile
     * @returns {boolean} True if valid pair
     */
    isValidPair(tile1, tile2) {
        if (!tile1 || !tile2) return false;
        if (tile1 === tile2) return false;

        // Basic matching: same suit and value
        if (tile1.suit === tile2.suit && tile1.value === tile2.value) {
            return true;
        }

        // Special cases: seasons and flowers
        if ((tile1.suit === 'season' && tile2.suit === 'flower') ||
            (tile1.suit === 'flower' && tile2.suit === 'season')) {
            return tile1.value === tile2.value;
        }

        return false;
    }

    /**
     * Apply shuffle penalty to score.
     */
    recordShuffle() {
        this.score = Math.max(0, this.score - this.options.shufflePenalty);
        this.shuffleCount++;
        this.consecutivePairs = 0; // Reset consecutive pairs counter
    }

    /**
     * Calculate final score including time bonus if enabled.
     * @returns {Object} Final score details
     */
    calculateFinalScore() {
        const elapsedTime = (Date.now() - this.startTime) / 1000; // in seconds
        let timeBonus = 0;

        if (this.options.timeBonus) {
            timeBonus = Math.floor(Math.max(0, 300 - elapsedTime) * this.options.timeBonusMultiplier);
        }

        const finalScore = this.score + timeBonus;

        return {
            baseScore: this.score,
            timeBonus: timeBonus,
            finalScore: finalScore,
            totalPairs: this.totalPairs,
            shuffleCount: this.shuffleCount,
            gameTime: elapsedTime
        };
    }

    /**
     * Get current score without time bonus.
     * @returns {number} Current score
     */
    getCurrentScore() {
        return this.score;
    }
}

// Example usage:
// const scorer = new MahjongScorer();
// scorer.recordPair(tile1, tile2);
// const finalScore = scorer.calculateFinalScore();
```
