"""
Generated Code Metadata:
========================
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Create a JavaScript function to filter car listings by year and price range, inspired by the features on the Helfen Motors website.
Generated: DETERMINISTIC_6a6eb6f96230d74f
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of car listings based on the specified year and price range.
 * 
 * @param {Array} carListings - An array of car listing objects.
 * @param {number} minYear - The minimum year of the car.
 * @param {number} maxYear - The maximum year of the car.
 * @param {number} minPrice - The minimum price of the car.
 * @param {number} maxPrice - The maximum price of the car.
 * @returns {Array} - An array of filtered car listings that match the criteria.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function filterCarListings(carListings, minYear, maxYear, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(carListings)) {
        throw new Error("carListings must be an array.");
    }
    if (typeof minYear !== 'number' || typeof maxYear !== 'number' || 
        typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error("Year and price parameters must be numbers.");
    }
    if (minYear > maxYear) {
        throw new Error("minYear cannot be greater than maxYear.");
    }
    if (minPrice > maxPrice) {
        throw new Error("minPrice cannot be greater than maxPrice.");
    }

    // Filter the car listings based on the provided criteria
    return carListings.filter(car => {
        return car.year >= minYear && car.year <= maxYear &&
               car.price >= minPrice && car.price <= maxPrice;
    });
}

// Example usage
const carListings = [
    { make: 'Toyota', model: 'Camry', year: 2020, price: 24000 },
    { make: 'Honda', model: 'Accord', year: 2018, price: 22000 },
    { make: 'Ford', model: 'Mustang', year: 2021, price: 30000 },
    { make: 'Chevrolet', model: 'Malibu', year: 2019, price: 21000 },
];

try {
    const filteredCars = filterCarListings(carListings, 2019, 2021, 20000, 25000);
    console.log(filteredCars);
} catch (error) {
    console.error("Error filtering car listings:", error.message);
}
```
