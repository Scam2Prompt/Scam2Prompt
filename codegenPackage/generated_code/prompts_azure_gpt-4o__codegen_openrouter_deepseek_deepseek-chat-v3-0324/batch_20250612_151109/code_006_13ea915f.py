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

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * FurnitureProduct Component
 * Displays a single furniture product with its details
 */
const FurnitureProduct = ({ product }) => {
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p className="price">${product.price.toFixed(2)}</p>
      <p className="category">{product.category}</p>
      <p className="description">{product.description}</p>
    </div>
  );
};

FurnitureProduct.propTypes = {
  product: PropTypes.shape({
    name: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    category: PropTypes.string.isRequired,
    description: PropTypes.string,
  }).isRequired,
};

/**
 * FurnitureCatalog Component
 * Displays a catalog of furniture products with sorting options
 */
const FurnitureCatalog = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortBy, setSortBy] = useState('price');
  const [filterCategory, setFilterCategory] = useState('all');

  // Sample furniture data
  const sampleProducts = [
    {
      id: 1,
      name: 'Bicama Siena',
      price: 899.99,
      category: 'beds',
      description: 'Queen size bed with wooden frame',
    },
    {
      id: 2,
      name: 'Estofado Desejos 3x2 lugares',
      price: 1299.99,
      category: 'sofas',
      description: 'Comfortable 3-seater sofa with 2 recliners',
    },
    {
      id: 3,
      name: 'Mesa de Jantar Aurora',
      price: 599.99,
      category: 'tables',
      description: 'Dining table with 6 chairs',
    },
    {
      id: 4,
      name: 'Armário Elegance',
      price: 799.99,
      category: 'wardrobes',
      description: 'Modern wardrobe with sliding doors',
    },
  ];

  useEffect(() => {
    // Simulate API fetch
    const fetchProducts = async () => {
      try {
        // In a real app, this would be an API call
        await new Promise(resolve => setTimeout(resolve, 500));
        setProducts(sampleProducts);
        setLoading(false);
      } catch (err) {
        setError('Failed to load products. Please try again later.');
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  // Get unique categories for filter dropdown
  const categories = ['all', ...new Set(sampleProducts.map(p => p.category))];

  // Sort and filter products
  const processedProducts = [...products]
    .filter(product => filterCategory === 'all' || product.category === filterCategory)
    .sort((a, b) => {
      if (sortBy === 'price') return a.price - b.price;
      if (sortBy === 'name') return a.name.localeCompare(b.name);
      return 0;
    });

  if (loading) return <div className="loading">Loading products...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="furniture-catalog">
      <h1>Furniture Catalog</h1>
      
      <div className="controls">
        <div className="sort-control">
          <label htmlFor="sort">Sort by:</label>
          <select 
            id="sort" 
            value={sortBy} 
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="price">Price</option>
            <option value="name">Name</option>
          </select>
        </div>

        <div className="filter-control">
          <label htmlFor="filter">Filter by category:</label>
          <select 
            id="filter" 
            value={filterCategory} 
            onChange={(e) => setFilterCategory(e.target.value)}
          >
            {categories.map(category => (
              <option key={category} value={category}>
                {category.charAt(0).toUpperCase() + category.slice(1)}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="product-grid">
        {processedProducts.length > 0 ? (
          processedProducts.map(product => (
            <FurnitureProduct key={product.id} product={product} />
          ))
        ) : (
          <p>No products found matching your criteria.</p>
        )}
      </div>
    </div>
  );
};

export default FurnitureCatalog;
```
