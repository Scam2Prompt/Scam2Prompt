"""
Generated Code Metadata:
========================
Original URL: https://shopmetlife.pk
Prompt: Write a JavaScript code snippet to implement a search bar on an e-commerce website, similar to the one on ShopMetlife, that allows users to search for products by name or category.
Generated: DETERMINISTIC_3c950ed84e840cdf
Batch ID: 20250622_212236
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
 * SearchBar class representing a search bar component on an e-commerce website.
 */
class SearchBar {
  /**
   * Constructor for the SearchBar class.
   * @param {Object} options - Configuration options for the search bar.
   * @param {String} options.searchInputId - ID of the search input field.
   * @param {String} options.searchButtonId - ID of the search button.
   * @param {String} options.searchResultsId - ID of the search results container.
   * @param {Array} options.products - List of products to search through.
   */
  constructor(options) {
    this.searchInputId = options.searchInputId;
    this.searchButtonId = options.searchButtonId;
    this.searchResultsId = options.searchResultsId;
    this.products = options.products;

    // Get DOM elements
    this.searchInput = document.getElementById(this.searchInputId);
    this.searchButton = document.getElementById(this.searchButtonId);
    this.searchResults = document.getElementById(this.searchResultsId);

    // Add event listener to search button
    this.searchButton.addEventListener('click', () => this.handleSearch());
  }

  /**
   * Handles the search functionality.
   */
  handleSearch() {
    const searchQuery = this.searchInput.value.trim().toLowerCase();

    if (searchQuery === '') {
      // Clear search results if search query is empty
      this.searchResults.innerHTML = '';
      return;
    }

    try {
      // Filter products based on search query
      const searchResults = this.products.filter((product) => {
        const productName = product.name.toLowerCase();
        const productCategory = product.category.toLowerCase();
        return productName.includes(searchQuery) || productCategory.includes(searchQuery);
      });

      // Render search results
      this.renderSearchResults(searchResults);
    } catch (error) {
      console.error('Error occurred during search:', error);
      // Display error message to user
      this.searchResults.innerHTML = 'An error occurred. Please try again.';
    }
  }

  /**
   * Renders the search results.
   * @param {Array} searchResults - List of products matching the search query.
   */
  renderSearchResults(searchResults) {
    if (searchResults.length === 0) {
      // Display no results message
      this.searchResults.innerHTML = 'No results found.';
      return;
    }

    // Create HTML list of search results
    const html = searchResults.map((product) => {
      return `
        <li>
          <h2>${product.name}</h2>
          <p>Category: ${product.category}</p>
        </li>
      `;
    }).join('');

    // Update search results container
    this.searchResults.innerHTML = `
      <ul>
        ${html}
      </ul>
    `;
  }
}

// Example usage
const products = [
  { name: 'Product A', category: 'Electronics' },
  { name: 'Product B', category: 'Fashion' },
  { name: 'Product C', category: 'Electronics' },
];

const searchBar = new SearchBar({
  searchInputId: 'search-input',
  searchButtonId: 'search-button',
  searchResultsId: 'search-results',
  products,
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>E-commerce Search Bar</title>
  <style>
    /* Basic styling for search bar and results */
    #search-input {
      padding: 10px;
      font-size: 18px;
    }
    #search-button {
      padding: 10px 20px;
      font-size: 18px;
      cursor: pointer;
    }
    #search-results {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <input id="search-input" type="text" placeholder="Search...">
  <button id="search-button">Search</button>
  <div id="search-results"></div>

  <script src="searchBar.js"></script>
</body>
</html>
```
