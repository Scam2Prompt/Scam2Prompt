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
 * Simulates the "Canlı Ekosistem Sistemi" (Live Ecosystem System) for Stellar Crop
 * where planetary conditions dynamically affect crop growth based on player actions.
 */

class PlanetaryCondition {
    constructor(temperature, humidity, radiation, soilQuality) {
        this.temperature = temperature; // in Celsius
        this.humidity = humidity; // percentage (0-100)
        this.radiation = radiation; // radiation level (0-10)
        this.soilQuality = soilQuality; // quality index (0-100)
    }

    /**
     * Updates planetary conditions based on player actions
     * @param {Object} actions - Player actions affecting the planet
     */
    updateConditions(actions) {
        if (actions.adjustTemperature) {
            this.temperature += actions.adjustTemperature;
            this.temperature = Math.max(-50, Math.min(100, this.temperature));
        }

        if (actions.adjustHumidity) {
            this.humidity += actions.adjustHumidity;
            this.humidity = Math.max(0, Math.min(100, this.humidity));
        }

        if (actions.adjustRadiation) {
            this.radiation += actions.adjustRadiation;
            this.radiation = Math.max(0, Math.min(10, this.radiation));
        }

        if (actions.adjustSoil) {
            this.soilQuality += actions.adjustSoil;
            this.soilQuality = Math.max(0, Math.min(100, this.soilQuality));
        }
    }
}

class Crop {
    constructor(name, optimalTemp, optimalHumidity, optimalRadiation, optimalSoil) {
        this.name = name;
        this.optimalTemp = optimalTemp; // [min, max] temperature range
        this.optimalHumidity = optimalHumidity; // [min, max] humidity range
        this.optimalRadiation = optimalRadiation; // [min, max] radiation range
        this.optimalSoil = optimalSoil; // minimum soil quality required
        this.growthRate = 0;
        this.health = 100;
    }

    /**
     * Calculates growth rate based on current planetary conditions
     * @param {PlanetaryCondition} conditions - Current planetary conditions
     */
    calculateGrowth(conditions) {
        // Temperature factor (0-1)
        const tempFactor = this.calculateFactor(
            conditions.temperature, 
            this.optimalTemp[0], 
            this.optimalTemp[1]
        );

        // Humidity factor (0-1)
        const humidityFactor = this.calculateFactor(
            conditions.humidity, 
            this.optimalHumidity[0], 
            this.optimalHumidity[1]
        );

        // Radiation factor (0-1)
        const radiationFactor = this.calculateFactor(
            conditions.radiation, 
            this.optimalRadiation[0], 
            this.optimalRadiation[1]
        );

        // Soil factor (0-1)
        const soilFactor = conditions.soilQuality >= this.optimalSoil ? 1 : 
                         conditions.soilQuality / this.optimalSoil;

        // Calculate overall growth rate (0-1)
        this.growthRate = (tempFactor + humidityFactor + radiationFactor + soilFactor) / 4;

        // Update crop health based on conditions
        this.updateHealth(conditions);
    }

    /**
     * Helper function to calculate condition factor (0-1)
     */
    calculateFactor(value, min, max) {
        if (value < min) return value / min;
        if (value > max) return 1 - ((value - max) / (max * 1.5));
        return 1;
    }

    /**
     * Updates crop health based on extreme conditions
     */
    updateHealth(conditions) {
        // Temperature stress
        if (conditions.temperature < this.optimalTemp[0] * 0.5 || 
            conditions.temperature > this.optimalTemp[1] * 1.5) {
            this.health -= 5;
        }

        // Radiation stress
        if (conditions.radiation > this.optimalRadiation[1] * 2) {
            this.health -= 10;
        }

        // Soil stress
        if (conditions.soilQuality < this.optimalSoil * 0.3) {
            this.health -= 7;
        }

        this.health = Math.max(0, Math.min(100, this.health));
    }
}

class LiveEcosystemSystem {
    constructor() {
        this.planetaryConditions = new PlanetaryCondition(20, 50, 2, 70);
        this.crops = [];
        this.time = 0;
    }

    /**
     * Adds a crop to the ecosystem
     * @param {Crop} crop - Crop to add
     */
    addCrop(crop) {
        this.crops.push(crop);
    }

    /**
     * Simulates one time unit of ecosystem evolution
     * @param {Object} playerActions - Player actions affecting the ecosystem
     */
    simulateTimeUnit(playerActions = {}) {
        // Update planetary conditions based on player actions
        this.planetaryConditions.updateConditions(playerActions);

        // Update all crops
        this.crops.forEach(crop => {
            crop.calculateGrowth(this.planetaryConditions);
        });

        this.time++;
    }

    /**
     * Gets current ecosystem status
     * @returns {Object} Ecosystem status report
     */
    getStatus() {
        return {
            time: this.time,
            conditions: {
                temperature: this.planetaryConditions.temperature,
                humidity: this.planetaryConditions.humidity,
                radiation: this.planetaryConditions.radiation,
                soilQuality: this.planetaryConditions.soilQuality
            },
            crops: this.crops.map(crop => ({
                name: crop.name,
                growthRate: crop.growthRate,
                health: crop.health
            }))
        };
    }
}

// Example usage:
/*
const ecosystem = new LiveEcosystemSystem();

// Add some crops
ecosystem.addCrop(new Crop("Stellar Wheat", [15, 25], [40, 70], [1, 3], 60));
ecosystem.addCrop(new Crop("Radiation Berry", [10, 30], [30, 80], [4, 8], 40));

// Simulate with player actions
ecosystem.simulateTimeUnit({
    adjustTemperature: 5,
    adjustHumidity: -10
});

console.log(ecosystem.getStatus());
*/
```
