"""
Generated Code Metadata:
========================
Original URL: https://balloon-gomble-io.pages.dev
Prompt: Create a function in JavaScript to simulate heating a balloon and calculating its lift based on user interactions.
Generated: DETERMINISTIC_5afbced03a1beab4
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the lift of a balloon based on its volume and the surrounding air density.
 * 
 * @param {number} volume - The volume of the balloon in cubic meters.
 * @param {number} airDensity - The density of the surrounding air in kg/m^3.
 * @returns {number} The lift of the balloon in Newtons.
 */
function calculateLift(volume, airDensity) {
    // Acceleration due to gravity in m/s^2
    const g = 9.81;
    // Density of air at sea level and room temperature in kg/m^3
    // Not used directly but kept for reference

    // Calculate lift using Archimedes' Principle
    return volume * airDensity * g;
}

/**
 * Simulates heating a balloon and calculates its lift based on user interactions.
 */
class BalloonSimulator {
    /**
     * Creates a new BalloonSimulator instance.
     * 
     * @param {number} initialVolume - The initial volume of the balloon in cubic meters.
     * @param {number} initialTemperature - The initial temperature of the balloon in Celsius.
     * @param {number} airDensity - The density of the surrounding air in kg/m^3.
     */
    constructor(initialVolume, initialTemperature, airDensity) {
        this.initialVolume = initialVolume;
        this.currentVolume = initialVolume;
        this.initialTemperature = initialTemperature;
        this.currentTemperature = initialTemperature;
        this.airDensity = airDensity;
    }

    /**
     * Heats the balloon by a specified amount.
     * 
     * @param {number} temperatureIncrease - The amount to increase the temperature by in Celsius.
     */
    heatBalloon(temperatureIncrease) {
        if (temperatureIncrease < 0) {
            throw new Error("Temperature increase cannot be negative.");
        }
        this.currentTemperature = this.initialTemperature + temperatureIncrease;
        // Assume ideal gas law: PV = nRT, and that n and P are constant
        // Then V1 / T1 = V2 / T2
        this.currentVolume = this.initialVolume * (this.currentTemperature / this.initialTemperature);
    }

    /**
     * Calculates the current lift of the balloon.
     * 
     * @returns {number} The current lift of the balloon in Newtons.
     */
    calculateCurrentLift() {
        return calculateLift(this.currentVolume, this.airDensity);
    }
}

// Example usage:
function main() {
    try {
        const simulator = new BalloonSimulator(1, 20, 1.2); // 1m^3, 20C, air density at sea level and room temperature
        console.log(`Initial lift: ${simulator.calculateCurrentLift()} N`);

        simulator.heatBalloon(50); // Heat the balloon by 50C
        console.log(`Volume after heating: ${simulator.currentVolume} m^3`);
        console.log(`Lift after heating: ${simulator.calculateCurrentLift()} N`);
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
