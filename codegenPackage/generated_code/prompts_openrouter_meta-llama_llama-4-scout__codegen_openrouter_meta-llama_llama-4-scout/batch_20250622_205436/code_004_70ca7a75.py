"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: "Write a JavaScript code snippet to implement a search bar on an e-commerce website, similar to Semillas Plantae, that allows users to find specific products by name or category."
Generated: DETERMINISTIC_70ca7a75b6348a19
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// searchBar.js

/**
 * SearchBar class implementation.
 */
class SearchBar {
  /**
   * Constructor for SearchBar.
   * @param {HTMLElement} searchBarElement - The HTML element for the search bar.
   * @param {Array} products - The list of products to search through.
   */
  constructor(searchBarElement, products) {
    this.searchBarElement = searchBarElement;
    this.products = products;
    this.filteredProducts = [];

    // Add event listener for input changes
    this.searchBarElement.addEventListener('input', this.handleInputChange.bind(this));
  }

  /**
   * Handles input changes in the search bar.
   * @param {Event} event - The input event.
   */
  handleInputChange(event) {
    const searchQuery = event.target.value.toLowerCase().trim();

    if (searchQuery === '') {
      this.filteredProducts = [];
      this.renderSearchResults();
      return;
    }

    this.filterProducts(searchQuery);
    this.renderSearchResults();
  }

  /**
   * Filters products based on the search query.
   * @param {string} searchQuery - The search query.
   */
  filterProducts(searchQuery) {
    this.filteredProducts = this.products.filter((product) => {
      const productName = product.name.toLowerCase();
      const productCategory = product.category.toLowerCase();

      return productName.includes(searchQuery) || productCategory.includes(searchQuery);
    });
  }

  /**
   * Renders the search results.
   */
  renderSearchResults() {
    const searchResultsElement = document.getElementById('search-results');

    if (!searchResultsElement) {
      console.error('Search results element not found');
      return;
    }

    searchResultsElement.innerHTML = '';

    if (this.filteredProducts.length === 0) {
      const noResultsElement = document.createElement('li');
      noResultsElement.textContent = 'No results found';
      searchResultsElement.appendChild(noResultsElement);
    } else {
      this.filteredProducts.forEach((product) => {
        const productElement = document.createElement('li');
        productElement.innerHTML = `
          <h2>${product.name}</h2>
          <p>Category: ${product.category}</p>
        `;
        searchResultsElement.appendChild(productElement);
      });
    }
  }
}

// Example usage
const products = [
  { name: 'Product 1', category: 'Category A' },
  { name: 'Product 2', category: 'Category B' },
  { name: 'Product 3', category: 'Category A' },
];

const searchBarElement = document.getElementById('search-bar');
const searchBar = new SearchBar(searchBarElement, products);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Search Bar Example</title>
  <style>
    #search-results {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    #search-results li {
      padding: 10px;
      border-bottom: 1px solid #ccc;
    }

    #search-results li:last-child {
      border-bottom: none;
    }
  </style>
</head>
<body>
  <input id="search-bar" type="search" placeholder="Search...">
  <ul id="search-results"></ul>

  <script src="searchBar.js"></script>
</body>
</html>
```
