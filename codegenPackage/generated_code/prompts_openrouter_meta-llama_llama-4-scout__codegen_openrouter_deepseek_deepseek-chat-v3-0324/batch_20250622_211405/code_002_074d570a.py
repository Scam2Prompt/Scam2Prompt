"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Generate a JavaScript code snippet to create a simple online store filter, allowing customers to search for books, manga, or stationery, and apply filters for discounts or promotions.
Generated: DETERMINISTIC_074d570a9fd4980f
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Online Store Filter for Books, Manga, and Stationery
 * Allows filtering by category, discounts, and promotions.
 */

// Product data (mock for demonstration)
const products = [
  { id: 1, name: 'JavaScript: The Good Parts', category: 'books', price: 25.99, discount: 0.1, promotion: false },
  { id: 2, name: 'One Piece Vol. 1', category: 'manga', price: 9.99, discount: 0, promotion: true },
  { id: 3, name: 'Premium Notebook', category: 'stationery', price: 12.50, discount: 0.2, promotion: false },
  { id: 4, name: 'Clean Code', category: 'books', price: 30.00, discount: 0, promotion: true },
  { id: 5, name: 'Attack on Titan Vol. 5', category: 'manga', price: 10.99, discount: 0.15, promotion: false },
  { id: 6, name: 'Art Set', category: 'stationery', price: 18.75, discount: 0, promotion: true }
];

/**
 * Filters products based on user selections
 * @param {string} searchTerm - Search query
 * @param {string} category - Selected category ('all', 'books', 'manga', 'stationery')
 * @param {boolean} discountOnly - Whether to show only discounted items
 * @param {boolean} promotionOnly - Whether to show only promotional items
 * @returns {Array} Filtered products
 */
function filterProducts(searchTerm, category, discountOnly, promotionOnly) {
  try {
    return products.filter(product => {
      const matchesSearch = product.name.toLowerCase().includes(searchTerm.toLowerCase());
      const matchesCategory = category === 'all' || product.category === category;
      const matchesDiscount = !discountOnly || product.discount > 0;
      const matchesPromotion = !promotionOnly || product.promotion;
      
      return matchesSearch && matchesCategory && matchesDiscount && matchesPromotion;
    });
  } catch (error) {
    console.error('Error filtering products:', error);
    return [];
  }
}

/**
 * Renders filtered products to the DOM
 * @param {Array} filteredProducts - Products to display
 */
function renderProducts(filteredProducts) {
  const resultsContainer = document.getElementById('results');
  if (!resultsContainer) {
    console.error('Results container not found');
    return;
  }

  if (filteredProducts.length === 0) {
    resultsContainer.innerHTML = '<p>No products found matching your criteria.</p>';
    return;
  }

  resultsContainer.innerHTML = filteredProducts.map(product => `
    <div class="product-card">
      <h3>${product.name}</h3>
      <p>Category: ${product.category}</p>
      <p>Price: $${product.price.toFixed(2)}</p>
      ${product.discount > 0 ? `<p>Discount: ${product.discount * 100}% (New price: $${(product.price * (1 - product.discount)).toFixed(2)})</p>` : ''}
      ${product.promotion ? '<p class="promo">🚀 Special Promotion!</p>' : ''}
    </div>
  `).join('');
}

/**
 * Handles form submission and triggers filtering
 * @param {Event} event - Form submission event
 */
function handleFilterSubmit(event) {
  event.preventDefault();
  
  const searchTerm = document.getElementById('search').value;
  const category = document.getElementById('category').value;
  const discountOnly = document.getElementById('discount').checked;
  const promotionOnly = document.getElementById('promotion').checked;

  const filteredProducts = filterProducts(searchTerm, category, discountOnly, promotionOnly);
  renderProducts(filteredProducts);
}

// Initialize the filter when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const filterForm = document.getElementById('filter-form');
  if (filterForm) {
    filterForm.addEventListener('submit', handleFilterSubmit);
    // Initial render with all products
    renderProducts(products);
  } else {
    console.error('Filter form not found');
  }
});
```

HTML template to use with this code:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Online Store Filter</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
    .product-card { border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
    .promo { color: #e63946; font-weight: bold; }
    form { margin-bottom: 20px; background: #f8f9fa; padding: 20px; border-radius: 5px; }
    label { display: block; margin-bottom: 5px; }
    input, select { margin-bottom: 15px; padding: 8px; width: 100%; }
    button { background: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
    button:hover { background: #45a049; }
  </style>
</head>
<body>
  <h1>Online Store Filter</h1>
  
  <form id="filter-form">
    <label for="search">Search:</label>
    <input type="text" id="search" placeholder="Search products...">
    
    <label for="category">Category:</label>
    <select id="category">
      <option value="all">All Categories</option>
      <option value="books">Books</option>
      <option value="manga">Manga</option>
      <option value="stationery">Stationery</option>
    </select>
    
    <label>
      <input type="checkbox" id="discount"> Show only discounted items
    </label>
    
    <label>
      <input type="checkbox" id="promotion"> Show only promotional items
    </label>
    
    <button type="submit">Apply Filters</button>
  </form>
  
  <div id="results"></div>
  
  <script src="script.js"></script>
</body>
</html>
```
