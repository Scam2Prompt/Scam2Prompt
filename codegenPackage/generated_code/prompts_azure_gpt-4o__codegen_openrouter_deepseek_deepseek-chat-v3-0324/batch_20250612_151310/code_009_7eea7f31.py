"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Design a simulation in JavaScript to model the aggressive behavior of Wolves in Wolf Game, including scenarios where they steal Sheep and resources from other players.
Generated: DETERMINISTIC_7eea7f31c2eac62e
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Wolf Game Simulation
 * Models aggressive behavior of Wolves, including stealing Sheep and resources.
 */

class Player {
    constructor(id, type, sheepCount = 0, resources = 0) {
        this.id = id;
        this.type = type; // 'wolf' or 'shepherd'
        this.sheepCount = sheepCount;
        this.resources = resources;
    }

    /**
     * Add sheep to the player's count
     * @param {number} count - Number of sheep to add
     */
    addSheep(count) {
        this.sheepCount += count;
    }

    /**
     * Remove sheep from the player's count
     * @param {number} count - Number of sheep to remove
     * @returns {boolean} True if sheep were removed, false if not enough sheep
     */
    removeSheep(count) {
        if (this.sheepCount >= count) {
            this.sheepCount -= count;
            return true;
        }
        return false;
    }

    /**
     * Add resources to the player
     * @param {number} amount - Amount of resources to add
     */
    addResources(amount) {
        this.resources += amount;
    }

    /**
     * Remove resources from the player
     * @param {number} amount - Amount of resources to remove
     * @returns {boolean} True if resources were removed, false if not enough
     */
    removeResources(amount) {
        if (this.resources >= amount) {
            this.resources -= amount;
            return true;
        }
        return false;
    }
}

class WolfGame {
    constructor() {
        this.players = new Map();
        this.nextPlayerId = 1;
    }

    /**
     * Add a new player to the game
     * @param {string} type - 'wolf' or 'shepherd'
     * @param {number} initialSheep - Initial sheep count
     * @param {number} initialResources - Initial resources
     * @returns {number} The ID of the new player
     */
    addPlayer(type, initialSheep = 0, initialResources = 0) {
        const id = this.nextPlayerId++;
        this.players.set(id, new Player(id, type, initialSheep, initialResources));
        return id;
    }

    /**
     * Simulate a wolf attacking a shepherd to steal sheep and resources
     * @param {number} wolfId - ID of the wolf player
     * @param {number} shepherdId - ID of the shepherd player
     * @param {number} maxStealAttempt - Maximum number of sheep/resources to attempt to steal
     * @returns {object} Result of the attack { success: boolean, sheepStolen: number, resourcesStolen: number }
     */
    wolfAttack(wolfId, shepherdId, maxStealAttempt) {
        const wolf = this.players.get(wolfId);
        const shepherd = this.players.get(shepherdId);

        // Validate players exist and are correct types
        if (!wolf || !shepherd || wolf.type !== 'wolf' || shepherd.type !== 'shepherd') {
            throw new Error('Invalid player types for wolf attack');
        }

        // Calculate actual amounts to steal (can't steal more than available)
        const sheepToSteal = Math.min(
            maxStealAttempt,
            shepherd.sheepCount
        );
        const resourcesToSteal = Math.min(
            maxStealAttempt,
            shepherd.resources
        );

        // Attempt to steal
        const sheepStolen = shepherd.removeSheep(sheepToSteal) ? sheepToSteal : 0;
        const resourcesStolen = shepherd.removeResources(resourcesToSteal) ? resourcesToSteal : 0;

        if (sheepStolen > 0 || resourcesStolen > 0) {
            wolf.addSheep(sheepStolen);
            wolf.addResources(resourcesStolen);
            return {
                success: true,
                sheepStolen,
                resourcesStolen
            };
        }

        return {
            success: false,
            sheepStolen: 0,
            resourcesStolen: 0
        };
    }

    /**
     * Simulate random wolf behavior across all players
     * @param {number} maxStealAttempt - Maximum number of sheep/resources to attempt to steal per attack
     * @returns {Array} Array of attack results
     */
    simulateWolfBehavior(maxStealAttempt = 3) {
        const wolves = Array.from(this.players.values()).filter(p => p.type === 'wolf');
        const shepherds = Array.from(this.players.values()).filter(p => p.type === 'shepherd');

        if (wolves.length === 0 || shepherds.length === 0) {
            return [];
        }

        const attackResults = [];

        wolves.forEach(wolf => {
            // Select a random shepherd to attack
            const randomShepherd = shepherds[Math.floor(Math.random() * shepherds.length)];
            const result = this.wolfAttack(wolf.id, randomShepherd.id, maxStealAttempt);
            attackResults.push({
                wolfId: wolf.id,
                shepherdId: randomShepherd.id,
                ...result
            });
        });

        return attackResults;
    }

    /**
     * Get the current game state
     * @returns {object} Object containing all players and their stats
     */
    getGameState() {
        return Array.from(this.players.values()).map(player => ({
            id: player.id,
            type: player.type,
            sheepCount: player.sheepCount,
            resources: player.resources
        }));
    }
}

// Example usage:
/*
const game = new WolfGame();

// Add players
const wolf1 = game.addPlayer('wolf');
const shepherd1 = game.addPlayer('shepherd', 10, 50);
const shepherd2 = game.addPlayer('shepherd', 5, 30);

// Simulate wolf behavior
const results = game.simulateWolfBehavior();

console.log('Attack results:', results);
console.log('Game state:', game.getGameState());
*/
```
