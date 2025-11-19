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
// SportsApparelComponent.js
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * Sports Apparel Component
 * 
 * Displays a list of sports apparel items.
 * 
 * @param {Object} props
 * @param {Array} props.apparel - List of apparel items
 * @param {Function} props.onAddToCart - Callback function for add to cart button
 */
function SportsApparelComponent({ apparel, onAddToCart }) {
  // State to store filtered apparel items
  const [filteredApparel, setFilteredApparel] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');

  // Categories for filtering
  const categories = ['Coletes', 'Calções', 'Meiões'];

  useEffect(() => {
    // Initialize filtered apparel with all items
    setFilteredApparel(apparel);
  }, [apparel]);

  // Handle category filter change
  const handleFilterChange = (category) => {
    setSelectedCategory(category);
    if (category) {
      // Filter apparel by selected category
      const filteredItems = apparel.filter((item) => item.category === category);
      setFilteredApparel(filteredItems);
    } else {
      // Show all items when no category is selected
      setFilteredApparel(apparel);
    }
  };

  return (
    <div className="sports-apparel-component">
      <h2>Sports Apparel</h2>
      <div className="filter-section">
        {categories.map((category) => (
          <button
            key={category}
            className={selectedCategory === category ? 'active' : ''}
            onClick={() => handleFilterChange(category)}
          >
            {category}
          </button>
        ))}
        <button onClick={() => handleFilterChange('')}>All</button>
      </div>
      <div className="apparel-list">
        {filteredApparel.map((item) => (
          <div key={item.id} className="apparel-item">
            <h3>{item.name}</h3>
            <p>{item.description}</p>
            <p>Price: {item.price}</p>
            <button onClick={() => onAddToCart(item)}>Add to Cart</button>
          </div>
        ))}
      </div>
    </div>
  );
}

SportsApparelComponent.propTypes = {
  apparel: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      category: PropTypes.string.isRequired,
      description: PropTypes.string,
      price: PropTypes.number.isRequired,
    })
  ).isRequired,
  onAddToCart: PropTypes.func.isRequired,
};

export default SportsApparelComponent;
```

```css
/* SportsApparelComponent.css */
.sports-apparel-component {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.filter-section {
  margin-bottom: 20px;
}

.filter-section button {
  margin-right: 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

.filter-section button.active {
  background-color: #3e8e41;
}

.filter-section button:hover {
  background-color: #3e8e41;
}

.apparel-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.apparel-item {
  margin: 20px;
  padding: 20px;
  width: calc(33.33% - 20px);
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.apparel-item h3 {
  margin-top: 0;
}

.apparel-item button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.apparel-item button:hover {
  background-color: #3e8e41;
}
```

```javascript
// App.js
import React, { useState } from 'react';
import SportsApparelComponent from './SportsApparelComponent';

function App() {
  const [apparel, setApparel] = useState([
    { id: 1, name: 'Colete 1', category: 'Coletes', description: 'Colete de treino', price: 29.99 },
    { id: 2, name: 'Calções 1', category: 'Calções', description: 'Calções de corrida', price: 39.99 },
    { id: 3, name: 'Meiões 1', category: 'Meiões', description: 'Meiões de futebol', price: 19.99 },
    { id: 4, name: 'Colete 2', category: 'Coletes', description: 'Colete de treino', price: 29.99 },
    { id: 5, name: 'Calções 2', category: 'Calções', description: 'Calções de corrida', price: 39.99 },
    { id: 6, name: 'Meiões 2', category: 'Meiões', description: 'Meiões de futebol', price: 19.99 },
  ]);

  const [cart, setCart] = useState([]);

  const handleAddToCart = (item) => {
    setCart([...cart, item]);
  };

  return (
    <div className="app">
      <SportsApparelComponent apparel={apparel} onAddToCart={handleAddToCart} />
      <div className="cart">
        <h2>Cart</h2>
        <ul>
          {cart.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
```
