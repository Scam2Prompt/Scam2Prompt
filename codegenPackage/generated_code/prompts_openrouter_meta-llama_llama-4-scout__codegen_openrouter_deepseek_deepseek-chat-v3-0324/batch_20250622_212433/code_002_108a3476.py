"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Generate a JavaScript code snippet to implement a simple "farm and level up" system, similar to Farmville, within the SIMemes game environment.
Generated: DETERMINISTIC_108a34761bf8bb81
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Farm and Level Up System for SIMemes Game
 * 
 * This module implements a simple farming system where players can:
 * - Plant and harvest crops
 * - Gain experience points (XP)
 * - Level up based on accumulated XP
 */

class FarmSystem {
  constructor() {
    this.crops = [];
    this.inventory = {};
    this.experience = 0;
    this.level = 1;
    this.levelThresholds = this._calculateLevelThresholds();
    this._initializeDefaultInventory();
  }

  /**
   * Pre-calculate XP required for each level (scales exponentially)
   * @private
   */
  _calculateLevelThresholds() {
    const thresholds = {};
    for (let i = 1; i <= 50; i++) {
      thresholds[i] = Math.floor(100 * Math.pow(1.2, i - 1));
    }
    return thresholds;
  }

  /**
   * Initialize default inventory with basic items
   * @private
   */
  _initializeDefaultInventory() {
    this.inventory = {
      seeds: {
        wheat: 5,
        carrot: 3,
        potato: 2
      },
      crops: {
        wheat: 0,
        carrot: 0,
        potato: 0
      }
    };
  }

  /**
   * Plant a crop
   * @param {string} cropType - Type of crop to plant
   * @param {number} quantity - Number of crops to plant
   * @returns {boolean} True if planting was successful
   */
  plantCrop(cropType, quantity = 1) {
    if (!this.inventory.seeds[cropType] || this.inventory.seeds[cropType] < quantity) {
      console.error(`Not enough ${cropType} seeds to plant`);
      return false;
    }

    this.inventory.seeds[cropType] -= quantity;
    
    const growthTime = this._getGrowthTime(cropType);
    const harvestTime = Date.now() + growthTime;
    
    for (let i = 0; i < quantity; i++) {
      this.crops.push({
        type: cropType,
        plantedAt: Date.now(),
        harvestAt: harvestTime,
        isReady: false
      });
    }

    console.log(`Planted ${quantity} ${cropType}(s)`);
    return true;
  }

  /**
   * Get growth time for a crop type (in milliseconds)
   * @private
   * @param {string} cropType 
   * @returns {number} Growth time in ms
   */
  _getGrowthTime(cropType) {
    const growthTimes = {
      wheat: 30000,    // 30 seconds
      carrot: 60000,   // 1 minute
      potato: 120000   // 2 minutes
    };
    return growthTimes[cropType] || 30000;
  }

  /**
   * Check and update crop statuses
   * @private
   */
  _updateCropStatuses() {
    const now = Date.now();
    this.crops.forEach(crop => {
      if (!crop.isReady && now >= crop.harvestAt) {
        crop.isReady = true;
      }
    });
  }

  /**
   * Harvest ready crops
   * @returns {Object} Harvest results { harvested: number, xpGained: number }
   */
  harvestCrops() {
    this._updateCropStatuses();
    const readyCrops = this.crops.filter(crop => crop.isReady);
    
    if (readyCrops.length === 0) {
      console.log("No crops ready for harvest");
      return { harvested: 0, xpGained: 0 };
    }

    let xpGained = 0;
    readyCrops.forEach(crop => {
      this.inventory.crops[crop.type] = (this.inventory.crops[crop.type] || 0) + 1;
      xpGained += this._getXpForCrop(crop.type);
    });

    // Remove harvested crops
    this.crops = this.crops.filter(crop => !crop.isReady);
    
    this._addExperience(xpGained);
    
    console.log(`Harvested ${readyCrops.length} crops and gained ${xpGained} XP`);
    return {
      harvested: readyCrops.length,
      xpGained: xpGained
    };
  }

  /**
   * Get XP value for a crop type
   * @private
   * @param {string} cropType 
   * @returns {number} XP value
   */
  _getXpForCrop(cropType) {
    const xpValues = {
      wheat: 10,
      carrot: 15,
      potato: 20
    };
    return xpValues[cropType] || 5;
  }

  /**
   * Add experience points and check for level up
   * @private
   * @param {number} xp 
   */
  _addExperience(xp) {
    this.experience += xp;
    this._checkLevelUp();
  }

  /**
   * Check if player should level up
   * @private
   */
  _checkLevelUp() {
    while (this.experience >= this.levelThresholds[this.level]) {
      this.experience -= this.levelThresholds[this.level];
      this.level++;
      console.log(`Level up! Now level ${this.level}`);
      this._onLevelUp();
    }
  }

  /**
   * Called when player levels up
   * @private
   */
  _onLevelUp() {
    // Reward player with seeds when they level up
    const rewardSeeds = {
      wheat: Math.floor(this.level * 1.5),
      carrot: Math.floor(this.level * 1.2),
      potato: Math.floor(this.level * 0.8)
    };

    for (const [type, quantity] of Object.entries(rewardSeeds)) {
      this.inventory.seeds[type] = (this.inventory.seeds[type] || 0) + quantity;
    }

    console.log(`Received level up reward: ${JSON.stringify(rewardSeeds)}`);
  }

  /**
   * Get current farm status
   * @returns {Object} Farm status object
   */
  getStatus() {
    this._updateCropStatuses();
    return {
      level: this.level,
      experience: this.experience,
      nextLevelXp: this.levelThresholds[this.level],
      crops: this.crops,
      inventory: this.inventory
    };
  }
}

// Example usage:
// const farm = new FarmSystem();
// farm.plantCrop('wheat', 2);
// setTimeout(() => {
//   farm.harvestCrops();
//   console.log(farm.getStatus());
// }, 35000);
```
