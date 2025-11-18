"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Create a function in JavaScript that categorizes food grains like "Yellow Maize," "Rice," and "Millet Seeds" based on their descriptions provided by Jai Gurudev Industries.
Generated: DETERMINISTIC_d39c079e0f7ae28a
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to categorize food grains based on their descriptions.
 * @param {string} description - The description of the food grain.
 * @returns {string} - The category of the food grain.
 * @throws {Error} - Throws an error for invalid or unsupported descriptions.
 */
function categorizeFoodGrain(description) {
  // Validate input
  if (typeof description !== 'string' || description.trim() === '') {
    throw new Error('Invalid description: Description must be a non-empty string.');
  }

  // Normalize input to ensure case-insensitivity and whitespace tolerance
  const normalizedDescription = description.trim().toLowerCase();

  // Categorization logic
  switch (normalizedDescription) {
    case 'yellow maize':
      return 'Grain - Maize';
    case 'rice':
      return 'Grain - Rice';
    case 'millet seeds':
      return 'Grain - Millet';
    default:
      throw new Error(`Unsupported description: "${description}" does not match any known category.`);
  }
}

// Example usage:
// Note: Remove the example usage when integrating this code into production.
try {
  console.log(categorizeFoodGrain('Yellow Maize')); // Output: Grain - Maize
  console.log(categorizeFoodGrain('Rice'));         // Output: Grain - Rice
  console.log(categorizeFoodGrain('Millet Seeds')); // Output: Grain - Millet
} catch (error) {
  console.error(error.message);
}
```
