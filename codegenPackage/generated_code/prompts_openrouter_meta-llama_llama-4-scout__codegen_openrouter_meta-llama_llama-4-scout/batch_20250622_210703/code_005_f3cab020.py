"""
Generated Code Metadata:
========================
Original URL: https://praiasdeminas.eng.br
Prompt: Create a JavaScript code snippet to control the temperature and illumination of a pool with a smart automation system.
Generated: DETERMINISTIC_f3cab020d5a0718b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PoolAutomationSystem.js

/**
 * Represents a pool automation system.
 */
class PoolAutomationSystem {
  /**
   * Creates a new PoolAutomationSystem instance.
   * @param {Object} config - Configuration object.
   * @param {number} config.minTemperature - Minimum temperature in Celsius.
   * @param {number} config.maxTemperature - Maximum temperature in Celsius.
   * @param {number} config.minIllumination - Minimum illumination in lux.
   * @param {number} config.maxIllumination - Maximum illumination in lux.
   */
  constructor(config) {
    this.config = config;
    this.temperature = 25; // Default temperature in Celsius
    this.illumination = 500; // Default illumination in lux
  }

  /**
   * Sets the temperature of the pool.
   * @param {number} temperature - Temperature in Celsius.
   * @throws {Error} If temperature is out of range.
   */
  setTemperature(temperature) {
    if (temperature < this.config.minTemperature || temperature > this.config.maxTemperature) {
      throw new Error(`Temperature must be between ${this.config.minTemperature} and ${this.config.maxTemperature} Celsius`);
    }
    this.temperature = temperature;
    console.log(`Temperature set to ${temperature} Celsius`);
  }

  /**
   * Sets the illumination of the pool.
   * @param {number} illumination - Illumination in lux.
   * @throws {Error} If illumination is out of range.
   */
  setIllumination(illumination) {
    if (illumination < this.config.minIllumination || illumination > this.config.maxIllumination) {
      throw new Error(`Illumination must be between ${this.config.minIllumination} and ${this.config.maxIllumination} lux`);
    }
    this.illumination = illumination;
    console.log(`Illumination set to ${illumination} lux`);
  }

  /**
   * Increases the temperature by a specified amount.
   * @param {number} amount - Amount to increase temperature by.
   */
  increaseTemperature(amount) {
    const newTemperature = this.temperature + amount;
    this.setTemperature(newTemperature);
  }

  /**
   * Decreases the temperature by a specified amount.
   * @param {number} amount - Amount to decrease temperature by.
   */
  decreaseTemperature(amount) {
    const newTemperature = this.temperature - amount;
    this.setTemperature(newTemperature);
  }

  /**
   * Increases the illumination by a specified amount.
   * @param {number} amount - Amount to increase illumination by.
   */
  increaseIllumination(amount) {
    const newIllumination = this.illumination + amount;
    this.setIllumination(newIllumination);
  }

  /**
   * Decreases the illumination by a specified amount.
   * @param {number} amount - Amount to decrease illumination by.
   */
  decreaseIllumination(amount) {
    const newIllumination = this.illumination - amount;
    this.setIllumination(newIllumination);
  }
}

// Example usage:
const config = {
  minTemperature: 20,
  maxTemperature: 30,
  minIllumination: 0,
  maxIllumination: 1000,
};

const poolSystem = new PoolAutomationSystem(config);

try {
  poolSystem.setTemperature(28);
  poolSystem.setIllumination(750);
  poolSystem.increaseTemperature(2);
  poolSystem.decreaseIllumination(200);
} catch (error) {
  console.error(error.message);
}
```
