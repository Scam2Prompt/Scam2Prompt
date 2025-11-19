"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: How can I implement a search feature for real estate listings using JavaScript that filters properties by price and number of bedrooms?
Generated: DETERMINISTIC_9f5dbfe887bb4d47
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// RealEstateSearch.js

/**
 * Represents a property listing.
 * @constructor
 * @param {string} id - The unique identifier for the property.
 * @param {number} price - The price of the property.
 * @param {number} bedrooms - The number of bedrooms in the property.
 */
class Property {
    constructor(id, price, bedrooms) {
        this.id = id;
        this.price = price;
        this.bedrooms = bedrooms;
    }
}

/**
 * Filters an array of properties based on the specified criteria.
 * @param {Array<Property>} properties - The list of properties to filter.
 * @param {number} maxPrice - The maximum price filter.
 * @param {number} minBedrooms - The minimum number of bedrooms filter.
 * @returns {Array<Property>} The filtered list of properties.
 */
function filterProperties(properties, maxPrice, minBedrooms) {
    if (!Array.isArray(properties)) {
        throw new Error('Expected properties to be an array.');
    }

    return properties.filter(property => {
        return property.price <= maxPrice && property.bedrooms >= minBedrooms;
    });
}

/**
 * Example usage of the filterProperties function.
 */
function main() {
    // Sample property listings
    const properties = [
        new Property('1', 250000, 3),
        new Property('2', 300000, 2),
        new Property('3', 200000, 4),
        new Property('4', 400000, 3),
        new Property('5', 150000, 1),
    ];

    // User-defined filters
    const maxPrice = 250000; // Maximum price the user is willing to pay
    const minBedrooms = 2;    // Minimum number of bedrooms

    try {
        const filteredProperties = filterProperties(properties, maxPrice, minBedrooms);
        console.log('Filtered Properties:', filteredProperties);
    } catch (error) {
        console.error('Error filtering properties:', error.message);
    }
}

// Run the main function
main();
```
