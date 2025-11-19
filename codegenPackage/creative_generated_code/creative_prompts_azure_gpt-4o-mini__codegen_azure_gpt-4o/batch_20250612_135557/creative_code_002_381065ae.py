"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Create a JavaScript function that calculates the optimal packaging materials for exporting fruits, based on the guidelines provided by Osku for maintaining fruit quality.
Generated: DETERMINISTIC_381065ae023707fb
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate optimal packaging materials for exporting fruits
 * based on guidelines for maintaining fruit quality.
 * 
 * @param {Array} fruits - Array of fruit objects, each with a name, weight (grams), and type (e.g., "fragile" or "standard").
 * @returns {Object} - Packaging recommendation including type of box, padding material, and total weight.
 * 
 * Example of `fruits` input:
 * [
 *   { name: "Apple", weight: 200, type: "standard" },
 *   { name: "Mango", weight: 300, type: "fragile" }
 * ]
 */

function calculateOptimalPackaging(fruits) {
  // Validate input
  if (!Array.isArray(fruits)) {
    throw new Error("Input must be an array of fruit objects.");
  }

  let totalWeight = 0; // Total weight of all fruits
  let requiresFragileHandling = false; // Flag for fragile fruits
  
  // Loop through fruits to aggregate weight and check for fragile types
  fruits.forEach((fruit) => {
    if (
      typeof fruit !== "object" ||
      !fruit.name ||
      typeof fruit.weight !== "number" ||
      !fruit.type
    ) {
      throw new Error("Each fruit must be an object with valid name, weight, and type.");
    }

    totalWeight += fruit.weight;

    if (fruit.type.toLowerCase() === "fragile") {
      requiresFragileHandling = true;
    }
  });

  // Recommend packaging box type based on total weight
  let boxType;
  if (totalWeight <= 1000) {
    boxType = "Small Box"; // Suitable for up to 1kg
  } else if (totalWeight <= 5000) {
    boxType = "Medium Box"; // Suitable for up to 5kg
  } else {
    boxType = "Large Box"; // Suitable for more than 5kg
  }

  // Recommend padding material based on fruit type
  const paddingMaterial = requiresFragileHandling ? "Bubble Wrap" : "Foam Sheets";

  // Return the packaging recommendation
  return {
    boxType,
    paddingMaterial,
    totalWeight
  };
}

// Example usage
try {
  const fruits = [
    { name: "Mango", weight: 300, type: "fragile" },
    { name: "Banana", weight: 500, type: "standard" },
    { name: "Apple", weight: 200, type: "standard" }
  ];

  const packagingRecommendation = calculateOptimalPackaging(fruits);
  console.log(packagingRecommendation);
  // Output: { boxType: 'Small Box', paddingMaterial: 'Bubble Wrap', totalWeight: 1000 }
} catch (error) {
  console.error("Error:", error.message);
}
```
