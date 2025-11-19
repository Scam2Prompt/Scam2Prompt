"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Create a function in JavaScript that models the "Poop AI" described in SIMemes, including its role in token management and adapting to player actions.
Generated: DETERMINISTIC_db9ad31493d2b7c7
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * PoopAI - A token management system that adapts to player actions.
 * 
 * @class PoopAI
 */
class PoopAI {
    /**
     * Creates an instance of PoopAI.
     * @param {Object} config - Configuration object for the AI.
     * @param {number} config.initialTokens - Initial number of tokens.
     * @param {number} config.maxTokens - Maximum number of tokens allowed.
     * @param {number} config.tokenRegenRate - Rate at which tokens regenerate per tick.
     */
    constructor(config) {
        this.tokens = config.initialTokens || 10;
        this.maxTokens = config.maxTokens || 20;
        this.tokenRegenRate = config.tokenRegenRate || 1;
        this.players = new Map();
        this.adaptationRate = 0.1;
        this.history = [];
    }

    /**
     * Registers a player with the AI system.
     * @param {string} playerId - Unique identifier for the player.
     */
    registerPlayer(playerId) {
        if (!this.players.has(playerId)) {
            this.players.set(playerId, {
                tokenUsage: 0,
                lastAction: null,
                adaptationFactor: 1.0
            });
        }
    }

    /**
     * Updates token count based on regeneration rate.
     */
    regenerateTokens() {
        this.tokens = Math.min(this.tokens + this.tokenRegenRate, this.maxTokens);
    }

    /**
     * Attempts to spend tokens for a player action.
     * @param {string} playerId - Player requesting tokens.
     * @param {number} requestedTokens - Number of tokens requested.
     * @returns {boolean} True if tokens were spent, false otherwise.
     */
    spendTokens(playerId, requestedTokens) {
        if (!this.players.has(playerId)) {
            throw new Error(`Player ${playerId} not registered`);
        }

        if (requestedTokens <= 0 || requestedTokens > this.tokens) {
            return false;
        }

        const player = this.players.get(playerId);
        this.tokens -= requestedTokens;
        player.tokenUsage += requestedTokens;
        player.lastAction = Date.now();

        this.history.push({
            playerId,
            tokensSpent: requestedTokens,
            timestamp: Date.now()
        });

        this.adaptToPlayerBehavior(playerId);
        return true;
    }

    /**
     * Adapts token costs based on player behavior.
     * @param {string} playerId - Player to adapt to.
     */
    adaptToPlayerBehavior(playerId) {
        const player = this.players.get(playerId);
        if (!player) return;

        // Calculate average token usage across all players
        let totalUsage = 0;
        let playerCount = 0;
        this.players.forEach(p => {
            totalUsage += p.tokenUsage;
            playerCount++;
        });

        const avgUsage = totalUsage / playerCount;

        // Adjust adaptation factor based on player's usage compared to average
        if (player.tokenUsage > avgUsage * 1.5) {
            player.adaptationFactor = Math.min(
                player.adaptationFactor + this.adaptationRate,
                2.0
            );
        } else if (player.tokenUsage < avgUsage * 0.5) {
            player.adaptationFactor = Math.max(
                player.adaptationFactor - this.adaptationRate,
                0.5
            );
        }
    }

    /**
     * Gets the effective token cost for a player after adaptation.
     * @param {string} playerId - Player to check.
     * @param {number} baseCost - Base token cost.
     * @returns {number} Adjusted token cost.
     */
    getAdjustedTokenCost(playerId, baseCost) {
        const player = this.players.get(playerId);
        if (!player) return baseCost;

        return Math.ceil(baseCost * player.adaptationFactor);
    }

    /**
     * Processes a player action with token management.
     * @param {string} playerId - Player performing the action.
     * @param {number} baseCost - Base token cost of the action.
     * @returns {boolean} True if action was successful, false if insufficient tokens.
     */
    processAction(playerId, baseCost) {
        this.registerPlayer(playerId);
        const adjustedCost = this.getAdjustedTokenCost(playerId, baseCost);

        if (this.spendTokens(playerId, adjustedCost)) {
            this.regenerateTokens();
            return true;
        }
        return false;
    }

    /**
     * Gets the current token count.
     * @returns {number} Current number of tokens.
     */
    getTokenCount() {
        return this.tokens;
    }

    /**
     * Gets player-specific information.
     * @param {string} playerId - Player to query.
     * @returns {Object|null} Player data or null if not found.
     */
    getPlayerInfo(playerId) {
        return this.players.get(playerId) || null;
    }
}

// Example usage:
// const poopAI = new PoopAI({
//     initialTokens: 15,
//     maxTokens: 30,
//     tokenRegenRate: 2
// });
// 
// poopAI.registerPlayer('player1');
// const success = poopAI.processAction('player1', 5);
// console.log(success ? "Action successful" : "Insufficient tokens");
```
