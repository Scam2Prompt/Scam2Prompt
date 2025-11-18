"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Create a function in JavaScript to dynamically filter travel packages by price range, such as "Camping Ado" at 49,000 FCFA and "Plongée sous marine" at 25,000 FCFA.
Generated: DETERMINISTIC_b32337ec7eb5556e
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters travel packages by price range.
 * 
 * @param {Array} packages - An array of travel package objects to filter.
 * @param {number} minPrice - The minimum price of the travel package.
 * @param {number} maxPrice - The maximum price of the travel package.
 * @returns {Array} - An array of travel packages that fall within the specified price range.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterTravelPackagesByPrice(packages, minPrice, maxPrice) {
    // Validate input types
    if (!Array.isArray(packages)) {
        throw new Error('Invalid input: packages should be an array.');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Invalid input: minPrice and maxPrice should be numbers.');
    }
    if (minPrice < 0 || maxPrice < 0) {
        throw new Error('Invalid input: Prices should be non-negative.');
    }
    if (minPrice > maxPrice) {
        throw new Error('Invalid input: minPrice should not be greater than maxPrice.');
    }

    // Filter packages by price range
    return packages.filter(package => {
        return package.price >= minPrice && package.price <= maxPrice;
    });
}

// Example usage
const travelPackages = [
    { name: "Camping Ado", price: 49000 },
    { name: "Plongée sous marine", price: 25000 },
    { name: "Safari Adventure", price: 70000 },
    { name: "City Tour", price: 15000 },
];

try {
    const filteredPackages = filterTravelPackagesByPrice(travelPackages, 20000, 50000);
    console.log('Filtered Travel Packages:', filteredPackages);
} catch (error) {
    console.error('Error filtering travel packages:', error.message);
}
```
