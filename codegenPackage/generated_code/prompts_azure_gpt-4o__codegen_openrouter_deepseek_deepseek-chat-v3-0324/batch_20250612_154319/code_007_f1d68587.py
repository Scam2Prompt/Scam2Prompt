"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Using React, design a dynamic product gallery for a plastic manufacturing company that displays items like chairs, tables, and houseware, similar to the Samba Plastic Industries website.
Generated: DETERMINISTIC_f1d68587663141b5
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import './ProductGallery.css';

// Sample product data
const products = [
  {
    id: 1,
    name: 'Plastic Chair',
    category: 'chairs',
    image: 'chair.jpg',
    description: 'Durable plastic chair for indoor and outdoor use.'
  },
  {
    id: 2,
    name: 'Plastic Table',
    category: 'tables',
    image: 'table.jpg',
    description: 'Lightweight plastic table perfect for any setting.'
  },
  {
    id: 3,
    name: 'Storage Box',
    category: 'houseware',
    image: 'storage.jpg',
    description: 'Versatile plastic storage solution.'
  },
  {
    id: 4,
    name: 'Dining Set',
    category: 'tables',
    image: 'dining.jpg',
    description: 'Complete plastic dining set for families.'
  },
  {
    id: 5,
    name: 'Garden Chair',
    category: 'chairs',
    image: 'garden-chair.jpg',
    description: 'Weather-resistant garden chair.'
  },
  {
    id: 6,
    name: 'Kitware Set',
    category: 'houseware',
    image: 'kitware.jpg',
    description: 'Essential plastic kitchen items.'
  }
];

const ProductGallery = () => {
  const [activeCategory, setActiveCategory] = useState('all');
  const [filteredProducts, setFilteredProducts] = useState(products);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Get unique categories for filter buttons
  const categories = ['all', ...new Set(products.map(product => product.category))];

  // Filter products based on active category
  useEffect(() => {
    const filterProducts = () => {
      try {
        setIsLoading(true);
        if (activeCategory === 'all') {
          setFilteredProducts(products);
        } else {
          const filtered = products.filter(
            product => product.category === activeCategory
          );
          setFilteredProducts(filtered);
        }
      } catch (err) {
        setError('Failed to filter products. Please try again.');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    filterProducts();
  }, [activeCategory]);

  // Handle image loading errors
  const handleImageError = (e) => {
    e.target.src = 'placeholder.jpg';
  };

  return (
    <div className="product-gallery">
      <h1 className="gallery-title">Our Products</h1>
      
      {error && <div className="error-message">{error}</div>}

      {/* Category filter buttons */}
      <div className="category-filter">
        {categories.map(category => (
          <button
            key={category}
            className={`filter-btn ${activeCategory === category ? 'active' : ''}`}
            onClick={() => setActiveCategory(category)}
          >
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </button>
        ))}
      </div>

      {/* Product grid */}
      {isLoading ? (
        <div className="loading">Loading products...</div>
      ) : (
        <div className="product-grid">
          {filteredProducts.length > 0 ? (
            filteredProducts.map(product => (
              <div key={product.id} className="product-card">
                <div className="product-image-container">
                  <img
                    src={product.image}
                    alt={product.name}
                    onError={handleImageError}
                    className="product-image"
                  />
                </div>
                <div className="product-info">
                  <h3 className="product-name">{product.name}</h3>
                  <p className="product-description">{product.description}</p>
                </div>
              </div>
            ))
          ) : (
            <div className="no-products">No products found in this category.</div>
          )}
        </div>
      )}
    </div>
  );
};

export default ProductGallery;
```

```css
/* ProductGallery.css */
.product-gallery {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.gallery-title {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.error-message {
  color: #d32f2f;
  background-color: #fde8e8;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
  text-align: center;
}

.category-filter {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 30px;
}

.filter-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #f0f0f0;
  color: #333;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-btn:hover {
  background-color: #ddd;
}

.filter-btn.active {
  background-color: #1976d2;
  color: white;
}

.loading, .no-products {
  text-align: center;
  padding: 40px;
  color: #666;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.product-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.product-image-container {
  height: 200px;
  overflow: hidden;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.product-card:hover .product-image {
  transform: scale(1.05);
}

.product-info {
  padding: 15px;
}

.product-name {
  margin: 0 0 10px 0;
  color: #333;
}

.product-description {
  margin: 0;
  color: #666;
  font-size: 14px;
}

@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (max-width: 480px) {
  .category-filter {
    flex-direction: column;
    align-items: center;
  }
  
  .filter-btn {
    width: 100%;
    max-width: 200px;
  }
}
```
