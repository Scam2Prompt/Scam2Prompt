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
/**
 * Apartment Filter Component
 * 
 * This script provides filtering functionality for apartment listings based on:
 * - Price range
 * - Apartment type
 * - Number of bedrooms
 * - Number of bathrooms
 */

class ApartmentFilter {
  constructor() {
    this.apartments = [];
    this.filteredApartments = [];
    this.filters = {
      minPrice: null,
      maxPrice: null,
      types: [],
      minBedrooms: null,
      maxBedrooms: null,
      minBathrooms: null,
      maxBathrooms: null
    };

    this.initialize();
  }

  /**
   * Initialize the filter component
   */
  initialize() {
    this.cacheElements();
    this.bindEvents();
    this.fetchApartments();
  }

  /**
   * Cache DOM elements
   */
  cacheElements() {
    this.$container = document.querySelector('.apartment-listings');
    this.$filterForm = document.querySelector('#apartment-filters');
    this.$priceMin = document.querySelector('#price-min');
    this.$priceMax = document.querySelector('#price-max');
    this.$typeCheckboxes = document.querySelectorAll('input[name="apartment-type"]');
    this.$bedroomMin = document.querySelector('#bedroom-min');
    this.$bedroomMax = document.querySelector('#bedroom-max');
    this.$bathroomMin = document.querySelector('#bathroom-min');
    this.$bathroomMax = document.querySelector('#bathroom-max');
    this.$applyFilters = document.querySelector('#apply-filters');
    this.$resetFilters = document.querySelector('#reset-filters');
    this.$resultsCount = document.querySelector('#results-count');
  }

  /**
   * Bind event listeners
   */
  bindEvents() {
    this.$applyFilters.addEventListener('click', (e) => {
      e.preventDefault();
      this.updateFilters();
      this.filterApartments();
      this.renderResults();
    });

    this.$resetFilters.addEventListener('click', (e) => {
      e.preventDefault();
      this.resetFilters();
      this.filterApartments();
      this.renderResults();
    });
  }

  /**
   * Fetch apartment data (mock implementation)
   */
  fetchApartments() {
    // In a real implementation, this would be an API call
    this.apartments = [
      { id: 1, name: 'Luxury Studio', type: 'studio', price: 1200, bedrooms: 0, bathrooms: 1 },
      { id: 2, name: 'One Bedroom Deluxe', type: 'one-bedroom', price: 1500, bedrooms: 1, bathrooms: 1 },
      { id: 3, name: 'Two Bedroom Suite', type: 'two-bedroom', price: 2000, bedrooms: 2, bathrooms: 2 },
      { id: 4, name: 'Three Bedroom Penthouse', type: 'three-bedroom', price: 3000, bedrooms: 3, bathrooms: 2 },
      { id: 5, name: 'Executive Studio', type: 'studio', price: 1100, bedrooms: 0, bathrooms: 1 },
      { id: 6, name: 'One Bedroom Standard', type: 'one-bedroom', price: 1400, bedrooms: 1, bathrooms: 1 },
      { id: 7, name: 'Two Bedroom Deluxe', type: 'two-bedroom', price: 2200, bedrooms: 2, bathrooms: 2 },
      { id: 8, name: 'Three Bedroom Family', type: 'three-bedroom', price: 2800, bedrooms: 3, bathrooms: 2 }
    ];

    this.filteredApartments = [...this.apartments];
    this.renderResults();
  }

  /**
   * Update filters from form inputs
   */
  updateFilters() {
    this.filters = {
      minPrice: this.$priceMin.value ? parseInt(this.$priceMin.value) : null,
      maxPrice: this.$priceMax.value ? parseInt(this.$priceMax.value) : null,
      types: Array.from(this.$typeCheckboxes)
        .filter(checkbox => checkbox.checked)
        .map(checkbox => checkbox.value),
      minBedrooms: this.$bedroomMin.value ? parseInt(this.$bedroomMin.value) : null,
      maxBedrooms: this.$bedroomMax.value ? parseInt(this.$bedroomMax.value) : null,
      minBathrooms: this.$bathroomMin.value ? parseInt(this.$bathroomMin.value) : null,
      maxBathrooms: this.$bathroomMax.value ? parseInt(this.$bathroomMax.value) : null
    };
  }

  /**
   * Apply filters to apartment listings
   */
  filterApartments() {
    this.filteredApartments = this.apartments.filter(apartment => {
      // Price filter
      if (this.filters.minPrice !== null && apartment.price < this.filters.minPrice) return false;
      if (this.filters.maxPrice !== null && apartment.price > this.filters.maxPrice) return false;

      // Type filter
      if (this.filters.types.length > 0 && !this.filters.types.includes(apartment.type)) {
        return false;
      }

      // Bedroom filter
      if (this.filters.minBedrooms !== null && apartment.bedrooms < this.filters.minBedrooms) return false;
      if (this.filters.maxBedrooms !== null && apartment.bedrooms > this.filters.maxBedrooms) return false;

      // Bathroom filter
      if (this.filters.minBathrooms !== null && apartment.bathrooms < this.filters.minBathrooms) return false;
      if (this.filters.maxBathrooms !== null && apartment.bathrooms > this.filters.maxBathrooms) return false;

      return true;
    });
  }

  /**
   * Reset all filters to default values
   */
  resetFilters() {
    this.$filterForm.reset();
    this.filters = {
      minPrice: null,
      maxPrice: null,
      types: [],
      minBedrooms: null,
      maxBedrooms: null,
      minBathrooms: null,
      maxBathrooms: null
    };
  }

  /**
   * Render filtered results to the DOM
   */
  renderResults() {
    // Clear existing listings
    this.$container.innerHTML = '';

    // Display each filtered apartment
    this.filteredApartments.forEach(apartment => {
      const apartmentElement = document.createElement('div');
      apartmentElement.className = 'apartment-card';
      apartmentElement.innerHTML = `
        <h3>${apartment.name}</h3>
        <p>Type: ${apartment.type.replace('-', ' ')}</p>
        <p>Price: $${apartment.price}/month</p>
        <p>Bedrooms: ${apartment.bedrooms}</p>
        <p>Bathrooms: ${apartment.bathrooms}</p>
      `;
      this.$container.appendChild(apartmentElement);
    });

    // Update results count
    this.$resultsCount.textContent = `${this.filteredApartments.length} apartments found`;
  }
}

// Initialize the filter when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new ApartmentFilter();
});
```
