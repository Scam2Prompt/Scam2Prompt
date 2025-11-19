"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aquatic-green.ir
Prompt: Develop a React component that lists TRUST's skincare products, allowing users to filter by category and price.
Generated: DETERMINISTIC_eff4904002ddf4b2
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './ProductList.css'; // Assuming you have a CSS file for styling

// Mock data representing TRUST's skincare products
const mockProducts = [
  { id: 1, name: 'Moisturizer', category: 'Hydration', price: 25.00 },
  { id: 2, name: 'Sunscreen', category: 'Protection', price: 20.00 },
  { id: 3, name: 'Cleanser', category: 'Cleansing', price: 15.00 },
  { id: 4, name: 'Toner', category: 'Hydration', price: 18.00 },
  { id: 5, name: 'Exfoliator', category: 'Cleansing', price: 22.00 },
];

// ProductList component to list and filter skincare products
const ProductList = () => {
  const [products, setProducts] = useState(mockProducts);
  const [filteredProducts, setFilteredProducts] = useState(mockProducts);
  const [categoryFilter, setCategoryFilter] = useState('');
  const [priceFilter, setPriceFilter] = useState('');

  // Effect to filter products based on selected filters
  useEffect(() => {
    let filtered = products;

    // Filter by category if a category is selected
    if (categoryFilter) {
      filtered = filtered.filter(product => product.category === categoryFilter);
    }

    // Filter by price if a price is entered
    if (priceFilter) {
      const priceLimit = parseFloat(priceFilter);
      if (!isNaN(priceLimit)) {
        filtered = filtered.filter(product => product.price <= priceLimit);
      }
    }

    setFilteredProducts(filtered);
  }, [categoryFilter, priceFilter, products]);

  // Handle category filter change
  const handleCategoryChange = (event) => {
    setCategoryFilter(event.target.value);
  };

  // Handle price filter change
  const handlePriceChange = (event) => {
    setPriceFilter(event.target.value);
  };

  return (
    <div className="product-list">
      <h2>TRUST Skincare Products</h2>
      
      <div className="filters">
        <select onChange={handleCategoryChange} value={categoryFilter}>
          <option value="">All Categories</option>
          <option value="Hydration">Hydration</option>
          <option value="Protection">Protection</option>
          <option value="Cleansing">Cleansing</option>
        </select>
        
        <input
          type="number"
          placeholder="Max Price"
          value={priceFilter}
          onChange={handlePriceChange}
        />
      </div>

      <ul>
        {filteredProducts.length > 0 ? (
          filteredProducts.map(product => (
            <li key={product.id}>
              <strong>{product.name}</strong> - ${product.price.toFixed(2)} ({product.category})
            </li>
          ))
        ) : (
          <li>No products found.</li>
        )}
      </ul>
    </div>
  );
};

// Prop types for type checking
ProductList.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      category: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    })
  ),
};

// Default export of the component
export default ProductList;
```
