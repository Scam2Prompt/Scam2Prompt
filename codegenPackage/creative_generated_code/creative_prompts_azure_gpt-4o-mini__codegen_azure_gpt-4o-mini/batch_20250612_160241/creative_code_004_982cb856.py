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
// Import the necessary library for sorting
import _ from 'lodash'; // Assuming lodash is used for ease of sorting

// Sample real estate listings data
const listings = [
    { id: 1, price: 300000, bedrooms: 3, location: 'New York' },
    { id: 2, price: 150000, bedrooms: 2, location: 'Los Angeles' },
    { id: 3, price: 500000, bedrooms: 4, location: 'Miami' },
    { id: 4, price: 200000, bedrooms: 3, location: 'Chicago' },
    { id: 5, price: 400000, bedrooms: 2, location: 'San Francisco' },
];

// Function to sort listings by specified criteria
/**
 * Sorts real estate listings based on the provided field.
 * 
 * @param {Array} data - The listings data to be sorted.
 * @param {String} criteria - The criteria to sort by (e.g., 'price', 'bedrooms').
 * @param {Boolean} ascending - Defines the sort order; true for ascending, false for descending.
 * @returns {Array} - The sorted listings.
 */
function sortListings(data, criteria, ascending = true) {
    if (!Array.isArray(data)) {
        throw new Error('Invalid data: Expected an array of listings.');
    }

    // Check if the criteria is valid
    const validCriteria = ['price', 'bedrooms'];
    if (!validCriteria.includes(criteria)) {
        throw new Error(`Invalid criteria: Expected one of ${validCriteria.join(', ')}`);
    }

    const sortedData = _.orderBy(data, [criteria], [ascending ? 'asc' : 'desc']);
    return sortedData;
}

// Example usage of the sortListings function
try {
    const sortedByPriceAsc = sortListings(listings, 'price', true);
    console.log('Listings sorted by price (ascending):', sortedByPriceAsc);

    const sortedByBedroomsDesc = sortListings(listings, 'bedrooms', false);
    console.log('Listings sorted by bedrooms (descending):', sortedByBedroomsDesc);
} catch (error) {
    console.error('Error sorting listings:', error.message);
}
```
