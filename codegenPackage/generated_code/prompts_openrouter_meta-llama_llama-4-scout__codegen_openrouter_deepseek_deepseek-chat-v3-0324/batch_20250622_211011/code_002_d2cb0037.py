"""
Generated Code Metadata:
========================
Original URL: https://claytest.vercel.app
Prompt: Generate code to implement a simple challenge system using JavaScript, focusing on enabling/disabling app functionality.
Generated: DETERMINISTIC_d2cb003756f187a8
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Challenge System Module
 * 
 * This module provides functionality to enable/disable app features based on challenge status.
 * It includes methods to activate, deactivate, and check the status of challenges.
 */

class ChallengeSystem {
  /**
   * Initialize the challenge system with default state
   * @param {Object} config - Configuration object for challenges
   * @param {boolean} config.defaultState - Default state for challenges (true=enabled, false=disabled)
   */
  constructor(config = { defaultState: false }) {
    this.challenges = new Map();
    this.defaultState = config.defaultState;
  }

  /**
   * Add a new challenge to the system
   * @param {string} challengeId - Unique identifier for the challenge
   * @param {string} description - Description of the challenge
   * @param {boolean} initialState - Initial state of the challenge
   * @throws {Error} If challengeId already exists
   */
  addChallenge(challengeId, description, initialState = this.defaultState) {
    if (this.challenges.has(challengeId)) {
      throw new Error(`Challenge with ID ${challengeId} already exists`);
    }

    this.challenges.set(challengeId, {
      description,
      isActive: initialState,
      createdAt: new Date(),
      updatedAt: new Date()
    });
  }

  /**
   * Enable a challenge
   * @param {string} challengeId - ID of the challenge to enable
   * @throws {Error} If challengeId doesn't exist
   */
  enableChallenge(challengeId) {
    this._validateChallengeExists(challengeId);
    const challenge = this.challenges.get(challengeId);
    challenge.isActive = true;
    challenge.updatedAt = new Date();
  }

  /**
   * Disable a challenge
   * @param {string} challengeId - ID of the challenge to disable
   * @throws {Error} If challengeId doesn't exist
   */
  disableChallenge(challengeId) {
    this._validateChallengeExists(challengeId);
    const challenge = this.challenges.get(challengeId);
    challenge.isActive = false;
    challenge.updatedAt = new Date();
  }

  /**
   * Toggle a challenge's state
   * @param {string} challengeId - ID of the challenge to toggle
   * @throws {Error} If challengeId doesn't exist
   */
  toggleChallenge(challengeId) {
    this._validateChallengeExists(challengeId);
    const challenge = this.challenges.get(challengeId);
    challenge.isActive = !challenge.isActive;
    challenge.updatedAt = new Date();
  }

  /**
   * Check if a challenge is active
   * @param {string} challengeId - ID of the challenge to check
   * @returns {boolean} True if challenge is active, false otherwise
   * @throws {Error} If challengeId doesn't exist
   */
  isChallengeActive(challengeId) {
    this._validateChallengeExists(challengeId);
    return this.challenges.get(challengeId).isActive;
  }

  /**
   * Get all challenges
   * @returns {Array} Array of all challenges with their details
   */
  getAllChallenges() {
    return Array.from(this.challenges.entries()).map(([id, challenge]) => ({
      id,
      ...challenge
    }));
  }

  /**
   * Validate that a challenge exists
   * @private
   * @param {string} challengeId - ID of the challenge to validate
   * @throws {Error} If challengeId doesn't exist
   */
  _validateChallengeExists(challengeId) {
    if (!this.challenges.has(challengeId)) {
      throw new Error(`Challenge with ID ${challengeId} does not exist`);
    }
  }
}

// Example usage:
// const challengeSystem = new ChallengeSystem();
// challengeSystem.addChallenge('login-challenge', 'Special login requirements');
// challengeSystem.enableChallenge('login-challenge');
// if (challengeSystem.isChallengeActive('login-challenge')) {
//   // Implement challenge-specific logic
// }

module.exports = ChallengeSystem;
```
