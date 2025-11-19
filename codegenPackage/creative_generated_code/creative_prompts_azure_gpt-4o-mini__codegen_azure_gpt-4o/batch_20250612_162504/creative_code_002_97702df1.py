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
 * Filters a list of apartments for sale based on criteria.
 * @param {Array<Object>} apartments - List of apartments. Each apartment is an object with properties:
 *                                      - price {number} : Price of the apartment.
 *                                      - bedrooms {number} : Number of bedrooms.
 *                                      - amenities {Array<string>} : List of amenities available (e.g., ["gym", "spa"]).
 * @param {Object} criteria - Criteria for filtering apartments. Contains:
 *                            - maxPrice {number} : Maximum price for the apartment. (Optional)
 *                            - minBedrooms {number} : Minimum number of bedrooms. (Optional)
 *                            - requiredAmenities {Array<string>} : List of required amenities. (Optional)
 * @returns {Array<Object>} - List of apartments that match all the criteria.
 */
function filterApartments(apartments, criteria) {
  // Validate inputs
  if (!Array.isArray(apartments) || typeof criteria !== 'object') {
    throw new Error("Invalid inputs. 'apartments' must be an array and 'criteria' must be an object.");
  }

  // Extract criteria values with defaults
  const {
    maxPrice = Infinity,
    minBedrooms = 0,
    requiredAmenities = []
  } = criteria;

  // Filter apartments based on criteria
  return apartments.filter(apartment => {
    // Check price
    if (apartment.price > maxPrice) {
      return false;
    }

    // Check number of bedrooms
    if (apartment.bedrooms < minBedrooms) {
      return false;
    }

    // Check required amenities
    if (!requiredAmenities.every(amenity => apartment.amenities.includes(amenity))) {
      return false;
    }

    // Apartment matches all criteria
    return true;
  });
}

// Example Usage:
// List of apartments
const apartments = [
  { price: 150000, bedrooms: 2, amenities: ["gym", "spa", "pool"] },
  { price: 200000, bedrooms: 3, amenities: ["gym", "spa"] },
  { price: 120000, bedrooms: 1, amenities: ["pool"] },
  { price: 300000, bedrooms: 4, amenities: ["gym", "spa", "sauna"] }
];

// Criteria to filter apartments
const criteria = {
  maxPrice: 200000,
  minBedrooms: 2,
  requiredAmenities: ["gym", "spa"]
};

// Filter apartments based on criteria
const filteredApartments = filterApartments(apartments, criteria);
console.log(filteredApartments);
// Output: [{ price: 150000, bedrooms: 2, amenities: ["gym", "spa", "pool"] }]
```
