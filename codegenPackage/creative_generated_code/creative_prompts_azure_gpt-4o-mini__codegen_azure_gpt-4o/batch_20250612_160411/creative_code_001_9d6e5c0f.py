"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinsup.blogspot.com
Prompt: Write a JavaScript function that filters shoe categories such as running shoes and social shoes from the Raila Sapatos em Geral inventory.
Generated: DETERMINISTIC_9d6e5c0f283247de
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters shoe categories such as running shoes and social shoes 
 * from the Raila Sapatos em Geral inventory.
 * 
 * @param {Array} inventory - Array of shoe objects.
 * @returns {Object} Filtered inventory containing running and social shoes.
 */ 
function filterShoeCategories(inventory) {
  // Validate input
  if (!Array.isArray(inventory)) {
    throw new Error("Invalid inventory input. Expected an array of shoes.");
  }

  // Define categories to filter
  const targetCategories = ["running shoes", "social shoes"];

  // Filter inventory based on the target categories
  const filteredInventory = inventory.filter(shoe => {
    // Validate each shoe object
    if (!shoe || typeof shoe.category !== "string") {
      console.warn("Skipping invalid shoe entry:", shoe);
      return false;
    }
    // Check if the shoe category matches one of the target categories
    return targetCategories.includes(shoe.category.toLowerCase());
  });

  // Group filtered inventory by categories
  const groupedInventory = {
    runningShoes: filteredInventory.filter(shoe => shoe.category.toLowerCase() === "running shoes"),
    socialShoes: filteredInventory.filter(shoe => shoe.category.toLowerCase() === "social shoes"),
  };

  return groupedInventory;
}

// Example usage:
const railaSapatosInventory = [
  { id: 1, name: "Nike Air Zoom Pegasus 38", category: "Running Shoes", price: 120 },
  { id: 2, name: "Adidas Ultraboost 22", category: "Running Shoes", price: 180 },
  { id: 3, name: "Oxford Classic", category: "Social Shoes", price: 90 },
  { id: 4, name: "Leather Loafers", category: "Social Shoes", price: 110 },
  { id: 5, name: "Flip Flops", category: "Casual Shoes", price: 15 }, // Not a target category
  { id: 6, name: "Trail Running GTX", category: "Running Shoes", price: 150 },
  null, // Invalid entry
];

try {
  const filteredCategories = filterShoeCategories(railaSapatosInventory);
  console.log("Filtered Inventory:", filteredCategories);
} catch (error) {
  console.error("Error filtering shoe categories:", error.message);
}
```
