"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: "Generate a code snippet in JavaScript to create a simple property search filter on a website, inspired by the property search options on Inmobiliaria Capri's website."
Generated: DETERMINISTIC_f902244f9449acdb
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PropertySearchFilter.js

/**
 * Property Search Filter class.
 * 
 * This class provides a simple property search filter functionality.
 * It filters properties based on location, property type, and price range.
 */
class PropertySearchFilter {
  /**
   * Constructor.
   * 
   * @param {Object[]} properties - Array of property objects.
   * @param {string[]} locations - Array of available locations.
   * @param {string[]} propertyTypes - Array of available property types.
   */
  constructor(properties, locations, propertyTypes) {
    this.properties = properties;
    this.locations = locations;
    this.propertyTypes = propertyTypes;
    this.filteredProperties = [];
  }

  /**
   * Filter properties by location.
   * 
   * @param {string} location - Location to filter by.
   * @returns {Object[]} Filtered properties.
   */
  filterByLocation(location) {
    return this.properties.filter(property => property.location === location);
  }

  /**
   * Filter properties by property type.
   * 
   * @param {string} propertyType - Property type to filter by.
   * @returns {Object[]} Filtered properties.
   */
  filterByPropertyType(propertyType) {
    return this.properties.filter(property => property.type === propertyType);
  }

  /**
   * Filter properties by price range.
   * 
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @returns {Object[]} Filtered properties.
   */
  filterByPriceRange(minPrice, maxPrice) {
    return this.properties.filter(property => property.price >= minPrice && property.price <= maxPrice);
  }

  /**
   * Filter properties by multiple criteria.
   * 
   * @param {string} location - Location to filter by.
   * @param {string} propertyType - Property type to filter by.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @returns {Object[]} Filtered properties.
   */
  filterProperties(location, propertyType, minPrice, maxPrice) {
    let filteredProperties = this.properties;

    if (location) {
      filteredProperties = filteredProperties.filter(property => property.location === location);
    }

    if (propertyType) {
      filteredProperties = filteredProperties.filter(property => property.type === propertyType);
    }

    if (minPrice && maxPrice) {
      filteredProperties = filteredProperties.filter(property => property.price >= minPrice && property.price <= maxPrice);
    }

    this.filteredProperties = filteredProperties;
    return filteredProperties;
  }
}

// Example usage:
const properties = [
  { id: 1, location: 'New York', type: 'Apartment', price: 100000 },
  { id: 2, location: 'New York', type: 'House', price: 500000 },
  { id: 3, location: 'Los Angeles', type: 'Apartment', price: 200000 },
  { id: 4, location: 'Los Angeles', type: 'House', price: 700000 },
];

const locations = ['New York', 'Los Angeles'];
const propertyTypes = ['Apartment', 'House'];

const propertySearchFilter = new PropertySearchFilter(properties, locations, propertyTypes);

// Filter properties
const filteredProperties = propertySearchFilter.filterProperties('New York', '', 0, 1000000);
console.log(filteredProperties);

// Get filtered properties by location
const filteredPropertiesByLocation = propertySearchFilter.filterByLocation('New York');
console.log(filteredPropertiesByLocation);

// Get filtered properties by property type
const filteredPropertiesByType = propertySearchFilter.filterByPropertyType('Apartment');
console.log(filteredPropertiesByType);

// Get filtered properties by price range
const filteredPropertiesByPriceRange = propertySearchFilter.filterByPriceRange(100000, 500000);
console.log(filteredPropertiesByPriceRange);

// Error handling example
try {
  const invalidProperties = propertySearchFilter.filterProperties(null, null, null, null);
  console.log(invalidProperties);
} catch (error) {
  console.error('Error:', error.message);
}
```
