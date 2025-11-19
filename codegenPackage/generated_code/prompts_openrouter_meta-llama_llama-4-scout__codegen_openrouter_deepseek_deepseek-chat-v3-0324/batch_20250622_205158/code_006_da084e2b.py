"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: "Write a JavaScript code snippet to implement a search bar like the one on Weavely, which allows users to search for products by keyword, category, and price range."
Generated: DETERMINISTIC_da084e2b1adb726d
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * SearchBar Component for Product Search
 * 
 * Features:
 * - Keyword search
 * - Category filter
 * - Price range filter
 * - Debounced search to prevent excessive API calls
 */

class SearchBar {
  constructor(options) {
    this.element = options.element;
    this.onSearch = options.onSearch || (() => {});
    this.debounceTimeout = null;
    this.debounceDelay = 300;
    
    // Initialize categories from options or empty array
    this.categories = options.categories || [];
    
    this.render();
    this.bindEvents();
  }

  /**
   * Render the search bar HTML
   */
  render() {
    this.element.innerHTML = `
      <div class="search-container">
        <div class="search-input-group">
          <input type="text" class="search-input" placeholder="Search products..." />
          <button class="search-button">Search</button>
        </div>
        
        <div class="search-filters">
          <select class="category-filter">
            <option value="">All Categories</option>
            ${this.categories.map(cat => `<option value="${cat.id}">${cat.name}</option>`).join('')}
          </select>
          
          <div class="price-range-filter">
            <label>Price Range:</label>
            <input type="number" class="min-price" placeholder="Min" min="0" />
            <span>-</span>
            <input type="number" class="max-price" placeholder="Max" min="0" />
          </div>
        </div>
      </div>
    `;
  }

  /**
   * Bind event listeners
   */
  bindEvents() {
    const searchInput = this.element.querySelector('.search-input');
    const searchButton = this.element.querySelector('.search-button');
    const categoryFilter = this.element.querySelector('.category-filter');
    const minPrice = this.element.querySelector('.min-price');
    const maxPrice = this.element.querySelector('.max-price');

    // Debounced search on input
    searchInput.addEventListener('input', () => {
      clearTimeout(this.debounceTimeout);
      this.debounceTimeout = setTimeout(() => this.performSearch(), this.debounceDelay);
    });

    // Immediate search on button click
    searchButton.addEventListener('click', () => this.performSearch());

    // Search when filters change
    categoryFilter.addEventListener('change', () => this.performSearch());
    minPrice.addEventListener('change', () => this.performSearch());
    maxPrice.addEventListener('change', () => this.performSearch());
  }

  /**
   * Get current search parameters
   */
  getSearchParams() {
    return {
      keyword: this.element.querySelector('.search-input').value.trim(),
      category: this.element.querySelector('.category-filter').value,
      minPrice: this.element.querySelector('.min-price').value,
      maxPrice: this.element.querySelector('.max-price').value
    };
  }

  /**
   * Validate search parameters
   */
  validateSearchParams(params) {
    // Validate price range
    if (params.minPrice && params.maxPrice && parseFloat(params.minPrice) > parseFloat(params.maxPrice)) {
      throw new Error('Minimum price cannot be greater than maximum price');
    }
    
    return params;
  }

  /**
   * Perform the search with current parameters
   */
  performSearch() {
    try {
      const params = this.validateSearchParams(this.getSearchParams());
      this.onSearch(params);
    } catch (error) {
      console.error('Search error:', error.message);
      // In a real app, you might show this to the user
      alert(error.message);
    }
  }

  /**
   * Update available categories
   */
  updateCategories(categories) {
    this.categories = categories;
    const categorySelect = this.element.querySelector('.category-filter');
    
    if (categorySelect) {
      categorySelect.innerHTML = `
        <option value="">All Categories</option>
        ${categories.map(cat => `<option value="${cat.id}">${cat.name}</option>`).join('')}
      `;
    }
  }
}

// Example usage:
/*
const searchBar = new SearchBar({
  element: document.getElementById('search-container'),
  categories: [
    { id: '1', name: 'Electronics' },
    { id: '2', name: 'Clothing' },
    { id: '3', name: 'Home Goods' }
  ],
  onSearch: (params) => {
    console.log('Searching with:', params);
    // Here you would typically make an API call
  }
});
*/
```
