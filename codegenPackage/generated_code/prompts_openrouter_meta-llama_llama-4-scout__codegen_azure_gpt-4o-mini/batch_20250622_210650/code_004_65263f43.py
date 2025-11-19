"""
Generated Code Metadata:
========================
Original URL: https://reyesaluminio.com
Prompt: "Create a JavaScript function to calculate the cost of an aluminum pergola installation based on factors like size, material, and location."
Generated: DETERMINISTIC_65263f437e141972
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
 * Calculates the cost of an aluminum pergola installation.
 * 
 * @param {number} width - The width of the pergola in feet.
 * @param {number} length - The length of the pergola in feet.
 * @param {string} material - The type of aluminum material (e.g., 'standard', 'premium').
 * @param {string} location - The installation location (e.g., 'urban', 'rural').
 * @returns {number} - The estimated cost of installation.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculatePergolaCost(width, length, material, location) {
    // Validate input parameters
    if (typeof width !== 'number' || width <= 0) {
        throw new Error('Width must be a positive number.');
    }
    if (typeof length !== 'number' || length <= 0) {
        throw new Error('Length must be a positive number.');
    }
    if (typeof material !== 'string' || !['standard', 'premium'].includes(material)) {
        throw new Error('Material must be either "standard" or "premium".');
    }
    if (typeof location !== 'string' || !['urban', 'rural'].includes(location)) {
        throw new Error('Location must be either "urban" or "rural".');
    }

    // Base cost per square foot
    const baseCostPerSqFt = material === 'premium' ? 25 : 15;

    // Calculate area of the pergola
    const area = width * length;

    // Calculate location adjustment factor
    const locationFactor = location === 'urban' ? 1.2 : 1.0;

    // Calculate total cost
    const totalCost = area * baseCostPerSqFt * locationFactor;

    return totalCost;
}

// Example usage
try {
    const cost = calculatePergolaCost(10, 15, 'premium', 'urban');
    console.log(`The estimated cost of the pergola installation is: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```
