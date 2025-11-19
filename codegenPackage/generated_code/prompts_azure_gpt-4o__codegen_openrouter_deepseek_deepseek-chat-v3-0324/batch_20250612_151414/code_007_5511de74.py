"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Create a front-end component for displaying sports apparel such as "Coletes," "Calções," and "Meiões" in an e-commerce application.
Generated: DETERMINISTIC_5511de74508155be
Batch ID: 20250612_151414
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
import './SportsApparel.css';

/**
 * SportsApparel Component
 * Displays a grid of sports apparel items with filtering and sorting options.
 */
const SportsApparel = ({ initialItems }) => {
  const [items, setItems] = useState(initialItems || []);
  const [filteredItems, setFilteredItems] = useState(initialItems || []);
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [sortOption, setSortOption] = useState('default');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Available categories for filtering
  const categories = [
    { id: 'all', name: 'All' },
    { id: 'coletes', name: 'Coletes' },
    { id: 'calcoes', name: 'Calções' },
    { id: 'meioes', name: 'Meiões' }
  ];

  // Available sorting options
  const sortOptions = [
    { id: 'default', name: 'Default' },
    { id: 'price-asc', name: 'Price: Low to High' },
    { id: 'price-desc', name: 'Price: High to Low' },
    { id: 'name-asc', name: 'Name: A to Z' },
    { id: 'name-desc', name: 'Name: Z to A' }
  ];

  useEffect(() => {
    const fetchItems = async () => {
      if (!initialItems || initialItems.length === 0) {
        try {
          setLoading(true);
          // In a real app, this would be an API call
          const mockItems = [
            { id: 1, name: 'Colete Performance', category: 'coletes', price: 29.99, image: 'colete1.jpg' },
            { id: 2, name: 'Calção Training Pro', category: 'calcoes', price: 24.99, image: 'calcao1.jpg' },
            { id: 3, name: 'Meião Elite', category: 'meioes', price: 14.99, image: 'meiao1.jpg' },
            { id: 4, name: 'Colete Team', category: 'coletes', price: 34.99, image: 'colete2.jpg' },
            { id: 5, name: 'Calção Match', category: 'calcoes', price: 19.99, image: 'calcao2.jpg' },
            { id: 6, name: 'Meião Comfort', category: 'meioes', price: 12.99, image: 'meiao2.jpg' }
          ];
          setItems(mockItems);
          setFilteredItems(mockItems);
        } catch (err) {
          setError('Failed to load items. Please try again later.');
          console.error('Error fetching items:', err);
        } finally {
          setLoading(false);
        }
      }
    };

    fetchItems();
  }, [initialItems]);

  useEffect(() => {
    // Filter items by category
    let result = items;
    if (selectedCategory !== 'all') {
      result = items.filter(item => item.category === selectedCategory);
    }

    // Sort items
    switch (sortOption) {
      case 'price-asc':
        result = [...result].sort((a, b) => a.price - b.price);
        break;
      case 'price-desc':
        result = [...result].sort((a, b) => b.price - a.price);
        break;
      case 'name-asc':
        result = [...result].sort((a, b) => a.name.localeCompare(b.name));
        break;
      case 'name-desc':
        result = [...result].sort((a, b) => b.name.localeCompare(a.name));
        break;
      default:
        break;
    }

    setFilteredItems(result);
  }, [selectedCategory, sortOption, items]);

  const handleAddToCart = (itemId) => {
    // In a real app, this would add the item to the cart
    console.log(`Added item ${itemId} to cart`);
  };

  if (loading) {
    return <div className="loading">Loading sports apparel...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="sports-apparel">
      <h1>Sports Apparel</h1>
      
      <div className="controls">
        <div className="filter-control">
          <label htmlFor="category-filter">Filter by:</label>
          <select
            id="category-filter"
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
          >
            {categories.map(category => (
              <option key={category.id} value={category.id}>{category.name}</option>
            ))}
          </select>
        </div>

        <div className="sort-control">
          <label htmlFor="sort-option">Sort by:</label>
          <select
            id="sort-option"
            value={sortOption}
            onChange={(e) => setSortOption(e.target.value)}
          >
            {sortOptions.map(option => (
              <option key={option.id} value={option.id}>{option.name}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="items-grid">
        {filteredItems.length > 0 ? (
          filteredItems.map(item => (
            <div key={item.id} className="item-card">
              <div className="item-image">
                <img src={item.image} alt={item.name} />
              </div>
              <div className="item-details">
                <h3>{item.name}</h3>
                <p className="price">${item.price.toFixed(2)}</p>
                <button 
                  className="add-to-cart"
                  onClick={() => handleAddToCart(item.id)}
                >
                  Add to Cart
                </button>
              </div>
            </div>
          ))
        ) : (
          <p className="no-items">No items found matching your criteria.</p>
        )}
      </div>
    </div>
  );
};

SportsApparel.propTypes = {
  initialItems: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
      name: PropTypes.string.isRequired,
      category: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      image: PropTypes.string.isRequired
    })
  )
};

export default SportsApparel;
```

```css
/* SportsApparel.css */
.sports-apparel {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.sports-apparel h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.controls {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 15px;
}

.filter-control, .sort-control {
  display: flex;
  align-items: center;
  gap: 10px;
}

.filter-control label, .sort-control label {
  font-weight: bold;
}

select {
  padding: 8px 12px;
  border-radius: 4px;
  border: 1px solid #ddd;
  background-color: white;
  font-size: 14px;
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.item-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.item-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.item-image {
  height: 200px;
  overflow: hidden;
}

.item-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-details {
  padding: 15px;
  text-align: center;
}

.item-details h3 {
  margin: 0 0 10px;
  font-size: 16px;
  color: #333;
}

.price {
  font-weight: bold;
  color: #e63946;
  margin: 10px 0;
}

.add-to-cart {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
}

.add-to-cart:hover {
  background-color: #45a049;
}

.loading, .error, .no-items {
  text-align: center;
