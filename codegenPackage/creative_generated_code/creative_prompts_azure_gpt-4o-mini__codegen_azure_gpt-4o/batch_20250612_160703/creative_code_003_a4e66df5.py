"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Develop a JavaScript function that calculates the estimated cost for industrial cleaning services based on the unique needs outlined by Star Cleaning Services.
Generated: DETERMINISTIC_a4e66df5e6c7fa1a
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the estimated cost for industrial cleaning services.
 * 
 * @param {number} area - The size of the area in square meters to be cleaned.
 * @param {string} cleaningType - The type of cleaning required ('basic', 'deep', 'specialized').
 * @param {boolean} hazardousMaterials - Whether hazardous materials are present (true/false).
 * @param {number} frequency - The frequency of cleaning per month (e.g., 1 for once a month, 4 for weekly).
 * @returns {number} - The estimated cost in USD for the cleaning service.
 * 
 * @throws {Error} If invalid inputs are provided.
 */
function calculateCleaningCost(area, cleaningType, hazardousMaterials, frequency) {
    // Validate inputs
    if (typeof area !== 'number' || area <= 0) {
        throw new Error("Invalid area. Area must be a positive number.");
    }
    const validCleaningTypes = ['basic', 'deep', 'specialized'];
    if (!validCleaningTypes.includes(cleaningType)) {
        throw new Error(
            `Invalid cleaning type. Must be one of: ${validCleaningTypes.join(', ')}`
        );
    }
    if (typeof hazardousMaterials !== 'boolean') {
        throw new Error("Invalid hazardousMaterials flag. Must be true or false.");
    }
    if (typeof frequency !== 'number' || frequency <= 0) {
        throw new Error("Invalid frequency. Must be a positive number.");
    }

    // Base rates per square meter for cleaning types
    const cleaningRates = {
        basic: 1.5, // $1.5 per square meter
        deep: 2.5,  // $2.5 per square meter
        specialized: 4.0 // $4.0 per square meter
    };

    // Hazardous materials surcharge (fixed percentage)
    const hazardousSurchargeRate = 0.15; // 15% surcharge

    // Calculate base cost
    let baseCost = area * cleaningRates[cleaningType];

    // Apply hazardous materials surcharge if applicable
    if (hazardousMaterials) {
        baseCost += baseCost * hazardousSurchargeRate;
    }

    // Adjust cost based on frequency (bulk discount for frequent cleaning)
    const frequencyDiscountRate = frequency >= 4 ? 0.10 : 0.0; // 10% discount for weekly cleaning
    const finalCost = baseCost - (baseCost * frequencyDiscountRate);

    // Round the final cost to two decimal places
    return Math.round(finalCost * 100) / 100;
}

// Example usage
try {
    const estimatedCost = calculateCleaningCost(500, 'deep', true, 4);
    console.log(`Estimated Cleaning Cost: $${estimatedCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
