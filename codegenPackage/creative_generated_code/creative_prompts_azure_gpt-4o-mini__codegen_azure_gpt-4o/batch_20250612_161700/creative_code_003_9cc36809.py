"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Develop a JavaScript function that calculates the cost estimation for glass and aluminum projects based on user inputs, similar to the offerings of CristalesGraf.
Generated: DETERMINISTIC_9cc3680962042119
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cost estimation for glass and aluminum projects.
 * 
 * @param {string} projectType - The type of project ("glass" or "aluminum").
 * @param {number} area - The area in square meters (m²) for the project.
 * @param {number} materialQuality - The quality of the material (scale of 1-5).
 * @param {number} laborRate - The cost of labor per square meter.
 * @returns {number} - The estimated total cost of the project.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateCost(projectType, area, materialQuality, laborRate) {
    // Validate inputs
    if (typeof projectType !== 'string' || !["glass", "aluminum"].includes(projectType.toLowerCase())) {
        throw new Error("Invalid project type. Please specify 'glass' or 'aluminum'.");
    }
    if (typeof area !== 'number' || area <= 0) {
        throw new Error("Area must be a positive number.");
    }
    if (typeof materialQuality !== 'number' || materialQuality < 1 || materialQuality > 5) {
        throw new Error("Material quality must be a number between 1 and 5.");
    }
    if (typeof laborRate !== 'number' || laborRate <= 0) {
        throw new Error("Labor rate must be a positive number.");
    }

    // Base cost per square meter for glass and aluminum
    const baseCost = {
        glass: 50,       // Base cost per m² for glass
        aluminum: 70     // Base cost per m² for aluminum
    };

    // Calculate material cost multiplier based on quality (e.g., higher quality = higher multiplier)
    const materialMultiplier = 1 + (materialQuality - 1) * 0.2;

    // Calculate total cost
    const materialCost = baseCost[projectType.toLowerCase()] * materialMultiplier * area;
    const laborCost = laborRate * area;
    const totalCost = materialCost + laborCost;

    return totalCost;
}

// Example usage:
try {
    const projectType = "glass";      // Type of project (glass or aluminum)
    const area = 25;                 // Area in m²
    const materialQuality = 4;       // Material quality (1 to 5 scale)
    const laborRate = 30;            // Labor cost per m²
    
    const estimatedCost = calculateCost(projectType, area, materialQuality, laborRate);
    console.log(`Estimated Cost: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
