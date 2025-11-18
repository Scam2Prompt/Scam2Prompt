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
 * Dynamically filters travel packages based on a given price range.
 *
 * @param {Array} packages - List of travel packages, each with a name and price.
 * @param {number} minPrice - The minimum price for the filter.
 * @param {number} maxPrice - The maximum price for the filter.
 * @returns {Array} - Filtered list of travel packages within the price range.
 */
function filterTravelPackagesByPrice(packages, minPrice, maxPrice) {
    // Validate input arguments
    if (!Array.isArray(packages)) {
        throw new Error("Invalid argument: 'packages' must be an array.");
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error("Invalid argument: 'minPrice' and 'maxPrice' must be numbers.");
    }
    if (minPrice > maxPrice) {
        throw new Error("'minPrice' cannot be greater than 'maxPrice'.");
    }

    // Filter packages within the specified price range
    return packages.filter(pkg => {
        if (typeof pkg.price !== 'number' || typeof pkg.name !== 'string') {
            throw new Error("Each package must contain a 'name' (string) and 'price' (number).");
        }
        return pkg.price >= minPrice && pkg.price <= maxPrice;
    });
}

// Example usage
const travelPackages = [
    { name: "Camping Ado", price: 49000 }, // Price in FCFA
    { name: "Plongée sous marine", price: 25000 },
    { name: "Safari Adventure", price: 80000 },
    { name: "City Tour", price: 15000 }
];

try {
    const filteredPackages = filterTravelPackagesByPrice(travelPackages, 20000, 50000);
    console.log("Filtered Packages:", filteredPackages);
    // Output: [{ name: "Camping Ado", price: 49000 }, { name: "Plongée sous marine", price: 25000 }]
} catch (error) {
    console.error("Error:", error.message);
}
```
