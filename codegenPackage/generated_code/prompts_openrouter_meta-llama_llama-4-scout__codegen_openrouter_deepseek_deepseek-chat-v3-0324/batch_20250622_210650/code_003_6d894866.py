"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Create a JavaScript function that can be used to display a list of products with different sizes, styles, and designs, like the 'Skladové okná' section on nellyservis.sk."
Generated: DETERMINISTIC_6d8948669a2efe9b
Batch ID: 20250622_210650
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/window1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/window2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * Product class representing a single product with its attributes.
 */
class Product {
  /**
   * @param {string} id - Unique identifier for the product
   * @param {string} name - Name of the product
   * @param {string} description - Product description
   * @param {number} price - Product price
   * @param {string[]} sizes - Available sizes
   * @param {string[]} styles - Available styles
   * @param {string[]} designs - Available designs
   * @param {string} imageUrl - URL of the product image
   */
  constructor(id, name, description, price, sizes, styles, designs, imageUrl) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.price = price;
    this.sizes = sizes;
    this.styles = styles;
    this.designs = designs;
    this.imageUrl = imageUrl;
  }
}

/**
 * ProductDisplay component for rendering a list of products with filters.
 */
class ProductDisplay {
  /**
   * @param {HTMLElement} container - DOM element to render the products in
   * @param {Product[]} products - Array of Product objects
   */
  constructor(container, products) {
    this.container = container;
    this.products = products;
    this.filteredProducts = [...products];
    this.selectedFilters = {
      size: null,
      style: null,
      design: null
    };
  }

  /**
   * Initializes the product display and renders all components.
   */
  init() {
    this.renderFilters();
    this.renderProducts();
    this.setupEventListeners();
  }

  /**
   * Renders filter controls based on available product attributes.
   */
  renderFilters() {
    const filterContainer = document.createElement('div');
    filterContainer.className = 'product-filters';

    const sizeFilter = this.createFilter('size', 'Veľkosť', this.getAllSizes());
    const styleFilter = this.createFilter('style', 'Štýl', this.getAllStyles());
    const designFilter = this.createFilter('design', 'Dizajn', this.getAllDesigns());

    filterContainer.appendChild(sizeFilter);
    filterContainer.appendChild(styleFilter);
    filterContainer.appendChild(designFilter);

    this.container.appendChild(filterContainer);
  }

  /**
   * Creates a single filter dropdown.
   * @param {string} id - Filter ID
   * @param {string} label - Filter label
   * @param {string[]} options - Filter options
   * @returns {HTMLElement} The filter element
   */
  createFilter(id, label, options) {
    const filterGroup = document.createElement('div');
    filterGroup.className = 'filter-group';

    const filterLabel = document.createElement('label');
    filterLabel.textContent = label;
    filterLabel.htmlFor = id;
    filterGroup.appendChild(filterLabel);

    const filterSelect = document.createElement('select');
    filterSelect.id = id;
    filterSelect.className = 'filter-select';

    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = 'Všetky';
    filterSelect.appendChild(defaultOption);

    options.forEach(option => {
      const opt = document.createElement('option');
      opt.value = option;
      opt.textContent = option;
      filterSelect.appendChild(opt);
    });

    filterGroup.appendChild(filterSelect);
    return filterGroup;
  }

  /**
   * Gets all unique sizes from products.
   * @returns {string[]} Array of sizes
   */
  getAllSizes() {
    const sizes = new Set();
    this.products.forEach(product => {
      product.sizes.forEach(size => sizes.add(size));
    });
    return Array.from(sizes).sort();
  }

  /**
   * Gets all unique styles from products.
   * @returns {string[]} Array of styles
   */
  getAllStyles() {
    const styles = new Set();
    this.products.forEach(product => {
      product.styles.forEach(style => styles.add(style));
    });
    return Array.from(styles).sort();
  }

  /**
   * Gets all unique designs from products.
   * @returns {string[]} Array of designs
   */
  getAllDesigns() {
    const designs = new Set();
    this.products.forEach(product => {
      product.designs.forEach(design => designs.add(design));
    });
    return Array.from(designs).sort();
  }

  /**
   * Renders the product cards based on current filters.
   */
  renderProducts() {
    const productsContainer = document.createElement('div');
    productsContainer.className = 'products-container';

    if (this.filteredProducts.length === 0) {
      const noResults = document.createElement('p');
      noResults.className = 'no-results';
      noResults.textContent = 'Nenašli sa žiadne produkty podľa zadaných filtrov.';
      productsContainer.appendChild(noResults);
    } else {
      this.filteredProducts.forEach(product => {
        const productCard = this.createProductCard(product);
        productsContainer.appendChild(productCard);
      });
    }

    const existingContainer = this.container.querySelector('.products-container');
    if (existingContainer) {
      this.container.replaceChild(productsContainer, existingContainer);
    } else {
      this.container.appendChild(productsContainer);
    }
  }

  /**
   * Creates a product card element.
   * @param {Product} product - Product to display
   * @returns {HTMLElement} The product card element
   */
  createProductCard(product) {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.dataset.id = product.id;

    const image = document.createElement('img');
    image.src = product.imageUrl;
    image.alt = product.name;
    image.className = 'product-image';
    card.appendChild(image);

    const name = document.createElement('h3');
    name.textContent = product.name;
    card.appendChild(name);

    const description = document.createElement('p');
    description.textContent = product.description;
    card.appendChild(description);

    const price = document.createElement('div');
    price.className = 'product-price';
    price.textContent = `${product.price.toFixed(2)} €`;
    card.appendChild(price);

    const attributes = document.createElement('div');
    attributes.className = 'product-attributes';

    const sizes = document.createElement('p');
    sizes.textContent = `Veľkosti: ${product.sizes.join(', ')}`;
    attributes.appendChild(sizes);

    const styles = document.createElement('p');
    styles.textContent = `Štýly: ${product.styles.join(', ')}`;
    attributes.appendChild(styles);

    const designs = document.createElement('p');
    designs.textContent = `Dizajny: ${product.designs.join(', ')}`;
    attributes.appendChild(designs);

    card.appendChild(attributes);

    return card;
  }

  /**
   * Sets up event listeners for filter changes.
   */
  setupEventListeners() {
    const sizeFilter = this.container.querySelector('#size');
    const styleFilter = this.container.querySelector('#style');
    const designFilter = this.container.querySelector('#design');

    sizeFilter.addEventListener('change', (e) => this.handleFilterChange('size', e.target.value));
    styleFilter.addEventListener('change', (e) => this.handleFilterChange('style', e.target.value));
    designFilter.addEventListener('change', (e) => this.handleFilterChange('design', e.target.value));
  }

  /**
   * Handles filter changes and updates the product list.
   * @param {string} filterType - Type of filter (size, style, design)
   * @param {string} value - Selected filter value
   */
  handleFilterChange(filterType, value) {
    this.selectedFilters[filterType] = value === '' ? null : value;
    this.applyFilters();
  }

  /**
   * Applies all active filters to the product list.
   */
  applyFilters() {
    this.filteredProducts = this.products.filter(product => {
      return (
        (this.selectedFilters.size === null || product.sizes.includes(this.selectedFilters.size)) &&
        (this.selectedFilters.style === null || product.styles.includes(this.selectedFilters.style)) &&
        (this.selectedFilters.design === null || product.designs.includes(this.selectedFilters.design))
      );
    });
    this.renderProducts();
  }
}

// Example usage:
/*
const sampleProducts = [
  new Product(
    '1',
    'Okno Standard',
    'Kvalitné plastové okno s dobrou izoláciou',
    199.99,
    ['80x120', '100x140', '120x160'],
    ['Klasické', 'Moderné'],
    ['Biela', 'Hnedá'],
    'https://example.com/window1.jpg'
  ),
  new Product(
    '2',
    'Okno Premium',
    'Prémiové okno s vynikajúcou tepelnou izoláciou',
    299.99,
    ['90x130', '110x150'],
    ['Moderné', 'Minimalistické'],
    ['Biela', 'Čierna', 'Drevený vzhľad'],
    'https://example.com/window2.jpg'
  )
];

const container = document.getElementById('products-container');
const
