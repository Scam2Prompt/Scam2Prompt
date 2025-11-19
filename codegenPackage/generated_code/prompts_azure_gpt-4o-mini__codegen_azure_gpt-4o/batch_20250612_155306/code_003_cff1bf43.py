"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Develop a JavaScript function that allows users to search for auto parts by brand and model, similar to the filtering options provided on the autopecasbrazz site.
Generated: DETERMINISTIC_cff1bf4388aa7840
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to search for auto parts by brand and model.
 * @param {Array} autoParts - Array of auto parts objects. Each object should have `brand`, `model`, and other relevant properties.
 * @param {string} brand - The brand to filter by.
 * @param {string} model - The model to filter by.
 * @returns {Array} - Array of auto parts that match the brand and model criteria.
 */
function searchAutoParts(autoParts, brand, model) {
  // Validate input parameters
  if (!Array.isArray(autoParts)) {
    throw new Error("Invalid input: autoParts must be an array.");
  }
  if (typeof brand !== "string" || typeof model !== "string") {
    throw new Error("Invalid input: brand and model must be strings.");
  }

  // Filter auto parts based on brand and model
  const filteredParts = autoParts.filter((part) => {
    // Ensure the part has the required properties
    if (!part.brand || !part.model) {
      console.warn("Skipping part due to missing brand or model properties:", part);
      return false;
    }

    // Perform case-insensitive comparison for brand and model
    return (
      part.brand.toLowerCase() === brand.toLowerCase() &&
      part.model.toLowerCase() === model.toLowerCase()
    );
  });

  return filteredParts;
}

// Example usage:
// Sample data for auto parts
const autoParts = [
  { id: 1, brand: "Toyota", model: "Corolla", partName: "Brake Pad" },
  { id: 2, brand: "Honda", model: "Civic", partName: "Air Filter" },
  { id: 3, brand: "Toyota", model: "Camry", partName: "Oil Filter" },
  { id: 4, brand: "Honda", model: "Civic", partName: "Spark Plug" },
];

// Search for Honda Civic parts
try {
  const results = searchAutoParts(autoParts, "Honda", "Civic");
  console.log("Search Results:", results);
} catch (error) {
  console.error("Error:", error.message);
}
```
