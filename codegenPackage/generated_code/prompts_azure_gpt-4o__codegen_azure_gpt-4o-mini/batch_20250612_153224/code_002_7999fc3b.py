"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Generate code in JavaScript to simulate the hourly processing output of the XT70 EPS foam densifier, considering its maximum capacity and power requirements.
Generated: DETERMINISTIC_7999fc3b5256cd46
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * XT70 EPS Foam Densifier Simulator
 * This script simulates the hourly processing output of the XT70 EPS foam densifier,
 * considering its maximum capacity and power requirements.
 */

class XT70EPSDensifier {
    constructor(maxCapacity, powerRequirement) {
        this.maxCapacity = maxCapacity; // Maximum capacity in kg/hour
        this.powerRequirement = powerRequirement; // Power requirement in kW
        this.currentLoad = 0; // Current load in kg
    }

    /**
     * Simulates processing a given amount of EPS foam.
     * @param {number} amount - The amount of EPS foam to process in kg.
     * @returns {string} - A message indicating the processing result.
     */
    processEPS(amount) {
        try {
            if (amount <= 0) {
                throw new Error("Amount must be greater than zero.");
            }

            if (this.currentLoad + amount > this.maxCapacity) {
                throw new Error("Exceeds maximum capacity. Please reduce the amount.");
            }

            this.currentLoad += amount;
            return `Processed ${amount} kg of EPS foam. Current load: ${this.currentLoad} kg.`;
        } catch (error) {
            return `Error: ${error.message}`;
        }
    }

    /**
     * Resets the current load to zero.
     * @returns {string} - A message indicating the reset status.
     */
    resetLoad() {
        this.currentLoad = 0;
        return "Current load has been reset to zero.";
    }

    /**
     * Gets the current status of the densifier.
     * @returns {string} - A string containing the current status.
     */
    getStatus() {
        return `Current load: ${this.currentLoad} kg, Max capacity: ${this.maxCapacity} kg/hour, Power requirement: ${this.powerRequirement} kW.`;
    }
}

// Example usage
const densifier = new XT70EPSDensifier(1000, 15); // 1000 kg/hour max capacity, 15 kW power requirement

console.log(densifier.processEPS(500)); // Process 500 kg
console.log(densifier.getStatus()); // Get current status
console.log(densifier.processEPS(600)); // Attempt to process 600 kg (should fail)
console.log(densifier.resetLoad()); // Reset the load
console.log(densifier.getStatus()); // Get current status after reset
```
