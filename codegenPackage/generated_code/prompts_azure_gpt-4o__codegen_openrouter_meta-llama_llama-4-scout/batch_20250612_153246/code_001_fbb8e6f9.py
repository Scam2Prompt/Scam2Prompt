"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Generate JavaScript code to implement a filter functionality for a webpage that allows users to search for apartments by price, type, number of bedrooms, and bathrooms, similar to the filters on the Dunhill Serviced Apartments website.
Generated: DETERMINISTIC_fbb8e6f9a36b35d3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ApartmentFilter.js

class Apartment {
  /**
   * Represents an apartment with its properties.
   * @param {number} price - The price of the apartment.
   * @param {string} type - The type of the apartment.
   * @param {number} bedrooms - The number of bedrooms in the apartment.
   * @param {number} bathrooms - The number of bathrooms in the apartment.
   */
  constructor(price, type, bedrooms, bathrooms) {
    this.price = price;
    this.type = type;
    this.bedrooms = bedrooms;
    this.bathrooms = bathrooms;
  }
}

class ApartmentFilter {
  /**
   * Filters apartments based on the given criteria.
   * @param {Apartment[]} apartments - The list of apartments to filter.
   */
  constructor(apartments) {
    this.apartments = apartments;
  }

  /**
   * Filters apartments by price range.
   * @param {number} minPrice - The minimum price.
   * @param {number} maxPrice - The maximum price.
   * @returns {Apartment[]} The filtered apartments.
   */
  filterByPrice(minPrice, maxPrice) {
    return this.apartments.filter(apartment => apartment.price >= minPrice && apartment.price <= maxPrice);
  }

  /**
   * Filters apartments by type.
   * @param {string} type - The type of apartment to filter by.
   * @returns {Apartment[]} The filtered apartments.
   */
  filterByType(type) {
    return this.apartments.filter(apartment => apartment.type.toLowerCase() === type.toLowerCase());
  }

  /**
   * Filters apartments by number of bedrooms.
   * @param {number} bedrooms - The number of bedrooms to filter by.
   * @returns {Apartment[]} The filtered apartments.
   */
  filterByBedrooms(bedrooms) {
    return this.apartments.filter(apartment => apartment.bedrooms === bedrooms);
  }

  /**
   * Filters apartments by number of bathrooms.
   * @param {number} bathrooms - The number of bathrooms to filter by.
   * @returns {Apartment[]} The filtered apartments.
   */
  filterByBathrooms(bathrooms) {
    return this.apartments.filter(apartment => apartment.bathrooms === bathrooms);
  }

  /**
   * Applies multiple filters to the apartments.
   * @param {object} filters - An object containing the filter criteria.
   * @param {number} [filters.minPrice] - The minimum price.
   * @param {number} [filters.maxPrice] - The maximum price.
   * @param {string} [filters.type] - The type of apartment.
   * @param {number} [filters.bedrooms] - The number of bedrooms.
   * @param {number} [filters.bathrooms] - The number of bathrooms.
   * @returns {Apartment[]} The filtered apartments.
   */
  applyFilters(filters) {
    let filteredApartments = this.apartments;

    if (filters.minPrice && filters.maxPrice) {
      filteredApartments = this.filterByPrice(filters.minPrice, filters.maxPrice);
    }

    if (filters.type) {
      filteredApartments = this.filterByType(filters.type);
    }

    if (filters.bedrooms) {
      filteredApartments = this.filterByBedrooms(filters.bedrooms);
    }

    if (filters.bathrooms) {
      filteredApartments = this.filterByBathrooms(filters.bathrooms);
    }

    return filteredApartments;
  }
}

// Example usage:
const apartments = [
  new Apartment(100, 'Studio', 1, 1),
  new Apartment(200, '1 Bedroom', 1, 1),
  new Apartment(300, '2 Bedrooms', 2, 2),
  new Apartment(400, '3 Bedrooms', 3, 3),
];

const filter = new ApartmentFilter(apartments);

try {
  const filters = {
    minPrice: 200,
    type: '1 Bedroom',
  };

  const filteredApartments = filter.applyFilters(filters);

  console.log('Filtered Apartments:');
  filteredApartments.forEach(apartment => {
    console.log(`Price: ${apartment.price}, Type: ${apartment.type}, Bedrooms: ${apartment.bedrooms}, Bathrooms: ${apartment.bathrooms}`);
  });
} catch (error) {
  console.error('Error:', error.message);
}
```
