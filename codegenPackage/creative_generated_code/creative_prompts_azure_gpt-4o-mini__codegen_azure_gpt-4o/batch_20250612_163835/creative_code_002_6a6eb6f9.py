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
 * Filters car listings by year and price range.
 * 
 * @param {Array<Object>} carListings - Array of car objects. Each object should have the structure:
 *                                       { id: number, make: string, model: string, year: number, price: number }
 * @param {Object} filterCriteria - An object specifying the filter criteria:
 *                                   { minYear: number, maxYear: number, minPrice: number, maxPrice: number }
 * @returns {Array<Object>} - Array of car objects that match the filter criteria.
 * 
 * Usage:
 * const cars = [
 *   { id: 1, make: 'Toyota', model: 'Camry', year: 2020, price: 20000 },
 *   { id: 2, make: 'Honda', model: 'Accord', year: 2019, price: 18000 },
 *   { id: 3, make: 'Ford', model: 'Focus', year: 2021, price: 22000 },
 * ];
 * const criteria = { minYear: 2019, maxYear: 2021, minPrice: 18000, maxPrice: 21000 };
 * const filteredCars = filterCarListings(cars, criteria);
 * console.log(filteredCars);
 */
function filterCarListings(carListings, filterCriteria) {
    // Validate input: Ensure carListings is an array and filterCriteria is an object
    if (!Array.isArray(carListings)) {
        throw new Error('carListings must be an array of car objects.');
    }
    if (typeof filterCriteria !== 'object' || filterCriteria === null) {
        throw new Error('filterCriteria must be a valid object.');
    }

    const { minYear, maxYear, minPrice, maxPrice } = filterCriteria;

    // Validate filter criteria: Ensure year and price range are numeric
    if (typeof minYear !== 'number' || typeof maxYear !== 'number' || typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Filter criteria values must be numbers.');
    }

    // Filter car listings based on criteria
    return carListings.filter(car => {
        // Validate car object structure
        if (typeof car.year !== 'number' || typeof car.price !== 'number') {
            console.warn(`Invalid car object detected: ${JSON.stringify(car)}. Skipping.`);
            return false;
        }

        // Check if the car matches the year and price range criteria
        return car.year >= minYear &&
               car.year <= maxYear &&
               car.price >= minPrice &&
               car.price <= maxPrice;
    });
}

// Example usage:
const cars = [
    { id: 1, make: 'Toyota', model: 'Camry', year: 2020, price: 20000 },
    { id: 2, make: 'Honda', model: 'Accord', year: 2019, price: 18000 },
    { id: 3, make: 'Ford', model: 'Focus', year: 2021, price: 22000 },
];
const criteria = { minYear: 2019, maxYear: 2021, minPrice: 18000, maxPrice: 21000 };
const filteredCars = filterCarListings(cars, criteria);
console.log(filteredCars);
```
