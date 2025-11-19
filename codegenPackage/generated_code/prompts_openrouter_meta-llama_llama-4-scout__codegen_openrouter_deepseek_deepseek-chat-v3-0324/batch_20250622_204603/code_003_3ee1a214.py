"""
Generated Code Metadata:
========================
Original URL: https://linkevent.net
Prompt: Write a JavaScript code snippet to calculate the power factor kvr.
Generated: DETERMINISTIC_3ee1a21450aebb0a
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the power factor (kvr) based on active power (kW) and apparent power (kVA).
 * 
 * @param {number} activePower - Active power in kilowatts (kW)
 * @param {number} apparentPower - Apparent power in kilovolt-amperes (kVA)
 * @returns {number} Power factor (kvr) as a decimal value between 0 and 1
 * @throws {Error} If inputs are invalid (non-numeric, zero, or negative values)
 */
function calculatePowerFactor(activePower, apparentPower) {
    // Validate input parameters
    if (typeof activePower !== 'number' || typeof apparentPower !== 'number') {
        throw new Error('Both parameters must be numbers');
    }
    
    if (activePower <= 0 || apparentPower <= 0) {
        throw new Error('Both parameters must be positive numbers');
    }
    
    if (activePower > apparentPower) {
        throw new Error('Active power cannot be greater than apparent power');
    }
    
    // Calculate and return power factor
    return activePower / apparentPower;
}

// Example usage:
try {
    const pf = calculatePowerFactor(8, 10); // 0.8 power factor
    console.log(`Power Factor: ${pf.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating power factor: ${error.message}`);
}
```
