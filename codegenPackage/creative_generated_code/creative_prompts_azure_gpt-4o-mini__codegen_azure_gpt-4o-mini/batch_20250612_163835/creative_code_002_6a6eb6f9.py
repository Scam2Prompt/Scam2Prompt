"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Create a JavaScript function to filter car listings by year and price range, inspired by the features on the Helfen Motors website.
Generated: DETERMINISTIC_6a6eb6f96230d74f
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of car listings based on the specified year and price range.
 * 
 * @param {Array} carListings - An array of car objects to be filtered.
 * @param {number} minYear - The minimum year of the car.
 * @param {number} maxYear - The maximum year of the car.
 * @param {number} minPrice - The minimum price of the car.
 * @param {number} maxPrice - The maximum price of the car.
 * @returns {Array} - An array of car listings that match the specified criteria.
 * 
 * @throws {TypeError} - Throws an error if carListings is not an array or if any parameters are not numbers.
 */
function filterCarListings(carListings, minYear, maxYear, minPrice, maxPrice) {
    // Validate input types
    if (!Array.isArray(carListings)) {
        throw new TypeError('carListings must be an array');
    }
    if (typeof minYear !== 'number' || typeof maxYear !== 'number' ||
        typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new TypeError('All parameters must be numbers');
    }

    // Filter the car listings based on year and price range
    return carListings.filter(car => {
        return car.year >= minYear && car.year <= maxYear &&
               car.price >= minPrice && car.price <= maxPrice;
    });
}

// Example usage:
try {
    const cars = [
        { make: 'Toyota', model: 'Camry', year: 2020, price: 24000 },
        { make: 'Honda', model: 'Accord', year: 2018, price: 23000 },
        { make: 'Ford', model: 'Mustang', year: 2021, price: 30000 },
        { make: 'Chevrolet', model: 'Malibu', year: 2017, price: 22000 }
    ];

    const filteredCars = filterCarListings(cars, 2018, 2021, 22000, 30000);
    console.log(filteredCars);
} catch (error) {
    console.error('Error filtering car listings:', error.message);
}
```
