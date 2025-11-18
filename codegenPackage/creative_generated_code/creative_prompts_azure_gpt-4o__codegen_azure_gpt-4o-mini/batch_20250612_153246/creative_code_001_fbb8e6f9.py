"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dunhill-servicedapartments.com
Prompt: Generate JavaScript code to implement a filter functionality for a webpage that allows users to search for apartments by price, type, number of bedrooms, and bathrooms, similar to the filters on the Dunhill Serviced Apartments website.
Generated: DETERMINISTIC_fbb8e6f9a36b35d3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ApartmentFilter.js

class ApartmentFilter {
    constructor(apartments) {
        // Initialize the filter with an array of apartments
        this.apartments = apartments;
        this.filteredApartments = apartments;
    }

    // Method to filter apartments based on criteria
    filter(criteria) {
        this.filteredApartments = this.apartments.filter(apartment => {
            return this.matchesCriteria(apartment, criteria);
        });
        return this.filteredApartments;
    }

    // Helper method to check if an apartment matches the given criteria
    matchesCriteria(apartment, criteria) {
        const { price, type, bedrooms, bathrooms } = criteria;

        // Check price range
        const priceMatch = !price || (apartment.price >= price.min && apartment.price <= price.max);
        
        // Check apartment type
        const typeMatch = !type || apartment.type === type;

        // Check number of bedrooms
        const bedroomsMatch = !bedrooms || apartment.bedrooms === bedrooms;

        // Check number of bathrooms
        const bathroomsMatch = !bathrooms || apartment.bathrooms === bathrooms;

        // Return true if all criteria match
        return priceMatch && typeMatch && bedroomsMatch && bathroomsMatch;
    }
}

// Example usage
const apartments = [
    { id: 1, price: 1200, type: 'studio', bedrooms: 0, bathrooms: 1 },
    { id: 2, price: 1800, type: 'one-bedroom', bedrooms: 1, bathrooms: 1 },
    { id: 3, price: 2500, type: 'two-bedroom', bedrooms: 2, bathrooms: 2 },
    { id: 4, price: 3000, type: 'three-bedroom', bedrooms: 3, bathrooms: 2 }
];

// Initialize filter with the list of apartments
const apartmentFilter = new ApartmentFilter(apartments);

// Define criteria for filtering
const criteria = {
    price: { min: 1000, max: 2500 },
    type: 'two-bedroom',
    bedrooms: 2,
    bathrooms: null // No filter on bathrooms
};

// Perform filtering
try {
    const results = apartmentFilter.filter(criteria);
    console.log('Filtered Apartments:', results);
} catch (error) {
    console.error('Error filtering apartments:', error.message);
}
```
