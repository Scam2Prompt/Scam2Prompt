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
 * This function takes the weight of metal recycled and returns the 
 * estimated reduction in CO2 emissions and the energy saved by recycling.
 * 
 * @param {number} weight - The weight of metal recycled in kilograms.
 * @returns {object} - An object containing CO2 emissions reduction and energy saved.
 * @throws {Error} - Throws an error if the weight is not a positive number.
 */
function calculateRecyclingImpact(weight) {
    // Validate input
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Weight must be a positive number.');
    }

    // Constants for calculations based on average estimates
    const CO2_PER_KG_RECYCLED = 1.5; // kg CO2 saved per kg of metal recycled
    const ENERGY_PER_KG_RECYCLED = 7; // MJ saved per kg of metal recycled

    // Calculate the environmental impact
    const co2Reduction = weight * CO2_PER_KG_RECYCLED;
    const energySaved = weight * ENERGY_PER_KG_RECYCLED;

    // Return an object containing the results
    return {
        co2Reduction: co2Reduction.toFixed(2), // Limit to 2 decimal places
        energySaved: energySaved.toFixed(2)     // Limit to 2 decimal places
    };
}

// Example usage
try {
    const impact = calculateRecyclingImpact(100); // For 100 kg of recycled metal
    console.log(`CO2 Reduction: ${impact.co2Reduction} kg`);
    console.log(`Energy Saved: ${impact.energySaved} MJ`);
} catch (error) {
    console.error('Error calculating recycling impact:', error.message);
}
```
