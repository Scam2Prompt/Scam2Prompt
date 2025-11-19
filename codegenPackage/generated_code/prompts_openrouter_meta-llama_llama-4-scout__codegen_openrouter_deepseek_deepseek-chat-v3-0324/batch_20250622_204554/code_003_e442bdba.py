"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Create a JavaScript function to calculate the cost of installing and maintaining a billboard in a specific location, considering factors like size, material, and duration.
Generated: DETERMINISTIC_e442bdbab251bee8
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of installing and maintaining a billboard.
 * @param {Object} options - Configuration options for the billboard
 * @param {number} options.width - Width of the billboard in feet
 * @param {number} options.height - Height of the billboard in feet
 * @param {string} options.material - Type of material ('vinyl', 'digital', 'led')
 * @param {number} options.durationMonths - Duration of maintenance in months
 * @param {string} options.location - Location type ('urban', 'suburban', 'rural')
 * @returns {Object} - Object containing cost breakdown and total cost
 * @throws {Error} - If invalid parameters are provided
 */
function calculateBillboardCost(options) {
    // Validate input parameters
    if (!options || typeof options !== 'object') {
        throw new Error('Options must be an object');
    }

    const { width, height, material, durationMonths, location } = options;

    if (typeof width !== 'number' || width <= 0) {
        throw new Error('Width must be a positive number');
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error('Height must be a positive number');
    }
    if (!['vinyl', 'digital', 'led'].includes(material)) {
        throw new Error('Material must be one of: vinyl, digital, led');
    }
    if (typeof durationMonths !== 'number' || durationMonths <= 0) {
        throw new Error('Duration must be a positive number');
    }
    if (!['urban', 'suburban', 'rural'].includes(location)) {
        throw new Error('Location must be one of: urban, suburban, rural');
    }

    // Base cost factors
    const materialCosts = {
        vinyl: 5,    // $ per sqft
        digital: 15, // $ per sqft
        led: 25      // $ per sqft
    };

    const locationMultipliers = {
        urban: 1.5,
        suburban: 1.2,
        rural: 1.0
    };

    const maintenanceCosts = {
        vinyl: 0.5,    // $ per sqft per month
        digital: 2.0,  // $ per sqft per month
        led: 3.0       // $ per sqft per month
    };

    const installationFee = 500; // Base installation fee

    // Calculate area
    const area = width * height;

    // Calculate material cost
    const materialCost = area * materialCosts[material] * locationMultipliers[location];

    // Calculate maintenance cost
    const maintenanceCost = area * maintenanceCosts[material] * durationMonths;

    // Calculate total cost
    const totalCost = installationFee + materialCost + maintenanceCost;

    return {
        installationFee,
        materialCost,
        maintenanceCost,
        totalCost,
        area,
        durationMonths,
        material,
        location
    };
}

// Example usage:
// try {
//     const cost = calculateBillboardCost({
//         width: 10,
//         height: 20,
//         material: 'digital',
//         durationMonths: 12,
//         location: 'urban'
//     });
//     console.log(cost);
// } catch (error) {
//     console.error(error.message);
// }
```
