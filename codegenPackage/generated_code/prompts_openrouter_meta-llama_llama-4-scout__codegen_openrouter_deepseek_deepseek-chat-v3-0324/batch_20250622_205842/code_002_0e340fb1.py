"""
Generated Code Metadata:
========================
Original URL: https://bafkreibrmd7zoxzx2es22p5yfwvme3g2owtwkq5xurzi5rb5jtp64hlm3u.ipfs.dweb.link
Prompt: Generate JavaScript code snippet for a simple allocation checker like the one described for friend.tech's Allocation Launchpad v1.0.
Generated: DETERMINISTIC_0e340fb1443c0466
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Allocation Checker for Friend.Tech's Allocation Launchpad v1.0
 * 
 * This script checks if a user is eligible for allocation based on their points,
 * tier, and other criteria. It also calculates the exact allocation amount.
 */

class AllocationChecker {
  /**
   * @param {Object} config - Configuration object containing allocation rules
   * @param {number} config.baseAllocation - Base allocation amount
   * @param {Object} config.tierMultipliers - Multipliers for different tiers
   * @param {number} config.minPointsThreshold - Minimum points required
   * @param {number} config.maxAllocationCap - Maximum allocation cap
   */
  constructor(config) {
    this.config = {
      baseAllocation: 1000,
      tierMultipliers: {
        bronze: 1,
        silver: 1.5,
        gold: 2,
        platinum: 3
      },
      minPointsThreshold: 100,
      maxAllocationCap: 10000,
      ...config
    };
  }

  /**
   * Checks if user is eligible for allocation
   * @param {Object} user - User object
   * @param {number} user.points - User's points
   * @param {string} user.tier - User's tier (bronze|silver|gold|platinum)
   * @returns {Object} - { eligible: boolean, reason: string }
   */
  checkEligibility(user) {
    if (!user || typeof user !== 'object') {
      throw new Error('Invalid user object');
    }

    const { points, tier } = user;

    if (typeof points !== 'number' || points < 0) {
      throw new Error('Invalid points value');
    }

    if (!this.config.tierMultipliers[tier]) {
      throw new Error('Invalid tier specified');
    }

    if (points < this.config.minPointsThreshold) {
      return {
        eligible: false,
        reason: `Points below minimum threshold (${this.config.minPointsThreshold})`
      };
    }

    return {
      eligible: true,
      reason: 'User meets all eligibility criteria'
    };
  }

  /**
   * Calculates user's allocation amount
   * @param {Object} user - User object
   * @param {number} user.points - User's points
   * @param {string} user.tier - User's tier (bronze|silver|gold|platinum)
   * @returns {number} - Calculated allocation amount
   */
  calculateAllocation(user) {
    const eligibility = this.checkEligibility(user);
    if (!eligibility.eligible) {
      throw new Error(`User not eligible: ${eligibility.reason}`);
    }

    const { points, tier } = user;
    const { baseAllocation, tierMultipliers, maxAllocationCap } = this.config;

    // Calculate base allocation with tier multiplier
    let allocation = baseAllocation * tierMultipliers[tier];

    // Apply points-based scaling (1% per point over threshold)
    const pointsOverThreshold = points - this.config.minPointsThreshold;
    if (pointsOverThreshold > 0) {
      allocation += allocation * (pointsOverThreshold * 0.01);
    }

    // Apply cap if exceeded
    return Math.min(allocation, maxAllocationCap);
  }

  /**
   * Gets allocation details for a user
   * @param {Object} user - User object
   * @returns {Object} - Allocation details
   */
  getAllocationDetails(user) {
    try {
      const eligibility = this.checkEligibility(user);
      if (!eligibility.eligible) {
        return eligibility;
      }

      const allocation = this.calculateAllocation(user);
      return {
        eligible: true,
        allocation: Math.floor(allocation),
        tier: user.tier,
        points: user.points,
        maxAllocationCap: this.config.maxAllocationCap
      };
    } catch (error) {
      console.error('Error calculating allocation:', error.message);
      return {
        eligible: false,
        reason: error.message
      };
    }
  }
}

// Example usage:
/*
const checker = new AllocationChecker();
const user = {
  points: 150,
  tier: 'gold'
};

const result = checker.getAllocationDetails(user);
console.log(result);
*/
```
