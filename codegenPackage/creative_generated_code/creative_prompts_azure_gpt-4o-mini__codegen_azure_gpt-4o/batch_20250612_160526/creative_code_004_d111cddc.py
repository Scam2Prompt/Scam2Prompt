"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://screciclados.mx
Prompt: Develop a function in JavaScript that calculates the environmental impact of recycling metals, based on the mission of SCR Reciclados.
Generated: DETERMINISTIC_d111cddc8a253866
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the environmental impact of recycling metals.
 * 
 * This function determines the amount of energy saved and CO2 emissions reduced
 * by recycling metals, based on industry averages and the mission of SCR Reciclados.
 * 
 * @param {number} weight - The weight of recycled metal in kilograms.
 * @param {string} metalType - The type of metal being recycled (e.g., 'aluminum', 'steel', 'copper').
 * @returns {object} An object containing energySaved (kWh) and co2Reduced (kg).
 * @throws Will throw an error if weight is not a positive number or metalType is invalid.
 */
function calculateEnvironmentalImpact(weight, metalType) {
    // Validate input
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error("Weight must be a positive number.");
    }
    if (typeof metalType !== 'string' || !['aluminum', 'steel', 'copper'].includes(metalType.toLowerCase())) {
        throw new Error("Invalid metal type. Valid options are 'aluminum', 'steel', or 'copper'.");
    }

    // Define industry averages for energy savings and CO2 reduction per kilogram of metal recycled
    const metalData = {
        aluminum: { energySavedPerKg: 14, co2ReducedPerKg: 9 }, // Data is hypothetical
        steel: { energySavedPerKg: 4, co2ReducedPerKg: 1.8 },  // Replace with actual industry values
        copper: { energySavedPerKg: 5, co2ReducedPerKg: 3.5 }  // Replace with actual industry values
    };

    // Retrieve data specific to the selected metal type
    const metalImpact = metalData[metalType.toLowerCase()];

    // Calculate total impact
    const energySaved = metalImpact.energySavedPerKg * weight;
    const co2Reduced = metalImpact.co2ReducedPerKg * weight;

    // Return results as an object
    return {
        energySaved, // Energy saved in kWh
        co2Reduced   // CO2 emissions reduced in kilograms
    };
}

// Example Usage:
try {
    const impact = calculateEnvironmentalImpact(100, 'aluminum');
    console.log(`Energy Saved: ${impact.energySaved} kWh`);
    console.log(`CO2 Reduced: ${impact.co2Reduced} kg`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
