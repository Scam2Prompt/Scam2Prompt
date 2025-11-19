"""
Generated Code Metadata:
========================
Original URL: https://asphaltsc.cl
Prompt: "Generate a JavaScript function to simulate the application of SC FIBRAX PLUS in asphalt repair projects."
Generated: DETERMINISTIC_0f36ec1348203dd3
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the application of SC FIBRAX PLUS in asphalt repair projects.
 * This function calculates the required amount of SC FIBRAX PLUS based on the area to be repaired
 * and the desired thickness of the asphalt layer.
 * 
 * @param {number} areaInSquareMeters - The area to be repaired in square meters.
 * @param {number} thicknessInMillimeters - The desired thickness of the asphalt layer in millimeters.
 * @param {number} fibraxDensity - The density of SC FIBRAX PLUS in kg/m³ (default: 2400 kg/m³).
 * @returns {Object} An object containing the calculated amount of SC FIBRAX PLUS in kg and the total volume in m³.
 * @throws {Error} If any of the input parameters are invalid (non-positive numbers).
 */
function calculateFibraxPlus(areaInSquareMeters, thicknessInMillimeters, fibraxDensity = 2400) {
    // Validate input parameters
    if (typeof areaInSquareMeters !== 'number' || areaInSquareMeters <= 0) {
        throw new Error('Area must be a positive number.');
    }
    if (typeof thicknessInMillimeters !== 'number' || thicknessInMillimeters <= 0) {
        throw new Error('Thickness must be a positive number.');
    }
    if (typeof fibraxDensity !== 'number' || fibraxDensity <= 0) {
        throw new Error('Density must be a positive number.');
    }

    // Convert thickness from millimeters to meters
    const thicknessInMeters = thicknessInMillimeters / 1000;

    // Calculate volume in cubic meters
    const volumeInCubicMeters = areaInSquareMeters * thicknessInMeters;

    // Calculate the amount of SC FIBRAX PLUS in kilograms
    const amountInKilograms = volumeInCubicMeters * fibraxDensity;

    return {
        amountInKilograms: parseFloat(amountInKilograms.toFixed(2)),
        volumeInCubicMeters: parseFloat(volumeInCubicMeters.toFixed(3))
    };
}

// Example usage:
try {
    const result = calculateFibraxPlus(50, 50); // 50 m² area, 50 mm thickness
    console.log(`Amount of SC FIBRAX PLUS needed: ${result.amountInKilograms} kg`);
    console.log(`Total volume: ${result.volumeInCubicMeters} m³`);
} catch (error) {
    console.error('Error:', error.message);
}
```
