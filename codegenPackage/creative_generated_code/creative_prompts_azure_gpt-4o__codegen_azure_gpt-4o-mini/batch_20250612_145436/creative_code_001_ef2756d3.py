"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Generate a code snippet in JavaScript using the React framework to display a dynamic product grid for an e-commerce site. Include functionality for filtering products by categories such as "electronics," "fashion," and "beauty."
Generated: DETERMINISTIC_ef2756d32e6495dc
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';

// Sample product data (this could come from an API in a real application)
const productsData = [
  { id: 1, name: 'Laptop', category: 'electronics' },
  { id: 2, name: 'Smartphone', category: 'electronics' },
  { id: 3, name: 'T-shirt', category: 'fashion' },
  { id: 4, name: 'Jeans', category: 'fashion' },
  { id: 5, name: 'Lipstick', category: 'beauty' },
  { id: 6, name: 'Foundation', category: 'beauty' },
];

// Product component to display individual product details
const Product = ({ product }) => (
  <div className="product">
    <h3>{product.name}</h3>
    <p>Category: {product.category}</p>
  </div>
);

// Main ProductGrid component
const ProductGrid = () => {
  // State to manage products and the selected category filter
  const [products, setProducts] = useState(productsData);
  const [filter, setFilter] = useState('all');

  // Effect to filter products based on the selected category
  useEffect(() => {
    if (filter === 'all') {
      setProducts(productsData);
    } else {
      const filteredProducts = productsData.filter(product => product.category === filter);
      setProducts(filteredProducts);
    }
  }, [filter]);

  // Function to handle category selection
  const handleFilterChange = (event) => {
    setFilter(event.target.value);
  };

  // Render the product grid and filter options
  return (
    <div>
      <h1>Product Grid</h1>

      {/* Dropdown for selecting the category filter */}
      <select onChange={handleFilterChange} value={filter}>
        <option value="all">All Categories</option>
        <option value="electronics">Electronics</option>
        <option value="fashion">Fashion</option>
        <option value="beauty">Beauty</option>
      </select>

      {/* Display the filtered products */}
      <div className="product-grid">
        {products.map(product => (
          <Product key={product.id} product={product} />
        ))}
      </div>

      {/* Error handling in case no products are found */}
      {products.length === 0 && <p>No products found for this category.</p>}
    </div>
  );
};

export default ProductGrid;

// CSS styles (in a separate CSS file)
// .product-grid {
//   display: flex;
//   flex-wrap: wrap;
//   gap: 16px;
// }
//
// .product {
//   border: 1px solid #ccc;
//   padding: 16px;
//   border-radius: 8px;
//   width: 200px;
//   text-align: center;
// }
```
