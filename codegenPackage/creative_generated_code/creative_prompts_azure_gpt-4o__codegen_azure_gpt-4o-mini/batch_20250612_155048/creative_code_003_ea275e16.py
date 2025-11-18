"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Write a function in JavaScript to filter CM-Canada's plumbing fixtures catalog (Liv fixtures™) by price range and certification standards.
Generated: DETERMINISTIC_ea275e168ef1d701
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters the plumbing fixtures from CM-Canada's Liv fixtures™ catalog
 * based on a specified price range and certification standards.
 *
 * @param {Array} fixtures - Array of fixture objects to filter.
 * @param {number} minPrice - Minimum price for the filter.
 * @param {number} maxPrice - Maximum price for the filter.
 * @param {Array} certifications - Array of certification standards to filter by.
 * @returns {Array} - Filtered array of fixture objects matching the criteria.
 *
 * @throws {Error} - Throws an error if the inputs are invalid.
 */
function filterFixtures(fixtures, minPrice, maxPrice, certifications) {
    // Validate inputs
    if (!Array.isArray(fixtures)) {
        throw new Error('Invalid input: fixtures should be an array.');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Invalid input: minPrice and maxPrice should be numbers.');
    }
    if (!Array.isArray(certifications)) {
        throw new Error('Invalid input: certifications should be an array.');
    }

    // Filter fixtures based on price range and certifications
    return fixtures.filter(fixture => {
        const isPriceInRange = fixture.price >= minPrice && fixture.price <= maxPrice;
        const hasValidCertification = certifications.length === 0 || certifications.includes(fixture.certification);
        
        return isPriceInRange && hasValidCertification;
    });
}

// Example usage:
const fixturesCatalog = [
    { id: 1, name: 'Fixture A', price: 150, certification: 'WaterSense' },
    { id: 2, name: 'Fixture B', price: 200, certification: 'CSA' },
    { id: 3, name: 'Fixture C', price: 300, certification: 'WaterSense' },
    { id: 4, name: 'Fixture D', price: 50, certification: 'None' },
];

try {
    const filteredFixtures = filterFixtures(fixturesCatalog, 100, 250, ['WaterSense', 'CSA']);
    console.log('Filtered Fixtures:', filteredFixtures);
} catch (error) {
    console.error('Error filtering fixtures:', error.message);
}
```
