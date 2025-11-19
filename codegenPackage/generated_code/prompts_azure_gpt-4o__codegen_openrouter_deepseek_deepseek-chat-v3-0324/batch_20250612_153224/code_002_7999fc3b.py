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
 * Simulates the hourly processing output of the XT70 EPS foam densifier.
 * 
 * This class models the behavior of the XT70 EPS foam densifier, including:
 * - Maximum capacity (70 kg/hour)
 * - Power requirements (15 kW)
 * - Processing efficiency based on input material quality
 */
class XT70Densifier {
    /**
     * Create a new XT70Densifier instance.
     * @param {number} initialMaterial - Initial amount of material in kg (0-70)
     */
    constructor(initialMaterial = 0) {
        this.maxCapacity = 70; // kg/hour
        this.powerRequirement = 15; // kW
        this.currentMaterial = Math.min(initialMaterial, this.maxCapacity);
    }

    /**
     * Add material to be processed.
     * @param {number} amount - Amount of material to add in kg
     * @returns {number} Amount actually added (may be less if over capacity)
     */
    addMaterial(amount) {
        const availableSpace = this.maxCapacity - this.currentMaterial;
        const added = Math.min(amount, availableSpace);
        this.currentMaterial += added;
        return added;
    }

    /**
     * Process material for one hour.
     * @param {number} [efficiency=1.0] - Processing efficiency (0.0 to 1.0)
     * @returns {Object} Result containing processed amount and power used
     * @throws {Error} If efficiency is invalid or no material to process
     */
    processHour(efficiency = 1.0) {
        if (efficiency < 0 || efficiency > 1) {
            throw new Error('Efficiency must be between 0.0 and 1.0');
        }

        if (this.currentMaterial <= 0) {
            throw new Error('No material available to process');
        }

        const processedAmount = Math.min(
            this.currentMaterial,
            this.maxCapacity * efficiency
        );
        this.currentMaterial -= processedAmount;

        return {
            processed: processedAmount,
            powerUsed: this.powerRequirement,
            remainingMaterial: this.currentMaterial
        };
    }

    /**
     * Get current status of the densifier.
     * @returns {Object} Status containing current material and capacity info
     */
    getStatus() {
        return {
            currentMaterial: this.currentMaterial,
            maxCapacity: this.maxCapacity,
            powerRequirement: this.powerRequirement,
            utilization: (this.currentMaterial / this.maxCapacity) * 100
        };
    }
}

// Example usage:
// const densifier = new XT70Densifier(50);
// console.log(densifier.getStatus());
// const result = densifier.processHour(0.9);
// console.log(result);
// densifier.addMaterial(30);
// console.log(densifier.getStatus());
```
