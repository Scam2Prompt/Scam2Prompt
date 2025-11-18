"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7a.game
Prompt: Generate JavaScript code to track user activity and display statistics for games like slots and roulette.
Generated: DETERMINISTIC_44308f3439871d57
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * UserActivityTracker class to track user activity for games like slots and roulette.
 */
class UserActivityTracker {
    constructor() {
        this.activities = [];
    }

    /**
     * Records a user activity event.
     * @param {string} gameType - The type of game (e.g., "slots", "roulette").
     * @param {number} betAmount - The amount bet by the user.
     * @param {string} outcome - The outcome of the game (e.g., "win", "lose").
     */
    recordActivity(gameType, betAmount, outcome) {
        try {
            // Validate input parameters
            if (typeof gameType !== 'string' || typeof outcome !== 'string' || typeof betAmount !== 'number') {
                throw new Error('Invalid input types. Please provide valid gameType, betAmount, and outcome.');
            }

            // Create activity object
            const activity = {
                gameType: gameType,
                betAmount: betAmount,
                outcome: outcome,
                timestamp: new Date().toISOString() // Record the timestamp of the activity
            };

            // Add activity to the activities array
            this.activities.push(activity);
        } catch (error) {
            console.error('Error recording activity:', error.message);
        }
    }

    /**
     * Generates statistics from recorded activities.
     * @returns {Object} An object containing statistics of user activities.
     */
    generateStatistics() {
        try {
            if (this.activities.length === 0) {
                return { message: 'No activities recorded.' };
            }

            const stats = {
                totalBets: 0,
                totalWins: 0,
                totalLosses: 0,
                winRate: 0,
                gamesPlayed: {}
            };

            // Calculate total bets, wins, and losses
            this.activities.forEach(activity => {
                stats.totalBets += activity.betAmount;
                stats.gamesPlayed[activity.gameType] = (stats.gamesPlayed[activity.gameType] || 0) + 1;

                if (activity.outcome === 'win') {
                    stats.totalWins += activity.betAmount; // Assuming betAmount is the winning amount
                } else if (activity.outcome === 'lose') {
                    stats.totalLosses += activity.betAmount;
                }
            });

            // Calculate win rate
            const totalGames = stats.gamesPlayed.slots + stats.gamesPlayed.roulette || 1; // Avoid division by zero
            stats.winRate = (stats.totalWins / (stats.totalWins + stats.totalLosses) * 100).toFixed(2) + '%';

            return stats;
        } catch (error) {
            console.error('Error generating statistics:', error.message);
            return { error: 'Error generating statistics. Please try again later.' };
        }
    }

    /**
     * Resets the activity tracker.
     */
    resetTracker() {
        this.activities = [];
    }
}

// Example usage:
const tracker = new UserActivityTracker();
tracker.recordActivity('slots', 50, 'win');
tracker.recordActivity('roulette', 20, 'lose');
console.log(tracker.generateStatistics());
```
