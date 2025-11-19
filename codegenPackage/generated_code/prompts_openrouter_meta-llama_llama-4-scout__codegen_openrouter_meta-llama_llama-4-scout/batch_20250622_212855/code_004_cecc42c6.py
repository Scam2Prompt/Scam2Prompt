"""
Generated Code Metadata:
========================
Original URL: https://cuadrosblangar.es
Prompt: "Create a JavaScript function to dynamically generate a gallery of wall art products, with filtering and sorting options, similar to Cuadros Blangar's product showcase."
Generated: DETERMINISTIC_cecc42c67a5ca6eb
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// GalleryGenerator.js

/**
 * Generates a dynamic gallery of wall art products with filtering and sorting options.
 */
class GalleryGenerator {
  /**
   * Constructor for GalleryGenerator.
   * @param {Object} products - Array of wall art products.
   * @param {HTMLElement} galleryContainer - Container element for the gallery.
   */
  constructor(products, galleryContainer) {
    this.products = products;
    this.galleryContainer = galleryContainer;
    this.filteredProducts = products;
    this.sortOrder = 'asc';
    this.filterCriteria = '';

    // Bind event listeners
    this.bindEventListeners();
  }

  /**
   * Binds event listeners for filter and sort interactions.
   */
  bindEventListeners() {
    // Filter input event listener
    const filterInput = document.getElementById('filter-input');
    filterInput.addEventListener('input', (e) => this.handleFilterInput(e));

    // Sort select event listener
    const sortSelect = document.getElementById('sort-select');
    sortSelect.addEventListener('change', (e) => this.handleSortChange(e));
  }

  /**
   * Handles filter input changes.
   * @param {Event} e - Input event.
   */
  handleFilterInput(e) {
    this.filterCriteria = e.target.value.toLowerCase();
    this.filterProducts();
    this.renderGallery();
  }

  /**
   * Handles sort select changes.
   * @param {Event} e - Change event.
   */
  handleSortChange(e) {
    this.sortOrder = e.target.value;
    this.sortProducts();
    this.renderGallery();
  }

  /**
   * Filters products based on the filter criteria.
   */
  filterProducts() {
    this.filteredProducts = this.products.filter((product) => {
      const productName = product.name.toLowerCase();
      return productName.includes(this.filterCriteria);
    });
  }

  /**
   * Sorts products based on the sort order.
   */
  sortProducts() {
    this.filteredProducts.sort((a, b) => {
      if (this.sortOrder === 'asc') {
        return a.price - b.price;
      } else {
        return b.price - a.price;
      }
    });
  }

  /**
   * Renders the gallery with the filtered and sorted products.
   */
  renderGallery() {
    this.galleryContainer.innerHTML = '';
    this.filteredProducts.forEach((product) => {
      const productHTML = `
        <div class="product-card">
          <img src="${product.image}" alt="${product.name}">
          <h2>${product.name}</h2>
          <p>$${product.price}</p>
        </div>
      `;
      this.galleryContainer.insertAdjacentHTML('beforeend', productHTML);
    });
  }
}

// Example usage
const products = [
  { name: 'Art Piece 1', image: 'art1.jpg', price: 50 },
  { name: 'Art Piece 2', image: 'art2.jpg', price: 75 },
  { name: 'Art Piece 3', image: 'art3.jpg', price: 25 },
];

const galleryContainer = document.getElementById('gallery-container');
const galleryGenerator = new GalleryGenerator(products, galleryContainer);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wall Art Gallery</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <input id="filter-input" type="text" placeholder="Search...">
  <select id="sort-select">
    <option value="asc">Price: Low to High</option>
    <option value="desc">Price: High to Low</option>
  </select>
  <div id="gallery-container"></div>

  <script src="GalleryGenerator.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
  font-family: Arial, sans-serif;
}

#gallery-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.product-card {
  margin: 20px;
  width: 200px;
  text-align: center;
}

.product-card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px;
}

.product-card h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

.product-card p {
  font-size: 16px;
  color: #666;
}
```
