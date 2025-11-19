"""
Generated Code Metadata:
========================
Original URL: https://ittastours.com
Prompt: "Write a JavaScript function to filter and display tour packages based on user preferences for destination, duration, and price range."
Generated: DETERMINISTIC_317d539fe937ae08
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters tour packages based on user preferences.
 * 
 * @param {Array} packages - An array of tour package objects.
 * @param {Object} preferences - User preferences for filtering.
 * @param {string} preferences.destination - Desired destination.
 * @param {number} preferences.minDuration - Minimum duration in days.
 * @param {number} preferences.maxDuration - Maximum duration in days.
 * @param {number} preferences.minPrice - Minimum price.
 * @param {number} preferences.maxPrice - Maximum price.
 * @returns {Array} - An array of filtered tour packages.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterTourPackages(packages, preferences) {
    // Validate input types
    if (!Array.isArray(packages)) {
        throw new Error('Invalid input: packages should be an array.');
    }
    if (typeof preferences !== 'object' || preferences === null) {
        throw new Error('Invalid input: preferences should be an object.');
    }

    // Destructure preferences for easier access
    const {
        destination = '',
        minDuration = 0,
        maxDuration = Infinity,
        minPrice = 0,
        maxPrice = Infinity
    } = preferences;

    // Filter packages based on user preferences
    return packages.filter(pkg => {
        const isDestinationMatch = pkg.destination.toLowerCase().includes(destination.toLowerCase());
        const isDurationMatch = pkg.duration >= minDuration && pkg.duration <= maxDuration;
        const isPriceMatch = pkg.price >= minPrice && pkg.price <= maxPrice;

        return isDestinationMatch && isDurationMatch && isPriceMatch;
    });
}

// Example usage
const tourPackages = [
    { destination: 'Paris', duration: 5, price: 1200 },
    { destination: 'London', duration: 3, price: 800 },
    { destination: 'New York', duration: 7, price: 1500 },
    { destination: 'Tokyo', duration: 10, price: 2000 },
];

const userPreferences = {
    destination: 'paris',
    minDuration: 3,
    maxDuration: 7,
    minPrice: 1000,
    maxPrice: 1300
};

try {
    const filteredPackages = filterTourPackages(tourPackages, userPreferences);
    console.log('Filtered Tour Packages:', filteredPackages);
} catch (error) {
    console.error('Error filtering tour packages:', error.message);
}
```
