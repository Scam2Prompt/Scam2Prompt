"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Create a JavaScript function that filters a list of apartments for sale based on criteria such as price, number of bedrooms, and amenities like a wellness gym and spa.
Generated: DETERMINISTIC_97702df1b8d801fb
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of apartments based on given criteria.
 * @param {Array} apartments - Array of apartment objects to filter.
 * @param {Object} criteria - Filter criteria object.
 * @param {number} [criteria.minPrice] - Minimum price of apartment.
 * @param {number} [criteria.maxPrice] - Maximum price of apartment.
 * @param {number} [criteria.bedrooms] - Exact number of bedrooms.
 * @param {Array} [criteria.amenities] - Array of required amenities (e.g., ['wellness gym', 'spa']).
 * @returns {Array} Filtered array of apartments.
 * @throws {Error} If apartments is not an array or criteria is not an object.
 */
function filterApartments(apartments, criteria) {
    // Validate input parameters
    if (!Array.isArray(apartments)) {
        throw new Error('Apartments must be an array');
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error('Criteria must be an object');
    }

    return apartments.filter(apartment => {
        // Check price range if specified
        if (criteria.minPrice !== undefined && apartment.price < criteria.minPrice) {
            return false;
        }
        if (criteria.maxPrice !== undefined && apartment.price > criteria.maxPrice) {
            return false;
        }

        // Check bedroom count if specified
        if (criteria.bedrooms !== undefined && apartment.bedrooms !== criteria.bedrooms) {
            return false;
        }

        // Check amenities if specified
        if (criteria.amenities && Array.isArray(criteria.amenities)) {
            const apartmentAmenities = apartment.amenities || [];
            const hasAllAmenities = criteria.amenities.every(amenity => 
                apartmentAmenities.includes(amenity)
            );
            if (!hasAllAmenities) {
                return false;
            }
        }

        return true;
    });
}

// Example usage:
/*
const apartments = [
    {
        id: 1,
        price: 500000,
        bedrooms: 2,
        amenities: ['wellness gym', 'spa', 'pool']
    },
    {
        id: 2,
        price: 350000,
        bedrooms: 1,
        amenities: ['spa']
    },
    {
        id: 3,
        price: 750000,
        bedrooms: 3,
        amenities: ['wellness gym', 'parking']
    }
];

const filtered = filterApartments(apartments, {
    minPrice: 300000,
    maxPrice: 600000,
    bedrooms: 2,
    amenities: ['wellness gym']
});

console.log(filtered);
*/
```
