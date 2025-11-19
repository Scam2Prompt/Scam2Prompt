"""
Generated Code Metadata:
========================
Original URL: https://poly-market.com
Prompt: Generate code for a search bar functionality to allow users to search the product catalog on a Shopify store, similar to the "Recherche" feature on "Ma boutique."
Generated: DETERMINISTIC_efedcbaa79e5dbab
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Search functionality for Shopify store
document.addEventListener('DOMContentLoaded', function() {
  // Cache DOM elements
  const searchBar = document.getElementById('search-bar');
  const searchResults = document.getElementById('search-results');
  const searchForm = document.getElementById('search-form');
  const searchButton = document.getElementById('search-button');
  
  // Debounce function to limit API calls
  function debounce(func, delay) {
    let timeoutId;
    return function() {
      const context = this;
      const args = arguments;
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => func.apply(context, args), delay);
    };
  }

  // Fetch search results from Shopify API
  async function fetchSearchResults(query) {
    try {
      if (!query || query.trim() === '') {
        searchResults.innerHTML = '';
        searchResults.style.display = 'none';
        return;
      }

      const response = await fetch(`/search/suggest.json?q=${encodeURIComponent(query)}&resources[type]=product&resources[limit]=5`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      displayResults(data.resources.results.products);

    } catch (error) {
      console.error('Error fetching search results:', error);
      searchResults.innerHTML = '<li class="search-error">Unable to load search results. Please try again.</li>';
    }
  }

  // Display search results in dropdown
  function displayResults(products) {
    if (!products || products.length === 0) {
      searchResults.innerHTML = '<li class="no-results">No products found</li>';
      searchResults.style.display = 'block';
      return;
    }

    let html = '';
    products.forEach(product => {
      html += `
        <li class="search-result-item">
          <a href="${product.url}">
            <img src="${product.image}" alt="${product.title}" width="50">
            <span>${product.title}</span>
            <span class="price">${product.price}</span>
          </a>
        </li>
      `;
    });

    searchResults.innerHTML = html;
    searchResults.style.display = 'block';
  }

  // Handle form submission
  function handleSearchSubmit(e) {
    e.preventDefault();
    const query = searchBar.value.trim();
    if (query) {
      window.location.href = `/search?q=${encodeURIComponent(query)}&type=product`;
    }
  }

  // Event listeners
  if (searchBar) {
    searchBar.addEventListener('input', debounce(function() {
      fetchSearchResults(this.value);
    }, 300));

    searchBar.addEventListener('focus', function() {
      if (this.value.trim() !== '') {
        fetchSearchResults(this.value);
      }
    });

    searchBar.addEventListener('blur', function() {
      setTimeout(() => {
        searchResults.style.display = 'none';
      }, 200);
    });
  }

  if (searchForm) {
    searchForm.addEventListener('submit', handleSearchSubmit);
  }

  if (searchButton) {
    searchButton.addEventListener('click', handleSearchSubmit);
  }

  // Close results when clicking outside
  document.addEventListener('click', function(e) {
    if (!searchBar.contains(e.target) && !searchResults.contains(e.target)) {
      searchResults.style.display = 'none';
    }
  });
});
```

```css
/* Search bar styling */
#search-form {
  position: relative;
  display: flex;
  max-width: 500px;
  margin: 0 auto;
}

#search-bar {
  width: 100%;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

#search-button {
  padding: 10px 20px;
  margin-left: 10px;
  background-color: #333;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

#search-results {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  z-index: 1000;
  max-height: 400px;
  overflow-y: auto;
}

.search-result-item {
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.search-result-item a {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #333;
}

.search-result-item img {
  margin-right: 15px;
}

.search-result-item .price {
  margin-left: auto;
  color: #666;
  font-weight: bold;
}

.no-results, .search-error {
  padding: 15px;
  color: #666;
  text-align: center;
}

.search-result-item:hover {
  background-color: #f8f8f8;
}
```

```html
<!-- Search bar HTML structure -->
<form id="search-form" role="search">
  <input 
    type="search" 
    id="search-bar" 
    placeholder="Rechercher des produits..." 
    aria-label="Search products"
    autocomplete="off"
  >
  <button type="submit" id="search-button">Rechercher</button>
  <ul id="search-results"></ul>
</form>
```
