"""
Generated Code Metadata:
========================
Original URL: https://dflow-reward.pages.dev
Prompt: Generate JavaScript code to implement a rewards system with phases, such as Phase 0: Early Access and Phase 1: App launch.
Generated: DETERMINISTIC_f2b24363f7e030a1
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * RewardsSystem - A class to manage reward phases and user rewards.
 */
class RewardsSystem {
  /**
   * @constructor
   * @param {Object} phasesConfig - Configuration for reward phases
   */
  constructor(phasesConfig) {
    this.phases = phasesConfig;
    this.currentPhase = null;
    this.users = new Map();
  }

  /**
   * Initialize the rewards system with the starting phase
   * @param {string} phaseName - Name of the starting phase
   * @throws {Error} If phase doesn't exist in configuration
   */
  initialize(phaseName) {
    if (!this.phases[phaseName]) {
      throw new Error(`Phase ${phaseName} not found in configuration`);
    }
    this.currentPhase = phaseName;
  }

  /**
   * Transition to a new phase
   * @param {string} newPhase - Name of the new phase
   * @throws {Error} If phase doesn't exist or transition is invalid
   */
  transitionPhase(newPhase) {
    if (!this.phases[newPhase]) {
      throw new Error(`Phase ${newPhase} not found in configuration`);
    }

    if (this.phases[this.currentPhase].allowedTransitions &&
        !this.phases[this.currentPhase].allowedTransitions.includes(newPhase)) {
      throw new Error(`Invalid transition from ${this.currentPhase} to ${newPhase}`);
    }

    this.currentPhase = newPhase;
  }

  /**
   * Add a user to the rewards system
   * @param {string} userId - Unique identifier for the user
   * @param {Object} userData - Additional user data
   */
  addUser(userId, userData = {}) {
    if (this.users.has(userId)) {
      throw new Error(`User ${userId} already exists`);
    }
    this.users.set(userId, {
      ...userData,
      points: 0,
      rewards: []
    });
  }

  /**
   * Award points to a user
   * @param {string} userId - User to award points to
   * @param {number} points - Points to award
   * @throws {Error} If user doesn't exist or points are invalid
   */
  awardPoints(userId, points) {
    if (!this.users.has(userId)) {
      throw new Error(`User ${userId} not found`);
    }
    if (typeof points !== 'number' || points <= 0) {
      throw new Error('Points must be a positive number');
    }

    const user = this.users.get(userId);
    user.points += points;
  }

  /**
   * Redeem a reward for a user
   * @param {string} userId - User redeeming the reward
   * @param {string} rewardId - Reward to redeem
   * @throws {Error} If user doesn't exist, reward isn't available, or user doesn't have enough points
   */
  redeemReward(userId, rewardId) {
    if (!this.users.has(userId)) {
      throw new Error(`User ${userId} not found`);
    }

    const user = this.users.get(userId);
    const reward = this.phases[this.currentPhase].rewards.find(r => r.id === rewardId);

    if (!reward) {
      throw new Error(`Reward ${rewardId} not available in current phase`);
    }

    if (user.points < reward.pointsRequired) {
      throw new Error(`User doesn't have enough points for this reward`);
    }

    user.points -= reward.pointsRequired;
    user.rewards.push({
      id: rewardId,
      name: reward.name,
      redeemedAt: new Date()
    });
  }

  /**
   * Get current phase information
   * @returns {Object} Current phase details
   */
  getCurrentPhase() {
    return {
      name: this.currentPhase,
      ...this.phases[this.currentPhase]
    };
  }

  /**
   * Get user information
   * @param {string} userId - User to get information for
   * @returns {Object} User details
   * @throws {Error} If user doesn't exist
   */
  getUser(userId) {
    if (!this.users.has(userId)) {
      throw new Error(`User ${userId} not found`);
    }
    return this.users.get(userId);
  }
}

// Example configuration
const phasesConfig = {
  'Phase 0: Early Access': {
    description: 'Early access phase with limited rewards',
    allowedTransitions: ['Phase 1: App Launch'],
    rewards: [
      { id: 'early-badge', name: 'Early Supporter Badge', pointsRequired: 100 },
      { id: 'beta-access', name: 'Extended Beta Access', pointsRequired: 250 }
    ]
  },
  'Phase 1: App Launch': {
    description: 'Public launch phase with full rewards',
    allowedTransitions: ['Phase 2: Seasonal'],
    rewards: [
      { id: 'launch-badge', name: 'Launch Participant Badge', pointsRequired: 150 },
      { id: 'premium-trial', name: 'Premium 30-day Trial', pointsRequired: 300 }
    ]
  },
  'Phase 2: Seasonal': {
    description: 'Seasonal rewards phase',
    rewards: [
      { id: 'seasonal-badge', name: 'Seasonal Participant Badge', pointsRequired: 200 },
      { id: 'exclusive-content', name: 'Exclusive Seasonal Content', pointsRequired: 500 }
    ]
  }
};

// Example usage
const rewardsSystem = new RewardsSystem(phasesConfig);
rewardsSystem.initialize('Phase 0: Early Access');
rewardsSystem.addUser('user123', { name: 'John Doe' });
rewardsSystem.awardPoints('user123', 150);
rewardsSystem.redeemReward('user123', 'early-badge');
rewardsSystem.transitionPhase('Phase 1: App Launch');
```
