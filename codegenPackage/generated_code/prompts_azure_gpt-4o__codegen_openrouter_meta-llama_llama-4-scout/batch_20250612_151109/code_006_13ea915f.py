"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write a React component to display a furniture product catalog, including items like "Bicama Siena" and "Estofado Desejos 3x2 lugares," with options to sort by price and category.
Generated: DETERMINISTIC_13ea915fb60e76a4
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// FurnitureProductCatalog.js
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * Furniture product catalog component.
 *
 * @param {Object} props - Component props.
 * @param {Array} props.products - List of furniture products.
 */
function FurnitureProductCatalog({ products }) {
  // State to store sorted products
  const [sortedProducts, setSortedProducts] = useState(products);
  const [sortOption, setSortOption] = useState('price-asc');
  const [categoryFilter, setCategoryFilter] = useState('');

  // Update sorted products when products or sort option change
  useEffect(() => {
    let sorted = [...products];

    // Filter by category if selected
    if (categoryFilter) {
      sorted = sorted.filter(product => product.category === categoryFilter);
    }

    // Sort products based on selected option
    switch (sortOption) {
      case 'price-asc':
        sorted.sort((a, b) => a.price - b.price);
        break;
      case 'price-desc':
        sorted.sort((a, b) => b.price - a.price);
        break;
      case 'category-asc':
        sorted.sort((a, b) => a.category.localeCompare(b.category));
        break;
      default:
        break;
    }

    setSortedProducts(sorted);
  }, [products, sortOption, categoryFilter]);

  // Handle sort option change
  const handleSortChange = event => {
    setSortOption(event.target.value);
  };

  // Handle category filter change
  const handleCategoryFilterChange = event => {
    setCategoryFilter(event.target.value);
  };

  // Handle product removal (example)
  const handleProductRemove = productId => {
    // Implement product removal logic here (e.g., API call)
    console.log(`Product ${productId} removed`);
  };

  return (
    <div className="furniture-product-catalog">
      <h2>Furniture Product Catalog</h2>

      {/* Sorting and filtering options */}
      <div className="sorting-options">
        <label>
          Sort by:
          <select value={sortOption} onChange={handleSortChange}>
            <option value="price-asc">Price (asc)</option>
            <option value="price-desc">Price (desc)</option>
            <option value="category-asc">Category (asc)</option>
          </select>
        </label>

        <label>
          Filter by category:
          <select value={categoryFilter} onChange={handleCategoryFilterChange}>
            <option value="">All categories</option>
            {[...new Set(products.map(product => product.category))].map(category => (
              <option key={category} value={category}>
                {category}
              </option>
            ))}
          </select>
        </label>
      </div>

      {/* Product list */}
      <ul className="product-list">
        {sortedProducts.map(product => (
          <li key={product.id}>
            <h3>{product.name}</h3>
            <p>Category: {product.category}</p>
            <p>Price: ${product.price.toFixed(2)}</p>
            <button onClick={() => handleProductRemove(product.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

FurnitureProductCatalog.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      category: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    }),
  ).isRequired,
};

// Example usage
const products = [
  { id: 1, name: 'Bicama Siena', category: 'Bedroom', price: 499.99 },
  { id: 2, name: 'Estofado Desejos 3x2 lugares', category: 'Living Room', price: 799.99 },
  { id: 3, name: 'Sofa Modern', category: 'Living Room', price: 599.99 },
  { id: 4, name: 'Dresser Deluxe', category: 'Bedroom', price: 299.99 },
];

function App() {
  return (
    <div className="App">
      <FurnitureProductCatalog products={products} />
    </div>
  );
}

export default App;
```
