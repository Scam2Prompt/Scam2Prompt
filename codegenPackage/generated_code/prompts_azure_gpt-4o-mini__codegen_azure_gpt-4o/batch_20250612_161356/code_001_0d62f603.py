"""
Generated Code Metadata:
========================
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: What JavaScript functionalities are required to run the Gitcoin Round Manager app?
Generated: DETERMINISTIC_0d62f60369a986ba
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Gitcoin Round Manager App
 * This script provides the core functionalities required to manage Gitcoin rounds.
 * It includes features for creating rounds, managing contributions, and calculating results.
 * 
 * Author: [Your Name]
 * Date: [Today's Date]
 */

// Ensure strict mode for better error handling and cleaner code
"use strict";

/**
 * RoundManager class to encapsulate all functionalities related to Gitcoin rounds.
 */
class RoundManager {
  constructor() {
    // Initialize rounds and contributions
    this.rounds = [];
    this.contributions = {};
  }

  /**
   * Create a new round.
   * @param {string} roundName - Name of the round.
   * @param {Date} startDate - Start date of the round.
   * @param {Date} endDate - End date of the round.
   * @returns {object} - The created round object.
   */
  createRound(roundName, startDate, endDate) {
    if (!roundName || !startDate || !endDate) {
      throw new Error("Invalid input: roundName, startDate, and endDate are required.");
    }

    const newRound = {
      id: this.rounds.length + 1,
      name: roundName,
      startDate: new Date(startDate),
      endDate: new Date(endDate),
      contributions: [],
    };

    this.rounds.push(newRound);
    return newRound;
  }

  /**
   * Add a contribution to a specific round.
   * @param {number} roundId - ID of the round.
   * @param {string} contributor - Name of the contributor.
   * @param {number} amount - Contribution amount.
   * @returns {object} - The updated round object.
   */
  addContribution(roundId, contributor, amount) {
    if (!roundId || !contributor || !amount || amount <= 0) {
      throw new Error("Invalid input: roundId, contributor, and a positive amount are required.");
    }

    const round = this.rounds.find((r) => r.id === roundId);
    if (!round) {
      throw new Error(`Round with ID ${roundId} not found.`);
    }

    const contribution = { contributor, amount };
    round.contributions.push(contribution);

    // Track contributions globally
    if (!this.contributions[contributor]) {
      this.contributions[contributor] = 0;
    }
    this.contributions[contributor] += amount;

    return round;
  }

  /**
   * Calculate total contributions for a specific round.
   * @param {number} roundId - ID of the round.
   * @returns {number} - Total contributions for the round.
   */
  calculateTotalContributions(roundId) {
    const round = this.rounds.find((r) => r.id === roundId);
    if (!round) {
      throw new Error(`Round with ID ${roundId} not found.`);
    }

    return round.contributions.reduce((total, contribution) => total + contribution.amount, 0);
  }

  /**
   * Get all contributions made by a specific contributor.
   * @param {string} contributor - Name of the contributor.
   * @returns {number} - Total contributions made by the contributor.
   */
  getContributorTotal(contributor) {
    if (!contributor) {
      throw new Error("Invalid input: contributor name is required.");
    }

    return this.contributions[contributor] || 0;
  }

  /**
   * List all rounds.
   * @returns {Array} - Array of all rounds.
   */
  listRounds() {
    return this.rounds;
  }
}

// Example usage
try {
  const manager = new RoundManager();

  // Create rounds
  const round1 = manager.createRound("Round 1", "2023-10-01", "2023-10-15");
  const round2 = manager.createRound("Round 2", "2023-11-01", "2023-11-15");

  console.log("Created Rounds:", manager.listRounds());

  // Add contributions
  manager.addContribution(round1.id, "Alice", 100);
  manager.addContribution(round1.id, "Bob", 200);
  manager.addContribution(round2.id, "Alice", 150);

  console.log("Total Contributions for Round 1:", manager.calculateTotalContributions(round1.id));
  console.log("Total Contributions for Alice:", manager.getContributorTotal("Alice"));
} catch (error) {
  console.error("Error:", error.message);
}
```
