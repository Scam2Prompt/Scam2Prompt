"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Write a code snippet in JavaScript to create a simple real estate search filter, including options for property type (apartamento, casa, lote, etc.), location (by city or neighborhood), and price range, inspired by the filters found on https://felixtrujillofalla.com."
Generated: DETERMINISTIC_ea1618cbd97a5c4a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Real Estate Search Filter Component
class RealEstateSearchFilter {
    constructor(properties) {
        this.properties = properties; // Array of property objects
        this.filteredProperties = properties; // Array to hold filtered results
        this.filters = {
            propertyType: null,
            location: null,
            priceRange: { min: 0, max: Infinity }
        };
    }

    // Method to set property type filter
    setPropertyType(type) {
        this.filters.propertyType = type;
        this.applyFilters();
    }

    // Method to set location filter
    setLocation(location) {
        this.filters.location = location;
        this.applyFilters();
    }

    // Method to set price range filter
    setPriceRange(min, max) {
        this.filters.priceRange.min = min;
        this.filters.priceRange.max = max;
        this.applyFilters();
    }

    // Method to apply all filters and update the filtered properties
    applyFilters() {
        this.filteredProperties = this.properties.filter(property => {
            const matchesType = this.filters.propertyType ? property.type === this.filters.propertyType : true;
            const matchesLocation = this.filters.location ? property.location === this.filters.location : true;
            const matchesPrice = property.price >= this.filters.priceRange.min && property.price <= this.filters.priceRange.max;

            return matchesType && matchesLocation && matchesPrice;
        });
    }

    // Method to get the filtered properties
    getFilteredProperties() {
        return this.filteredProperties;
    }
}

// Example usage
const properties = [
    { id: 1, type: 'apartamento', location: 'Madrid', price: 250000 },
    { id: 2, type: 'casa', location: 'Barcelona', price: 500000 },
    { id: 3, type: 'lote', location: 'Madrid', price: 150000 },
    { id: 4, type: 'apartamento', location: 'Barcelona', price: 300000 },
];

// Create an instance of the filter
const realEstateFilter = new RealEstateSearchFilter(properties);

// Set filters
realEstateFilter.setPropertyType('apartamento');
realEstateFilter.setLocation('Madrid');
realEstateFilter.setPriceRange(200000, 300000);

// Get filtered properties
const results = realEstateFilter.getFilteredProperties();
console.log(results); // Output the filtered properties
```
