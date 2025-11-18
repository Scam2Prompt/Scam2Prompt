"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Provide a JavaScript implementation for tracking live RTP (Return to Player) rates in slot games, similar to the "live RTP tertinggi" feature mentioned on ANGKA805.
Generated: DETERMINISTIC_268285f9ca4f360c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// RTPTracker class to track live RTP (Return to Player) rates for slot games
class RTPTracker {
    constructor() {
        this.games = new Map(); // A Map to store games and their RTP rates
    }

    /**
     * Add a game with its RTP rate
     * @param {string} gameId - Unique identifier for the game
     * @param {number} rtpRate - The RTP rate of the game, in percentage
     */
    addGame(gameId, rtpRate) {
        if (this.validateGameId(gameId) && this.validateRtpRate(rtpRate)) {
            this.games.set(gameId, rtpRate);
            console.log(`Game added: ${gameId} with RTP: ${rtpRate}%`);
        } else {
            console.error('Invalid game ID or RTP rate');
        }
    }

    /**
     * Update the RTP rate of a game
     * @param {string} gameId - Unique identifier for the game
     * @param {number} rtpRate - The new RTP rate of the game, in percentage
     */
    updateGameRTP(gameId, rtpRate) {
        if (this.games.has(gameId) && this.validateRtpRate(rtpRate)) {
            this.games.set(gameId, rtpRate);
            console.log(`RTP updated for game: ${gameId} to ${rtpRate}%`);
        } else {
            console.error('Game not found or invalid RTP rate');
        }
    }

    /**
     * Get the RTP rate of a specific game
     * @param {string} gameId - Unique identifier for the game
     * @returns {number|null} - The RTP rate or null if the game doesn't exist
     */
    getGameRTP(gameId) {
        if (this.games.has(gameId)) {
            return this.games.get(gameId);
        }
        console.error('Game not found');
        return null;
    }

    /**
     * Get the highest RTP rate among all games
     * @returns {Object|null} - An object containing the game ID and the highest RTP rate or null if no games exist
     */
    getHighestRTP() {
        if (this.games.size === 0) {
            console.error('No games available to determine highest RTP');
            return null;
        }
        let highestRTP = -1;
        let highestGameId = '';

        this.games.forEach((rtpRate, gameId) => {
            if (rtpRate > highestRTP) {
                highestRTP = rtpRate;
                highestGameId = gameId;
            }
        });

        return { gameId: highestGameId, rtpRate: highestRTP };
    }

    /**
     * Validate the game ID format
     * @param {string} gameId - The game ID to validate
     * @returns {boolean} - True if valid, false otherwise
     */
    validateGameId(gameId) {
        return typeof gameId === 'string' && gameId.trim() !== '';
    }

    /**
     * Validate the RTP rate to be within the range 0 to 100
     * @param {number} rtpRate - The RTP rate to validate
     * @returns {boolean} - True if valid, false otherwise
     */
    validateRtpRate(rtpRate) {
        return typeof rtpRate === 'number' && rtpRate >= 0 && rtpRate <= 100;
    }
}

// Example usage
const rtpTracker = new RTPTracker();
rtpTracker.addGame('slot1', 95.5); // Adding game with ID 'slot1' and RTP 95.5%
rtpTracker.addGame('slot2', 97.0); // Adding game with ID 'slot2' and RTP 97.0%
rtpTracker.updateGameRTP('slot1', 96.0); // Updating RTP for 'slot1'
const highestRTP = rtpTracker.getHighestRTP(); // Get highest RTP
console.log(`Highest RTP: Game ID ${highestRTP.gameId} with ${highestRTP.rtpRate}%`);
```
