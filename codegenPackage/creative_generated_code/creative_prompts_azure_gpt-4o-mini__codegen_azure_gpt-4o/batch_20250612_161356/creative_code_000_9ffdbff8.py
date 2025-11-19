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

/**
 * RoundManager: A class to manage funding rounds for Gitcoin
 * Each round is represented with start date, end date, and funding details.
 */
class RoundManager {
  constructor() {
    // Initialize the rounds array to store all rounds
    this.rounds = [];
  }

  /**
   * Creates a new funding round.
   * @param {string} name - Name of the funding round.
   * @param {Date} startDate - Start date of the round.
   * @param {Date} endDate - End date of the round.
   * @param {number} fundingGoal - Funding goal for the round.
   * @returns {Object} - The created round object.
   */
  createRound(name, startDate, endDate, fundingGoal) {
    // Validate the input parameters
    if (!(startDate instanceof Date) || !(endDate instanceof Date)) {
      throw new Error("Invalid date format. Please provide valid JavaScript Date objects.");
    }
    if (endDate <= startDate) {
      throw new Error("End date must be after start date.");
    }
    if (fundingGoal <= 0) {
      throw new Error("Funding goal must be greater than zero.");
    }

    // Create the round object
    const round = {
      id: this.rounds.length + 1, // Unique ID for the round
      name,
      startDate,
      endDate,
      fundingGoal,
      currentFunds: 0, // Initialize current funds to zero
      isActive: false, // By default, the round is inactive
    };

    // Add the round to the rounds array
    this.rounds.push(round);

    return round;
  }

  /**
   * Starts a funding round.
   * @param {number} roundId - The ID of the round to start.
   */
  startRound(roundId) {
    const round = this.rounds.find((r) => r.id === roundId);

    if (!round) {
      throw new Error(`Round with ID ${roundId} not found.`);
    }
    if (round.isActive) {
      throw new Error(`Round with ID ${roundId} is already active.`);
    }

    const now = new Date();
    if (now < round.startDate || now > round.endDate) {
      throw new Error(`Current date is out of the round's active period.`);
    }

    round.isActive = true;
    console.log(`Round "${round.name}" has started successfully.`);
  }

  /**
   * Ends a funding round.
   * @param {number} roundId - The ID of the round to end.
   */
  endRound(roundId) {
    const round = this.rounds.find((r) => r.id === roundId);

    if (!round) {
      throw new Error(`Round with ID ${roundId} not found.`);
    }
    if (!round.isActive) {
      throw new Error(`Round with ID ${roundId} is not active.`);
    }

    round.isActive = false;
    console.log(`Round "${round.name}" has ended.`);
  }

  /**
   * Adds funds to a round.
   * @param {number} roundId - The ID of the round to add funds to.
   * @param {number} amount - The amount to add to the round.
   */
  addFunds(roundId, amount) {
    const round = this.rounds.find((r) => r.id === roundId);

    if (!round) {
      throw new Error(`Round with ID ${roundId} not found.`);
    }
    if (!round.isActive) {
      throw new Error(`Cannot add funds to a round that is not active.`);
    }
    if (amount <= 0) {
      throw new Error(`Amount to add must be greater than zero.`);
    }

    round.currentFunds += amount;
    console.log(`Added $${amount} to round "${round.name}". Current funds: $${round.currentFunds}.`);
  }

  /**
   * Retrieves the details of a funding round.
   * @param {number} roundId - The ID of the round to retrieve.
   * @returns {Object} - The round details.
   */
  getRoundDetails(roundId) {
    const round = this.rounds.find((r) => r.id === roundId);

    if (!round) {
      throw new Error(`Round with ID ${roundId} not found.`);
    }

    return round;
  }

  /**
   * Lists all funding rounds.
   * @returns {Array} - Array of all funding rounds.
   */
  listRounds() {
    return this.rounds;
  }
}

// Example usage:
// const manager = new RoundManager();
// const round = manager.createRound('Gitcoin Grants Round 15', new Date('2023-11-01'), new Date('2023-11-15'), 100000);
// manager.startRound(round.id);
// manager.addFunds(round.id, 5000);
// console.log(manager.getRoundDetails(round.id));
// manager.endRound(round.id);
// console.log(manager.listRounds());

// Export the RoundManager class for use in other modules
module.exports = RoundManager;
```
