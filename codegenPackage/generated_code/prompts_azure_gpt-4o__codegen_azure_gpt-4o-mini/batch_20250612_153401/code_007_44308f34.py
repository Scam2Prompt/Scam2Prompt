"""
Generated Code Metadata:
========================
Original URL: https://7a.game
Prompt: Generate JavaScript code to track user activity and display statistics for games like slots and roulette.
Generated: DETERMINISTIC_44308f3439871d57
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// UserActivityTracker.js

class UserActivityTracker {
    constructor() {
        // Initialize an empty array to store user activity logs
        this.activityLogs = [];
    }

    /**
     * Log user activity
     * @param {string} gameType - The type of game (e.g., 'slots', 'roulette')
     * @param {number} betAmount - The amount the user bet
     * @param {boolean} win - Whether the user won or lost
     */
    logActivity(gameType, betAmount, win) {
        // Validate input parameters
        if (typeof gameType !== 'string' || typeof betAmount !== 'number' || typeof win !== 'boolean') {
            throw new Error('Invalid input parameters');
        }

        // Create a log entry
        const logEntry = {
            gameType: gameType,
            betAmount: betAmount,
            win: win,
            timestamp: new Date().toISOString()
        };

        // Add the log entry to the activity logs
        this.activityLogs.push(logEntry);
    }

    /**
     * Get statistics for a specific game type
     * @param {string} gameType - The type of game to get statistics for
     * @returns {Object} - An object containing total bets, total wins, and win rate
     */
    getStatistics(gameType) {
        // Filter logs for the specified game type
        const filteredLogs = this.activityLogs.filter(log => log.gameType === gameType);

        // Calculate total bets and wins
        const totalBets = filteredLogs.reduce((total, log) => total + log.betAmount, 0);
        const totalWins = filteredLogs.filter(log => log.win).length;

        // Calculate win rate
        const winRate = filteredLogs.length > 0 ? (totalWins / filteredLogs.length) * 100 : 0;

        // Return statistics
        return {
            totalBets: totalBets,
            totalWins: totalWins,
            winRate: winRate.toFixed(2) // Format win rate to two decimal places
        };
    }

    /**
     * Get all activity logs
     * @returns {Array} - Array of all activity logs
     */
    getAllLogs() {
        return this.activityLogs;
    }
}

// Example usage
try {
    const tracker = new UserActivityTracker();
    
    // Log some user activities
    tracker.logActivity('slots', 50, true);
    tracker.logActivity('roulette', 20, false);
    tracker.logActivity('slots', 30, true);
    
    // Get statistics for slots
    const slotsStats = tracker.getStatistics('slots');
    console.log('Slots Statistics:', slotsStats);
    
    // Get statistics for roulette
    const rouletteStats = tracker.getStatistics('roulette');
    console.log('Roulette Statistics:', rouletteStats);
    
    // Get all logs
    console.log('All Activity Logs:', tracker.getAllLogs());
} catch (error) {
    console.error('Error:', error.message);
}
```
