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
 * Challenge System Implementation
 * 
 * This module provides a simple challenge system to enable/disable app functionality.
 * 
 * @module ChallengeSystem
 */

class ChallengeSystem {
  /**
   * Creates an instance of ChallengeSystem.
   * 
   * @param {Object} challenges - An object containing challenge configurations.
   */
  constructor(challenges) {
    /**
     * Challenge configurations.
     * 
     * @type {Object}
     */
    this.challenges = challenges;

    /**
     * Current challenge status.
     * 
     * @type {Object}
     */
    this.status = {};

    // Initialize challenge status
    Object.keys(challenges).forEach((challengeId) => {
      this.status[challengeId] = challenges[challengeId].enabled;
    });
  }

  /**
   * Enables a challenge.
   * 
   * @param {string} challengeId - The ID of the challenge to enable.
   * @throws {Error} If the challenge does not exist.
   */
  enableChallenge(challengeId) {
    if (!this.challenges[challengeId]) {
      throw new Error(`Challenge '${challengeId}' does not exist.`);
    }

    this.status[challengeId] = true;
  }

  /**
   * Disables a challenge.
   * 
   * @param {string} challengeId - The ID of the challenge to disable.
   * @throws {Error} If the challenge does not exist.
   */
  disableChallenge(challengeId) {
    if (!this.challenges[challengeId]) {
      throw new Error(`Challenge '${challengeId}' does not exist.`);
    }

    this.status[challengeId] = false;
  }

  /**
   * Checks if a challenge is enabled.
   * 
   * @param {string} challengeId - The ID of the challenge to check.
   * @returns {boolean} True if the challenge is enabled, false otherwise.
   * @throws {Error} If the challenge does not exist.
   */
  isChallengeEnabled(challengeId) {
    if (!this.challenges[challengeId]) {
      throw new Error(`Challenge '${challengeId}' does not exist.`);
    }

    return this.status[challengeId];
  }

  /**
   * Checks if a feature is enabled based on the challenge status.
   * 
   * @param {string} featureId - The ID of the feature to check.
   * @param {string} challengeId - The ID of the challenge associated with the feature.
   * @returns {boolean} True if the feature is enabled, false otherwise.
   * @throws {Error} If the challenge or feature does not exist.
   */
  isFeatureEnabled(featureId, challengeId) {
    if (!this.challenges[challengeId]) {
      throw new Error(`Challenge '${challengeId}' does not exist.`);
    }

    if (!this.challenges[challengeId].features || !this.challenges[challengeId].features.includes(featureId)) {
      throw new Error(`Feature '${featureId}' does not exist for challenge '${challengeId}'.`);
    }

    return this.isChallengeEnabled(challengeId);
  }
}

// Example usage
const challenges = {
  challenge1: {
    enabled: true,
    features: ['feature1', 'feature2']
  },
  challenge2: {
    enabled: false,
    features: ['feature3']
  }
};

const challengeSystem = new ChallengeSystem(challenges);

try {
  console.log(challengeSystem.isChallengeEnabled('challenge1')); // Output: true
  console.log(challengeSystem.isFeatureEnabled('feature1', 'challenge1')); // Output: true

  challengeSystem.disableChallenge('challenge1');
  console.log(challengeSystem.isChallengeEnabled('challenge1')); // Output: false
  console.log(challengeSystem.isFeatureEnabled('feature1', 'challenge1')); // Output: false
} catch (error) {
  console.error(error.message);
}
```
