"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code to implement a search bar for an e-commerce site that allows users to filter products by price range and category, similar to the functionality described on "asacanelbrazzz."
Generated: DETERMINISTIC_dce782b5f0428a19
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries (assuming React is used)
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// ProductSearch component
const ProductSearch = () => {
  // State for products, search term, price range, and selected category
  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [priceRange, setPriceRange] = useState([0, 1000]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch products and categories on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [productsRes, categoriesRes] = await Promise.all([
          axios.get('/api/products'),
          axios.get('/api/categories')
        ]);
        setProducts(productsRes.data);
        setCategories(categoriesRes.data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Filter products based on search criteria
  const filteredProducts = products.filter(product => {
    const matchesSearch = product.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                         product.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesPrice = product.price >= priceRange[0] && product.price <= priceRange[1];
    const matchesCategory = selectedCategory === 'all' || product.category === selectedCategory;
    
    return matchesSearch && matchesPrice && matchesCategory;
  });

  // Handle price range change
  const handlePriceChange = (e, index) => {
    const newPriceRange = [...priceRange];
    newPriceRange[index] = Number(e.target.value);
    setPriceRange(newPriceRange);
  };

  // Handle category change
  const handleCategoryChange = (e) => {
    setSelectedCategory(e.target.value);
  };

  // Handle search term change
  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="product-search-container">
      <div className="search-filters">
        {/* Search Bar */}
        <div className="search-bar">
          <input
            type="text"
            placeholder="Search products..."
            value={searchTerm}
            onChange={handleSearchChange}
          />
        </div>

        {/* Price Range Filter */}
        <div className="price-filter">
          <label>Price Range:</label>
          <div className="price-inputs">
            <input
              type="number"
              min="0"
              value={priceRange[0]}
              onChange={(e) => handlePriceChange(e, 0)}
            />
            <span>to</span>
            <input
              type="number"
              min="0"
              value={priceRange[1]}
              onChange={(e) => handlePriceChange(e, 1)}
            />
          </div>
        </div>

        {/* Category Filter */}
        <div className="category-filter">
          <label>Category:</label>
          <select value={selectedCategory} onChange={handleCategoryChange}>
            <option value="all">All Categories</option>
            {categories.map(category => (
              <option key={category.id} value={category.id}>
                {category.name}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Product Results */}
      <div className="product-results">
        {filteredProducts.length === 0 ? (
          <div>No products found matching your criteria.</div>
        ) : (
          <ul className="product-list">
            {filteredProducts.map(product => (
              <li key={product.id} className="product-item">
                <h3>{product.name}</h3>
                <p>{product.description}</p>
                <p>Price: ${product.price.toFixed(2)}</p>
                <p>Category: {product.category}</p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default ProductSearch;
```

```css
/* ProductSearch.css */
.product-search-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.search-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 30px;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
}

.search-bar input {
  padding: 10px;
  width: 300px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.price-filter, .category-filter {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.price-inputs {
  display: flex;
  align-items: center;
  gap: 10px;
}

.price-inputs input {
  width: 80px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.category-filter select {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  min-width: 200px;
}

.product-results {
  margin-top: 20px;
}

.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  list-style: none;
  padding: 0;
}

.product-item {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 8px;
  background-color: white;
}

.product-item h3 {
  margin-top: 0;
  color: #333;
}

.product-item p {
  margin: 5px 0;
  color: #666;
}
```
