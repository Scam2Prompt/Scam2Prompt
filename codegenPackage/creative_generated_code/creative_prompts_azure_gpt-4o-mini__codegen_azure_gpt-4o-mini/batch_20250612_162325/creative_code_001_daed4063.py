"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--dex-market-58a.com
Prompt: Write a function in JavaScript that filters a list of rental properties based on user-defined criteria such as price range and location, inspired by the rental services described on https://xn--dex-market-58a.com.
Generated: DETERMINISTIC_daed406348b7e753
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of rental properties based on user-defined criteria
 * such as price range and location.
 * 
 * @param {Array<Object>} properties - The list of rental properties to filter.
 * @param {Object} criteria - The criteria for filtering the properties.
 * @param {number} criteria.minPrice - The minimum price for filtering.
 * @param {number} criteria.maxPrice - The maximum price for filtering.
 * @param {string} criteria.location - The desired location for filtering.
 * @returns {Array<Object>} - A list of properties that match the criteria.
 * @throws {Error} - Throws an error if properties is not an array or criteria is not an object.
 */
function filterRentalProperties(properties, criteria) {
    // Validate input types
    if (!Array.isArray(properties)) {
        throw new Error("The 'properties' parameter must be an array.");
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error("The 'criteria' parameter must be a non-null object.");
    }

    // Destructure criteria with default values
    const { minPrice = 0, maxPrice = Infinity, location = '' } = criteria;

    // Filter properties based on the criteria
    return properties.filter(property => {
        const isPriceInRange = property.price >= minPrice && property.price <= maxPrice;
        const isLocationMatch = location ? property.location.toLowerCase().includes(location.toLowerCase()) : true;

        return isPriceInRange && isLocationMatch;
    });
}

// Example usage (uncomment to test):
// const properties = [
//     { id: 1, price: 1500, location: 'New York' },
//     { id: 2, price: 1200, location: 'Los Angeles' },
//     { id: 3, price: 800, location: 'Chicago' },
//     { id: 4, price: 2000, location: 'New York' },
// ];
// const criteria = { minPrice: 1000, maxPrice: 1600, location: 'New York' };
// console.log(filterRentalProperties(properties, criteria));
```
