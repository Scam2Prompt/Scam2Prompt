"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wizfairllc.com
Prompt: Write a JavaScript function to filter travel packages by destination and discount percentage, using Wizfair LLC's package details.
Generated: DETERMINISTIC_f9258025017eb3c5
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters travel packages based on destination and discount percentage.
 * 
 * @param {Array} packages - Array of travel package objects. Each object should have `destination`, `price`, and `discountPercentage` properties.
 * @param {string} destination - Destination to filter by.
 * @param {number} minDiscount - Minimum discount percentage to filter by.
 * @returns {Array} - Filtered array of travel packages matching the criteria.
 */
function filterTravelPackages(packages, destination, minDiscount) {
    // Input validation
    if (!Array.isArray(packages)) {
        throw new Error("Invalid input: packages must be an array.");
    }
    if (typeof destination !== "string") {
        throw new Error("Invalid input: destination must be a string.");
    }
    if (typeof minDiscount !== "number" || minDiscount < 0 || minDiscount > 100) {
        throw new Error("Invalid input: minDiscount must be a number between 0 and 100.");
    }

    // Filter packages based on destination and minimum discount percentage
    return packages.filter((pkg) => {
        // Check destination match and discount percentage criteria
        return pkg.destination.toLowerCase() === destination.toLowerCase() &&
               pkg.discountPercentage >= minDiscount;
    });
}

// Example usage:
// Sample travel packages data
const travelPackages = [
    { destination: "Paris", price: 1200, discountPercentage: 20 },
    { destination: "New York", price: 800, discountPercentage: 15 },
    { destination: "Tokyo", price: 1500, discountPercentage: 10 },
    { destination: "Paris", price: 1000, discountPercentage: 25 }
];

// Filter packages for Paris with at least a 20% discount
const filteredPackages = filterTravelPackages(travelPackages, "Paris", 20);

console.log(filteredPackages);
// Output: [{ destination: 'Paris', price: 1200, discountPercentage: 20 }, { destination: 'Paris', price: 1000, discountPercentage: 25 }]
```
