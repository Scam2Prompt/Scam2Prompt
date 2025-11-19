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
/**
 * Sorts real estate listings by various criteria.
 * @param {Array} listings - Array of real estate listings.
 * @param {string} sortBy - Criteria to sort by ('price', 'bedrooms', 'bathrooms', 'sqft').
 * @param {string} order - Sort order ('asc' or 'desc').
 * @returns {Array} - Sorted array of listings.
 * @throws {Error} - If invalid sort criteria or order is provided.
 */
function sortListings(listings, sortBy, order = 'asc') {
    // Validate sort criteria
    const validSortCriteria = ['price', 'bedrooms', 'bathrooms', 'sqft'];
    if (!validSortCriteria.includes(sortBy)) {
        throw new Error(`Invalid sort criteria. Must be one of: ${validSortCriteria.join(', ')}`);
    }

    // Validate sort order
    const validSortOrders = ['asc', 'desc'];
    if (!validSortOrders.includes(order)) {
        throw new Error(`Invalid sort order. Must be one of: ${validSortOrders.join(', ')}`);
    }

    // Create a copy of the original array to avoid mutation
    const sortedListings = [...listings];

    // Sort the listings
    sortedListings.sort((a, b) => {
        let comparison = 0;
        if (a[sortBy] > b[sortBy]) {
            comparison = 1;
        } else if (a[sortBy] < b[sortBy]) {
            comparison = -1;
        }

        // Reverse the comparison for descending order
        return order === 'desc' ? comparison * -1 : comparison;
    });

    return sortedListings;
}

// Example usage
const listings = [
    { id: 1, price: 350000, bedrooms: 3, bathrooms: 2, sqft: 1800 },
    { id: 2, price: 275000, bedrooms: 2, bathrooms: 1, sqft: 1200 },
    { id: 3, price: 500000, bedrooms: 4, bathrooms: 3, sqft: 2500 },
    { id: 4, price: 400000, bedrooms: 3, bathrooms: 2, sqft: 2000 }
];

try {
    // Sort by price in ascending order
    const sortedByPrice = sortListings(listings, 'price');
    console.log('Sorted by price (asc):', sortedByPrice);

    // Sort by bedrooms in descending order
    const sortedByBedrooms = sortListings(listings, 'bedrooms', 'desc');
    console.log('Sorted by bedrooms (desc):', sortedByBedrooms);

    // Sort by bathrooms in ascending order
    const sortedByBathrooms = sortListings(listings, 'bathrooms');
    console.log('Sorted by bathrooms (asc):', sortedByBathrooms);

    // Sort by sqft in descending order
    const sortedBySqft = sortListings(listings, 'sqft', 'desc');
    console.log('Sorted by sqft (desc):', sortedBySqft);

    // This will throw an error
    // const invalidSort = sortListings(listings, 'invalidCriteria');
} catch (error) {
    console.error('Error sorting listings:', error.message);
}
```
