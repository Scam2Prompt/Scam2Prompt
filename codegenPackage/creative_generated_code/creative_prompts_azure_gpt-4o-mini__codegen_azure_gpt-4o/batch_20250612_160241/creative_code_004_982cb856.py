"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: Provide an example of how to use a JavaScript library to sort real estate listings by various criteria such as price and number of bedrooms.
Generated: DETERMINISTIC_982cb8562e97faa0
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing Lodash library for sorting functionality
// Ensure Lodash is installed using npm: `npm install lodash`
const _ = require('lodash');

// Sample real estate listings data
const realEstateListings = [
  { id: 1, price: 300000, bedrooms: 3, location: 'New York' },
  { id: 2, price: 200000, bedrooms: 2, location: 'Los Angeles' },
  { id: 3, price: 400000, bedrooms: 4, location: 'Chicago' },
  { id: 4, price: 250000, bedrooms: 2, location: 'Houston' },
];

// Function to sort listings based on a given criterion
/**
 * Sorts real estate listings by specified criteria.
 * @param {Array} listings - Array of real estate objects.
 * @param {String} criterion - Sorting criterion ('price' or 'bedrooms').
 * @param {Boolean} ascending - If true, sort in ascending order; otherwise, sort in descending order.
 * @returns {Array} - Sorted array of listings.
 */
function sortListings(listings, criterion, ascending = true) {
  try {
    // Validate input
    if (!Array.isArray(listings)) {
      throw new Error('Listings must be an array.');
    }
    if (!['price', 'bedrooms'].includes(criterion)) {
      throw new Error('Invalid sorting criterion. Use "price" or "bedrooms".');
    }

    // Sort using Lodash's `orderBy` method
    const sortedListings = _.orderBy(
      listings,
      [criterion],
      [ascending ? 'asc' : 'desc']
    );

    return sortedListings;
  } catch (error) {
    console.error('Error while sorting listings:', error.message);
    return [];
  }
}

// Example usage
console.log('Sort by price (ascending):');
console.log(sortListings(realEstateListings, 'price', true));

console.log('Sort by bedrooms (descending):');
console.log(sortListings(realEstateListings, 'bedrooms', false));
```

This code snippet uses the Lodash library to sort real estate listings by various criteria such as price and number of bedrooms. Ensure Lodash is installed in your project before running the code.
