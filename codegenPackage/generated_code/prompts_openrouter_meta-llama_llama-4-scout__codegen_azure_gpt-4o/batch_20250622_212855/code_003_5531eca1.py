"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Create a JavaScript function to sort a list of toys by category, including "Brinquedos de Cowboy", "Brinquedos de Pedal", and "Brinquedos Eletrônicos".
Generated: DETERMINISTIC_5531eca1bc548d57
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to sort a list of toys by category.
 * Categories: "Brinquedos de Cowboy", "Brinquedos de Pedal", "Brinquedos Eletrônicos".
 * Any toys not matching these categories will be grouped under "Outros".
 *
 * @param {Array} toys - Array of toy objects. Each object should have a `name` and `category` property.
 * @returns {Object} - An object with toys grouped by category.
 */
function sortToysByCategory(toys) {
  // Validate input
  if (!Array.isArray(toys)) {
    throw new Error("Input must be an array of toy objects.");
  }

  // Define valid categories
  const validCategories = [
    "Brinquedos de Cowboy",
    "Brinquedos de Pedal",
    "Brinquedos Eletrônicos",
  ];

  // Initialize result object with categories
  const sortedToys = {
    "Brinquedos de Cowboy": [],
    "Brinquedos de Pedal": [],
    "Brinquedos Eletrônicos": [],
    Outros: [],
  };

  // Iterate through the toys array
  toys.forEach((toy) => {
    // Validate toy object structure
    if (!toy || typeof toy.name !== "string" || typeof toy.category !== "string") {
      throw new Error("Each toy must have a `name` (string) and `category` (string).");
    }

    // Check if the toy's category is valid
    if (validCategories.includes(toy.category)) {
      sortedToys[toy.category].push(toy);
    } else {
      // If category is invalid, add to "Outros"
      sortedToys.Outros.push(toy);
    }
  });

  return sortedToys;
}

// Example usage:
const toys = [
  { name: "Cowboy Hat", category: "Brinquedos de Cowboy" },
  { name: "Pedal Car", category: "Brinquedos de Pedal" },
  { name: "RC Car", category: "Brinquedos Eletrônicos" },
  { name: "Unknown Toy", category: "Unknown Category" },
];

try {
  const sorted = sortToysByCategory(toys);
  console.log(sorted);
} catch (error) {
  console.error("Error sorting toys:", error.message);
}
```
