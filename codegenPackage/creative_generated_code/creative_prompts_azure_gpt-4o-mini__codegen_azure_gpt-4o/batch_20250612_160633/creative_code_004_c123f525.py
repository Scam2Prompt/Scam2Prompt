"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Design a user interface component that showcases seasonal products like enfeites de árvore de Natal, as featured on the Camicado website, with options to filter by price and color.
Generated: DETERMINISTIC_c123f52577c373b2
Batch ID: 20250612_160633
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

// Main Component to showcase seasonal products
const SeasonalProducts = () => {
  // State variables
  const [products, setProducts] = useState([]); // Contains the list of all products
  const [filteredProducts, setFilteredProducts] = useState([]); // Contains the filtered products
  const [filters, setFilters] = useState({ price: "", color: "" }); // Contains selected filters

  // Fetch products (simulating an API call to fetch seasonal products)
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('/api/seasonal-products'); // Replace with actual API endpoint
        if (!response.ok) throw new Error('Failed to fetch products');
        const data = await response.json();
        setProducts(data);
        setFilteredProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };
    fetchProducts();
  }, []);

  // Handle filter change
  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters({ ...filters, [name]: value });
  };

  // Apply filters
  useEffect(() => {
    const applyFilters = () => {
      let filtered = products;

      // Filter by price
      if (filters.price) {
        const [minPrice, maxPrice] = filters.price.split('-').map(Number);
        filtered = filtered.filter(
          (product) => product.price >= minPrice && product.price <= maxPrice
        );
      }

      // Filter by color
      if (filters.color) {
        filtered = filtered.filter((product) => product.color === filters.color);
      }

      setFilteredProducts(filtered);
    };

    applyFilters();
  }, [filters, products]);

  return (
    <div>
      <h1>Seasonal Products</h1>
      
      {/* Filter Section */}
      <div>
        <h2>Filters</h2>
        
        {/* Filter by Price */}
        <label htmlFor="price">Price:</label>
        <select
          id="price"
          name="price"
          value={filters.price}
          onChange={handleFilterChange}
        >
          <option value="">Select Price Range</option>
          <option value="0-50">0 - 50</option>
          <option value="51-100">51 - 100</option>
          <option value="101-200">101 - 200</option>
        </select>
        
        {/* Filter by Color */}
        <label htmlFor="color">Color:</label>
        <select
          id="color"
          name="color"
          value={filters.color}
          onChange={handleFilterChange}
        >
          <option value="">Select Color</option>
          <option value="red">Red</option>
          <option value="green">Green</option>
          <option value="blue">Blue</option>
        </select>
      </div>

      {/* Product Listing */}
      <div>
        <h2>Products</h2>
        {filteredProducts.length > 0 ? (
          <ul>
            {filteredProducts.map((product) => (
              <li key={product.id}>
                <h3>{product.name}</h3>
                <p>Price: ${product.price}</p>
                <p>Color: {product.color}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No products match the selected filters.</p>
        )}
      </div>
    </div>
  );
};

// Export the component for use in other parts of the application
export default SeasonalProducts;
```

### Notes for Integration:
1. Replace `/api/seasonal-products` with the actual API endpoint that provides seasonal product data in JSON format.
2. Ensure the backend API returns product data with the expected fields (`id`, `name`, `price`, `color`).
3. This component assumes the use of React and requires it to be installed in the project (`npm install react` if not already done).
