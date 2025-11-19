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
 * Filters travel packages by price range.
 * @param {Array} packages - Array of travel package objects.
 * @param {number} minPrice - Minimum price in FCFA.
 * @param {number} maxPrice - Maximum price in FCFA.
 * @returns {Array} Filtered array of packages within the price range.
 * @throws {Error} If packages is not an array or min/max prices are invalid.
 */
function filterPackagesByPrice(packages, minPrice, maxPrice) {
    // Validate inputs
    if (!Array.isArray(packages)) {
        throw new Error('Packages must be an array');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number' || minPrice < 0 || maxPrice < 0) {
        throw new Error('Price values must be positive numbers');
    }
    if (minPrice > maxPrice) {
        throw new Error('Minimum price cannot be greater than maximum price');
    }

    // Filter packages within the price range
    return packages.filter(pkg => {
        if (typeof pkg.price !== 'number' || pkg.price < 0) {
            console.warn(`Invalid price found for package: ${pkg.name || 'Unknown'}`);
            return false;
        }
        return pkg.price >= minPrice && pkg.price <= maxPrice;
    });
}

// Example usage:
/*
const travelPackages = [
    { name: "Camping Ado", price: 49000 },
    { name: "Plongée sous marine", price: 25000 },
    { name: "Safari", price: 75000 }
];

const filteredPackages = filterPackagesByPrice(travelPackages, 20000, 50000);
console.log(filteredPackages);
*/
```
