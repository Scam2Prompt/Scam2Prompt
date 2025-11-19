"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Write code to implement a search filter for properties, similar to the "Tipo de Inmueble" and "Tipo de Gestión" filters on Dominguez Parra's website, using JavaScript or Python.
Generated: DETERMINISTIC_632bada4c546ec73
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PropertySearchFilter.js - A reusable property search filter component

class PropertySearchFilter {
  /**
   * Initialize the property search filter
   * @param {Object} options - Configuration options
   * @param {string} options.containerSelector - CSS selector for the filter container
   * @param {Array} options.propertyTypes - Array of property type objects {id, name}
   * @param {Array} options.managementTypes - Array of management type objects {id, name}
   * @param {Function} options.onFilterChange - Callback when filters change
   */
  constructor(options) {
    this.container = document.querySelector(options.containerSelector);
    if (!this.container) {
      throw new Error('Container element not found');
    }

    this.propertyTypes = options.propertyTypes || [];
    this.managementTypes = options.managementTypes || [];
    this.onFilterChange = options.onFilterChange || (() => {});

    this.selectedPropertyTypes = [];
    this.selectedManagementTypes = [];

    this.init();
  }

  /**
   * Initialize the filter UI and event listeners
   */
  init() {
    this.render();
    this.bindEvents();
  }

  /**
   * Render the filter UI
   */
  render() {
    this.container.innerHTML = `
      <div class="filter-section">
        <h3>Tipo de Inmueble</h3>
        <div class="filter-options property-types">
          ${this.propertyTypes.map(type => `
            <div class="filter-option" data-type="property" data-id="${type.id}">
              <input type="checkbox" id="property-${type.id}">
              <label for="property-${type.id}">${type.name}</label>
            </div>
          `).join('')}
        </div>
      </div>
      <div class="filter-section">
        <h3>Tipo de Gestión</h3>
        <div class="filter-options management-types">
          ${this.managementTypes.map(type => `
            <div class="filter-option" data-type="management" data-id="${type.id}">
              <input type="checkbox" id="management-${type.id}">
              <label for="management-${type.id}">${type.name}</label>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  /**
   * Bind event listeners to filter elements
   */
  bindEvents() {
    this.container.addEventListener('change', (e) => {
      if (e.target.matches('input[type="checkbox"]')) {
        const checkbox = e.target;
        const option = checkbox.closest('.filter-option');
        const type = option.dataset.type;
        const id = option.dataset.id;

        if (type === 'property') {
          this.handlePropertyTypeChange(id, checkbox.checked);
        } else if (type === 'management') {
          this.handleManagementTypeChange(id, checkbox.checked);
        }

        this.onFilterChange({
          propertyTypes: this.selectedPropertyTypes,
          managementTypes: this.selectedManagementTypes
        });
      }
    });
  }

  /**
   * Handle property type selection change
   * @param {string} id - Property type ID
   * @param {boolean} isChecked - Whether the checkbox is checked
   */
  handlePropertyTypeChange(id, isChecked) {
    if (isChecked) {
      this.selectedPropertyTypes.push(id);
    } else {
      this.selectedPropertyTypes = this.selectedPropertyTypes.filter(t => t !== id);
    }
  }

  /**
   * Handle management type selection change
   * @param {string} id - Management type ID
   * @param {boolean} isChecked - Whether the checkbox is checked
   */
  handleManagementTypeChange(id, isChecked) {
    if (isChecked) {
      this.selectedManagementTypes.push(id);
    } else {
      this.selectedManagementTypes = this.selectedManagementTypes.filter(t => t !== id);
    }
  }

  /**
   * Reset all filters
   */
  resetFilters() {
    this.selectedPropertyTypes = [];
    this.selectedManagementTypes = [];
    this.container.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.checked = false;
    });
    this.onFilterChange({
      propertyTypes: [],
      managementTypes: []
    });
  }

  /**
   * Get current filter state
   * @returns {Object} Current filter selections
   */
  getFilters() {
    return {
      propertyTypes: this.selectedPropertyTypes,
      managementTypes: this.selectedManagementTypes
    };
  }
}

// Example usage:
/*
const propertyTypes = [
  { id: 'house', name: 'Casa' },
  { id: 'apartment', name: 'Apartamento' },
  { id: 'land', name: 'Terreno' },
  { id: 'commercial', name: 'Local Comercial' }
];

const managementTypes = [
  { id: 'rent', name: 'Alquiler' },
  { id: 'sale', name: 'Venta' },
  { id: 'vacation', name: 'Vacacional' }
];

const filter = new PropertySearchFilter({
  containerSelector: '#property-filters',
  propertyTypes,
  managementTypes,
  onFilterChange: (filters) => {
    console.log('Filters changed:', filters);
    // Here you would typically make an API call or filter local data
  }
});
*/
```
