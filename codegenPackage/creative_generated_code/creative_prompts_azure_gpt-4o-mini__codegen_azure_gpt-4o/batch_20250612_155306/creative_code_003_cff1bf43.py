"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Develop a JavaScript function that allows users to search for auto parts by brand and model, similar to the filtering options provided on the autopecasbrazz site.
Generated: DETERMINISTIC_cff1bf4388aa7840
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to search auto parts by brand and model.
 * @param {Array} inventory - List of auto parts in the inventory.
 * @param {String} brand - Brand name to filter the parts.
 * @param {String} model - Model name to filter the parts.
 * @returns {Array} - List of auto parts matching the criteria.
 */
function searchAutoParts(inventory, brand, model) {
  // Validate input parameters
  if (!Array.isArray(inventory)) {
    throw new Error("Invalid inventory provided. Expected an array.");
  }
  if (typeof brand !== "string" || typeof model !== "string") {
    throw new Error("Brand and model must be strings.");
  }

  // Filter auto parts matching the brand and model criteria
  const filteredParts = inventory.filter(part => {
    // Ensure part has brand and model properties for comparison
    if (!part.brand || !part.model) {
      console.warn("Skipping part due to missing brand or model property:", part);
      return false;
    }
    return part.brand.toLowerCase() === brand.toLowerCase() &&
           part.model.toLowerCase() === model.toLowerCase();
  });

  return filteredParts;
}

// Example inventory data (for testing purposes)
const autoPartsInventory = [
  { id: 1, brand: "Toyota", model: "Corolla", part: "Brake Pad", price: 50 },
  { id: 2, brand: "Honda", model: "Civic", part: "Oil Filter", price: 20 },
  { id: 3, brand: "Toyota", model: "Camry", part: "Air Filter", price: 30 },
  { id: 4, brand: "Honda", model: "Civic", part: "Headlight", price: 100 },
  { id: 5, brand: "Toyota", model: "Corolla", part: "Wiper Blade", price: 15 },
];

// Example usage of the function
try {
  const searchResults = searchAutoParts(autoPartsInventory, "Toyota", "Corolla");
  console.log("Search Results:", searchResults);
} catch (error) {
  console.error("Error:", error.message);
}
```
