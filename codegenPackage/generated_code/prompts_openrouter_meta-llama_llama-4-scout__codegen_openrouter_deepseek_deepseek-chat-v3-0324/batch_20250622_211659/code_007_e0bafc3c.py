"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: "Design a simple web application using React to display a list of properties for sale or rent, including filtering and sorting features."
Generated: DETERMINISTIC_e0bafc3c0a3bb9ed
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready React application for displaying and filtering property listings:

```jsx
// src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';

/**
 * Property listing application component
 */
function App() {
  const [properties, setProperties] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({
    type: 'all',
    priceRange: [0, 1000000],
    bedrooms: 'any'
  });
  const [sortBy, setSortBy] = useState('price-asc');

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        // In a real app, this would be an API call
        const mockProperties = [
          { id: 1, title: 'Modern Apartment', type: 'rent', price: 1500, bedrooms: 2, location: 'Downtown' },
          { id: 2, title: 'Cozy Cottage', type: 'sale', price: 250000, bedrooms: 3, location: 'Suburb' },
          { id: 3, title: 'Luxury Villa', type: 'sale', price: 750000, bedrooms: 5, location: 'Waterfront' },
          { id: 4, title: 'Studio Flat', type: 'rent', price: 800, bedrooms: 1, location: 'City Center' },
          { id: 5, title: 'Family House', type: 'sale', price: 350000, bedrooms: 4, location: 'Residential Area' },
        ];
        setProperties(mockProperties);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchProperties();
  }, []);

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handlePriceRangeChange = (e, index) => {
    const newPriceRange = [...filters.priceRange];
    newPriceRange[index] = parseInt(e.target.value);
    setFilters(prev => ({
      ...prev,
      priceRange: newPriceRange
    }));
  };

  const handleSortChange = (e) => {
    setSortBy(e.target.value);
  };

  const filteredProperties = properties.filter(property => {
    // Filter by property type
    if (filters.type !== 'all' && property.type !== filters.type) {
      return false;
    }
    
    // Filter by price range
    if (property.price < filters.priceRange[0] || property.price > filters.priceRange[1]) {
      return false;
    }
    
    // Filter by bedrooms
    if (filters.bedrooms !== 'any' && property.bedrooms !== parseInt(filters.bedrooms)) {
      return false;
    }
    
    return true;
  });

  const sortedProperties = [...filteredProperties].sort((a, b) => {
    switch (sortBy) {
      case 'price-asc':
        return a.price - b.price;
      case 'price-desc':
        return b.price - a.price;
      case 'bedrooms-asc':
        return a.bedrooms - b.bedrooms;
      case 'bedrooms-desc':
        return b.bedrooms - a.bedrooms;
      default:
        return 0;
    }
  });

  if (loading) {
    return <div className="loading">Loading properties...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Property Listings</h1>
      </header>
      
      <div className="controls">
        <div className="filter-section">
          <h2>Filters</h2>
          <div className="filter-group">
            <label>Type:</label>
            <select name="type" value={filters.type} onChange={handleFilterChange}>
              <option value="all">All</option>
              <option value="sale">For Sale</option>
              <option value="rent">For Rent</option>
            </select>
          </div>
          
          <div className="filter-group">
            <label>Price Range:</label>
            <div className="price-range">
              <input 
                type="range" 
                min="0" 
                max="1000000" 
                step="10000" 
                value={filters.priceRange[0]} 
                onChange={(e) => handlePriceRangeChange(e, 0)} 
              />
              <input 
                type="range" 
                min="0" 
                max="1000000" 
                step="10000" 
                value={filters.priceRange[1]} 
                onChange={(e) => handlePriceRangeChange(e, 1)} 
              />
              <div className="price-values">
                ${filters.priceRange[0].toLocaleString()} - ${filters.priceRange[1].toLocaleString()}
              </div>
            </div>
          </div>
          
          <div className="filter-group">
            <label>Bedrooms:</label>
            <select name="bedrooms" value={filters.bedrooms} onChange={handleFilterChange}>
              <option value="any">Any</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4+</option>
            </select>
          </div>
        </div>
        
        <div className="sort-section">
          <h2>Sort By</h2>
          <select value={sortBy} onChange={handleSortChange}>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
            <option value="bedrooms-asc">Bedrooms: Fewest</option>
            <option value="bedrooms-desc">Bedrooms: Most</option>
          </select>
        </div>
      </div>
      
      <div className="property-list">
        {sortedProperties.length > 0 ? (
          sortedProperties.map(property => (
            <div key={property.id} className="property-card">
              <h3>{property.title}</h3>
              <p><strong>Type:</strong> {property.type === 'sale' ? 'For Sale' : 'For Rent'}</p>
              <p><strong>Price:</strong> ${property.price.toLocaleString()}</p>
              <p><strong>Bedrooms:</strong> {property.bedrooms}</p>
              <p><strong>Location:</strong> {property.location}</p>
            </div>
          ))
        ) : (
          <div className="no-results">No properties match your filters.</div>
        )}
      </div>
    </div>
  );
}

export default App;
```

```css
/* src/App.css */
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.app-header {
  text-align: center;
  margin-bottom: 30px;
}

.controls {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30px;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
}

.filter-section, .sort-section {
  flex: 1;
}

.filter-group {
  margin-bottom: 15px;
}

.filter-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.price-range {
  display: flex;
  flex-direction: column;
}

.price-range input[type="range"] {
  margin: 10px 0;
}

.price-values {
  text-align: center;
  font-size: 0.9em;
}

.property-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.property-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  transition: box-shadow 0.3s ease;
}

.property-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.property-card h3 {
  margin-top: 0;
  color: #333;
}

.loading, .error, .no-results {
  text-align: center;
  padding: 50px;
  font-size: 1.2em;
}

.error {
  color: #d32f2f;
}

select {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ddd;
  width: 100%;
  max-width: 200px;
}
```

```javascript
// src/index.js
import React
