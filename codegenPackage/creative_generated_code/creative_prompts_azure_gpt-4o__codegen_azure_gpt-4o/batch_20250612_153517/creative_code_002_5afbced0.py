"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balloon-gomble-io.pages.dev
Prompt: Create a function in JavaScript to simulate heating a balloon and calculating its lift based on user interactions.
Generated: DETERMINISTIC_5afbced03a1beab4
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates heating a balloon and calculates its lift based on user interactions.
 * The lift is determined by the temperature of the air inside the balloon.
 * The higher the temperature, the greater the lift.
 */

// Balloon object to encapsulate properties and methods
const Balloon = {
  temperature: 20, // Initial temperature in Celsius
  maxTemperature: 100, // Maximum safe temperature in Celsius
  baseLift: 0, // Initial lift in Newtons
  maxLift: 100, // Maximum lift in Newtons

  /**
   * Heats the balloon by increasing the temperature.
   * @param {number} increment - The amount to increase the temperature.
   */
  heat(increment) {
    if (typeof increment !== "number" || increment <= 0) {
      throw new Error("Invalid increment value. It must be a positive number.");
    }

    // Increase the temperature, but do not exceed maxTemperature
    this.temperature = Math.min(this.temperature + increment, this.maxTemperature);

    console.log(`Balloon heated. Current temperature: ${this.temperature}°C`);
  },

  /**
   * Calculates the lift based on the current temperature.
   * Lift scales linearly with temperature relative to maxTemperature.
   */
  calculateLift() {
    // Lift scales linearly between baseLift and maxLift
    const lift = (this.temperature / this.maxTemperature) * this.maxLift;

    console.log(`Current lift: ${lift.toFixed(2)} Newtons`);
    return lift;
  },

  /**
   * Simulates user interaction to heat the balloon and calculate lift.
   */
  simulateHeating() {
    try {
      const userIncrement = parseFloat(
        prompt("Enter the amount to increase the temperature (in °C):")
      );

      if (isNaN(userIncrement) || userIncrement <= 0) {
        throw new Error("Invalid input. Please enter a positive number.");
      }

      // Heat the balloon and calculate lift
      this.heat(userIncrement);
      this.calculateLift();
    } catch (error) {
      console.error(error.message);
    }
  },
};

// Example usage:
// Uncomment the line below to simulate heating when running in a browser environment
// Balloon.simulateHeating();
```
