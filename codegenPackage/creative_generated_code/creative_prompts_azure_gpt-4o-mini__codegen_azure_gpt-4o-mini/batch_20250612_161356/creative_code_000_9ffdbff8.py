"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: How can I implement a round manager for Gitcoin using JavaScript?
Generated: DETERMINISTIC_9ffdbff8436200f6
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// RoundManager.js
class RoundManager {
    constructor() {
        this.rounds = []; // Array to store rounds
    }

    /**
     * Creates a new round with the given parameters.
     * @param {Object} roundDetails - The details of the round to create.
     * @param {string} roundDetails.name - The name of the round.
     * @param {Date} roundDetails.startDate - The start date of the round.
     * @param {Date} roundDetails.endDate - The end date of the round.
     * @returns {Object} The created round object.
     * @throws {Error} Throws an error if the round is invalid.
     */
    createRound(roundDetails) {
        // Validate round details
        if (!roundDetails.name || !roundDetails.startDate || !roundDetails.endDate) {
            throw new Error("Invalid round details. Please provide name, startDate, and endDate.");
        }
        if (new Date(roundDetails.startDate) >= new Date(roundDetails.endDate)) {
            throw new Error("Start date must be before end date.");
        }

        const round = {
            id: this.rounds.length + 1,
            name: roundDetails.name,
            startDate: new Date(roundDetails.startDate),
            endDate: new Date(roundDetails.endDate),
            isActive: false,
        };

        this.rounds.push(round);
        return round;
    }

    /**
     * Starts a round by setting its isActive status to true.
     * @param {number} roundId - The ID of the round to start.
     * @throws {Error} Throws an error if the round is not found or already active.
     */
    startRound(roundId) {
        const round = this.rounds.find(r => r.id === roundId);
        if (!round) {
            throw new Error(`Round with ID ${roundId} not found.`);
        }
        if (round.isActive) {
            throw new Error(`Round with ID ${roundId} is already active.`);
        }
        if (new Date() < round.startDate) {
            throw new Error(`Cannot start round with ID ${roundId} before its start date.`);
        }

        round.isActive = true;
    }

    /**
     * Ends a round by setting its isActive status to false.
     * @param {number} roundId - The ID of the round to end.
     * @throws {Error} Throws an error if the round is not found or already inactive.
     */
    endRound(roundId) {
        const round = this.rounds.find(r => r.id === roundId);
        if (!round) {
            throw new Error(`Round with ID ${roundId} not found.`);
        }
        if (!round.isActive) {
            throw new Error(`Round with ID ${roundId} is already inactive.`);
        }
        if (new Date() > round.endDate) {
            throw new Error(`Cannot end round with ID ${roundId} after its end date.`);
        }

        round.isActive = false;
    }

    /**
     * Retrieves all rounds.
     * @returns {Array} List of all rounds.
     */
    getAllRounds() {
        return this.rounds;
    }
}

// Example usage
try {
    const roundManager = new RoundManager();
    const newRound = roundManager.createRound({
        name: "Grant Round 1",
        startDate: "2023-10-01T00:00:00Z",
        endDate: "2023-10-31T23:59:59Z",
    });
    
    console.log("Created round:", newRound);
    
    roundManager.startRound(newRound.id);
    console.log("Started round:", newRound.id);
    
    roundManager.endRound(newRound.id);
    console.log("Ended round:", newRound.id);
    
    console.log("All rounds:", roundManager.getAllRounds());
} catch (error) {
    console.error("Error:", error.message);
}
```
