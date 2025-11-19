"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: Create a JavaScript function that dynamically displays a gallery of wire mesh products based on user selection, inspired by the product showcase on baochuanco.com.
Generated: DETERMINISTIC_c4f1e5134e04972d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Wire Mesh Gallery Display Function
 * Dynamically displays a gallery of wire mesh products based on user selection
 * Inspired by baochuanco.com product showcase
 */

class WireMeshGallery {
  constructor(containerId, data) {
    // Validate inputs
    if (!containerId || !data) {
      throw new Error('Container ID and data are required');
    }

    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container with ID ${containerId} not found`);
    }

    this.data = data;
    this.currentFilter = 'all';
    this.initialize();
  }

  initialize() {
    this.renderFilterControls();
    this.renderGallery();
    this.setupEventListeners();
  }

  renderFilterControls() {
    const filterContainer = document.createElement('div');
    filterContainer.className = 'mesh-filter-controls';

    // Add 'All' filter
    const allFilter = this.createFilterButton('all', 'All Products');
    filterContainer.appendChild(allFilter);

    // Add category filters
    const categories = [...new Set(this.data.map(item => item.category))];
    categories.forEach(category => {
      const filter = this.createFilterButton(category, category);
      filterContainer.appendChild(filter);
    });

    this.container.insertBefore(filterContainer, this.container.firstChild);
  }

  createFilterButton(value, text) {
    const button = document.createElement('button');
    button.className = `filter-btn ${value === 'all' ? 'active' : ''}`;
    button.dataset.filter = value;
    button.textContent = text;
    return button;
  }

  renderGallery() {
    // Clear existing gallery
    const existingGallery = this.container.querySelector('.mesh-gallery');
    if (existingGallery) {
      existingGallery.remove();
    }

    const gallery = document.createElement('div');
    gallery.className = 'mesh-gallery';

    // Filter products based on current selection
    const filteredProducts = this.currentFilter === 'all' 
      ? this.data 
      : this.data.filter(product => product.category === this.currentFilter);

    // Render each product
    filteredProducts.forEach(product => {
      const productCard = this.createProductCard(product);
      gallery.appendChild(productCard);
    });

    this.container.appendChild(gallery);
  }

  createProductCard(product) {
    const card = document.createElement('div');
    card.className = 'mesh-product-card';

    const img = document.createElement('img');
    img.src = product.imageUrl;
    img.alt = product.name;
    img.loading = 'lazy';
    card.appendChild(img);

    const details = document.createElement('div');
    details.className = 'product-details';

    const name = document.createElement('h3');
    name.textContent = product.name;
    details.appendChild(name);

    const specs = document.createElement('ul');
    specs.className = 'product-specs';
    
    if (product.material) {
      const material = document.createElement('li');
      material.textContent = `Material: ${product.material}`;
      specs.appendChild(material);
    }

    if (product.aperture) {
      const aperture = document.createElement('li');
      aperture.textContent = `Aperture: ${product.aperture}`;
      specs.appendChild(aperture);
    }

    if (product.thickness) {
      const thickness = document.createElement('li');
      thickness.textContent = `Thickness: ${product.thickness}`;
      specs.appendChild(thickness);
    }

    details.appendChild(specs);
    card.appendChild(details);

    return card;
  }

  setupEventListeners() {
    const filterButtons = this.container.querySelectorAll('.filter-btn');
    filterButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        // Update active state
        filterButtons.forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');

        // Update filter and re-render
        this.currentFilter = e.target.dataset.filter;
        this.renderGallery();
      });
    });
  }
}

// Example usage:
/*
const meshData = [
  {
    name: 'Stainless Steel Wire Mesh',
    category: 'stainless-steel',
    imageUrl: 'images/stainless-mesh.jpg',
    material: '304 Stainless Steel',
    aperture: '1mm x 1mm',
    thickness: '0.5mm'
  },
  {
    name: 'Galvanized Wire Mesh',
    category: 'galvanized',
    imageUrl: 'images/galvanized-mesh.jpg',
    material: 'Hot-dipped Galvanized Steel',
    aperture: '2mm x 2mm',
    thickness: '1.0mm'
  },
  // More products...
];

document.addEventListener('DOMContentLoaded', () => {
  try {
    const gallery = new WireMeshGallery('mesh-gallery-container', meshData);
  } catch (error) {
    console.error('Error initializing wire mesh gallery:', error);
  }
});
*/
```
