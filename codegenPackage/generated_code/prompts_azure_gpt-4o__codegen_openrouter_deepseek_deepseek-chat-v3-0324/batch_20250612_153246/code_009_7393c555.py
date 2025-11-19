"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Write a JavaScript script to implement a search bar with autocomplete functionality for furniture collections, similar to the search feature described on Nodo Italia's website.
Generated: DETERMINISTIC_7393c555b6640f13
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
 * SearchBar with Autocomplete for Furniture Collections
 * 
 * Features:
 * - Debounced input handling
 * - Autocomplete suggestions
 * - Keyboard navigation
 * - Mobile responsive
 * - Accessibility compliant
 */

class FurnitureSearch {
  constructor(options) {
    // Configuration with defaults
    this.config = {
      searchInput: '#search-input',
      suggestionsContainer: '#suggestions-container',
      debounceTime: 300,
      minChars: 2,
      apiEndpoint: '/api/search',
      ...options
    };

    // DOM elements
    this.searchInput = document.querySelector(this.config.searchInput);
    this.suggestionsContainer = document.querySelector(this.config.config.suggestionsContainer);

    // State
    this.suggestions = [];
    this.selectedIndex = -1;
    this.isFetching = false;
    this.abortController = null;

    // Initialize
    this.init();
  }

  init() {
    if (!this.searchInput || !this.suggestionsContainer) {
      console.error('Search input or suggestions container not found');
      return;
    }

    this.setupEventListeners();
  }

  setupEventListeners() {
    // Debounced input handler
    const debouncedInput = this.debounce(() => this.handleInput(), this.config.debounceTime);
    this.searchInput.addEventListener('input', debouncedInput);

    // Keyboard navigation
    this.searchInput.addEventListener('keydown', (e) => this.handleKeyDown(e));

    // Click outside to close suggestions
    document.addEventListener('click', (e) => {
      if (!this.suggestionsContainer.contains(e.target) && e.target !== this.searchInput) {
        this.clearSuggestions();
      }
    });

    // Handle suggestion clicks
    this.suggestionsContainer.addEventListener('click', (e) => {
      const suggestionItem = e.target.closest('.suggestion-item');
      if (suggestionItem) {
        this.selectSuggestion(parseInt(suggestionItem.dataset.index));
      }
    });
  }

  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }

  async handleInput() {
    const query = this.searchInput.value.trim();
    
    if (query.length < this.config.minChars) {
      this.clearSuggestions();
      return;
    }

    this.showLoadingState();
    await this.fetchSuggestions(query);
  }

  async fetchSuggestions(query) {
    // Cancel previous request if it exists
    if (this.abortController) {
      this.abortController.abort();
    }

    this.abortController = new AbortController();
    this.isFetching = true;

    try {
      const response = await fetch(`${this.config.apiEndpoint}?q=${encodeURIComponent(query)}`, {
        signal: this.abortController.signal
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      this.suggestions = data.suggestions || [];
      this.renderSuggestions();
    } catch (error) {
      if (error.name !== 'AbortError') {
        console.error('Error fetching suggestions:', error);
        this.showErrorState();
      }
    } finally {
      this.isFetching = false;
      this.abortController = null;
    }
  }

  renderSuggestions() {
    if (this.suggestions.length === 0) {
      this.suggestionsContainer.innerHTML = '<div class="no-results">No matching furniture found</div>';
      return;
    }

    const fragment = document.createDocumentFragment();
    
    this.suggestions.forEach((suggestion, index) => {
      const suggestionElement = document.createElement('div');
      suggestionElement.className = `suggestion-item ${index === this.selectedIndex ? 'selected' : ''}`;
      suggestionElement.dataset.index = index;
      
      suggestionElement.innerHTML = `
        <div class="suggestion-name">${this.highlightMatch(suggestion.name, this.searchInput.value)}</div>
        ${suggestion.category ? `<div class="suggestion-category">${suggestion.category}</div>` : ''}
      `;
      
      fragment.appendChild(suggestionElement);
    });

    this.suggestionsContainer.innerHTML = '';
    this.suggestionsContainer.appendChild(fragment);
    this.suggestionsContainer.style.display = 'block';
  }

  highlightMatch(text, query) {
    if (!query) return text;
    
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<span class="highlight">$1</span>');
  }

  handleKeyDown(e) {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        this.navigateSuggestions(1);
        break;
      case 'ArrowUp':
        e.preventDefault();
        this.navigateSuggestions(-1);
        break;
      case 'Enter':
        if (this.selectedIndex >= 0) {
          e.preventDefault();
          this.selectSuggestion(this.selectedIndex);
        }
        break;
      case 'Escape':
        this.clearSuggestions();
        break;
    }
  }

  navigateSuggestions(direction) {
    if (this.suggestions.length === 0) return;

    const newIndex = this.selectedIndex + direction;
    
    if (newIndex >= 0 && newIndex < this.suggestions.length) {
      this.selectedIndex = newIndex;
      this.renderSuggestions();
      this.scrollToSelected();
    }
  }

  scrollToSelected() {
    const selectedElement = this.suggestionsContainer.querySelector('.selected');
    if (selectedElement) {
      selectedElement.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest'
      });
    }
  }

  selectSuggestion(index) {
    const selectedSuggestion = this.suggestions[index];
    if (!selectedSuggestion) return;

    this.searchInput.value = selectedSuggestion.name;
    this.clearSuggestions();
    
    // Trigger search or navigation
    this.performSearch(selectedSuggestion);
  }

  performSearch(suggestion) {
    // Implement actual search/navigation logic here
    console.log('Searching for:', suggestion);
    // window.location.href = `/products/${suggestion.id}`;
  }

  showLoadingState() {
    this.suggestionsContainer.innerHTML = '<div class="loading-state">Searching...</div>';
    this.suggestionsContainer.style.display = 'block';
  }

  showErrorState() {
    this.suggestionsContainer.innerHTML = '<div class="error-state">Failed to load suggestions</div>';
    this.suggestionsContainer.style.display = 'block';
  }

  clearSuggestions() {
    this.suggestions = [];
    this.selectedIndex = -1;
    this.suggestionsContainer.innerHTML = '';
    this.suggestionsContainer.style.display = 'none';
  }
}

// Initialize the search when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const furnitureSearch = new FurnitureSearch({
    searchInput: '#furniture-search',
    suggestionsContainer: '#search-suggestions',
    apiEndpoint: '/api/furniture/search'
  });
});

// CSS should be added separately, but here's a minimal version for reference:
/*
#search-suggestions {
  display: none;
  position: absolute;
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  background: white;
  border: 1px solid #ddd;
  border-top: none;
  z-index: 1000;
}

.suggestion-item {
  padding: 10px;
  cursor: pointer;
}

.suggestion-item:hover, .suggestion-item.selected {
  background-color: #f5f5f5;
}

.suggestion-name {
  font-weight: bold;
}

.suggestion-category {
  font-size: 0.8em;
  color: #666;
}

.highlight {
  background-color: #fff8e1;
  font-weight: bold;
}

.loading-state, .no-results, .error-state {
  padding: 10px;
  color: #666;
}
*/
```
