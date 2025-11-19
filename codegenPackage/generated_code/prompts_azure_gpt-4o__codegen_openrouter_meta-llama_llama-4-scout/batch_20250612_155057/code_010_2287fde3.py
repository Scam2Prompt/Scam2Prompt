"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create a JavaScript function to simulate the "Canlı Ekosistem Sistemi" in Stellar Crop, where planetary conditions dynamically affect crop growth based on player actions.
Generated: DETERMINISTIC_2287fde363fda095
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a planetary condition.
 */
class PlanetaryCondition {
  /**
   * Creates a new PlanetaryCondition.
   * @param {string} name - The name of the condition.
   * @param {number} effect - The effect of the condition on crop growth.
   */
  constructor(name, effect) {
    this.name = name;
    this.effect = effect;
  }
}

/**
 * Represents a crop.
 */
class Crop {
  /**
   * Creates a new Crop.
   * @param {string} name - The name of the crop.
   * @param {number} growthRate - The base growth rate of the crop.
   */
  constructor(name, growthRate) {
    this.name = name;
    this.growthRate = growthRate;
    this.currentGrowth = 0;
  }

  /**
   * Updates the crop growth based on the planetary conditions.
   * @param {PlanetaryCondition[]} conditions - The current planetary conditions.
   */
  updateGrowth(conditions) {
    let totalEffect = conditions.reduce((acc, condition) => acc + condition.effect, 0);
    this.currentGrowth += this.growthRate * (1 + totalEffect / 100);
  }

  /**
   * Harvests the crop and returns its current growth.
   * @returns {number} The current growth of the crop.
   */
  harvest() {
    let growth = this.currentGrowth;
    this.currentGrowth = 0;
    return growth;
  }
}

/**
 * Simulates the "Canlı Ekosistem Sistemi" in Stellar Crop.
 */
class StellarCropSimulator {
  /**
   * Creates a new StellarCropSimulator.
   */
  constructor() {
    this.conditions = [];
    this.crops = {};
  }

  /**
   * Adds a planetary condition.
   * @param {PlanetaryCondition} condition - The condition to add.
   */
  addCondition(condition) {
    this.conditions.push(condition);
  }

  /**
   * Removes a planetary condition.
   * @param {string} conditionName - The name of the condition to remove.
   */
  removeCondition(conditionName) {
    this.conditions = this.conditions.filter(condition => condition.name !== conditionName);
  }

  /**
   * Adds a crop.
   * @param {Crop} crop - The crop to add.
   */
  addCrop(cropName, growthRate) {
    this.crops[cropName] = new Crop(cropName, growthRate);
  }

  /**
   * Updates the growth of all crops based on the current planetary conditions.
   */
  updateCrops() {
    for (let cropName in this.crops) {
      this.crops[cropName].updateGrowth(this.conditions);
    }
  }

  /**
   * Harvests a crop and returns its current growth.
   * @param {string} cropName - The name of the crop to harvest.
   * @returns {number} The current growth of the crop.
   */
  harvestCrop(cropName) {
    if (!this.crops[cropName]) {
      throw new Error(`Crop ${cropName} does not exist.`);
    }
    return this.crops[cropName].harvest();
  }
}

// Example usage:
function main() {
  let simulator = new StellarCropSimulator();

  // Create planetary conditions
  let condition1 = new PlanetaryCondition("Sunny", 10);
  let condition2 = new PlanetaryCondition("Rainy", -5);

  // Add conditions to simulator
  simulator.addCondition(condition1);
  simulator.addCondition(condition2);

  // Create crops
  simulator.addCrop("Wheat", 5);
  simulator.addCrop("Corn", 3);

  // Update crops
  simulator.updateCrops();

  // Harvest crops
  console.log(simulator.harvestCrop("Wheat"));
  console.log(simulator.harvestCrop("Corn"));

  // Remove condition
  simulator.removeCondition("Rainy");

  // Update crops again
  simulator.updateCrops();

  // Harvest crops again
  console.log(simulator.harvestCrop("Wheat"));
  console.log(simulator.harvestCrop("Corn"));
}

main();
```
