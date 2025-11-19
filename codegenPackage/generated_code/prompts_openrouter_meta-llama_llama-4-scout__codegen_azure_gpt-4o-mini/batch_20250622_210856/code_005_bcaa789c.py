"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: "Create a simple electrical engineering calculator using JavaScript, incorporating formulas for energy efficiency and electrical design."
Generated: DETERMINISTIC_bcaa789c571c2df0
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Electrical Engineering Calculator
// This calculator provides functionalities to calculate energy efficiency and electrical design parameters.

class ElectricalCalculator {
    constructor() {
        // Initialize any necessary properties if needed
    }

    /**
     * Calculate energy efficiency
     * @param {number} outputPower - The useful output power in watts
     * @param {number} inputPower - The total input power in watts
     * @returns {number} - The energy efficiency as a percentage
     * @throws {Error} - Throws an error if inputPower is zero or negative
     */
    calculateEnergyEfficiency(outputPower, inputPower) {
        if (inputPower <= 0) {
            throw new Error("Input power must be greater than zero.");
        }
        const efficiency = (outputPower / inputPower) * 100;
        return efficiency.toFixed(2); // Return efficiency rounded to two decimal places
    }

    /**
     * Calculate the required wire gauge based on current and length
     * @param {number} current - The current in amperes
     * @param {number} length - The length of the wire in feet
     * @returns {string} - Recommended wire gauge
     * @throws {Error} - Throws an error if current or length is negative
     */
    calculateWireGauge(current, length) {
        if (current < 0 || length < 0) {
            throw new Error("Current and length must be non-negative.");
        }

        // Simple wire gauge calculation based on American Wire Gauge (AWG) standards
        // This is a placeholder for actual calculations
        if (current <= 15) {
            return "14 AWG";
        } else if (current <= 20) {
            return "12 AWG";
        } else {
            return "10 AWG or larger";
        }
    }
}

// Example usage
try {
    const calculator = new ElectricalCalculator();
    
    // Calculate energy efficiency
    const outputPower = 1500; // in watts
    const inputPower = 2000; // in watts
    const efficiency = calculator.calculateEnergyEfficiency(outputPower, inputPower);
    console.log(`Energy Efficiency: ${efficiency}%`);

    // Calculate wire gauge
    const current = 18; // in amperes
    const length = 100; // in feet
    const wireGauge = calculator.calculateWireGauge(current, length);
    console.log(`Recommended Wire Gauge: ${wireGauge}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
