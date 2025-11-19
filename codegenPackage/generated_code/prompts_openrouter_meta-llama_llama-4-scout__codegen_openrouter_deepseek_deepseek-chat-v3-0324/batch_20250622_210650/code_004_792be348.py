"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: "Develop a simple calculator using JavaScript that determines the required amount of a chemical substance, like Propionic acid (C3H6O2), needed for a specific laboratory experiment based on given parameters."
Generated: DETERMINISTIC_792be348d253a9a5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Chemical Calculator for Propionic Acid (C3H6O2)
 * Calculates the required amount based on molarity, volume, and concentration.
 */

class ChemicalCalculator {
    /**
     * @param {string} chemicalFormula - The chemical formula (e.g., "C3H6O2")
     * @param {number} molarMass - The molar mass of the chemical in g/mol
     */
    constructor(chemicalFormula, molarMass) {
        this.chemicalFormula = chemicalFormula;
        this.molarMass = molarMass;
    }

    /**
     * Calculates the mass required for a given molarity and volume
     * @param {number} molarity - Desired molarity in mol/L
     * @param {number} volume - Desired volume in liters
     * @returns {number} Mass in grams
     * @throws {Error} If inputs are invalid
     */
    calculateMass(molarity, volume) {
        if (molarity <= 0 || volume <= 0) {
            throw new Error("Molarity and volume must be positive numbers");
        }
        if (isNaN(molarity) || isNaN(volume)) {
            throw new Error("Molarity and volume must be valid numbers");
        }

        return molarity * volume * this.molarMass;
    }

    /**
     * Calculates the volume required for a given mass and concentration
     * @param {number} mass - Mass of chemical in grams
     * @param {number} concentration - Desired concentration in mol/L
     * @returns {number} Volume in liters
     * @throws {Error} If inputs are invalid
     */
    calculateVolume(mass, concentration) {
        if (mass <= 0 || concentration <= 0) {
            throw new Error("Mass and concentration must be positive numbers");
        }
        if (isNaN(mass) || isNaN(concentration)) {
            throw new Error("Mass and concentration must be valid numbers");
        }

        return mass / (this.molarMass * concentration);
    }
}

// Propionic Acid specific calculator
const PropionicAcidCalculator = new ChemicalCalculator("C3H6O2", 74.08);

// Example usage with error handling
try {
    const requiredMass = PropionicAcidCalculator.calculateMass(0.1, 0.5);
    console.log(`Required mass: ${requiredMass.toFixed(2)} grams`);

    const requiredVolume = PropionicAcidCalculator.calculateVolume(3.7, 0.1);
    console.log(`Required volume: ${requiredVolume.toFixed(2)} liters`);
} catch (error) {
    console.error("Calculation error:", error.message);
}
```
