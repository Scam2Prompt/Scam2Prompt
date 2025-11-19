"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Create a function in JavaScript to dynamically filter travel packages by price range, such as "Camping Ado" at 49,000 FCFA and "Plongée sous marine" at 25,000 FCFA.
Generated: DETERMINISTIC_b32337ec7eb5556e
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters travel packages based on a specified price range.
 * 
 * @param {Array} packages - An array of travel package objects, each containing a name and price.
 * @param {number} minPrice - The minimum price for the filter.
 * @param {number} maxPrice - The maximum price for the filter.
 * @returns {Array} - An array of travel packages that fall within the specified price range.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function filterTravelPackagesByPrice(packages, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(packages)) {
        throw new Error("The 'packages' parameter must be an array.");
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error("Both 'minPrice' and 'maxPrice' must be numbers.");
    }
    if (minPrice < 0 || maxPrice < 0) {
        throw new Error("Price values must be non-negative.");
    }
    if (minPrice > maxPrice) {
        throw new Error("Minimum price cannot be greater than maximum price.");
    }

    // Filter packages based on the price range
    return packages.filter(package => {
        return package.price >= minPrice && package.price <= maxPrice;
    });
}

// Example usage
const travelPackages = [
    { name: "Camping Ado", price: 49000 },
    { name: "Plongée sous marine", price: 25000 },
    { name: "Safari Adventure", price: 75000 },
    { name: "Beach Getaway", price: 30000 }
];

try {
    const filteredPackages = filterTravelPackagesByPrice(travelPackages, 20000, 50000);
    console.log("Filtered Travel Packages:", filteredPackages);
} catch (error) {
    console.error("Error filtering travel packages:", error.message);
}
```
