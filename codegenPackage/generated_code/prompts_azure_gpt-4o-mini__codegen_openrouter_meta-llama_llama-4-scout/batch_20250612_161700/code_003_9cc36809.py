"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Develop a JavaScript function that calculates the cost estimation for glass and aluminum projects based on user inputs, similar to the offerings of CristalesGraf.
Generated: DETERMINISTIC_9cc3680962042119
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost estimation for glass and aluminum projects.
 * 
 * @param {Object} projectDetails - Project details object.
 * @param {string} projectDetails.material - Material type (glass or aluminum).
 * @param {number} projectDetails.width - Width of the project in meters.
 * @param {number} projectDetails.height - Height of the project in meters.
 * @param {number} projectDetails.thickness - Thickness of the material in mm.
 * @param {number} [projectDetails.frameWidth=0] - Width of the frame in meters.
 * @returns {Object} Cost estimation object.
 */
function calculateCostEstimation(projectDetails) {
    try {
        // Validate input parameters
        if (!projectDetails || typeof projectDetails !== 'object') {
            throw new Error('Invalid project details');
        }

        const requiredProperties = ['material', 'width', 'height', 'thickness'];
        if (!requiredProperties.every(prop => prop in projectDetails)) {
            throw new Error('Missing required project details');
        }

        const materialPrices = {
            glass: 50, // price per square meter
            aluminum: 70 // price per square meter
        };

        const framePrice = 10; // price per meter

        // Calculate area
        const area = projectDetails.width * projectDetails.height;

        // Calculate material cost
        const material = projectDetails.material.toLowerCase();
        if (!(material in materialPrices)) {
            throw new Error(`Unsupported material: ${material}`);
        }
        const materialCost = area * materialPrices[material];

        // Calculate frame cost
        let frameCost = 0;
        if (projectDetails.frameWidth > 0) {
            const framePerimeter = 2 * (projectDetails.width + projectDetails.height);
            frameCost = framePerimeter * projectDetails.frameWidth * framePrice;
        }

        // Calculate total cost
        const totalCost = materialCost + frameCost;

        // Calculate thickness surcharge
        let thicknessSurcharge = 0;
        if (projectDetails.thickness > 5) {
            thicknessSurcharge = area * 5; // 5% surcharge for thickness above 5mm
        }

        // Return cost estimation
        return {
            materialCost,
            frameCost,
            thicknessSurcharge,
            totalCost: totalCost + thicknessSurcharge
        };
    } catch (error) {
        // Log and rethrow error
        // console.error(error); // Commented out for production code
        throw error;
    }
}

// Example usage:
const projectDetails = {
    material: 'glass',
    width: 2,
    height: 3,
    thickness: 6,
    frameWidth: 0.1
};

const costEstimation = calculateCostEstimation(projectDetails);
// console.log(costEstimation); // Commented out for production code
```
