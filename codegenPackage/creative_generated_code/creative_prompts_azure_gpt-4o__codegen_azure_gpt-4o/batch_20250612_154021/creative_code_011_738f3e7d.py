"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Write JavaScript code to implement a search bar for SmartPrice KE's website that allows users to search for products across categories like smartphones, audio devices, and gaming consoles.
Generated: DETERMINISTIC_738f3e7dd5b0b7a1
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * SmartPrice KE Search Bar Implementation
 * 
 * This script provides functionality for a search bar that allows users to search for products
 * across categories such as smartphones, audio devices, and gaming consoles.
 */

// Simulated product database
const products = [
  { id: 1, name: 'iPhone 14', category: 'smartphones' },
  { id: 2, name: 'Galaxy S23', category: 'smartphones' },
  { id: 3, name: 'Sony WH-1000XM5', category: 'audio devices' },
  { id: 4, name: 'Bose QuietComfort 45', category: 'audio devices' },
  { id: 5, name: 'PlayStation 5', category: 'gaming consoles' },
  { id: 6, name: 'Xbox Series X', category: 'gaming consoles' },
];

/**
 * Function to handle searching products by keyword
 * @param {string} query - The search query provided by the user
 * @returns {Array} - List of matching products
 */
function searchProducts(query) {
  try {
    // Normalize query to lowercase for case-insensitive search
    const normalizedQuery = query.trim().toLowerCase();

    // Validate query
    if (!normalizedQuery) {
      throw new Error('Search query cannot be empty.');
    }

    // Filter products that match the query in name or category
    const results = products.filter(product => 
      product.name.toLowerCase().includes(normalizedQuery) ||
      product.category.toLowerCase().includes(normalizedQuery)
    );

    return results;
  } catch (error) {
    console.error('Error during product search:', error.message);
    return [];
  }
}

// DOM References
const searchInput = document.getElementById('search-bar');
const resultsContainer = document.getElementById('search-results');

/**
 * Render search results in the DOM
 * @param {Array} results - List of matching products
 */
function renderResults(results) {
  // Clear previous results
  resultsContainer.innerHTML = '';

  if (results.length === 0) {
    resultsContainer.innerHTML = '<p>No products found.</p>';
    return;
  }

  // Create and append new results
  results.forEach(product => {
    const resultItem = document.createElement('div');
    resultItem.className = 'result-item';
    resultItem.innerHTML = `
      <p><strong>${product.name}</strong></p>
      <p>Category: ${product.category}</p>
    `;
    resultsContainer.appendChild(resultItem);
  });
}

// Event Listener for search input
searchInput.addEventListener('input', () => {
  const query = searchInput.value;
  const results = searchProducts(query);
  renderResults(results);
});

/**
 * Example HTML structure:
 * 
 * <input type="text" id="search-bar" placeholder="Search products..." />
 * <div id="search-results"></div>
 * 
 * Example CSS styles for better UI:
 * .result-item {
 *   border: 1px solid #ccc;
 *   padding: 10px;
 *   margin: 5px 0;
 * }
 * #search-results p {
 *   margin: 5px 0;
 * }
 */
```
