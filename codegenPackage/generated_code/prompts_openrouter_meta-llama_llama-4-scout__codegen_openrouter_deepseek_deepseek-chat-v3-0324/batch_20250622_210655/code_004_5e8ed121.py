"""
Generated Code Metadata:
========================
Original URL: https://www.navkarfurniture.com
Prompt: Write a JavaScript function to create a dynamic furniture product filter, similar to the one used on Navkar Furniture's website.
Generated: DETERMINISTIC_5e8ed121db96845c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamic Furniture Product Filter
 * 
 * This script creates a dynamic filter for furniture products similar to Navkar Furniture's website.
 * It allows users to filter products by category, price range, color, and material.
 */

class FurnitureFilter {
  /**
   * Initialize the filter with default settings
   * @param {Object} options - Configuration options
   * @param {string} options.containerSelector - CSS selector for the filter container
   * @param {string} options.productSelector - CSS selector for product items
   * @param {Object} options.filters - Available filter options
   */
  constructor(options) {
    this.settings = {
      containerSelector: '#furniture-filter',
      productSelector: '.product-item',
      filters: {
        categories: [],
        priceRanges: [
          { min: 0, max: 10000, label: 'Under ₹10,000' },
          { min: 10000, max: 20000, label: '₹10,000 - ₹20,000' },
          { min: 20000, max: 50000, label: '₹20,000 - ₹50,000' },
          { min: 50000, max: Infinity, label: 'Over ₹50,000' }
        ],
        colors: [],
        materials: []
      },
      ...options
    };

    this.selectedFilters = {
      category: null,
      priceRange: null,
      colors: [],
      materials: []
    };

    this.init();
  }

  /**
   * Initialize the filter UI and event listeners
   */
  init() {
    this.container = document.querySelector(this.settings.containerSelector);
    if (!this.container) {
      console.error('Filter container not found');
      return;
    }

    this.renderFilterControls();
    this.setupEventListeners();
    this.filterProducts();
  }

  /**
   * Render filter controls based on available options
   */
  renderFilterControls() {
    // Category filter
    if (this.settings.filters.categories.length > 0) {
      this.renderSelectFilter('category', 'Categories', this.settings.filters.categories);
    }

    // Price range filter
    if (this.settings.filters.priceRanges.length > 0) {
      this.renderRadioFilter('priceRange', 'Price Range', this.settings.filters.priceRanges);
    }

    // Color filter
    if (this.settings.filters.colors.length > 0) {
      this.renderCheckboxFilter('colors', 'Colors', this.settings.filters.colors);
    }

    // Material filter
    if (this.settings.filters.materials.length > 0) {
      this.renderCheckboxFilter('materials', 'Materials', this.settings.filters.materials);
    }

    // Add clear filters button
    const clearBtn = document.createElement('button');
    clearBtn.className = 'clear-filters';
    clearBtn.textContent = 'Clear All Filters';
    clearBtn.addEventListener('click', () => this.clearFilters());
    this.container.appendChild(clearBtn);
  }

  /**
   * Render a select dropdown filter
   * @param {string} filterName - Name of the filter
   * @param {string} label - Display label
   * @param {Array} options - Available options
   */
  renderSelectFilter(filterName, label, options) {
    const filterGroup = document.createElement('div');
    filterGroup.className = `filter-group ${filterName}-filter`;

    const filterLabel = document.createElement('h3');
    filterLabel.textContent = label;
    filterGroup.appendChild(filterLabel);

    const select = document.createElement('select');
    select.name = filterName;
    select.id = `${filterName}-filter`;

    // Add default option
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = `All ${label}`;
    select.appendChild(defaultOption);

    // Add other options
    options.forEach(option => {
      const opt = document.createElement('option');
      opt.value = option.value || option;
      opt.textContent = option.label || option;
      select.appendChild(opt);
    });

    select.addEventListener('change', (e) => {
      this.selectedFilters[filterName] = e.target.value === '' ? null : e.target.value;
      this.filterProducts();
    });

    filterGroup.appendChild(select);
    this.container.appendChild(filterGroup);
  }

  /**
   * Render a radio button filter
   * @param {string} filterName - Name of the filter
   * @param {string} label - Display label
   * @param {Array} options - Available options
   */
  renderRadioFilter(filterName, label, options) {
    const filterGroup = document.createElement('div');
    filterGroup.className = `filter-group ${filterName}-filter`;

    const filterLabel = document.createElement('h3');
    filterLabel.textContent = label;
    filterGroup.appendChild(filterLabel);

    options.forEach(option => {
      const radioDiv = document.createElement('div');
      radioDiv.className = 'radio-option';

      const radio = document.createElement('input');
      radio.type = 'radio';
      radio.name = filterName;
      radio.id = `${filterName}-${option.label.replace(/\s+/g, '-').toLowerCase()}`;
      radio.value = option.label;

      radio.addEventListener('change', () => {
        this.selectedFilters[filterName] = option;
        this.filterProducts();
      });

      const radioLabel = document.createElement('label');
      radioLabel.htmlFor = radio.id;
      radioLabel.textContent = option.label;

      radioDiv.appendChild(radio);
      radioDiv.appendChild(radioLabel);
      filterGroup.appendChild(radioDiv);
    });

    // Add "All" option
    const radioDiv = document.createElement('div');
    radioDiv.className = 'radio-option';

    const radio = document.createElement('input');
    radio.type = 'radio';
    radio.name = filterName;
    radio.id = `${filterName}-all`;
    radio.value = '';
    radio.checked = true;

    radio.addEventListener('change', () => {
      this.selectedFilters[filterName] = null;
      this.filterProducts();
    });

    const radioLabel = document.createElement('label');
    radioLabel.htmlFor = radio.id;
    radioLabel.textContent = 'All Prices';

    radioDiv.appendChild(radio);
    radioDiv.appendChild(radioLabel);
    filterGroup.appendChild(radioDiv);

    this.container.appendChild(filterGroup);
  }

  /**
   * Render a checkbox filter
   * @param {string} filterName - Name of the filter
   * @param {string} label - Display label
   * @param {Array} options - Available options
   */
  renderCheckboxFilter(filterName, label, options) {
    const filterGroup = document.createElement('div');
    filterGroup.className = `filter-group ${filterName}-filter`;

    const filterLabel = document.createElement('h3');
    filterLabel.textContent = label;
    filterGroup.appendChild(filterLabel);

    options.forEach(option => {
      const checkboxDiv = document.createElement('div');
      checkboxDiv.className = 'checkbox-option';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.name = filterName;
      checkbox.id = `${filterName}-${option.replace(/\s+/g, '-').toLowerCase()}`;
      checkbox.value = option;

      checkbox.addEventListener('change', (e) => {
        if (e.target.checked) {
          this.selectedFilters[filterName].push(option);
        } else {
          this.selectedFilters[filterName] = this.selectedFilters[filterName].filter(
            item => item !== option
          );
        }
        this.filterProducts();
      });

      const checkboxLabel = document.createElement('label');
      checkboxLabel.htmlFor = checkbox.id;
      checkboxLabel.textContent = option;

      checkboxDiv.appendChild(checkbox);
      checkboxDiv.appendChild(checkboxLabel);
      filterGroup.appendChild(checkboxDiv);
    });

    this.container.appendChild(filterGroup);
  }

  /**
   * Setup event listeners for filter controls
   */
  setupEventListeners() {
    // Additional event listeners can be added here if needed
  }

  /**
   * Filter products based on selected filters
   */
  filterProducts() {
    const products = document.querySelectorAll(this.settings.productSelector);
    if (!products.length) {
      console.warn('No products found to filter');
      return;
    }

    products.forEach(product => {
      const matchesFilters = this.productMatchesFilters(product);
      product.style.display = matchesFilters ? 'block' : 'none';
    });
  }

  /**
   * Check if a product matches all selected filters
   * @param {HTMLElement} product - Product element
   * @returns {boolean} True if product matches all filters
   */
  productMatchesFilters(product) {
    // Check category filter
    if (this.selectedFilters.category && 
        product.dataset.category !== this.selectedFilters.category) {
      return false;
    }

    // Check price range filter
    if (this.selectedFilters.priceRange) {
      const price = parseFloat(product.dataset.price);
      if (price < this.selectedFilters.priceRange.min || 
          price > this.selectedFilters.priceRange.max) {
        return false;
      }
    }

    // Check color filter
    if (this.selectedFilters.colors.length > 0) {
      const productColors = product.dat
