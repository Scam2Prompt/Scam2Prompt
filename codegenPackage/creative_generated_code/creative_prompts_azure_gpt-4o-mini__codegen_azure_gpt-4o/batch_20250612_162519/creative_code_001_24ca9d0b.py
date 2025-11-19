"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinconectswap.blogspot.com
Prompt: Write a function in JavaScript that filters a list of shoes to display only 'tenis de corrida' and 'chuteira infantil' as described on the Lara Sapatos em Geral page.
Generated: DETERMINISTIC_24ca9d0b920f9776
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of shoes to display only specific types.
 * 
 * @param {Array} shoes - Array of shoe objects where each object contains a `type` property.
 * @returns {Array} - Array of shoe objects that match the specified types.
 */
function filterShoes(shoes) {
  // Validate the input
  if (!Array.isArray(shoes)) {
    throw new Error("Invalid input: Expected an array of shoes.");
  }

  // Define the shoe types to filter
  const allowedTypes = ['tenis de corrida', 'chuteira infantil'];

  // Filter the shoes array based on the allowed types
  return shoes.filter(shoe => {
    if (typeof shoe !== 'object' || !shoe.type) {
      console.warn("Invalid shoe object encountered:", shoe);
      return false; // Skip invalid shoe objects
    }
    return allowedTypes.includes(shoe.type.toLowerCase());
  });
}

// Example usage:
const shoesList = [
  { id: 1, type: 'tenis de corrida', brand: 'Nike' },
  { id: 2, type: 'chuteira infantil', brand: 'Adidas' },
  { id: 3, type: 'sapato social', brand: 'Gucci' },
  { id: 4, type: 'tenis casual', brand: 'Puma' }
];

try {
  const filteredShoes = filterShoes(shoesList);
  console.log("Filtered Shoes:", filteredShoes);
} catch (error) {
  console.error("An error occurred:", error.message);
}
```
