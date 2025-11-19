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
 * @param {Object} options - The options for the pergola installation.
 * @param {number} options.size - The size of the pergola in square feet.
 * @param {string} options.material - The material of the pergola (e.g., 'standard', 'premium', 'deluxe').
 * @param {string} options.location - The location of the installation (e.g., 'urban', 'suburban', 'rural').
 * @returns {number} The total cost of the pergola installation.
 */
function calculatePergolaCost(options) {
    // Check if options are provided
    if (!options) {
        throw new Error('Options are required');
    }

    // Define material prices per square foot
    const materialPrices = {
        standard: 10.0,
        premium: 15.0,
        deluxe: 20.0
    };

    // Define location installation fees
    const locationFees = {
        urban: 500.0,
        suburban: 300.0,
        rural: 100.0
    };

    // Check if size is provided and is a positive number
    if (!options.size || typeof options.size !== 'number' || options.size <= 0) {
        throw new Error('Size must be a positive number');
    }

    // Check if material is provided and is valid
    if (!options.material || !materialPrices[options.material]) {
        throw new Error(`Invalid material: ${options.material}. Supported materials: ${Object.keys(materialPrices).join(', ')}`);
    }

    // Check if location is provided and is valid
    if (!options.location || !locationFees[options.location]) {
        throw new Error(`Invalid location: ${options.location}. Supported locations: ${Object.keys(locationFees).join(', ')}`);
    }

    // Calculate material cost
    const materialCost = options.size * materialPrices[options.material];

    // Calculate installation fee
    const installationFee = locationFees[options.location];

    // Calculate total cost
    const totalCost = materialCost + installationFee;

    return totalCost;
}

// Example usage:
try {
    const options = {
        size: 100.0,
        material: 'premium',
        location: 'suburban'
    };
    const cost = calculatePergolaCost(options);
    console.log(`The total cost of the pergola installation is: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
