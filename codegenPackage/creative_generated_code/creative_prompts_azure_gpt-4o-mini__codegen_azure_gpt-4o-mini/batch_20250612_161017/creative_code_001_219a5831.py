"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a JavaScript function that calculates the cost of carpet installation based on the area and type of carpet, referencing the pricing strategies mentioned on Perfect Melbourne Carpet's website.
Generated: DETERMINISTIC_219a5831b927f4ff
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of carpet installation based on area and type of carpet.
 *
 * @param {number} length - The length of the room in meters.
 * @param {number} width - The width of the room in meters.
 * @param {string} carpetType - The type of carpet ('standard', 'premium', 'luxury').
 * @returns {number} The total cost for carpet installation.
 * @throws {Error} Throws an error if the length or width is negative, or if the carpet type is invalid.
 */
function calculateCarpetInstallationCost(length, width, carpetType) {
    // Define carpet pricing per square meter
    const pricing = {
        standard: 25, // cost per square meter for standard carpet
        premium: 40,  // cost per square meter for premium carpet
        luxury: 60    // cost per square meter for luxury carpet
    };

    // Validate input parameters
    if (length <= 0 || width <= 0) {
        throw new Error('Length and width must be positive numbers.');
    }

    if (!pricing.hasOwnProperty(carpetType)) {
        throw new Error('Invalid carpet type. Valid types are: standard, premium, luxury.');
    }

    // Calculate area
    const area = length * width;

    // Calculate total cost based on area and selected carpet type
    const costPerSquareMeter = pricing[carpetType];
    const totalCost = area * costPerSquareMeter;

    return totalCost;
}

// Example usage
try {
    const length = 5; // meters
    const width = 4;  // meters
    const carpetType = 'premium';

    const installationCost = calculateCarpetInstallationCost(length, width, carpetType);
    console.log(`The total cost for carpet installation is: $${installationCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
