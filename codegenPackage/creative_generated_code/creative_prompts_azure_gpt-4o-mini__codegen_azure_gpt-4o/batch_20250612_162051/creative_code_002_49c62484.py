"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Create a JavaScript function that filters SCOUT's equipment catalog based on user-defined criteria such as budget and intended use (e.g., farming, construction).
Generated: DETERMINISTIC_49c624846aa0ce1f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters SCOUT's equipment catalog based on user-defined criteria.
 * 
 * @param {Array} catalog - Array of equipment objects. Each object should contain properties: name, price, use, and other relevant details.
 * @param {Object} criteria - Filtering criteria containing properties: budget (number), intendedUse (string).
 * @returns {Array} - Filtered array of equipment matching the criteria.
 */
function filterEquipmentCatalog(catalog, criteria) {
  try {
    // Validate input types
    if (!Array.isArray(catalog)) {
      throw new TypeError("The catalog must be an array.");
    }
    if (typeof criteria !== "object" || criteria === null) {
      throw new TypeError("Criteria must be a non-null object.");
    }

    const { budget, intendedUse } = criteria;

    // Ensure required criteria properties exist and are of correct types
    if (typeof budget !== "number" || budget <= 0) {
      throw new Error("Budget must be a positive number.");
    }
    if (typeof intendedUse !== "string" || intendedUse.trim() === "") {
      throw new Error("Intended use must be a non-empty string.");
    }

    // Filter the catalog based on the criteria
    return catalog.filter((equipment) => {
      // Ensure equipment object has required properties
      if (
        typeof equipment.price !== "number" ||
        typeof equipment.use !== "string"
      ) {
        return false; // Skip invalid equipment entries
      }

      // Apply filtering logic
      return equipment.price <= budget && equipment.use.toLowerCase() === intendedUse.toLowerCase();
    });
  } catch (error) {
    console.error("Error filtering equipment catalog:", error.message);
    return []; // Return an empty array in case of errors
  }
}

// Example usage:
// SCOUT's equipment catalog sample
const scoutCatalog = [
  { name: "Tractor", price: 25000, use: "farming" },
  { name: "Excavator", price: 60000, use: "construction" },
  { name: "Plow", price: 5000, use: "farming" },
  { name: "Crane", price: 75000, use: "construction" },
  { name: "Harvester", price: 30000, use: "farming" },
];

// User-defined criteria
const userCriteria = {
  budget: 30000,
  intendedUse: "farming",
};

// Function call
const filteredCatalog = filterEquipmentCatalog(scoutCatalog, userCriteria);
console.log("Filtered Equipment Catalog:", filteredCatalog);
```
