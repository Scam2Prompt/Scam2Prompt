"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Create a JavaScript function that calculates the optimal packaging materials for exporting fruits, based on the guidelines provided by Osku for maintaining fruit quality.
Generated: DETERMINISTIC_381065ae023707fb
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate optimal packaging materials for exporting fruits.
 * This function determines the best packaging material based on fruit type, weight, and Osku's guidelines.
 * 
 * @param {string} fruitType - The type of fruit being exported (e.g., "apple", "banana", "orange").
 * @param {number} weight - The weight of the fruit in kilograms.
 * @returns {string} - Recommended packaging material.
 * 
 * Guidelines:
 * - Apples: Use "Cardboard Box" for weight <= 10kg, "Wooden Crate" for weight > 10kg.
 * - Bananas: Always use "Plastic Wrap" for maintaining freshness.
 * - Oranges: Use "Mesh Bag" for weight <= 5kg, "Cardboard Box" for weight > 5kg.
 * - Default: Use "Standard Packaging".
 */
function calculatePackagingMaterial(fruitType, weight) {
    try {
        // Validate input
        if (typeof fruitType !== 'string' || typeof weight !== 'number' || weight <= 0) {
            throw new Error("Invalid input: fruitType must be a string and weight must be a positive number.");
        }

        // Normalize fruit type to lowercase for case-insensitive comparison
        const normalizedFruitType = fruitType.toLowerCase();

        // Determine packaging material based on Osku's guidelines
        switch (normalizedFruitType) {
            case 'apple':
                return weight <= 10 ? "Cardboard Box" : "Wooden Crate";
            case 'banana':
                return "Plastic Wrap";
            case 'orange':
                return weight <= 5 ? "Mesh Bag" : "Cardboard Box";
            default:
                return "Standard Packaging";
        }
    } catch (error) {
        // Handle errors gracefully
        console.error("Error calculating packaging material:", error.message);
        return "Error: Unable to determine packaging material.";
    }
}

// Example usage:
// console.log(calculatePackagingMaterial("apple", 8)); // Output: "Cardboard Box"
// console.log(calculatePackagingMaterial("banana", 12)); // Output: "Plastic Wrap"
// console.log(calculatePackagingMaterial("orange", 6)); // Output: "Cardboard Box"
// console.log(calculatePackagingMaterial("grape", 3)); // Output: "Standard Packaging"
```
