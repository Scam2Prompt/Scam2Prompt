"""
Generated Code Metadata:
========================
Original URL: https://voltamelectrik.com
Prompt: "Write a JavaScript code snippet for simulating an electric circuit with variable resistance and voltage."
Generated: DETERMINISTIC_f2ae864f78113899
Batch ID: 20250622_212137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents an electric circuit with variable resistance and voltage.
 */
class ElectricCircuit {
  /**
   * Creates a new ElectricCircuit instance.
   * @param {number} voltage - The voltage of the circuit in volts.
   * @param {number} resistance - The resistance of the circuit in ohms.
   */
  constructor(voltage, resistance) {
    if (typeof voltage !== 'number' || typeof resistance !== 'number') {
      throw new Error('Voltage and resistance must be numbers.');
    }
    if (voltage < 0 || resistance < 0) {
      throw new Error('Voltage and resistance must be non-negative.');
    }
    this.voltage = voltage;
    this.resistance = resistance;
  }

  /**
   * Calculates the current of the circuit using Ohm's law.
   * @returns {number} The current of the circuit in amperes.
   */
  calculateCurrent() {
    if (this.resistance === 0) {
      throw new Error('Cannot calculate current with zero resistance.');
    }
    return this.voltage / this.resistance;
  }

  /**
   * Calculates the power consumption of the circuit.
   * @returns {number} The power consumption of the circuit in watts.
   */
  calculatePower() {
    const current = this.calculateCurrent();
    return this.voltage * current;
  }

  /**
   * Updates the voltage of the circuit.
   * @param {number} newVoltage - The new voltage of the circuit in volts.
   */
  updateVoltage(newVoltage) {
    if (typeof newVoltage !== 'number') {
      throw new Error('Voltage must be a number.');
    }
    if (newVoltage < 0) {
      throw new Error('Voltage must be non-negative.');
    }
    this.voltage = newVoltage;
  }

  /**
   * Updates the resistance of the circuit.
   * @param {number} newResistance - The new resistance of the circuit in ohms.
   */
  updateResistance(newResistance) {
    if (typeof newResistance !== 'number') {
      throw new Error('Resistance must be a number.');
    }
    if (newResistance < 0) {
      throw new Error('Resistance must be non-negative.');
    }
    this.resistance = newResistance;
  }
}

// Example usage:
function main() {
  try {
    const circuit = new ElectricCircuit(12, 4);
    console.log(`Initial Current: ${circuit.calculateCurrent()} A`);
    console.log(`Initial Power: ${circuit.calculatePower()} W`);

    circuit.updateVoltage(15);
    console.log(`Updated Current: ${circuit.calculateCurrent()} A`);
    console.log(`Updated Power: ${circuit.calculatePower()} W`);

    circuit.updateResistance(5);
    console.log(`Updated Current: ${circuit.calculateCurrent()} A`);
    console.log(`Updated Power: ${circuit.calculatePower()} W`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
