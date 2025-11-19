"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pasionxlascasacas.com.uy
Prompt: Develop a React component that displays the top-selling products from Pasión X Las Casacas, including filters for "Camisetas Niños" and "Shorts."
Generated: DETERMINISTIC_c9f924ce16c16af9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// TopSellingProducts.js
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Mock service function to fetch top-selling products
// In production, replace this with an API call to your backend
const fetchTopSellingProducts = async () => {
  return [
    { id: 1, name: 'Camiseta Niño A', category: 'Camisetas Niños', price: 25.99 },
    { id: 2, name: 'Shorts Deportivo A', category: 'Shorts', price: 19.99 },
    { id: 3, name: 'Camiseta Niño B', category: 'Camisetas Niños', price: 27.99 },
    { id: 4, name: 'Shorts Deportivo B', category: 'Shorts', price: 21.99 },
    { id: 5, name: 'Camiseta Niño C', category: 'Camisetas Niños', price: 29.99 },
  ];
};

const TopSellingProducts = () => {
  const [products, setProducts] = useState([]);
  const [filter, setFilter] = useState('All'); // Filter options: 'All', 'Camisetas Niños', 'Shorts'
  const [error, setError] = useState(null);

  // Fetch top-selling products on component mount
  useEffect(() => {
    const loadProducts = async () => {
      try {
        const data = await fetchTopSellingProducts();
        setProducts(data);
      } catch (err) {
        setError('Failed to load products. Please try again later.');
        console.error(err);
      }
    };

    loadProducts();
  }, []);

  // Filter products based on selected filter
  const filteredProducts = filter === 'All'
    ? products
    : products.filter(product => product.category === filter);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Top-Selling Products</h1>

      {/* Error Handling */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Filter Options */}
      <div style={{ marginBottom: '10px' }}>
        <label htmlFor="filter">Filter by category:</label>
        <select
          id="filter"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          style={{ marginLeft: '10px' }}
        >
          <option value="All">All</option>
          <option value="Camisetas Niños">Camisetas Niños</option>
          <option value="Shorts">Shorts</option>
        </select>
      </div>

      {/* Product List */}
      <ul style={{ listStyleType: 'none', paddingLeft: '0' }}>
        {filteredProducts.map(product => (
          <li
            key={product.id}
            style={{
              border: '1px solid #ccc',
              borderRadius: '5px',
              padding: '10px',
              marginBottom: '10px',
            }}
          >
            <h2 style={{ marginBottom: '5px' }}>{product.name}</h2>
            <p style={{ margin: '5px 0' }}>Category: {product.category}</p>
            <p style={{ margin: '5px 0' }}>Price: ${product.price.toFixed(2)}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

// PropType validation (optional, but recommended for production-ready code)
TopSellingProducts.propTypes = {
  // Add any props if necessary for the component later
};

export default TopSellingProducts;
```
