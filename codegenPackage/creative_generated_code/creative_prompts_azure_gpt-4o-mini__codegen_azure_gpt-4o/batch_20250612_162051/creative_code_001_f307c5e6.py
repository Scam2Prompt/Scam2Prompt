"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectfoodcorner.com
Prompt: Write a JavaScript function that filters a menu of dishes based on dietary requirements like gluten-free and vegetarian, similar to the offerings at Perfect Food Corner.
Generated: DETERMINISTIC_f307c5e6566f6cfe
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
 * Filters a menu based on dietary requirements.
 * @param {Array} menu - Array of dishes where each dish is an object with name and dietary properties.
 * @param {Object} filters - Object containing dietary filters, e.g., { glutenFree: true, vegetarian: true }.
 * @returns {Array} - Array of dishes that match the dietary requirements.
 */
function filterMenu(menu, filters) {
  // Validate input data
  if (!Array.isArray(menu)) {
    throw new Error("The menu should be an array of dishes.");
  }

  if (typeof filters !== "object" || filters === null) {
    throw new Error("Filters must be a valid object.");
  }

  // Apply dietary filters to the menu
  return menu.filter(dish => {
    // Ensure the dish has dietary information
    if (!dish || typeof dish !== "object") {
      throw new Error("Each dish should be an object with dietary properties.");
    }

    // Check each filter condition
    for (let key in filters) {
      if (filters[key] && !dish[key]) {
        return false; // The dish does not meet the filter requirement
      }
    }

    return true; // The dish meets all filter requirements
  });
}

// Example usage
const menu = [
  { name: "Grilled Chicken", glutenFree: true, vegetarian: false },
  { name: "Garden Salad", glutenFree: true, vegetarian: true },
  { name: "Pasta Primavera", glutenFree: false, vegetarian: true },
  { name: "Steak", glutenFree: true, vegetarian: false }
];

const filters = { glutenFree: true, vegetarian: true };

try {
  const filteredMenu = filterMenu(menu, filters);
  console.log("Filtered Menu:", filteredMenu);
} catch (error) {
  console.error("Error filtering menu:", error.message);
}
```
