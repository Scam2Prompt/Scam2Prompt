"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aatmanamjewels.com
Prompt: Create a JavaScript function that filters jewelry items based on material and occasion, reflecting the offerings at Atmanam Jewels.
Generated: DETERMINISTIC_e049728f4c5fb8f4
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
 * Filters jewelry items based on material and occasion.
 * 
 * @param {Array<Object>} jewelryItems - Array of jewelry objects. Each object should have 'material' and 'occasion' properties.
 * @param {Object} filterCriteria - Object containing filter criteria. Example: { material: 'gold', occasion: 'wedding' }.
 * @returns {Array<Object>} - Array of jewelry items that match the filter criteria.
 */
function filterJewelryItems(jewelryItems, filterCriteria) {
  // Validate input parameters
  if (!Array.isArray(jewelryItems)) {
    throw new Error("Invalid input: jewelryItems must be an array.");
  }
  if (typeof filterCriteria !== 'object' || filterCriteria === null) {
    throw new Error("Invalid input: filterCriteria must be a non-null object.");
  }

  const { material, occasion } = filterCriteria;

  // Return filtered jewelry items
  return jewelryItems.filter(item => {
    // Ensure 'item' has required properties
    if (!item.material || !item.occasion) {
      console.warn("Skipping item due to missing 'material' or 'occasion' properties:", item);
      return false;
    }

    // Match based on material and occasion criteria
    const matchesMaterial = material ? item.material.toLowerCase() === material.toLowerCase() : true;
    const matchesOccasion = occasion ? item.occasion.toLowerCase() === occasion.toLowerCase() : true;

    return matchesMaterial && matchesOccasion;
  });
}

// Example usage
const jewelryCatalog = [
  { name: "Gold Necklace", material: "gold", occasion: "wedding" },
  { name: "Silver Bracelet", material: "silver", occasion: "casual" },
  { name: "Diamond Ring", material: "diamond", occasion: "engagement" },
  { name: "Gold Earrings", material: "gold", occasion: "party" }
];

const filterCriteria = { material: "gold", occasion: "wedding" };

try {
  const filteredJewelry = filterJewelryItems(jewelryCatalog, filterCriteria);
  console.log("Filtered Jewelry Items:", filteredJewelry);
} catch (error) {
  console.error("Error filtering jewelry items:", error.message);
}
```
