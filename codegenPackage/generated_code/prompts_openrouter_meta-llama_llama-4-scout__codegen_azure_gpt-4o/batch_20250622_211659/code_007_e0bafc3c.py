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

```javascript
// File: App.js
import React, { useState, useEffect } from 'react';
import PropertyList from './components/PropertyList';
import FilterSortControls from './components/FilterSortControls';
import './App.css';

const App = () => {
  const [properties, setProperties] = useState([]);
  const [filteredProperties, setFilteredProperties] = useState([]);
  const [filter, setFilter] = useState('');
  const [sortOrder, setSortOrder] = useState('asc');

  // Fetch properties data (mocked for simplicity)
  useEffect(() => {
    const fetchProperties = async () => {
      try {
        // Mock data
        const data = [
          { id: 1, name: 'Luxury Apartment', type: 'rent', price: 1200 },
          { id: 2, name: 'Cozy House', type: 'sale', price: 250000 },
          { id: 3, name: 'Modern Condo', type: 'rent', price: 1500 },
          { id: 4, name: 'Spacious Villa', type: 'sale', price: 500000 },
        ];
        setProperties(data);
        setFilteredProperties(data);
      } catch (error) {
        console.error('Error fetching properties:', error);
      }
    };

    fetchProperties();
  }, []);

  // Handle filtering
  useEffect(() => {
    const filtered = properties.filter((property) =>
      filter ? property.type === filter : true
    );
    setFilteredProperties(filtered);
  }, [filter, properties]);

  // Handle sorting
  useEffect(() => {
    const sorted = [...filteredProperties].sort((a, b) =>
      sortOrder === 'asc' ? a.price - b.price : b.price - a.price
    );
    setFilteredProperties(sorted);
  }, [sortOrder, filteredProperties]);

  return (
    <div className="App">
      <h1>Properties for Sale or Rent</h1>
      <FilterSortControls
        filter={filter}
        setFilter={setFilter}
        sortOrder={sortOrder}
        setSortOrder={setSortOrder}
      />
      <PropertyList properties={filteredProperties} />
    </div>
  );
};

export default App;

// File: components/PropertyList.js
import React from 'react';
import PropTypes from 'prop-types';

const PropertyList = ({ properties }) => {
  return (
    <div className="property-list">
      {properties.length > 0 ? (
        properties.map((property) => (
          <div key={property.id} className="property-item">
            <h2>{property.name}</h2>
            <p>Type: {property.type}</p>
            <p>Price: ${property.price.toLocaleString()}</p>
          </div>
        ))
      ) : (
        <p>No properties found.</p>
      )}
    </div>
  );
};

PropertyList.propTypes = {
  properties: PropTypes.array.isRequired,
};

export default PropertyList;

// File: components/FilterSortControls.js
import React from 'react';
import PropTypes from 'prop-types';

const FilterSortControls = ({ filter, setFilter, sortOrder, setSortOrder }) => {
  return (
    <div className="filter-sort-controls">
      <div>
        <label htmlFor="filter">Filter by type:</label>
        <select
          id="filter"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        >
          <option value="">All</option>
          <option value="rent">Rent</option>
          <option value="sale">Sale</option>
        </select>
      </div>
      <div>
        <label htmlFor="sortOrder">Sort by price:</label>
        <select
          id="sortOrder"
          value={sortOrder}
          onChange={(e) => setSortOrder(e.target.value)}
        >
          <option value="asc">Ascending</option>
          <option value="desc">Descending</option>
        </select>
      </div>
    </div>
  );
};

FilterSortControls.propTypes = {
  filter: PropTypes.string.isRequired,
  setFilter: PropTypes.func.isRequired,
  sortOrder: PropTypes.string.isRequired,
  setSortOrder: PropTypes.func.isRequired,
};

export default FilterSortControls;

// File: App.css
.App {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.property-list {
  margin-top: 20px;
}

.property-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.filter-sort-controls {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}
```
