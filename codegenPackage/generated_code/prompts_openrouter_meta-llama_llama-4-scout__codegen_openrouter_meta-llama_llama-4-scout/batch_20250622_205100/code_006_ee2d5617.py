"""
Generated Code Metadata:
========================
Original URL: https://missguilty.co.uk
Prompt: "Write a JavaScript function to implement a search bar feature on an e-commerce website like Miss Guilty's, allowing users to find products like the Pale Pink Ruffle Halter Crop Top & Shorts Co-ord Set."
Generated: DETERMINISTIC_ee2d56179ca83f90
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * SearchBar class to handle product search functionality.
 */
class SearchBar {
  /**
   * Constructor to initialize the search bar with products.
   * @param {Array} products - List of products to search through.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Function to filter products based on search query.
   * @param {string} query - Search query to filter products.
   * @returns {Array} Filtered list of products.
   */
  searchProducts(query) {
    try {
      // Check if query is a string and not empty
      if (typeof query !== 'string' || query.trim() === '') {
        throw new Error('Invalid search query');
      }

      // Convert query to lowercase for case-insensitive search
      const lowerCaseQuery = query.toLowerCase();

      // Filter products based on search query
      const filteredProducts = this.products.filter((product) => {
        // Check if product name or description contains the search query
        return product.name.toLowerCase().includes(lowerCaseQuery) ||
               (product.description && product.description.toLowerCase().includes(lowerCaseQuery));
      });

      return filteredProducts;
    } catch (error) {
      console.error('Error searching products:', error.message);
      return [];
    }
  }
}

// Example usage
const products = [
  {
    id: 1,
    name: 'Pale Pink Ruffle Halter Crop Top & Shorts Co-ord Set',
    description: 'A cute co-ord set with ruffle details',
  },
  {
    id: 2,
    name: 'Black Graphic T-Shirt',
    description: 'A basic black graphic t-shirt',
  },
  {
    id: 3,
    name: 'White Linen Pants',
    description: 'A pair of white linen pants',
  },
];

const searchBar = new SearchBar(products);

// Test search function
const searchQuery = 'Pale Pink';
const results = searchBar.searchProducts(searchQuery);
console.log(`Search results for "${searchQuery}":`, results);

// Test invalid search query
const invalidQuery = '';
const invalidResults = searchBar.searchProducts(invalidQuery);
console.log(`Search results for invalid query "${invalidQuery}":`, invalidResults);
```
