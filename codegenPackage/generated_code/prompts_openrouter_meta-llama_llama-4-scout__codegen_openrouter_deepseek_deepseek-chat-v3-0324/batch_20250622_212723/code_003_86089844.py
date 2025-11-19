"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Create a JavaScript code snippet to implement a search bar on an e-commerce website, allowing users to find products like "Milly Mally Scooter" or "Qplay Rowerek Trójkołowy".
Generated: DETERMINISTIC_860898444c69241f
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * SearchBar Component for E-commerce Website
 * 
 * Features:
 * - Debounced search to optimize performance
 * - Case-insensitive search
 * - Highlights matching text in results
 * - Handles empty search queries
 * - Error handling for API failures
 */

class SearchBar {
  constructor(options) {
    this.searchInput = document.querySelector(options.searchInputSelector);
    this.resultsContainer = document.querySelector(options.resultsContainerSelector);
    this.endpoint = options.endpoint;
    this.minQueryLength = options.minQueryLength || 2;
    this.debounceDelay = options.debounceDelay || 300;
    this.currentRequest = null;
    this.products = [];

    this.init();
  }

  init() {
    this.setupEventListeners();
  }

  setupEventListeners() {
    this.searchInput.addEventListener('input', this.debounce(() => {
      this.handleSearch();
    }, this.debounceDelay));

    document.addEventListener('click', (e) => {
      if (!this.resultsContainer.contains(e.target) && e.target !== this.searchInput) {
        this.clearResults();
      }
    });
  }

  debounce(func, delay) {
    let timeoutId;
    return (...args) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        func.apply(this, args);
      }, delay);
    };
  }

  async handleSearch() {
    const query = this.searchInput.value.trim();
    
    if (query.length < this.minQueryLength) {
      this.clearResults();
      return;
    }

    try {
      this.products = await this.fetchProducts(query);
      this.displayResults(this.products, query);
    } catch (error) {
      console.error('Search failed:', error);
      this.displayError();
    }
  }

  async fetchProducts(query) {
    if (this.currentRequest) {
      this.currentRequest.abort();
    }

    const controller = new AbortController();
    this.currentRequest = controller;

    try {
      const response = await fetch(`${this.endpoint}?q=${encodeURIComponent(query)}`, {
        signal: controller.signal
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } finally {
      this.currentRequest = null;
    }
  }

  displayResults(products, query) {
    this.clearResults();

    if (!products || products.length === 0) {
      this.resultsContainer.innerHTML = '<div class="search-no-results">No products found</div>';
      return;
    }

    const regex = new RegExp(query, 'gi');
    const fragment = document.createDocumentFragment();

    products.forEach(product => {
      const item = document.createElement('div');
      item.className = 'search-result-item';
      
      const highlightedName = product.name.replace(regex, match => 
        `<span class="search-highlight">${match}</span>`
      );
      
      item.innerHTML = `
        <div class="search-result-name">${highlightedName}</div>
        <div class="search-result-price">$${product.price.toFixed(2)}</div>
      `;
      
      item.addEventListener('click', () => {
        window.location.href = product.url;
      });

      fragment.appendChild(item);
    });

    this.resultsContainer.appendChild(fragment);
    this.resultsContainer.style.display = 'block';
  }

  displayError() {
    this.clearResults();
    this.resultsContainer.innerHTML = `
      <div class="search-error">
        Failed to load search results. Please try again later.
      </div>
    `;
    this.resultsContainer.style.display = 'block';
  }

  clearResults() {
    this.resultsContainer.innerHTML = '';
    this.resultsContainer.style.display = 'none';
  }
}

// Example usage:
// const searchBar = new SearchBar({
//   searchInputSelector: '#search-input',
//   resultsContainerSelector: '#search-results',
//   endpoint: '/api/search',
//   minQueryLength: 2,
//   debounceDelay: 300
// });
```
