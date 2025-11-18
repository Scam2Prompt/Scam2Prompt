"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Generate code in JavaScript to simulate the hourly processing output of the XT70 EPS foam densifier, considering its maximum capacity and power requirements.
Generated: DETERMINISTIC_7999fc3b5256cd46
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * XT70 EPS Foam Densifier Simulation
 * This script simulates the hourly processing output of the XT70 EPS foam densifier,
 * considering its maximum capacity and power requirements.
 */

// Constants representing machine specifications
const MAX_CAPACITY_KG_PER_HOUR = 300; // Maximum capacity in kilograms per hour
const POWER_REQUIREMENT_KW = 15; // Power requirement in kilowatts

// Function to simulate hourly output
function simulateHourlyOutput(machineRunningHours, powerAvailableKW) {
  /**
   * Simulates the hourly processing output of the XT70 EPS foam densifier.
   * @param {number} machineRunningHours - Number of hours the machine runs.
   * @param {number} powerAvailableKW - Available power in kilowatts.
   * @returns {Object} - Simulation results including total output and any errors.
   */

  // Validate inputs
  if (machineRunningHours <= 0) {
    return { error: "Machine running hours must be greater than zero." };
  }
  if (powerAvailableKW < POWER_REQUIREMENT_KW) {
    return { error: "Insufficient power available for operation." };
  }

  // Calculate total output based on hours and capacity
  const totalOutputKg = Math.min(powerAvailableKW / POWER_REQUIREMENT_KW, 1) * MAX_CAPACITY_KG_PER_HOUR * machineRunningHours;

  return {
    totalOutputKg,
    message: `Simulation completed successfully. Total output: ${totalOutputKg.toFixed(2)} kg.`,
  };
}

// Example usage
try {
  const machineRunningHours = 5; // Number of hours the machine runs
  const powerAvailableKW = 20; // Available power in kilowatts

  const simulationResult = simulateHourlyOutput(machineRunningHours, powerAvailableKW);

  if (simulationResult.error) {
    console.error(`Error: ${simulationResult.error}`);
  } else {
    console.log(simulationResult.message);
  }
} catch (error) {
  console.error(`An unexpected error occurred: ${error.message}`);
}
```
