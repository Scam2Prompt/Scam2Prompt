"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Generate a JavaScript function to dynamically filter Travis Scott merchandise by category (e.g., hoodies, t-shirts, sweatshirts) on an e-commerce website.
Generated: DETERMINISTIC_576885539123d2fa
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters merchandise by category dynamically.
 * @param {Array<Object>} merchandise - Array of merchandise objects.
 * @param {string} category - The category to filter by (e.g., 'hoodies', 't-shirts', 'sweatshirts').
 * @returns {Array<Object>} - Array of merchandise objects that match the given category.
 */
function filterMerchandiseByCategory(merchandise, category) {
  try {
    // Validate input: merchandise should be an array, and category should be a string.
    if (!Array.isArray(merchandise)) {
      throw new TypeError('Merchandise should be an array of objects.');
    }
    if (typeof category !== 'string') {
      throw new TypeError('Category should be a string.');
    }

    // Filter merchandise by the provided category.
    const filtered = merchandise.filter((item) => {
      // Ensure each item has a 'category' field and matches the given category.
      return item.category && item.category.toLowerCase() === category.toLowerCase();
    });

    return filtered;
  } catch (error) {
    // Log errors to the console for debugging purposes.
    console.error('Error filtering merchandise:', error.message);
    return [];
  }
}

// Example usage:
// Merchandise array example.
const merchandise = [
  { id: 1, name: 'Astroworld Hoodie', category: 'hoodies' },
  { id: 2, name: 'Astroworld T-shirt', category: 't-shirts' },
  { id: 3, name: 'Cactus Jack Sweatshirt', category: 'sweatshirts' },
  { id: 4, name: 'Sicko Mode Hoodie', category: 'hoodies' },
];

// Filtering hoodies.
const hoodies = filterMerchandiseByCategory(merchandise, 'hoodies');
console.log('Filtered Hoodies:', hoodies);

// Filtering t-shirts.
const tShirts = filterMerchandiseByCategory(merchandise, 't-shirts');
console.log('Filtered T-Shirts:', tShirts);
```
