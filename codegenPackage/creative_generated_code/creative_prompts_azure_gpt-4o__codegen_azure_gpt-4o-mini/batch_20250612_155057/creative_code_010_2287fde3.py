"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Create a JavaScript function to simulate the "Canlı Ekosistem Sistemi" in Stellar Crop, where planetary conditions dynamically affect crop growth based on player actions.
Generated: DETERMINISTIC_2287fde363fda095
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the "Canlı Ekosistem Sistemi" for crop growth in Stellar Crop.
 * The function dynamically adjusts crop growth based on planetary conditions and player actions.
 */

class Planet {
    constructor(name, temperature, moisture, nutrients) {
        this.name = name; // Name of the planet
        this.temperature = temperature; // Temperature in °C
        this.moisture = moisture; // Moisture level (0 to 100)
        this.nutrients = nutrients; // Nutrient level (0 to 100)
        this.crops = []; // Array to hold crops on the planet
    }

    /**
     * Adds a crop to the planet.
     * @param {Crop} crop - The crop to be added.
     */
    addCrop(crop) {
        this.crops.push(crop);
    }

    /**
     * Updates the environmental conditions.
     * @param {number} tempChange - Change in temperature.
     * @param {number} moistureChange - Change in moisture level.
     * @param {number} nutrientsChange - Change in nutrient level.
     */
    updateConditions(tempChange, moistureChange, nutrientsChange) {
        this.temperature += tempChange;
        this.moisture = Math.min(Math.max(this.moisture + moistureChange, 0), 100);
        this.nutrients = Math.min(Math.max(this.nutrients + nutrientsChange, 0), 100);
    }

    /**
     * Simulates the growth of crops based on current conditions.
     * @returns {Array} - An array with the growth status of each crop.
     */
    simulateGrowth() {
        return this.crops.map(crop => crop.grow(this.temperature, this.moisture, this.nutrients));
    }
}

class Crop {
    constructor(name, growthRate) {
        this.name = name; // Name of the crop
        this.growthRate = growthRate; // Base growth rate
        this.growthStage = 0; // Current growth stage (0 - 100)
    }

    /**
     * Simulates the growth of the crop based on environmental conditions.
     * @param {number} temperature - Current temperature of the planet.
     * @param {number} moisture - Current moisture level of the planet.
     * @param {number} nutrients - Current nutrient level of the planet.
     * @returns {string} - Growth status of the crop.
     */
    grow(temperature, moisture, nutrients) {
        // Ensure parameters are valid
        if (typeof temperature !== 'number' || typeof moisture !== 'number' || typeof nutrients !== 'number') {
            throw new Error('Invalid environmental condition values.');
        }

        const optimalConditions = this.getOptimalConditions();
        const growthFactor = this.calculateGrowthFactor(temperature, moisture, nutrients, optimalConditions);

        // Update growth stage
        this.growthStage += this.growthRate * growthFactor;

        if (this.growthStage >= 100) {
            return `${this.name} is fully grown!`;
        }
        return `${this.name} is at growth stage ${Math.floor(this.growthStage)}%`;
    }

    /**
     * Calculates the growth factor based on the difference between current and optimal conditions.
     * @param {number} temperature - Current temperature.
     * @param {number} moisture - Current moisture level.
     * @param {number} nutrients - Current nutrient level.
     * @param {Object} optimalConditions - Optimal conditions for growth.
     * @returns {number} - Growth factor (0 to 1).
     */
    calculateGrowthFactor(temperature, moisture, nutrients, optimalConditions) {
        const tempDiff = Math.max(0, optimalConditions.temperature - Math.abs(temperature - optimalConditions.temperature));
        const moistureDiff = Math.max(0, optimalConditions.moisture - Math.abs(moisture - optimalConditions.moisture));
        const nutrientsDiff = Math.max(0, optimalConditions.nutrients - Math.abs(nutrients - optimalConditions.nutrients));

        return (tempDiff + moistureDiff + nutrientsDiff) / 3;
    }

    /**
     * Returns the optimal conditions for this crop.
     * @returns {Object} - Optimal conditions for temperature, moisture, and nutrients.
     */
    getOptimalConditions() {
        // Example optimal conditions (these would ideally be defined per crop)
        return {
            temperature: 25, // °C
            moisture: 70, // Percentage
            nutrients: 80 // Percentage
        };
    }
}

// Example usage
try {
    const myPlanet = new Planet('Terra Nova', 20, 50, 60);
    const wheat = new Crop('Wheat', 1);
    myPlanet.addCrop(wheat);

    // Simulate conditions and growth
    myPlanet.updateConditions(5, 10, -5); // Adjust conditions
    const growthStatus = myPlanet.simulateGrowth();
    console.log(growthStatus);
} catch (error) {
    console.error('Error during simulation:', error.message);
}
```
