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
 * Simulates the "Canlı Ekosistem Sistemi" in Stellar Crop.
 * This function dynamically adjusts crop growth based on planetary conditions
 * and player actions.
 */

class Planet {
    constructor(name, temperature, humidity, soilQuality) {
        this.name = name; // Name of the planet
        this.temperature = temperature; // Temperature in Celsius
        this.humidity = humidity; // Humidity percentage
        this.soilQuality = soilQuality; // Soil quality rating (1-10)
        this.crops = []; // Array to hold crops on the planet
    }

    /**
     * Adds a crop to the planet.
     * @param {Crop} crop - The crop to be added.
     */
    addCrop(crop) {
        if (crop instanceof Crop) {
            this.crops.push(crop);
        } else {
            throw new Error("Invalid crop type. Must be an instance of Crop.");
        }
    }

    /**
     * Simulates the growth of crops based on planetary conditions.
     */
    simulateGrowth() {
        this.crops.forEach(crop => {
            crop.grow(this.temperature, this.humidity, this.soilQuality);
        });
    }
}

class Crop {
    constructor(name, growthRate) {
        this.name = name; // Name of the crop
        this.growthRate = growthRate; // Base growth rate
        this.growthStage = 0; // Current growth stage (0-10)
    }

    /**
     * Grows the crop based on environmental conditions.
     * @param {number} temperature - Current temperature.
     * @param {number} humidity - Current humidity.
     * @param {number} soilQuality - Current soil quality.
     */
    grow(temperature, humidity, soilQuality) {
        // Calculate growth factor based on conditions
        const growthFactor = this.calculateGrowthFactor(temperature, humidity, soilQuality);
        
        // Update growth stage
        this.growthStage += this.growthRate * growthFactor;

        // Cap growth stage at 10
        if (this.growthStage > 10) {
            this.growthStage = 10;
        }
    }

    /**
     * Calculates the growth factor based on environmental conditions.
     * @param {number} temperature - Current temperature.
     * @param {number} humidity - Current humidity.
     * @param {number} soilQuality - Current soil quality.
     * @returns {number} - Growth factor (0-1).
     */
    calculateGrowthFactor(temperature, humidity, soilQuality) {
        let factor = 1;

        // Adjust factor based on temperature
        if (temperature < 15 || temperature > 30) {
            factor -= 0.5; // Poor growth outside optimal range
        }

        // Adjust factor based on humidity
        if (humidity < 40 || humidity > 80) {
            factor -= 0.3; // Poor growth outside optimal range
        }

        // Adjust factor based on soil quality
        if (soilQuality < 5) {
            factor -= 0.2; // Poor growth with low soil quality
        }

        return Math.max(0, factor); // Ensure factor is not negative
    }
}

// Example usage
try {
    const planet = new Planet("Terra", 25, 60, 7);
    const wheat = new Crop("Wheat", 1);
    const corn = new Crop("Corn", 1.5);

    planet.addCrop(wheat);
    planet.addCrop(corn);

    // Simulate growth for a number of cycles
    for (let i = 0; i < 5; i++) {
        planet.simulateGrowth();
        console.log(`Cycle ${i + 1}: Wheat Growth Stage: ${wheat.growthStage}, Corn Growth Stage: ${corn.growthStage}`);
    }
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
