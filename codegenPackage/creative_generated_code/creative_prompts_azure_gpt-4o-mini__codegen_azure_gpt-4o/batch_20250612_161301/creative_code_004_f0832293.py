"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Construct a React component that showcases the new arrivals in the accessories category from Baazaars, including a filter for price range and product type.
Generated: DETERMINISTIC_f0832293dabe5cf1
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Mock API call to fetch new arrivals
const fetchNewArrivals = async () => {
  // Replace this with an actual API endpoint
  return [
    { id: 1, name: 'Leather Wallet', type: 'Wallet', price: 45 },
    { id: 2, name: 'Silk Scarf', type: 'Scarf', price: 25 },
    { id: 3, name: 'Gold-Tinted Sunglasses', type: 'Sunglasses', price: 120 },
    { id: 4, name: 'Canvas Tote Bag', type: 'Bag', price: 60 },
    { id: 5, name: 'Sterling Silver Bracelet', type: 'Jewelry', price: 80 },
  ];
};

// AccessoriesFilter Component
const AccessoriesFilter = ({ onFilterChange }) => {
  const [priceRange, setPriceRange] = useState([0, 200]);
  const [productType, setProductType] = useState('');

  const handlePriceRangeChange = (event) => {
    const value = event.target.value.split('-').map(Number);
    setPriceRange(value);
    onFilterChange({ priceRange: value, productType });
  };

  const handleProductTypeChange = (event) => {
    const value = event.target.value;
    setProductType(value);
    onFilterChange({ priceRange, productType: value });
  };

  return (
    <div style={{ marginBottom: '20px' }}>
      {/* Price Range Filter */}
      <label htmlFor="price-range">Price Range:</label>
      <select id="price-range" onChange={handlePriceRangeChange}>
        <option value="0-200">All</option>
        <option value="0-50">Below $50</option>
        <option value="50-100">$50 - $100</option>
        <option value="100-200">$100 - $200</option>
      </select>
      {/* Product Type Filter */}
      <label htmlFor="product-type" style={{ marginLeft: '20px' }}>
        Product Type:
      </label>
      <select id="product-type" onChange={handleProductTypeChange}>
        <option value="">All</option>
        <option value="Wallet">Wallet</option>
        <option value="Scarf">Scarf</option>
        <option value="Sunglasses">Sunglasses</option>
        <option value="Bag">Bag</option>
        <option value="Jewelry">Jewelry</option>
      </select>
    </div>
  );
};

AccessoriesFilter.propTypes = {
  onFilterChange: PropTypes.func.isRequired,
};

// NewArrivals Component
const NewArrivals = () => {
  const [newArrivals, setNewArrivals] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [filters, setFilters] = useState({ priceRange: [0, 200], productType: '' });

  useEffect(() => {
    // Fetch new arrivals on initial load
    const loadNewArrivals = async () => {
      try {
        const products = await fetchNewArrivals();
        setNewArrivals(products);
        setFilteredProducts(products);
      } catch (error) {
        console.error('Error fetching new arrivals:', error);
      }
    };

    loadNewArrivals();
  }, []);

  useEffect(() => {
    // Apply filters when they change
    const { priceRange, productType } = filters;
    const filtered = newArrivals.filter((product) => {
      const matchesPrice =
        product.price >= priceRange[0] && product.price <= priceRange[1];
      const matchesType = productType ? product.type === productType : true;
      return matchesPrice && matchesType;
    });
    setFilteredProducts(filtered);
  }, [filters, newArrivals]);

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>New Arrivals - Accessories</h1>
      {/* Filter Component */}
      <AccessoriesFilter onFilterChange={handleFilterChange} />
      {/* Product Display */}
      <div>
        {filteredProducts.length > 0 ? (
          filteredProducts.map((product) => (
            <div
              key={product.id}
              style={{
                border: '1px solid #ccc',
                padding: '10px',
                marginBottom: '10px',
              }}
            >
              <h3>{product.name}</h3>
              <p>Type: {product.type}</p>
              <p>Price: ${product.price}</p>
            </div>
          ))
        ) : (
          <p>No products match the selected filters.</p>
        )}
      </div>
    </div>
  );
};

export default NewArrivals;
```
