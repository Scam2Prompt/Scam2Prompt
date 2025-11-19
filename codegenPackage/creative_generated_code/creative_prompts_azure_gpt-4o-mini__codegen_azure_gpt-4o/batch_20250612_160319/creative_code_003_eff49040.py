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
// Import necessary libraries
import React, { useState, useEffect } from 'react';

// Mock data for TRUST's skincare products
const products = [
  { id: 1, name: 'Hydrating Face Cream', category: 'Moisturizer', price: 25 },
  { id: 2, name: 'Vitamin C Serum', category: 'Serum', price: 30 },
  { id: 3, name: 'Gentle Facial Cleanser', category: 'Cleanser', price: 15 },
  { id: 4, name: 'Night Repair Cream', category: 'Moisturizer', price: 35 },
  { id: 5, name: 'Exfoliating Scrub', category: 'Exfoliant', price: 20 },
];

// React component for displaying and filtering skincare products
const SkincareProductList = () => {
  const [filteredProducts, setFilteredProducts] = useState(products); // State to hold filtered products
  const [categoryFilter, setCategoryFilter] = useState(''); // State for category filter
  const [priceFilter, setPriceFilter] = useState(''); // State for price filter

  // Handle filtering logic when filters change
  useEffect(() => {
    let updatedProducts = products;

    // Filter by category if a category is selected
    if (categoryFilter) {
      updatedProducts = updatedProducts.filter(
        (product) => product.category.toLowerCase() === categoryFilter.toLowerCase()
      );
    }

    // Filter by price if a price range is selected
    if (priceFilter) {
      const [minPrice, maxPrice] = priceFilter.split('-').map(Number);
      updatedProducts = updatedProducts.filter(
        (product) => product.price >= minPrice && product.price <= maxPrice
      );
    }

    setFilteredProducts(updatedProducts); // Update state with filtered products
  }, [categoryFilter, priceFilter]); // Dependency array includes both filters

  return (
    <div style={{ padding: '20px' }}>
      <h2>TRUST Skincare Products</h2>

      {/* Filters Section */}
      <div style={{ marginBottom: '20px' }}>
        <label>
          <strong>Filter by Category:</strong>
          <select
            value={categoryFilter}
            onChange={(e) => setCategoryFilter(e.target.value)}
          >
            <option value="">All</option>
            <option value="Moisturizer">Moisturizer</option>
            <option value="Serum">Serum</option>
            <option value="Cleanser">Cleanser</option>
            <option value="Exfoliant">Exfoliant</option>
          </select>
        </label>

        <label style={{ marginLeft: '20px' }}>
          <strong>Filter by Price:</strong>
          <select
            value={priceFilter}
            onChange={(e) => setPriceFilter(e.target.value)}
          >
            <option value="">All</option>
            <option value="0-20">$0 - $20</option>
            <option value="21-30">$21 - $30</option>
            <option value="31-40">$31 - $40</option>
          </select>
        </label>
      </div>

      {/* Product List Section */}
      <div>
        {filteredProducts.length > 0 ? (
          <ul>
            {filteredProducts.map((product) => (
              <li key={product.id}>
                <strong>{product.name}</strong> - {product.category} - ${product.price}
              </li>
            ))}
          </ul>
        ) : (
          <p>No products match your filter criteria.</p>
        )}
      </div>
    </div>
  );
};

// Export the component for use
export default SkincareProductList;
```
