"""
Generated Code Metadata:
========================
Original URL: https://globaljournalpress.com
Prompt: Create a JavaScript function that analyzes the psychology behind online slots, focusing on user engagement metrics and player behavior.
Generated: DETERMINISTIC_cb93e17d4dd5afa4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Analyzes the psychology behind online slots by tracking user engagement metrics and player behavior.
 * 
 * @class SlotPsychologyAnalyzer
 */
class SlotPsychologyAnalyzer {
    /**
     * Creates an instance of SlotPsychologyAnalyzer.
     * @param {Object} config - Configuration object for the analyzer
     * @param {number} config.sessionTimeout - Time in minutes before a session is considered expired
     */
    constructor(config = { sessionTimeout: 30 }) {
        this.sessionTimeout = config.sessionTimeout * 60 * 1000; // Convert to milliseconds
        this.sessions = new Map(); // Stores player sessions
        this.metrics = {
            totalSpins: 0,
            totalWins: 0,
            totalLosses: 0,
            averageBet: 0,
            maxWin: 0,
            maxLoss: 0,
            playerCount: 0
        };
    }

    /**
     * Starts a new player session or updates an existing one
     * @param {string} playerId - Unique identifier for the player
     * @returns {string} Session ID
     */
    startSession(playerId) {
        const now = Date.now();
        const sessionId = `session_${now}_${Math.random().toString(36).substr(2, 9)}`;
        
        this.sessions.set(sessionId, {
            playerId,
            startTime: now,
            lastActivity: now,
            spins: 0,
            bets: [],
            wins: 0,
            losses: 0,
            currentStreak: 0,
            maxWinStreak: 0,
            maxLossStreak: 0
        });

        this.metrics.playerCount = this.sessions.size;
        return sessionId;
    }

    /**
     * Records a spin event for a player
     * @param {string} sessionId - The session ID
     * @param {number} betAmount - The amount bet on this spin
     * @param {number} winAmount - The amount won (0 if lost)
     * @throws {Error} If session is invalid or expired
     */
    recordSpin(sessionId, betAmount, winAmount) {
        this._validateSession(sessionId);
        
        const session = this.sessions.get(sessionId);
        const now = Date.now();
        
        // Update session
        session.lastActivity = now;
        session.spins++;
        session.bets.push(betAmount);
        
        // Update streak
        if (winAmount > 0) {
            session.wins++;
            session.currentStreak = Math.max(1, session.currentStreak + 1);
            session.maxWinStreak = Math.max(session.maxWinStreak, session.currentStreak);
        } else {
            session.losses++;
            session.currentStreak = Math.min(-1, session.currentStreak - 1);
            session.maxLossStreak = Math.min(session.maxLossStreak, session.currentStreak);
        }

        // Update global metrics
        this.metrics.totalSpins++;
        if (winAmount > 0) {
            this.metrics.totalWins++;
            this.metrics.maxWin = Math.max(this.metrics.maxWin, winAmount);
        } else {
            this.metrics.totalLosses++;
            this.metrics.maxLoss = Math.max(this.metrics.maxLoss, betAmount);
        }
        
        // Update average bet
        const totalBet = session.bets.reduce((sum, bet) => sum + bet, 0);
        this.metrics.averageBet = totalBet / session.bets.length;
    }

    /**
     * Gets player engagement metrics for a session
     * @param {string} sessionId - The session ID
     * @returns {Object} Engagement metrics
     * @throws {Error} If session is invalid or expired
     */
    getSessionMetrics(sessionId) {
        this._validateSession(sessionId);
        const session = this.sessions.get(sessionId);
        
        return {
            sessionDuration: (Date.now() - session.startTime) / 1000 / 60, // in minutes
            spinRate: session.spins / ((Date.now() - session.startTime) / 1000 / 60), // spins per minute
            winRate: session.wins / session.spins,
            lossRate: session.losses / session.spins,
            maxWinStreak: session.maxWinStreak,
            maxLossStreak: Math.abs(session.maxLossStreak),
            averageBet: session.bets.reduce((sum, bet) => sum + bet, 0) / session.bets.length
        };
    }

    /**
     * Gets aggregated metrics across all sessions
     * @returns {Object} Global metrics
     */
    getGlobalMetrics() {
        return {
            ...this.metrics,
            winRate: this.metrics.totalWins / this.metrics.totalSpins,
            lossRate: this.metrics.totalLosses / this.metrics.totalSpins
        };
    }

    /**
     * Cleans up expired sessions
     */
    cleanupSessions() {
        const now = Date.now();
        for (const [sessionId, session] of this.sessions.entries()) {
            if (now - session.lastActivity > this.sessionTimeout) {
                this.sessions.delete(sessionId);
            }
        }
        this.metrics.playerCount = this.sessions.size;
    }

    /**
     * Validates a session exists and is not expired
     * @private
     * @param {string} sessionId - The session ID to validate
     * @throws {Error} If session is invalid or expired
     */
    _validateSession(sessionId) {
        if (!this.sessions.has(sessionId)) {
            throw new Error('Invalid session ID');
        }
        
        const session = this.sessions.get(sessionId);
        if (Date.now() - session.lastActivity > this.sessionTimeout) {
            this.sessions.delete(sessionId);
            throw new Error('Session has expired');
        }
    }
}

// Example usage:
// const analyzer = new SlotPsychologyAnalyzer({ sessionTimeout: 30 });
// const sessionId = analyzer.startSession('player123');
// analyzer.recordSpin(sessionId, 10, 0); // Lost 10
// analyzer.recordSpin(sessionId, 10, 15); // Won 15
// console.log(analyzer.getSessionMetrics(sessionId));
// console.log(analyzer.getGlobalMetrics());
// analyzer.cleanupSessions();
```
