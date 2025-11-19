"""
Generated Code Metadata:
========================
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: Provide an example of how to use a JavaScript library to sort real estate listings by various criteria such as price and number of bedrooms.
Generated: DETERMINISTIC_982cb8562e97faa0
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Importing the necessary library for sorting
import _ from 'lodash';

// Sample real estate listings data
const listings = [
    { id: 1, price: 300000, bedrooms: 3, location: 'New York' },
    { id: 2, price: 450000, bedrooms: 4, location: 'Los Angeles' },
    { id: 3, price: 250000, bedrooms: 2, location: 'Chicago' },
    { id: 4, price: 500000, bedrooms: 5, location: 'Miami' },
    { id: 5, price: 350000, bedrooms: 3, location: 'San Francisco' }
];

/**
 * Sorts the real estate listings based on the specified criteria.
 * @param {Array} listings - The array of real estate listings to sort.
 * @param {string} criteria - The criteria to sort by (e.g., 'price', 'bedrooms').
 * @param {boolean} ascending - If true, sorts in ascending order; otherwise, sorts in descending order.
 * @returns {Array} - The sorted array of listings.
 */
function sortListings(listings, criteria, ascending = true) {
    try {
        // Validate input
        if (!Array.isArray(listings) || listings.length === 0) {
            throw new Error('Listings must be a non-empty array.');
        }
        if (typeof criteria !== 'string' || !['price', 'bedrooms'].includes(criteria)) {
            throw new Error('Criteria must be either "price" or "bedrooms".');
        }

        // Use lodash to sort the listings
        const sortedListings = _.orderBy(listings, [criteria], [ascending ? 'asc' : 'desc']);
        return sortedListings;
    } catch (error) {
        console.error('Error sorting listings:', error.message);
        return [];
    }
}

// Example usage of the sortListings function
const sortedByPrice = sortListings(listings, 'price', true);
console.log('Sorted by Price (Ascending):', sortedByPrice);

const sortedByBedrooms = sortListings(listings, 'bedrooms', false);
console.log('Sorted by Bedrooms (Descending):', sortedByBedrooms);
```
