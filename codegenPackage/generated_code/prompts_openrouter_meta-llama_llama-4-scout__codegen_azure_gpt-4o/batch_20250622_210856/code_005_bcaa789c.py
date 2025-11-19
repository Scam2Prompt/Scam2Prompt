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
/**
 * Electrical Engineering Calculator
 * This script provides functions to calculate energy efficiency and basic electrical design parameters.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Ensure the script runs in strict mode for better error handling
"use strict";

/**
 * Calculate energy efficiency.
 * Formula: Efficiency (%) = (Output Power / Input Power) * 100
 * 
 * @param {number} inputPower - The input power in watts.
 * @param {number} outputPower - The output power in watts.
 * @returns {number} - The efficiency percentage.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateEfficiency(inputPower, outputPower) {
    if (inputPower <= 0 || outputPower < 0) {
        throw new Error("Input power must be greater than 0 and output power must be non-negative.");
    }
    return (outputPower / inputPower) * 100;
}

/**
 * Calculate electrical resistance using Ohm's Law.
 * Formula: Resistance (R) = Voltage (V) / Current (I)
 * 
 * @param {number} voltage - The voltage in volts.
 * @param {number} current - The current in amperes.
 * @returns {number} - The resistance in ohms.
 * @throws {Error} - Throws an error if current is zero or negative.
 */
function calculateResistance(voltage, current) {
    if (current <= 0) {
        throw new Error("Current must be greater than 0.");
    }
    return voltage / current;
}

/**
 * Calculate electrical power.
 * Formula: Power (P) = Voltage (V) * Current (I)
 * 
 * @param {number} voltage - The voltage in volts.
 * @param {number} current - The current in amperes.
 * @returns {number} - The power in watts.
 */
function calculatePower(voltage, current) {
    return voltage * current;
}

/**
 * Calculate energy consumption.
 * Formula: Energy (E) = Power (P) * Time (T)
 * 
 * @param {number} power - The power in watts.
 * @param {number} time - The time in hours.
 * @returns {number} - The energy in watt-hours (Wh).
 * @throws {Error} - Throws an error if power or time is negative.
 */
function calculateEnergy(power, time) {
    if (power < 0 || time < 0) {
        throw new Error("Power and time must be non-negative.");
    }
    return power * time;
}

// Example usage
try {
    const inputPower = 100; // in watts
    const outputPower = 80; // in watts
    const voltage = 220; // in volts
    const current = 5; // in amperes
    const time = 2; // in hours

    console.log("Energy Efficiency:", calculateEfficiency(inputPower, outputPower).toFixed(2), "%");
    console.log("Resistance:", calculateResistance(voltage, current).toFixed(2), "ohms");
    console.log("Power:", calculatePower(voltage, current).toFixed(2), "watts");
    console.log("Energy Consumption:", calculateEnergy(calculatePower(voltage, current), time).toFixed(2), "Wh");
} catch (error) {
    console.error("Error:", error.message);
}
```
