"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskloug-us4.godaddysites.com
Prompt: Write a JavaScript function that filters real estate listings based on price range and location, inspired by the services offered on metamaskloug-us4.
Generated: DETERMINISTIC_bafef434ea76ba8a
Batch ID: 20250612_155721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters real estate listings based on a specified price range and location.
 * 
 * @param {Array} listings - The array of real estate listings to be filtered.
 * @param {Object} criteria - The criteria for filtering.
 * @param {number} criteria.minPrice - The minimum price for the listings.
 * @param {number} criteria.maxPrice - The maximum price for the listings.
 * @param {string} criteria.location - The location to filter listings by.
 * @returns {Array} - An array of listings that match the specified criteria.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterRealEstateListings(listings, criteria) {
    // Validate input parameters
    if (!Array.isArray(listings)) {
        throw new Error('Listings must be an array.');
    }
    
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error('Criteria must be a non-null object.');
    }
    
    const { minPrice, maxPrice, location } = criteria;

    // Validate criteria properties
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Min and max price must be numbers.');
    }

    if (typeof location !== 'string') {
        throw new Error('Location must be a string.');
    }

    // Filter listings based on price range and location
    return listings.filter(listing => {
        const price = listing.price;
        const matchesPrice = price >= minPrice && price <= maxPrice;
        const matchesLocation = listing.location.toLowerCase() === location.toLowerCase();

        return matchesPrice && matchesLocation;
    });
}

// Example usage
const realEstateListings = [
    { id: 1, price: 250000, location: 'New York' },
    { id: 2, price: 300000, location: 'Los Angeles' },
    { id: 3, price: 150000, location: 'New York' },
    { id: 4, price: 350000, location: 'Chicago' }
];

const criteria = {
    minPrice: 200000,
    maxPrice: 300000,
    location: 'New York'
};

try {
    const filteredListings = filterRealEstateListings(realEstateListings, criteria);
    console.log(filteredListings);
} catch (error) {
    console.error('Error filtering listings:', error.message);
}
```
