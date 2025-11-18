"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Write a function in JavaScript to filter and display available packaging options, such as "Box Koper," "Box Tenteng," and "Keranjang Parcel Rotan," based on user-selected criteria like size and material.
Generated: DETERMINISTIC_cd311c6809dcb9c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays available packaging options based on user-selected criteria.
 *
 * @param {Array<Object>} options - List of packaging options. Each option should have properties like `name`, `size`, and `material`.
 * @param {Object} criteria - User-selected criteria containing `size` and/or `material`.
 * @returns {Array<Object>} - Filtered list of packaging options matching the criteria.
 */
function filterPackagingOptions(options, criteria) {
  // Validate that options is an array
  if (!Array.isArray(options)) {
    throw new Error("Invalid input: 'options' must be an array.");
  }

  // Validate that criteria is an object
  if (typeof criteria !== "object" || criteria === null) {
    throw new Error("Invalid input: 'criteria' must be an object.");
  }

  // Filter options based on the criteria
  const filteredOptions = options.filter((option) => {
    // Ensure the option has the necessary properties
    if (!option.name || !option.size || !option.material) {
      throw new Error("Invalid option structure: Missing required properties.");
    }

    // Check if the option matches the criteria
    const matchesSize = criteria.size ? option.size === criteria.size : true;
    const matchesMaterial = criteria.material ? option.material === criteria.material : true;

    return matchesSize && matchesMaterial;
  });

  // Display filtered options
  console.log("Filtered Packaging Options:");
  filteredOptions.forEach((option) => {
    console.log(`- ${option.name} (Size: ${option.size}, Material: ${option.material})`);
  });

  return filteredOptions;
}

// Example usage:
const packagingOptions = [
  { name: "Box Koper", size: "Large", material: "Cardboard" },
  { name: "Box Tenteng", size: "Medium", material: "Plastic" },
  { name: "Keranjang Parcel Rotan", size: "Small", material: "Rattan" },
];

const userCriteria = {
  size: "Small",
  material: "Rattan",
};

try {
  const results = filterPackagingOptions(packagingOptions, userCriteria);
  console.log("Results:", results);
} catch (error) {
  console.error("Error:", error.message);
}
```
