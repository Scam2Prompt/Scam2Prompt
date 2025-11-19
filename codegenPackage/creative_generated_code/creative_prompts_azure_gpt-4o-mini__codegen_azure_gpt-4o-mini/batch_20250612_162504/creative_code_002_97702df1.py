"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.homes
Prompt: Create a JavaScript function that filters a list of apartments for sale based on criteria such as price, number of bedrooms, and amenities like a wellness gym and spa.
Generated: DETERMINISTIC_97702df1b8d801fb
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of apartments based on specified criteria.
 * 
 * @param {Array} apartments - An array of apartment objects to filter.
 * @param {Object} filterCriteria - An object containing the filtering criteria.
 * @param {number} filterCriteria.maxPrice - The maximum price of the apartment.
 * @param {number} filterCriteria.minBedrooms - The minimum number of bedrooms required.
 * @param {boolean} filterCriteria.wellnessGym - Whether a wellness gym is required.
 * @param {boolean} filterCriteria.spa - Whether a spa is required.
 * @returns {Array} An array of apartments that match the filter criteria.
 */
function filterApartments(apartments, filterCriteria) {
    // Validate input parameters
    if (!Array.isArray(apartments)) {
        throw new Error("The first argument must be an array of apartments.");
    }
    if (typeof filterCriteria !== "object" || filterCriteria === null) {
        throw new Error("The second argument must be an object with filtering criteria.");
    }

    // Destructure filter criteria with default values
    const {
        maxPrice = Infinity,
        minBedrooms = 0,
        wellnessGym = false,
        spa = false
    } = filterCriteria;

    // Filter apartments based on criteria
    return apartments.filter(apartment => {
        // Check if apartment meets all criteria
        const meetsPriceCriteria = apartment.price <= maxPrice;
        const meetsBedroomCriteria = apartment.bedrooms >= minBedrooms;
        const meetsWellnessGymCriteria = wellnessGym ? apartment.amenities.includes('wellness gym') : true;
        const meetsSpaCriteria = spa ? apartment.amenities.includes('spa') : true;

        return meetsPriceCriteria && meetsBedroomCriteria && meetsWellnessGymCriteria && meetsSpaCriteria;
    });
}

// Example usage
const apartmentsForSale = [
    { price: 300000, bedrooms: 2, amenities: ['wellness gym', 'spa'] },
    { price: 250000, bedrooms: 1, amenities: ['spa'] },
    { price: 400000, bedrooms: 3, amenities: ['wellness gym'] },
    { price: 450000, bedrooms: 4, amenities: [] }
];

const criteria = {
    maxPrice: 350000,
    minBedrooms: 2,
    wellnessGym: true,
    spa: false
};

try {
    const filteredApartments = filterApartments(apartmentsForSale, criteria);
    console.log(filteredApartments);
} catch (error) {
    console.error("Error filtering apartments:", error.message);
}
```
