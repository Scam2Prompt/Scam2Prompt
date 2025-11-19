"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.ilmaweb.com
Prompt: Create a JavaScript function to calculate the cost of a pre-wedding service package offered by Budi Bromo Tour.
Generated: DETERMINISTIC_5fd5c08a4924ff30
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of a pre-wedding service package offered by Budi Bromo Tour.
 * 
 * @param {string} packageName - The name of the package (e.g., "Sunrise", "Sunset", "Photography")
 * @param {number} numberOfGuests - The number of guests
 * @param {boolean} includeDroneCoverage - Whether to include drone coverage
 * @param {boolean} includeUnderwaterPhotos - Whether to include underwater photos
 * @returns {number} The total cost of the package
 */
function calculatePreWeddingPackageCost(packageName, numberOfGuests, includeDroneCoverage, includeUnderwaterPhotos) {
    // Define package prices
    const packagePrices = {
        "Sunrise": 5000000,
        "Sunset": 6000000,
        "Photography": 8000000
    };

    // Check if package exists
    if (!(packageName in packagePrices)) {
        throw new Error(`Invalid package name: ${packageName}`);
    }

    // Calculate base cost
    let baseCost = packagePrices[packageName];

    // Calculate guest cost
    const guestCost = 200000 * numberOfGuests;
    baseCost += guestCost;

    // Add drone coverage cost if included
    if (includeDroneCoverage) {
        baseCost += 1000000;
    }

    // Add underwater photos cost if included
    if (includeUnderwaterPhotos) {
        baseCost += 2000000;
    }

    return baseCost;
}

// Example usage:
try {
    const packageName = "Sunrise";
    const numberOfGuests = 50;
    const includeDroneCoverage = true;
    const includeUnderwaterPhotos = false;

    const totalCost = calculatePreWeddingPackageCost(packageName, numberOfGuests, includeDroneCoverage, includeUnderwaterPhotos);
    console.log(`The total cost of the ${packageName} package for ${numberOfGuests} guests with drone coverage is: Rp ${totalCost.toLocaleString()}`);
} catch (error) {
    console.error(error.message);
}
```
