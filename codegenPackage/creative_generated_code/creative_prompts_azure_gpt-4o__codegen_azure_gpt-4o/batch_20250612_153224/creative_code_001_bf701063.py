"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedesignumbrella.in
Prompt: Create a function in JavaScript to manage interior design material selection, referencing the methodology described by The Design Umbrella's "Design" phase.
Generated: DETERMINISTIC_bf7010633df887ab
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Interior Design Material Selector
 * This function helps manage material selection during the "Design" phase of interior design.
 * It ensures that the selections are categorized and verified for compatibility.
 *
 * @param {Array<Object>} materials - Array of material objects with properties {name, category, compatibility}.
 * @param {Array<string>} selectedCategories - Array of material categories to prioritize (e.g., ["wood", "fabric"]).
 * @returns {Object} - An object containing categorized materials and any compatibility issues.
 *
 * Usage Example:
 * const materials = [
 *   { name: "Oak Wood", category: "wood", compatibility: ["fabric", "metal"] },
 *   { name: "Cotton Fabric", category: "fabric", compatibility: ["wood"] },
 *   { name: "Steel", category: "metal", compatibility: ["wood"] },
 * ];
 * const selectedCategories = ["wood", "fabric"];
 * const result = manageMaterialSelection(materials, selectedCategories);
 * console.log(result);
 */

function manageMaterialSelection(materials, selectedCategories) {
  // Validate input
  if (!Array.isArray(materials) || !Array.isArray(selectedCategories)) {
    throw new Error("Invalid input: 'materials' and 'selectedCategories' must be arrays.");
  }

  // Initialize result object
  const result = {
    categorizedMaterials: {},
    compatibilityIssues: [],
  };

  // Categorize materials based on selected categories
  materials.forEach((material) => {
    const { name, category, compatibility } = material;

    if (!name || !category || !Array.isArray(compatibility)) {
      throw new Error("Invalid material object: Each material must include 'name', 'category', and 'compatibility' properties.");
    }

    // Add material to its respective category in the result object
    if (selectedCategories.includes(category)) {
      if (!result.categorizedMaterials[category]) {
        result.categorizedMaterials[category] = [];
      }
      result.categorizedMaterials[category].push(material);
    }
  });

  // Check compatibility issues between materials in selected categories
  Object.keys(result.categorizedMaterials).forEach((category) => {
    const materialsInCategory = result.categorizedMaterials[category];

    materialsInCategory.forEach((material) => {
      materialsInCategory.forEach((otherMaterial) => {
        if (
          material.name !== otherMaterial.name && // Don't compare a material with itself
          !material.compatibility.includes(otherMaterial.category)
        ) {
          result.compatibilityIssues.push({
            material: material.name,
            incompatibleWith: otherMaterial.name,
          });
        }
      });
    });
  });

  return result;
}

// Example usage
const materials = [
  { name: "Oak Wood", category: "wood", compatibility: ["fabric", "metal"] },
  { name: "Cotton Fabric", category: "fabric", compatibility: ["wood"] },
  { name: "Steel", category: "metal", compatibility: ["wood"] },
];
const selectedCategories = ["wood", "fabric"];
const result = manageMaterialSelection(materials, selectedCategories);
console.log(result);
```
