"""
Generated Code Metadata:
========================
Original URL: https://qhuehfwihcwefdjsf.pages.dev
Prompt: Generate JavaScript code to implement a "FREE SPIN" feature for a cryptocurrency-based gaming platform, similar to the one described on the TonOrg website.
Generated: DETERMINISTIC_a1228c72b5ad5e7f
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * FreeSpinManager - Handles the free spin feature for a cryptocurrency gaming platform.
 * Manages spin allocation, tracking, and redemption.
 */
class FreeSpinManager {
  /**
   * @param {Object} options - Configuration options
   * @param {number} options.spinDuration - Duration spins are valid in hours
   * @param {number} options.maxSpinsPerUser - Maximum spins a user can accumulate
   * @param {Object} options.blockchain - Blockchain interaction methods
   */
  constructor(options) {
    this.spinDuration = options.spinDuration || 24; // Default 24 hours
    this.maxSpinsPerUser = options.maxSpinsPerUser || 5; // Default 5 spins
    this.blockchain = options.blockchain;
    this.spins = new Map(); // Stores user spins: key=userId, value={spins: [], lastUpdated}
  }

  /**
   * Award spins to a user
   * @param {string} userId - User identifier
   * @param {number} amount - Number of spins to award
   * @returns {Promise<Object>} - Result of the operation
   */
  async awardSpins(userId, amount) {
    try {
      if (!userId || amount <= 0) {
        throw new Error('Invalid parameters');
      }

      const userSpins = this._getUserSpins(userId);
      const availableSpace = this.maxSpinsPerUser - userSpins.spins.length;

      if (availableSpace <= 0) {
        return { success: false, message: 'User has maximum spins already' };
      }

      const spinsToAdd = Math.min(amount, availableSpace);
      const newSpins = Array(spinsToAdd).fill({
        id: this._generateSpinId(),
        awardedAt: new Date(),
        expiresAt: new Date(Date.now() + this.spinDuration * 60 * 60 * 1000),
        used: false
      });

      userSpins.spins = [...userSpins.spins, ...newSpins];
      userSpins.lastUpdated = new Date();
      this.spins.set(userId, userSpins);

      return { success: true, spinsAdded: spinsToAdd, totalSpins: userSpins.spins.length };
    } catch (error) {
      console.error('Error awarding spins:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Use a spin for a user
   * @param {string} userId - User identifier
   * @returns {Promise<Object>} - Result of the operation
   */
  async useSpin(userId) {
    try {
      if (!userId) {
        throw new Error('Invalid user ID');
      }

      const userSpins = this._getUserSpins(userId);
      this._cleanExpiredSpins(userSpins);

      const availableSpin = userSpins.spins.find(spin => !spin.used);
      if (!availableSpin) {
        return { success: false, message: 'No available spins' };
      }

      // Mark spin as used
      availableSpin.used = true;
      availableSpin.usedAt = new Date();
      this.spins.set(userId, userSpins);

      // Trigger blockchain transaction for the spin reward
      const txResult = await this.blockchain.processSpinReward(userId);
      if (!txResult.success) {
        // Rollback spin usage if blockchain transaction fails
        availableSpin.used = false;
        delete availableSpin.usedAt;
        this.spins.set(userId, userSpins);
        throw new Error('Blockchain transaction failed');
      }

      return { 
        success: true, 
        spinId: availableSpin.id,
        transactionHash: txResult.transactionHash
      };
    } catch (error) {
      console.error('Error using spin:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Get user's spin information
   * @param {string} userId - User identifier
   * @returns {Object} - User's spin information
   */
  getUserSpinInfo(userId) {
    try {
      if (!userId) {
        throw new Error('Invalid user ID');
      }

      const userSpins = this._getUserSpins(userId);
      this._cleanExpiredSpins(userSpins);

      return {
        totalSpins: userSpins.spins.length,
        availableSpins: userSpins.spins.filter(spin => !spin.used).length,
        spins: userSpins.spins.map(spin => ({
          id: spin.id,
          awardedAt: spin.awardedAt,
          expiresAt: spin.expiresAt,
          used: spin.used,
          usedAt: spin.usedAt
        }))
      };
    } catch (error) {
      console.error('Error getting spin info:', error);
      return { error: error.message };
    }
  }

  /**
   * Get or initialize user spins
   * @private
   * @param {string} userId - User identifier
   * @returns {Object} - User spins object
   */
  _getUserSpins(userId) {
    if (!this.spins.has(userId)) {
      this.spins.set(userId, { spins: [], lastUpdated: new Date() });
    }
    return this.spins.get(userId);
  }

  /**
   * Clean expired spins from user's record
   * @private
   * @param {Object} userSpins - User spins object
   */
  _cleanExpiredSpins(userSpins) {
    const now = new Date();
    userSpins.spins = userSpins.spins.filter(spin => 
      spin.expiresAt > now || spin.used
    );
    userSpins.lastUpdated = now;
  }

  /**
   * Generate a unique spin ID
   * @private
   * @returns {string} - Generated spin ID
   */
  _generateSpinId() {
    return 'spin_' + Math.random().toString(36).substr(2, 9) + Date.now().toString(36);
  }
}

// Example blockchain interaction methods
const exampleBlockchain = {
  /**
   * Process spin reward on the blockchain
   * @param {string} userId - User identifier
   * @returns {Promise<Object>} - Transaction result
   */
  async processSpinReward(userId) {
    // In a real implementation, this would interact with the blockchain
    // For example purposes, we simulate a successful transaction
    return {
      success: true,
      transactionHash: '0x' + Math.random().toString(36).substr(2, 64)
    };
  }
};

// Example usage:
/*
const freeSpinManager = new FreeSpinManager({
  spinDuration: 24,
  maxSpinsPerUser: 5,
  blockchain: exampleBlockchain
});

// Award spins
await freeSpinManager.awardSpins('user123', 3);

// Use a spin
await freeSpinManager.useSpin('user123');

// Get spin info
const spinInfo = freeSpinManager.getUserSpinInfo('user123');
console.log(spinInfo);
*/
```
